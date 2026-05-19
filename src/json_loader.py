
import  json
from .json_validation import FunctionValidation, PromtValidation

def functions_loader(path : str):
    try:
        with open(path, "r", encoding= "utf-8") as file:
            data = json.load(file)
        return [FunctionValidation(**item) for item in data]
    except FileNotFoundError as e :
        print(f"ERROR : {e}")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR : {e}")
        exit(1)


def prompt_loader(path):
    try:
      with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
      return [PromtValidation(**item)for item in data]
    except FileNotFoundError as e :
        print(f"ERROR : {e}")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR : {e}")
        exit(1)
