from pydantic import BaseModel

class Inssan(BaseModel):
    name : str
    age : int

chakhs = [ {"name": "ff",
            "age" : 3}
            ,{"name" : "chi",
          "age" : 22}]

wee = [Inssan(**item)for item  in chakhs]
print(wee)
