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
    # return {"name": "taha"} # yeh function json response day ga 



#----------  POST API-------------

# interface
class Data(BaseModel): # inherit with basemodel
   name : str
   age : int



@app.post("/")  #url
def post_function(data:Data):
#    return {
#       "name":f"my name is {data.name}",
#       "age":f"my age is {data.age}"
#            }
     names.append(data.name)
     return names


#------------------------------delete api----------------


@app.delete("/{name}")
def delete_data(name):
  names.remove(name)
  return names
#    "message": f"Item with ID {item_id} deleted successfully"

   



#-----------------------update API-----------------

@app.put("/{name}")
def update_data(name:str, data:Data):
   
   #logic
   return names

# @app.put("/{item_id}")
# def update_data(item_id:int, data:Data):
#    #logic
#    return{
#         "message": f"Item with ID {item_id} updated successfully",
#         "name": f"my name is {data.name}",
#         "age": f"my age is {data.age}"
#    }









