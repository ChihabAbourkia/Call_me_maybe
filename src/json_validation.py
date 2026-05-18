from pydantic import BaseModel

class PromtValidation(BaseModel):
    prompt : str


class ParmatersType(BaseModel):
    type : str


class ReturnType(BaseModel):
    type: str

class FunctionValidation(BaseModel):
    name : str
    description : str
    parameters : dict[str, ParmatersType]
    returns : ReturnType

