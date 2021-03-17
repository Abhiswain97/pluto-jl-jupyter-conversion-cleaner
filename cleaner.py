import json
import codecs
import argparse
import sys
from fire import Fire


def clean(path: str):

    assert type(path) == str

    if path.split(".")[1] != "ipynb":
        raise Exception("Must be a .ipynb file")
    else:
        f = codecs.open(path, encoding="utf-8")
        source = json.loads(f.read())

        for cell in source["cells"]:
            s = cell["source"]
            if "md" in s[0]:
                if len(s) == 1:
                    s[0] = s[0].replace("md", "").replace('"', "")
                else:
                    s.pop(0)
                    s.pop()
                cell["cell_type"] = "markdown"
                cell.pop("execution_count")
                cell.pop("outputs")

        with open(path.split(".")[0] + "-cleaned.ipynb", mode="w") as output_file:
            json.dump(source, output_file)


if __name__ == "__main__":

    Fire(clean)