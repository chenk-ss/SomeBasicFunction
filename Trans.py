#!/user/bin/python3
# -*-coding:UTF-8-*-

def main(name1, name2):
    f1 = open('C:/Users/jsyl/Desktop/EntityTrans/file1.txt', 'r')
    f2 = open('C:/Users/jsyl/Desktop/EntityTrans/file2.txt', 'r')
    f1List = []
    f2List = []
    resultList = []
    readFile(f1, f1List)
    readFile(f2, f2List)
    if (len(f1List) != len(f2List)):
        print("---字段数量不同---")
        return

    a = 0;
    while (a < len(f1List)):
        sStr = setStr(f1List[a])
        gStr = getStr(f2List[a])
        resultList.append(name1 + sStr + "(" + name2 + gStr + "());")
        a = a + 1

    for i in resultList:
        print(i)


def setStr(str):
    return ".set" + str[0].upper() + str[1:]


def getStr(str):
    return ".get" + str[0].upper() + str[1:]


def readFile(f, fList):
    for str in f.readlines():
        str = str.strip()
        if (not len(str) or str.startswith("//")):
            continue
        # print(f1Str.strip())
        fList.append(str.split(" ")[-1].split(";")[0])


if __name__ == "__main__":
    """
    main中两个参数，第一个为需要set的名称，第二个为get的名称
    需set的字段放入file中，get的字段放入file2中
    两个实体中字段顺序和数量一致才能使用
    """
    main("bean", "entity")
