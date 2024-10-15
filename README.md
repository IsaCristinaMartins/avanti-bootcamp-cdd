# <Título do projeto>

Insira aqui um resumo do projeto que será construído. Tente apresentar uma justificativa para o projeto. É desejável que também se insira um [graphical abstract](https://www.elsevier.com/authors/tools-and-resources/visual-abstract).

## Desenvolvedores

- [Nome do desenvolvedor #1](url-do-github-do-desenvolvedor-#1)
- [Nome do desenvolvedor #2](url-do-github-do-desenvolvedor-#2)
- [Nome do desenvolvedor #3](url-do-github-do-desenvolvedor-#3)
- [Nome do desenvolvedor #4](url-do-github-do-desenvolvedor-#4)
- ...



### Organização de diretórios

.
├── data/ # Diretório contendo todos os arquivos de dados
│   ├── external/ # Arquivos de dados de fontes externas
│   ├── interim/ # Arquivos de dados intermediários
│   ├── processed/ # Arquivos de dados processados
│   └── raw/ # Arquivos de dados originais, imutáveis
├── docs/ # Documentação gerada através da biblioteca mkdocs
├── models/ # Modelos treinados e serializados, predições ou resumos de modelos
├── notebooks/ # Diretório contendo todos os notebooks utilizados nos passos
├── references/ # Dicionários de dados, manuais e todo o material exploratório
├── src/ # Código fonte utilizado nesse projeto
│   ├── data/ # Classes e funções utilizadas para download e processamento de dados
│   ├── deployment/ # Classes e funções utilizadas para implantação do modelo
│   └── model/ # Classes e funções utilizadas para modelagem
├── app.py # Arquivo com o código da aplicação do streamlit
├── Procfile # Arquivo de configuração do heroku
├── pyproject.toml # Arquivo de dependências para reprodução do projeto
├── poetry.lock # Arquivo com sub-dependências do projeto principal
├── README.md # Informações gerais do projeto
└── tasks.py # Arquivo com funções para criação de tarefas utilizadas pelo invoke

```

```
