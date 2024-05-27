# FastAPI IBGE Distritos

Esta é uma aplicação FastAPI que consome a API do IBGE para obter uma lista de distritos brasileiros. A aplicação permite a ordenação dos distritos pelo nome.

This is a FastAPI application that consumes the IBGE API to obtain a list of Brazilian districts. The application allows sorting districts by name

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/adrianomeneze/LocalidadesIBGE.git
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate   # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Executar a Aplicação

Para iniciar o servidor FastAPI, execute o seguinte comando:

```bash
uvicorn main:app --reload
```

## Endpoints

### Obter Distritos 

Ordenar distritos alfabeticamente pelo nome:

```bash
http://127.0.0.1:8000/distritos?orderBy=nome
```
Visualizar distritos em modo nivelado:

```bash
http://127.0.0.1:8000/distritos?view=nivelado
```

## Executar Testes

Para rodar os testes, utilize o comando:
```bash
pytest
```