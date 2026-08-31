import os
import pandas as pd
from pandas_gbq import read_gbq
 
# Define a query SQL válida
query = """
WITH UltimoStatus AS (
  SELECT *
  FROM `mrvlake-prd.gold_ceianalytics_funil_vendas.fat_funil_vendas`
  WHERE num_dbm IS NOT NULL
  QUALIFY ROW_NUMBER() OVER (
    PARTITION BY num_dbm
    ORDER BY dat_real_hora DESC
  ) = 1
)
 
SELECT 
num_dbm,
US.cod_lead,
US.des_status_funil, 
US.dat_real, 
US.nom_cidade_empreendimento,
US.des_status_funil,
US.des_tipo_reenvio,
US.vlr_renda_informada_lead,
ll.vlr_renda_mensal,
ll.des_midia_web
FROM UltimoStatus AS US
LEFT JOIN `mrvlake-prd.silver_mrv_salesforce.lead` as ll
on US.cod_lead = ll.cod_lead
WHERE dat_real >= '2026-06-01'
"""
 
# Caminho onde o arquivo será salvo
caminho_arquivo = r'C:\Users\VITOR.LOBO\OneDrive - MRV\Área de Trabalho\Vitor\Performance\Funnel Performance\DataBase\funil.xlsx'
 
# Garante que a pasta existe (apenas se houver um diretório no caminho)
diretorio = os.path.dirname(caminho_arquivo)
if diretorio:
    os.makedirs(diretorio, exist_ok=True)
 
try:
    # Lê os dados do BigQuery
    df = read_gbq(query, project_id='mkt-analytics-prd', dialect='standard')
   
    # Tratamento de tipos de dados
    for col in df.columns:
        # Converte objetos complexos para string
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).replace('nan', '')
       
        # Remove timezone de todas as colunas datetime
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            df[col] = pd.to_datetime(df[col]).dt.tz_localize(None)
   
    # Salva o dataframe em um arquivo Excel com engine específico
    with pd.ExcelWriter(caminho_arquivo, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Dados', index=False)
   
    print(f'Dados salvos em {caminho_arquivo}')
    print(f'Total de registros: {len(df)}')
 
except Exception as e:
    print("Erro durante execução:")
    print(e)
   
    # Tenta salvar como CSV caso Excel falhe
    try:
        df.to_csv(caminho_arquivo.replace('.xlsx', '.csv'), index=False)
        print(f"Arquivo salvo como CSV devido a erro no Excel")
    except:
        pass