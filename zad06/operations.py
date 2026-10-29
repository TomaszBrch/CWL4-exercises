import json


def write_to_txt(people):  # pyright: ignore[reportUnknownParameterType, reportMissingParameterType]
    with open("dane.txt", "w") as f:
        for person in people:  # pyright: ignore[reportUnknownVariableType]
            line: str = str(type(person).__name__) + ";" + ";".join(str(val) for val in person.__dict__.values())  # pyright: ignore[, reportUnknownMemberType, reportUnknownArgumentType, reportUnknownVariableType]
            _=f.write(line + "\n")
def write_to_json(people_dict):  # pyright: ignore[reportUnknownParameterType, reportMissingParameterType]
    with open("dane.json", "w") as f:
        json.dump(people_dict,f,indent=4)
