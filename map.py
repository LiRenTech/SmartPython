from os import listdir
from requests import get
from typing import Dict

result = []
format_ = "# 各个文件夹代表的视频\n\n> 这个文件由 [此脚本](./map.py) 自动生成，并且在每次提交时自动运行\n\n| 编号 | 标题 | 视频 |\n| - | - | - |\n{}\n"
videos: Dict[str, str] = {}  # example: { "050": "BVxxx" }

pn = 1
while True:
    # 2023-12-03 更新api
    resp = get(
        "https://api.bilibili.com/x/space/wbi/arc/search",
        params={"mid": "480804525", "ps": 50, "pn": pn},  # uid  # 每页数量  # 第几页
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42"
        },
    ).json()
    vlist = resp["data"]["list"]["vlist"]
    if len(vlist) > 0:
        for video in vlist:
            if video["title"].lower().startswith("【python技巧"):
                videos[video["title"][9:12]] = video["bvid"]
        pn += 1
    else:
        break

print(videos)

for dir in sorted(listdir(), key=lambda x: x[:3]):
    if dir[0].isdigit():
        result.append(
            f"| [{dir.split()[0]}](./{dir.replace(' ', '%20')}) | {dir[4:].replace('_', '.')} | [{videos[dir[:3]]}](https://www.bilibili.com/video/{videos[dir[:3]]}) |"
        )

print("write to map.md")

with open("./map.md", "w", encoding="utf-8") as f:
    f.write(format_.format("\n".join(result)))

print("success")
