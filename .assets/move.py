import os
import secrets
import json
from tqdm import tqdm


with open("data.json") as f:
    data = json.load(f)


imgs: list[str] = []


for roots, _, files in os.walk("converted"):
    for file in tqdm(files):
        path = os.path.join(roots, file)
        _id = secrets.token_hex(16)
        while True:
            if _id not in data["used_ids"]:
                break
            _id = secrets.token_hex(64)
        with open("data.json", "w") as f:
            data["used_ids"].append(_id)
            json.dump(data, f, indent=True)
        new_path = os.path.join(os.path.dirname(roots), "indexed", f"{_id}.jpg")
        os.replace(path, new_path)
import gen_html