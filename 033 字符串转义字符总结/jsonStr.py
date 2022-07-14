# -*- encoding: utf-8 -*-
"""
PyCharm jsonSt5r
2022年07月10日
by littlefean
"""
from typing import *
import json


def main():
    with open("js.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(
            str({
                "objName": "name",
                "objStr": str({
                    "arr": ["a", "b", "c"],
                    "age": 50
                })
            })
        ))

    b"\xff\xaa"
    print()
    "中文"
    a = 111
    return None


if __name__ == "__main__":
    main()
