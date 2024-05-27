from fastapi import FastAPI, Query
import requests


app = FastAPI()

IBGE_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"


@app.get("/distritos")
def get_distritos(order_by: str = Query(None, alias="orderBy"), view: str = Query(None)):
    params = {}
    if order_by:
        params["orderBy"] = order_by
    if view:
        params["view"] = view

    response = requests.get(IBGE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Não foi possível recuperar dados do IBGE"}
