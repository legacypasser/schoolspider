__author__ = 'panboyuan'
from urllib import urlopen
import re

fixed = "http://gkcx.eol.cn/schoolhtm/specialty/specialtyList/specialty"

ids = open("ids.txt", "r")
i = 0
majors = open("majors.txt", "w")
buf = []
for eachline in ids:
    linestr = eachline.strip("\n")
    i += 1
    if len(buf) > 2048:
        print("finished " + bytes(i))
        majors.writelines(buf)
        buf = []
    resp = urlopen(fixed + linestr + ".htm")
    text = resp.read()
    result = re.findall("/schoolhtm/specialty/\d.*<", text)
    for item in result:
        startpos = item.find(">")
        buf.append(linestr + ";" + item[startpos + 1: -5] + "\n")

majors.writelines(buf)
majors.close()
ids.close()