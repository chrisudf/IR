import os
import re
import xml.etree.ElementTree
import datetime
from collections import Counter
from collections import defaultdict
import collections
import gc

starttime = datetime.datetime.now()

task = open('C:/Users/Qiu/Desktop/' + 'tttest' + '.txt','w')
word=''
f1=open("C:/Users/Qiu/Desktop/dataset/common_words.txt")
for line in f1:
  line = re.sub("\n", ""
                      " ", line)
  word+=line
word=word.split(' ')

path = "C:/Users/Qiu/Desktop/dataset/cranfieldDocs"
fnum=(len(os.listdir(path)))

files= os.listdir(path)
# dic=collections.defaultdict(list)
dic=[]
count=0
#read files by files and read line in files line by line
#operations on each line
for file in files:
   if not os.path.isdir(file):
        f = open(path+"/"+file)
        str =""
        count+=1
        for line in f:
            line = re.sub("\n", " ", line)
            str = str + line
            #using regular expression elimate tag content
            str = re.sub((re.compile('<.*?>')), ' ', str)
            #using regular expression convert other characters into '\s'
            str = re.sub((re.compile("[^a-z0-9\s]")), ' ', str)
            str=str.lower()
        dic.append(str)
   gc.collect()

s=dic
s=''.join(s)
s=s.split(' ')
# print(dic,file=task)
# print(len(dic))
token=[]
for i in s:
   if i not in word:
       if (i!=''):
           token.append(i)

for i in range(0,len(dic)):
   tok = []
   dic[i]=''.join(dic[i])
   dic[i] = dic[i].split(' ')
   for j in dic[i]:
       if(j!=''):
           if j not in word:
               tok.append(j)
   dic[i]=tok
# print(dic)
# print(len(dic))
# print(type(dic))
#
# print(token,file=task)
print(len(token))

q = Counter(token).most_common(1000)
print(q,file=task)
# print(q[0])
# print(q[0][0])
w=[]
for i in range(1000):
    w.append(q[i][0])

f=[]
for i in range(1000):
    f.append(q[i][1])

v=[[0 for x in range(1000)] for y in range(fnum)]

tf=[]
for j in range(fnum):
    for i in w:
        counter=0
        for word in dic[0]:
            if i==word:
                counter+=1
        tf.append(counter/len(dic[0]))
    v[j]=tf
    gc.collect()

print(v,file=task)
# for j in range(fnum):
#     flag = 0
#     for i in w:
#         if i in dic[j]:
#             flag+=1
# idf=[]
# for i in w:
#     flag=0
#     if i in dic[0]:
#         flag+=1
# idf.append(flag)

#########################################################
endtime = datetime.datetime.now()
print ((endtime - starttime).seconds)


####################################
# print(w[25])
# fik=[]
# for i in w:
#     counter=0
#     for word in dic[0]:
#         if i==word:
#             counter+=1
#     fik.append(counter)
# v[0]=fik
# print(v[0][3])
# print(fik)
# print(len(fik))

# tf=[]
# for j in range(fnum):
#     for i in w:
#         counter=0
#         for word in dic[0]:
#             if i==word:
#                 counter+=1
#         tf.append(counter/len(dic[0]))
#     v[j]=tf

