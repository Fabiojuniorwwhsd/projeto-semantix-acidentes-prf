# Fontes de Dados e Método de Coleta

## Fonte principal
A base principal utilizada no projeto é composta pelos arquivos públicos da Polícia Rodoviária Federal (PRF), no formato CSV, agrupados por ocorrência, referentes aos anos de 2022, 2023 e 2024.

## Descrição da fonte
Os arquivos da PRF reúnem informações sobre acidentes em rodovias federais brasileiras, incluindo data, dia da semana, horário, UF, município, BR, quilômetro, causa do acidente, tipo de acidente, classificação, fase do dia, condição meteorológica, tipo de pista, traçado da via e quantitativos de pessoas, mortos, feridos e veículos.

## Tipo de dados disponíveis
Os dados são estruturados, em formato tabular CSV, e podem ser processados com Python, SQL, planilhas e ferramentas de visualização.

## Método de acesso e coleta
A coleta foi feita por download direto dos arquivos CSV disponibilizados em portal público oficial da PRF. Para a análise, os arquivos dos anos de 2022, 2023 e 2024 foram consolidados em uma única base no ambiente Python.

## Observações sobre a qualidade dos dados
Durante a auditoria inicial, foi identificado percentual relevante de valores ausentes na coluna de quilometragem (km), mas isso não inviabiliza a análise. As demais variáveis principais apresentaram boa consistência para exploração dos padrões de acidentes.