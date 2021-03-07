import json
import codecs
import argparse
import sys


def convert(fname):

    if fname.split(".")[1] != ".ipynb":
        print(
            """
        Must be a .ipynb file.
        Exiting.....
        """
        )
        sys.exit(0)

    else:
        f = codecs.open(fname, encoding="utf-8")
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

        with open(fname.split(".")[0] + "-converted.ipynb", mode="w") as output_file:
            json.dump(source, output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="convert Plutojl notebook to a Ipython notebook"
    )

    parser.add_argument(
        "--fname", type=str, required=True, help="Name of the file to convert"
    )

    args = parser.parse_args()

    convert(fname=args.fname)