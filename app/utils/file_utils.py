import json
from pathlib import Path


def save_to_json(records, filename):
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = [record.to_dict() for record in records]

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Data saved successfully to {filename}")


def load_from_json(filename):
    path = Path(filename)

    if not path.exists():
        return []

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)