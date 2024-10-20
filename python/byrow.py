# iconv-line.txt 数据来源：https://gist.github.com/hakre/4188459

import sys

#参数1：要操作的文件名
#参数2：分割符（字符串） 默认为：none  按照多个空白字符分割
def byrow(file_path : str , delimiter : str = None):

    result = []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()


    for line in lines:
        # 去除行末的换行符并按空格分割
        items = line.strip().split(delimiter)
        for item in items:
            # item 字符串 不为空
            if item :
                result.append(item)

    return result


# iconv-line.txt 数据来源：https://gist.github.com/hakre/4188459

input_file  = r'./test/byrow/iconv-line.txt'
output_file = r"./test/byrow/iconv-list.txt"
delimiter   = None

# 该脚本支持传入参数指定读取和写入的文件
# 参数1 读取内容的文件
# 参数2 写入内容的文件
# 参数3 分割内容的标识符 可选
# 示例： python byrow.py ./test/byrow/iconv-line.txt ./test/byrow/iconv-list.txt /
if len(sys.argv) == 3 or len(sys.argv) == 4 :
    input_file  = sys.argv[1]
    output_file = sys.argv[2]
    try:
        delimiter = sys.argv[3]
    except IndexError:
        delimiter = None

result = byrow(input_file,delimiter)

with open(output_file, 'w', encoding='utf-8') as output_file:
    for item in result:
        output_file.write(f"{item}\n")

"""
输入示例：
ANSI_X3.4-1968 ANSI_X3.4-1986 ASCII CP367 IBM367 ISO-IR-6 ISO646-US ISO_646.IRV:1991 US US-ASCII CSASCII
UTF-8
ISO-10646-UCS-2 UCS-2 CSUNICODE
UCS-2BE UNICODE-1-1 UNICODEBIG CSUNICODE11

输出结果：
ANSI_X3.4-1968
ANSI_X3.4-1986
ASCII
CP367
IBM367
ISO-IR-6
ISO646-US
ISO_646.IRV:1991
US
US-ASCII
CSASCII
UTF-8
ISO-10646-UCS-2
UCS-2
CSUNICODE
UCS-2BE
UNICODE-1-1
UNICODEBIG
CSUNICODE11
"""
