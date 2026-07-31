#!/usr/bin/env python3
"""将 data.json 内嵌到 index.html 的 const data = {...} 位置。

用法:
    python3 embed.py               # 默认读取 data.json -> index.html
    python3 embed.py --check       # 仅检查是否同步，不写入
"""

import json
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def embed(data_path=None, html_path=None, check_only=False):
    data_path = data_path or os.path.join(SCRIPT_DIR, "data.json")
    html_path = html_path or os.path.join(SCRIPT_DIR, "index.html")

    # 读取数据
    with open(data_path) as f:
        data = json.load(f)

    json_str = json.dumps(data, ensure_ascii=False)

    # 读取 HTML
    with open(html_path) as f:
        html = f.read()

    # --- 定位 const data = {...}; ---
    marker = "const data = {"
    pos = html.find(marker)
    if pos == -1:
        print("ERROR: 'const data = {' 未在 index.html 中找到")
        return False

    # start 指向 { 的位置
    start = pos + len(marker) - 1

    # 括号计数，找到匹配的 }
    depth = 1
    i = start + 1
    in_string = False
    escape = False

    while i < len(html) and depth > 0:
        c = html[i]
        if escape:
            escape = False
        elif c == "\\":
            escape = True
        elif c == '"':
            in_string = not in_string
        elif not in_string:
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
        i += 1

    if depth != 0:
        print("ERROR: 括号不匹配，无法定位 JSON 结束位置")
        return False

    # i 现在指向 } 之后的位置
    # 跳过紧随的 ;
    if i < len(html) and html[i] == ";":
        i += 1

    end = i  # 替换区间的结束位置

    existing_json = html[start:end]

    # 构造新的内嵌数据
    new_inline = json_str + ";"

    if check_only:
        if existing_json == new_inline:
            print("OK: data.json 与 index.html 已同步")
            return True
        else:
            print("MISMATCH: data.json 与 index.html 不一致，需要运行 embed")
            return False

    if existing_json == new_inline:
        print("已同步，无需更新。")
        return True

    # 替换
    new_html = html[:start] + new_inline + html[end:]
    with open(html_path, "w") as f:
        f.write(new_html)

    print(f"已嵌入: {data_path} -> {html_path}")
    return True


if __name__ == "__main__":
    check_only = "--check" in sys.argv
    embed(check_only=check_only)
