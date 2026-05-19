import json

def vocab_loder(model):
     with open(model.get_path_to_tokenizer_file(), "r", encoding= "utf-8") as file:
          data = json.load(file)
     vocab = data.get("model", {}).get("vocab", {})
     return vocab

def vocab_filter(vocab):
     safe_json = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    '0123456789*.,_:-+/\'!?()[]{}"ĠĊ\\')
     valid = set()
     for token_str, token_id in vocab.items():
        print(token_str)
        if token_str and all(c in safe_json for c in token_str):
             valid.add(token_id)
     return valid


def system_prompt_biulder(functions):
     lines = [
        "STRICT SYSTEM RULES: use ONLY a matching function "
        "from the list below",
        "If No function matches the user's intent (even if "
        "types match), set name:\"none\".",
        "Never use an unrelated function for a differnet task.",
        "",
        "Available functions:",
	 ]
     for f in functions:
          param = []
          for p , info in f.parameters.items():
               param.append(f" {p} : {info.type}")
          params = ",".join(param)
          lines.append(f" -{f.name}({params}): {f.description}")

     lines.append('\nOutput ONLY valid JSON: '
        '{"name": "<fn>", "args": "{<args>}"}')
     return "\n".join(lines)



