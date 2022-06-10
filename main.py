from fastapi import FastAPI
import db
app = FastAPI()






@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/client")
async def get_client():
   rv = db.select_data(db.connect_mongo(),'CreditRepair','person')
   return rv

@app.get("/client/{ssn}")
async def get_client_ssn(ssn: str):
    rv = db.select_one(db.connect_mongo(),'CreditRepair','person',{'ssn':ssn})
    return rv

