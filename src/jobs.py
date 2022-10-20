import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, "r") as file:
        content = csv.DictReader(file)
        new_content = list(content)
    return new_content
