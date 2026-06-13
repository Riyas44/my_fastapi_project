from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

BASE_URL = "/api/v1"

class Item(BaseModel):
    user_id:int
    name :str

users =[]

#CREATE USER USING POST METHOD

@app.post(f"{BASE_URL}/create")
def create_item(item:Item):
    for user in users:
      if user["item_id"] == item.user_id:
          return {
                "message" : "Item already there", 
                "remarks" : "create differnet user"
                 }  
    users.append(item.dict())
    print(users)
    return {
    "message" : "Item created successfully", 
    "user_id" :item.dict()
    }

#GET ALL USERS USING GET METHOD

@app.get(f"{BASE_URL}/users")
def get_users():
    return {"users" : users}

#GET PARTICALUR USER WITH ID USING GET METHOD

@app.get(f"{BASE_URL}/users/{{id}}")
def get_user(id:int):
    for user in users:
        if user["user_id"] == id:
            return{
                "user" : user.dict()
            }
    return {
        "message" : "User Not found"
        }

#UPDATE USER RECORD USING PUT METHOD

@app.put(f"{BASE_URL}/users/{{id}}")
def update_user(id:int , item:Item):
    for index,user in enumerate(users):

        # Dict
        if isinstance(user,dict) and user["user_id"] == id:
            users[index] = item
            return{
                "message": "user updated successfully",
                "user" : item.dict()
            }
        
        # Item
        elif isinstance(user,Item) and user.user_id == id:
            users[index] = item
            return{
                "message": "user updated successfully",
                "user" : item.dict()
            }
        
    return {
        "message" : "user not found"
    }


#DELETE USER RECORD USING DELETE METHOD

@app.delete(f"{BASE_URL}/users/{{id}}")
def deleteUser(id: int):
     for index,user in enumerate(users):

        # Dict
        if isinstance(user,dict) and user["user_id"] == id:
            deleted_user= users.pop(index)
            return{
                "message": "user deleted successfully",
                "user" : deleted_user
            }
        
        # Item
        elif isinstance(user,Item) and user.user_id == id:
           deleted_user= users.pop(index)
           return{
                "message": "user deleted successfully",
                "user" : deleted_user
            }   
        
     return {
        "message" : "user not found"
     }
    