Instruções do código
Objetivo geral
O objetivo do código é automatizar a geração de uma base atualizada e, a partir dela, criar um painel HTML executivo com análises de funil e indicadores principais.

Fluxo de execução
Ao executar o arquivo automation.py, o script deve primeiro rodar o extraction.py, que será responsável por gerar um arquivo Excel com os dados extraídos do BigQuery.

O arquivo Excel gerado ficará salvo em Funnel Performance/Extra/DataBase/funi.xlsx. Em seguida, esse arquivo deve ser lido pelo automation.py para dar continuidade ao processamento e gerar o arquivo final.

A base deve passar por um processo de de/para utilizando a coluna cidade_empreendimento e a planilha Apoio_Estrutura_Comercial, com o objetivo de adicionar os campos:

Regional
Diretoria
Após a inclusão de Regional e Diretoria, deve ser criada uma nova coluna chamada faixa de renda, com base no campo vlr_renda_informada. As faixas de renda devem seguir esta lógica:

<3.2K
3.2K-5K
5K-9.6K
9.6K-13K
13K>
Com a base final já tratada, o código deve gerar um arquivo HTML com as análises descritas abaixo.

Estrutura do painel HTML
O painel deve funcionar como um funil de vendas com 4 filtros:

Geral
des_tipo_reenvio
des_midia_web
faixa de renda
O funil deve ser construído com base no campo des_status_funil, considerando a quantidade de cod_lead distintos.

Conteúdo da página principal
A aba principal do painel deve conter:

Contagem total de leads da base
Quantidade de leads por faixa de renda
Quantidade de leads por mídia web
Quantidade de leads por tipo de reenvio
Funil de vendas com os filtros solicitados acima
Referência visual e técnica
Para a construção do funil, o código pode se basear nos arquivos abaixo(use os mesmos des_status_funil analisados):

C:\Users\VITOR.LOBO\OneDrive - MRV\Área de Trabalho\Vitor\Performance\Funil_Midia_WEB\funil_midia_web.html
C:\Users\VITOR.LOBO\OneDrive - MRV\Área de Trabalho\Vitor\Performance\Funil_Midia_WEB\Código\gcp.py
Identidade visual
O painel deve seguir as cores da MRV.

Requisito de atualização automática
O código precisa ser preparado para que, sempre que uma nova base for carregada na pasta Data_Base por meio da consulta do extraction, o arquivo HTML seja atualizado automaticamente com os novos dados, sem necessidade de alterar o código manualmente.
