from fastapi import FastAPI, Form
import uvicorn

import os
from dotenv import load_dotenv

load_dotenv()

database = "test"
password = os.getenv("DB_PASSWORD")
user = os.getenv("DB_USER")

import psycopg2

class ConnectionDB:
    def __init__(self, user, password, database):
        self.connect = psycopg2.connect(
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connect.cursor()

    def select(self, query, vars = None):
        self.cursor.execute(query, vars)
        return [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
    
    def close(self):
        self.cursor.close()

app = FastAPI()

con = ConnectionDB(user=user, password=password, database=database)

@app.get("/")
async def main():
    return None

@app.get("/get_all_data")
async def get_all_data():
    return con.select("select * from people limit 5")

@app.get("/get_ten_data")
async def get_ten_data():
    return con.select("select * from people limit 10")

@app.post("/search_by_name")
async def search_by_name(name: str = Form(None)):
    return con.select(f"select * from people where name='{name}'") if name else None

if __name__ == '__main__':
    uvicorn.run(
        app='Fast_api_test:app',
        host='localhost',
        port=8000,
        workers=4
    )
    con.close()