# 本代码是在其他代码的基础上进行修改和优化
# 链接：https://gist.github.com/Vopaaz/c5da9c71b7ac0723860fd48ffb977f27

import json
import re


def parse_header(raw_header: str , msg : bool = False ):

    dict_header = dict()

    for line in raw_header.split("\n"):

        # 跳过空行或纯注释行（如果有的话）
        if not re.match(r'^(.*?):\s', line) :

            if msg : # msg == True
                print('parse_header warnMsg: "' + line + '" Format Error')

            continue

        # 拆分键值对
        key, value = line.split(":", 1)

        # 去除 键值对 的空格
        dict_header[ key.strip() ] = value.strip()

    return dict_header

header = """
GET / HTTP/1.1
Host: 127.0.0.1:8080
Upgrade-Insecure-Requests: 1
Accept-Language: zh-CN,zh;
Cache-Control: no-cache
Connection: keep-alive
Pragma: no-cache
Accept-Encoding: gzip, deflate
"""

print(json.dumps(parse_header(header),indent=4))

"""
输出结果示例

{
    "Host": "127.0.0.1:8080",
    "Upgrade-Insecure-Requests": "1",
    "Accept-Language": "zh-CN,zh;",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Accept-Encoding": "gzip, deflate"
}
"""
