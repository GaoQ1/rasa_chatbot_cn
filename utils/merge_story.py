import codecs
import os

rootpath = os.getcwd() + os.sep + ".." + os.sep
readpath = os.path.join(rootpath, "1.md")
appendpath = os.path.join(rootpath + "data" + os.sep, "mobile_story.md")

with codecs.open(readpath, 'r', 'gbk') as f, codecs.open(appendpath, 'a', 'utf-8') as f2:
    f2.write('\n')
    for line in f:
        f2.write(line)
