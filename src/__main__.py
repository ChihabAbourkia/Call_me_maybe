
from .parse_args import arg_parse
from .json_loader import functions_loader, prompt_loader
from .constrained_decoding import system_prompt_biulder, vocab_filter, vocab_loder, mask_logits, next_valid_token, json_format
from llm_sdk.llm_sdk import Small_LLM_Model
import numpy as np

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

    print("✅ building valid ids")
    path = model.get_path_to_tokenizer_file()
    vocab  = vocab_loder(model)
    clean_vocab_id = vocab_filter(vocab)
    print("🧠 prossicing prompts... :")

    for p in prompts:
        prompt = p.prompt
        full_prompt = f"{system}\nuser:{prompt}\nAssistant:"
        all_generated = []
        all_generated.extend(model.encode('{"name": "')[0].tolist())
        clean_json = None
        for _ in range(50):
            input_id = model.encode(full_prompt)[0].tolist()
            logits = model.get_logits_from_input_ids(input_id + all_generated)
            next_token = next_valid_token(logits, clean_vocab_id)
            all_generated.append(next_token)
            text = model.decode(all_generated)
            print(text)
            clean_json = json_format(text)
            if clean_json:
                print("json ===", clean_json)
                break
            else:
                continue










if __name__ == "__main__":
    main()
