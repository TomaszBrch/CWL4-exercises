import json

from .model import Professor, Student


def write_to_txt(people:list[Student|Professor]):
    with open("dane.txt", "w") as f:
        for person in people:
            line: str = str(type(person).__name__) + ";" + ";".join(str(val) for val in person.__dict__.values())  # pyright: ignore[reportAny]
            _=f.write(line + "\n")
def write_to_json(people_dict:list[dict[str, str|int]]):

    with open("dane.json", "w") as f:
        json.dump(people_dict,f,indent=4)