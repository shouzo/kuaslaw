# -*- coding: utf-8 -*-

import sys


def main(n):
    fi = open(n).readlines()
    result = []

    for i in fi:
        if i.startswith("第 "):
            i = "# " + i
        elif i.startswith("第"):
            i = "## " + i
        elif i.startswith("中華民國"):
            i = "* " + i
        elif i.startswith("國立高雄應用科技大學"):
            i = "# " + i
        elif i[0] in "一二三四五六七八九":
            index = "一二三四五六七八九".index(i[0]) + 1
            i = "%d.  %s" % (index, i[2:])

        result.append(i.strip("  "))

    fo = open(n, "w")
    for i in result:
        fo.writelines(i)

if __name__ == "__main__":
    main(sys.argv[1])
