
import  json
from .json_validation import FunctionValidation, PromtValidation

def functions_loader(path):
        with open(path, "r", encoding= "utf-8") as file:
            data = json.load(file)
        return [FunctionValidation(**item) for item in data]

def prompt_loader(path):
      with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
      return [PromtValidation(**item)for item in data]
