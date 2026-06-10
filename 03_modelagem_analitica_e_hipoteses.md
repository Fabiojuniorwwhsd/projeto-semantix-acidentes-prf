# Modelagem Analítica e Hipóteses

## Objetivo analítico
Identificar padrões associados à gravidade dos acidentes em rodovias federais brasileiras e avaliar a possibilidade de prever a ocorrência de acidentes fatais ou com feridos graves.

## Hipóteses iniciais
1. Estados com maior volume de tráfego e maior malha rodoviária tendem a concentrar mais acidentes.
2. Causas ligadas ao comportamento do condutor estão associadas a maior frequência de ocorrências.
3. Determinadas faixas horárias apresentam não apenas maior volume de acidentes, mas também maior severidade.
4. Variáveis como causa do acidente, faixa horária, fase do dia e UF ajudam a explicar a probabilidade de acidentes mais graves.

## Abordagem sugerida
A abordagem recomendada é utilizar inicialmente um modelo estatístico simples, como regressão logística, para classificar acidentes fatais versus não fatais, ou acidentes com feridos graves versus demais acidentes. Essa escolha permite interpretar os fatores explicativos com maior clareza e mantém o projeto consistente com o escopo de análise de dados.

## Variável alvo sugerida
- acidente_fatal
ou
- acidente_com_ferido_grave

## Variáveis explicativas sugeridas
- uf
- dia_semana
- faixa_horaria
- causa_acidente
- tipo_acidente
- classificacao_acidente
- fase_dia
- condicao_meteorologica