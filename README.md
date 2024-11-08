## Análise dos preços de mais de 50.000 diamantes de lapidação redonda

<p align="center">
  <img src="https://usagif.com/wp-content/uploads/snow-white-56.gif" alt=" " />
</p>

Este projeto tem como objetivo analisar os preços de diamantes de lapidação redonda com base em diversas características, como o quilate (carat), o corte (cut), a cor (color), a pureza (clarity), a profundidade (depth) e a largura da parte superior do diamante em relação ao ponto mais largo (table) e outras variáveis. Além da análise exploratória dos dados, será desenvolvida uma análise comparativa de modelos para previsão do preço de novos diamantes com base em seus atributos.

## Justificativa

Por ser a lapidação preferida dos consumidores, o formato redondo é a mais escolhida do mercado de diamantes, conhecida por seu brilho e beleza, representando a maioria das vendas. Analisar seus preços é importante para entender fatores como oferta e demanda, qualidade e como novas tecnologias vão influenciar o valor das pedras. Isso ajuda tanto consumidores quanto investidores a fazer escolhas mais inteligentes, além de permitir que varejistas acompanhem tendências de mercado. Ademais, a análise ajuda a prever como eventos globais, economia e tecnologia, podem afetar o mercado de diamantes.

Neste projeto, vamos abordar as seguintes questões:

<div align=" ">

- 2.1: Análise da relação entre preço, corte, cor e clareza do diamante.
- 2.2: A influência entre peso (carat), preço e corte do diamante.
- 2.3: A influência das proporções (depth e table) no preço.


</div>

## Desenvolvedores

- Isabel Cristina Martins [https://github.com/IsaCristinaMartins]

## Metodologia

O projeto será desenvolvido utilizando a metodologia CRISP-DM, seguindo os seguintes passos:

<div align = " ">

- Entendimento de negócio
- Entendimento de dados
- Preparação dos dados
- Modelagem

</div>

O projeto também é dividido em duas entregas, a saber:

<div align = " ">

- Análise Exploratória de Dados (EDA): entendimento das variáveis que influenciam o MPG e identificação de padrões nos dados através de hipóteses, visualizações e insights.
- Análise comparativa de modelos: construção de modelos de aprendizado de máquina para rpevisão de consumo, com métricas de desempenho para avaliação da performance.

</div>

## Resultados Esperados

Esperamos identificar as principais variáveis que afetam o preço dos diamantes e criar um modelo preditivo que permita prever o valor de novos diamantes no mercado com alta precisão. Isso fornecerá informações úteis tanto para consumidores, investidores e joalheiros.

## Dicionário de dados

| Nome da Coluna | Nome em Português | Tipo de Dado  | Descrição                    | Valores Possíveis                                     |
| -------------- | ----------------- | ------------- | ---------------------------- | ----------------------------------------------------- |
| carat          | quilate           | float(quant)  | Peso do diamante em quilates | 0.2 ---- 5.01                                         |
| cut            | corte             | string(quali) | Qualidade do corte           | Fair, Good, Very Good, Premium, Ideal                 |
| color          | cor               | string(quali) | Cor do diamante              | from D (best) - J (worst)                             |
| clarity        | clareza           | string(quali) | Clareza do diamante          | I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best) |
| depth          | profundidade      | float(quanti) | Profundidade do diamante     | = z / mean(x, y) = 2 \* z / (x + y)(43-79)            |
| table          | propoção          | float(quanti) | Proporção base vs topo       | 43.0 - 95.0                                           |
| price          | preço             | int(quanti)   | Preço do diamante em USD     | $326 ---- $18,823                                     |
| x              | comprimento       | float(quanti) | Comprimento em mm            | length in mm (0--10.74)                               |
| y              | largura           | float(quanti) | Largura em mm                | width in mm (0--58.9)                                 |
| z              | altura            | float(quanti) | Altura em mm                 | depth in mm (0--31.8)                                 |
