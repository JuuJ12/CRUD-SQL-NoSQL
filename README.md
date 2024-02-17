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
Instale as Bibliotecas Necessárias
pip install streamlit
pip install mysql-connector-python
```

Insira as Informações Necessárias Para Conectar-se Com o Seu Banco de Dados vá na pasta SERVICES > conectar_com_banco.py

Execute o Arquivo Se Não Apontar Nenhum Erro, a Conexão Foi Feita Com Sucesso.



Vá ao Terminal e Execute o Comando streamlit run main.py

________________________________________________

## Uso do CRUD NoSQL:

### Create:

```
INSERT {
    "vinhoID": 90,
    "nomeVinho": "V9",
    "tipoVinho": "branco",
    "precoVinho": 500,
    "vinicolaID": 3
} IN Vinhos
```

"Vinhos" deve ser alterado para o nome de sua coleção, assim como os valores.

### Delete:

```
REMOVE "0000" IN Vinhos
```

"0000" e "Vinhos" devem ser alterado para a key e coleção do conteúdo que você deseja remover, respectivamente.

### Read:

```
FOR vinho IN Vinhos
  RETURN vinho
```

"Vinhos" deve ser alterado para o nome de sua coleção.

### Update:

```
UPDATE "0000" WITH

{
    "precoVinho": 200
} IN Vinhos
```

"0000" deve ser alterado para a key do conteúdo que você deseja remover, e, "Vinhos" deve ser alterado para o nome de sua coleção, assim como os valores.
