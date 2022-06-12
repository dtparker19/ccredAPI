from fastapi import FastAPI
import db

app = FastAPI()


def root():
    return {"message": "Hello World"}


def say_hello(name: str):
    print('say_hello')
    return {"message": f"Hello {name}"}


def get_client():
    print('get_client')
    rv = db.select_data('person')
    print(rv)
    for i in rv:
        print(i)
    return rv


def get_client_by_key(key: str):
    print('get_client_by_key')
    rv = db.select_one('person', {'person_key': key})
    return rv

if 1 == 1:
    get_client()