# -*- codeing=utf-8 -*-
# @Time: 16:33
# @Author :liuwei
# @File:文件输出.
fp=open('note.txt','w')
print('今年有世界杯',file=fp)
fp.close()