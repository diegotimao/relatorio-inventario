# Relatório de inventário

Projeto desenvolvido em python utilizando a Programação Orientada a Objetos que contém a implementação de um gerador de relatórios que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

Os dados de estoque poderão ser obtidos de diversas fontes:

-   Através da importação de um arquivo **CSV**
-   Através da importação de um arquivo **JSON**
-   Através da importação de um arquivo **XML**

Funcionalidades: O relatório possui duas versões: **simples** e **completa**

## Executado o projeto

Para executar o projeto primeiro você deve fazer o clone deste repositório, após isto deve abrir o projeto em algum editor de códigos.

**OBS**: Para que este projeto seja execultado você obritóriamente deve ter o `python` instalado em sua máquina, caso não tenha execulte o comando abixo para fazer a instalação em ambientes linux.

```
    sudo apt install python3
```

Verificando se o python foi instalado

```
    python3 --version
```

A saída deverá:

```
    Python 3.8.0
```

Criar o ambiente virtual:

```
    python3 -m venv .venv
```

Ativar o ambiente virtual

```
    source .venv/bin/activate
```

Instalar as dependências no ambiente virtual

```
    python3 -m pip install -r dev-requirements.txt
```

Agora para gerar o relatório é preciso que você precisa chamar o comando **`inventory_report`** passando seus argumentos:

```
inventory_report argumento1 argumento2
```

**argumento1**: deve receber o caminho de um arquivo a ser importado. O arquivo pode ser um **csv**, **json** ou **xml**.

**argumento2**: pode receber duas strings: simples ou completo, cada uma gerando o respectivo relatório.

## Habilidades trabalhadas:

-   Uso do terminal interativo do Python.
-   Utilização de estruturas condicionais e de repetição.
-   Leitura e escrita de arquivos (XML, CSV, JSON).
-   Tratamento de exceções em Python.
-   Escrita de teste com Pytest.
-   Utilização de módulos proprios e importação em outros códigos.
-   Padrões de projeto.
-   Orientação a Objetos em Python.

## Tecnologias

-   **Python** - Linguagem de programação
-   **Pytest** - Ferramenta de teste Python
-   **Flack8** - Linter de códigos python
-   **Black** - Formatador de código Python

## Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
  pytest
```
