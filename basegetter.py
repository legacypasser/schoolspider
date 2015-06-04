__author__ = 'panboyuan'
# _*_ coding:utf-8 _*_

schoolf = open("schoolbase.txt", "w")
majorf = open("majorbase.txt", "w")
regionf = open("regionbase.txt", "w")

grouped = open("group.txt", "r")
inim = open("majors.txt", "r")

nameDic = {}
idtoregion = {}
idtomajor = {}
regionDic = {}
majorDic = {}
regionNum = 0
majorNum = 0

for item in grouped:
    content = item.strip("\n").split(",")
    nameDic[content[0]] = content[1]
    if not regionDic.has_key(content[2]):
        regionDic[content[2]] = bytes(regionNum)
        idtoregion[content[0]] = bytes(regionNum)
        regionNum += 1
    else:
        idtoregion[content[0]] = regionDic[content[2]]

print(bytes(regionNum) + "regions")

for item in inim:
    content = item.strip("\n").split(";")
    if not majorDic.has_key(content[1]):
        majorDic[content[1]] = bytes(majorNum)
        majorNum += 1
    if idtomajor.has_key(content[0]):
        idtomajor[content[0]] += majorDic[content[1]] + ","
    else:
        idtomajor[content[0]] = majorDic[content[1]] + ","

inim.close()
grouped.close()

listResult = []
for item in regionDic:
    listResult.append(regionDic[item] + ";" + item + "省" + "\n")
regionf.writelines(listResult)

listResult = []

for item in majorDic:
    listResult.append(majorDic[item] + ";" + item + "\n")
majorf.writelines(listResult)


listResult = []
for item in nameDic:
    if idtomajor.has_key(item):
        majorstr = idtomajor[item]
    else:
        majorstr = "-1"
    temp = nameDic[item] + ";" + idtoregion[item] + ";" + majorstr
    if temp[-1] == ",":
        should = temp[0: -1]
    else:
        should = temp
    listResult.append(should + "\n")

schoolf.writelines(listResult)

regionf.close()
majorf.close()

schoolf.close()