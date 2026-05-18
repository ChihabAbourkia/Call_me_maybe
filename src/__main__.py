
from .parse_args import arg_parse
from .json_loader import functions_loader, prompt_loader

def main():
    print("🤖 Starting LLM fuction calling system....")
    parse = arg_parse()

    print("📂 Loading Functions and promts...")
    functions = functions_loader(parse.functions_definition)
    prompts = prompt_loader(parse.input)
    print(prompts)

main()
