from fastapi import FastAPI
from pydantic import BaseModel


#instance of fastapi
app = FastAPI()

names = ["taha", "ali", "ahmed"]  # list of names






# yeh static api hai jo kisi bhi url par chale gi
#Get request ka  endpoint define kar raha hai jo root ("/") par chaly gi

@app.get("/")
def get_function():  # jab url call hoga function khud sy chalga
    return names # yeh function json response day ga 
   


#----------  POST API-------------

# interface
class Data(BaseModel): # inherit with basemodel
   name : str
  



@app.post("/")  #url
def post_function(data:Data):
#    
     names.append(data.name)
     return names


#------------------------------delete api----------------


@app.delete("/{name}")
def delete_data(name):
  names.remove(name)
  return names

   



#-----------------------update API-----------------

@app.put("/{name}")
def update_data(name:str, ):
   
   #logic
   return names










