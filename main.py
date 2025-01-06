from fastapi import FastAPI
# Import date
from datetime import date
# Import BaseModel
from pydantic import BaseModel



# Create an instance of FastAPI
app = FastAPI()


# Get operation review
# HTTP Protocol - several types of operations
# GET - Read data
#   Host: api.example.com
#   Port: 80
#   Path: /search
#   Query: ?q=fastapi


# Define a route to handle GET requests

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# cURL : client URL


# Query parameters
@app.get('/hello')
def hello(name: str = "Alex"):
    return {"message": f"Hello {name}"}

# Post - create a new object
# Parameters are sent by the body of the request
# The important thing to remember for now is that POST requests 
# can send much more information to the server than GET requests can.

# Http request body
# pydantic : interface to definw request and response body schemas



# Define model Item
class Item(BaseModel):
    name: str
    quantity: int = 0
    expiration: date = None

