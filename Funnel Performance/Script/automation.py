""" 
Instrução do codigo
Passos:
1- Ao rodar automation.py, o codigo deve rodar o extraction.py para gerar o arquivo Excel com os dados do BigQuery.
2- O arquivo Excel gerado que vai ficar guardado em Funnel Performance/Extra/DataBase/funi.xlsx, será lido pelo automation.py para gerar o arquivo de saída final.
3- Precisa ser feito um de/para com a cidade_empreendimento usando a planilha Apoio_Estrutura_Comercial para adicionar os campos Regional e Diretoria para cada cidade.
4- Depois da base atualizada com regional e diretoria, existe uma outra coluna que precisamos adicionar que é faixa de renda. A faixa de renda tem o seguinte intervalo: <3.2K , 3.2K-5K, 5K-9.6K, 9.6K-13K , 13K>. Preciso que analise o campo de vlr_renda_informada e adicione a coluna nova com as faixas de renda.
4- Com a base nova feita quero que o codigo gere um html final com as seguintes analises:
-Quero simular um funil de vendas,com 4 filtros, onde 1 seria geralzao, 2 seria por des_tipo_reenvio e 3 seria por des_midia_web e o 4 seria por faixa de renda. O campo que vai servir para o funil é des_status_funil, e quero que o funil seja feito com base na quantidade de cod_lead distintos.
-Seria basicamente um painel executivo, onde na aba princiapl tenho uma contagem dos leads totais da base, a quantidade de leads por faixa de renda, quantida de leads por midia web e tipo de reenvio e abaixo ja teria o funil com os filtros que solicitei anteriormente. Para fazer o funil voce pode se basear em um código ja existente que é o C:\Users\VITOR.LOBO\OneDrive - MRV\Área de Trabalho\Vitor\Performance\Funil_Midia_WEB\funil_midia_web.html e C:\Users\VITOR.LOBO\OneDrive - MRV\Área de Trabalho\Vitor\Performance\Funil_Midia_WEB\Código\gcp.py
-Painel precisaria ter as cores da MRV 
-O codigo precisa garantir que quando eu subir uma base nova em "Data_Base" através da consulta do extraction, o html seja atualizado automaticamente com a nova base, sem precisar alterar o código.
- Quero uma funcionalidade do painel que quando eu apertar um botão "Atualizar Base", ele rode o extraction.py e atualize a base e o html final automaticamente. Precisa ter uma tela de loading para mostrar ao usuario que o processo está acontecendo, e quando terminar de atualizar a base e gerar o html, mostrar uma mensagem de sucesso para o usuário.
Instrução do visual

Quero criar um painel executivo, com as cores da MRV, que tenha apenas uma aba principal, onde tenha os seguintes elementos:
1- Um card com a quantidade total de leads distintos da base. (de acordo com os filtros selecionados). Essas informações ficaram na parte superior da tela.
2- Periodo que está sendo analisado. (opção de filtro para selecionar o periodo) (ao lado do card com total de leads)
3- Cidade (nom_cidade_empreendimento) que está sendo analisado. (opção de filtro para selecionar o periodo) (ao lado do card com total de leads)
4- Logo abaixo precisa ter um funil de vendas com 4 filtros (serão os filtros geral da base, além de filtrar para o funil o resto dos dados será atualizado), onde o primeiro filtro é geral, o segundo filtro é por des_tipo_reenvio, o terceiro filtro é por des_midia_web e o quarto filtro é por faixa de renda. O funil deve ser feito com base na quantidade de cod_lead distintos e no campo des_status_funil.
5- Abaixo do funil quero as seguintes informaçoes(podem vir em formato de tabela): Conversão por etapa do funil, Quantidade de leads por etapa do funil (dependendo do filtro vai trazer a quantidade de faixa de renda por etapa, de midia_web etc..) e um top 5 cidades por etapa do funil.
6- O painel deve ter as cores da MRV, e ser responsivo, para que possa ser visualizado em diferentes dispositivos.
7- Qualquer dúvida que tiver sobre a organização/disposição dos itens do painel, pode me perguntar antes de iniciar a construção. Se tiver duvida nos campos que precisa usar para cada dado, me perguntar também.
8- Quero um visual simples, limpo e bonito visualmente. Quero que as informações fiquem faceis de entender e que o painel seja intuitivo para o usuário final. Utilize suas melhores skills de front-end e UX para a criação do painel.

Acredito que para a criação do funil voce nao vai conseguir acessar o arquivo base por enquanto que tem o modelo que gosto de funil. Mas quero que voce utilize a melhor versão que tiver de um funil de vendas, ele precisa ter o formato correto e precisa ser moderno e intutivo. Use as etapas que listamos anteriormente (Lead, Documentação Enviada, CPF Aprovado, Ganho).

"""
