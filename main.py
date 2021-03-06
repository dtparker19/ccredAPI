from fastapi import FastAPI
import db

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    print('say_hello')
    return {"message": f"Hello {name}"}


@app.get("/client")
async def get_client():
    print('get_client')
    rv = db.select_data('person')
    return rv


@app.get("/client/{key}")
async def get_client_by_key(key: str):
    print('get_client_by_key')
    rv = db.select_one('person', {'person_key': key})
    return rv
