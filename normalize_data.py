import csv
import sys
import os
from pprint import pprint


def normalize_data(fp):
    fp_tuple = os.path.splitext(fp)
    ext = fp_tuple[-1]
    fn = fp_tuple[0]
    if (ext == ".tsv"):
        delimiter = "\t"
    else:
        delimiter = ","
    args = {"file": fp, "mode": "r",
            "encoding": "utf-8"}
    with open(**args) as csvfile:
        csvdata = csv.reader(csvfile, delimiter=delimiter)
        rows = [[r.strip() for r in row] for row in csvdata]
    new_fn = "{}_normalized{}".format(fn, ext)
    args["file"] = new_fn
    args["mode"] = "w"
    print(rows)
    with open(**args) as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=delimiter)
        csvwriter.writerows(rows)
    # pprint(rows)


if __name__ == "__main__":
    fp = sys.argv[-1]
    normalize_data(fp)
