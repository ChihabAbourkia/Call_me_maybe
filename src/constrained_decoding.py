import json
import numpy as np


def json_format(text):
    start = text.find("{")
    if start == -1:
        return None
    brace_count = 0
    for i in range(len(text)):
        if text[i] == "{":
            brace_count += 1
        if text[i] == "}":
            brace_count-= 1
        if brace_count == 0:
            return text[start:i+1]
    return None




def mask_logits(logits, vocab_id):
    for id in range(len(logits)):
        if id not in vocab_id:
            logits[id]  = -float('inf')
    return logits

def next_valid_token(logits, vocab_id):
    masked_logits = mask_logits(logits, vocab_id)
    next_token  = np.argmax(masked_logits)
    return next_token

def vocab_loder(model):
    with open(model.get_path_to_tokenizer_file(), "r", encoding="utf-8") as file:
        data = json.load(file)
    vocab = data.get("model", {}).get("vocab", {})
    return vocab


def vocab_filter(vocab):
    safe_json = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    '0123456789*.,_:-+/\'!?()[]{}"ĠĊ\\')
    valid = set()
    for token_str, token_id in vocab.items():
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
        for p, info in f.parameters.items():
            param.append(f" {p} : {info.type}")
        params = ",".join(param)
        lines.append(f" -{f.name}({params}): {f.description}")

    lines.append('Output ONLY valid JSON: '
                 '{"name": "<fn>", "args": "{<args>}"}')
    return "\n".join(lines)
