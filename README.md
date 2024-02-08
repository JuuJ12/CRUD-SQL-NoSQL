# CRUD-SQL-NoSQL

Sistema Computacional Web (Com Interface Gráfica) Utilizando o BD RELACIONAL MYSQL e Framework STREAMLIT (Python).

CRUD NoSQL Utilizando ArangoDB.

## Clonando o projeto

1. Abra o terminal e navegue até o diretório onde deseja clonar o projeto.
2. Clone o repositório do GitHub utilizando o seguinte comando:


```
git clone https://github.com/JuuJ12/CRUD-SQL-NoSQL

```

```
Instale as Bibliotecas Necessarias
pip install streamlit
pip install mysql-connector-python
```
```
Insira as Informações Necessárias Para Conectar-se Com o Seu Banco de Dados no Arquivo "conectar_com_banco.py"
```

```
Vá ao Terminal e Execute o Comando streamlit run tela.py
```
________________________________________________

## Uso do CRUD NoSQL:

### Create:

```
INSERT {
    "nomeVinho": "V9",
    "tipoVinho": "rosé",
    "precoVinho": 400.00,
    "vinicolaID": "6" 
} IN Vinicola
```

"Vinicola" deve ser alterado para o nome de sua coleção.

### Delete:

```
REMOVE "1780" IN Vinicola
```

"1780" deve ser alterado para a key do conteúdo que você deseja remover.

### Read:

```
FOR doc IN Vinicola
    RETURN doc
```

"Vinicola" deve ser alterado para o nome de sua coleção.

### Update:

```
UPDATE "1677" WITH

{
    "precoVinho": 200
} IN Vinicola
```

"1677" deve ser alterado para a key do conteúdo que você deseja remover, e, "Vinicola" deve ser alterado para o nome de sua coleção.
