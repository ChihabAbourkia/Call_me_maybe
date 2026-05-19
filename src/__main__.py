
from .parse_args import arg_parse
from .json_loader import functions_loader, prompt_loader
from .constrained_decoding import system_prompt_biulder, vocab_filter, vocab_loder
from llm_sdk.llm_sdk import Small_LLM_Model


def main():
    print("🤖 Starting LLM fuction calling system....")
    parse = arg_parse()

    print("📂 Loading Functions and promts...")
    functions = functions_loader(parse.functions_definition)
    if not functions:
        raise RuntimeError("No function difinetion found...")
    prompts = prompt_loader(parse.input)
    if not prompts:
        raise RuntimeError("No input prompts found. Please provide at least one prompt.")

    print("⚙️ Sytem prompt...")
    system = system_prompt_biulder(functions)

    print("🛠️ Loading model...")
    try:
        model = Small_LLM_Model(parse.model)
    except OSError:
        raise RuntimeError(f"Model {parse.model} not found or field to download")

    print("  building valid ids")
    path = model.get_path_to_tokenizer_file()
    vocab  = vocab_loder(model)
    clean_vocab = vocab_filter(vocab)
    print(clean_vocab)



main()
