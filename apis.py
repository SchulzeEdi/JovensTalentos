from fastapi import FastAPI
import pandas as pd 
import datetime as dt
import json
import sqlite3 as sql
app = FastAPI()

@app.get("/")
async def hello():
    return "hello!"

@app.get("/products")
async def all_products():
    conexao = sql.connect('globalstore_normalizada.db')
    products = pd.read_sql(
        con=conexao,
        sql='select * from products'
    )
    return products.to_json(orient = 'records')

@app.get("/products/pandas")
async def all_products_pandas():
    globalstore = pd.read_csv('globalstore.csv')
    products = globalstore[
        ['Product ID', 'Product Name', 'Category',
        'Sub-Category'
        ]
    ].drop_duplicates()
    return products.to_json(orient = 'records')

@app.get("/products/categorydf/{category_name}")
async def category_products(category_name: str):
    conexao = sql.connect('globalstore_normalizada.db')
    products = pd.read_sql(con=conexao, 
sql="select * from products")
    subcategory = pd.read_sql(con=conexao, 
sql="select * from subcategory")
    category = pd.read_sql(con=conexao, 
sql="select * from category")
    products = products.merge(subcategory, on='sub_sequence', how='left')
    products = products.merge(category, on='cat_sequence', how='left')
    return products[
products['category'] == category_name
].to_json(orient = 'records')

@app.get("/clientes")
async def cliente_mercado():
    conexao = sql.connect('globalstore_normalizada.db')
    clientes = pd.read_sql(con=conexao,
sql= "select * from customer")
    cidade = pd.read_sql(con=conexao,
sql= "select * from city")
    regiao = pd.read_sql(con=conexao,
sql= "select * from region")
    clientes = clientes.merge(cidade, on='cty_sequence', how='left')
    clientes = clientes.merge(regiao, on='reg_sequence', how='left')
    return clientes[
    clientes['market'] == ('LATAM' or 'US' or 'Canada')
    ].to_json(orient = 'records')

@app.get("pedidos_itens")
async def pedidos_itens():
    conexao = sql.connect('globalstore_normalizada.db')
    ordens = pd.read_sql(con=conexao,
sql = "select * from orders")
    items = pd.read_sql(con=conexao,
sql = "select * from items")
    