import time
from itertools import product
import os

len=int(input("\nEnter lenght : "))
minlen=3
# chrs="اتقسکمی"
chrs=input("Input combination :")

getMilli=lambda: int(round(time.time() * 1000))
loadb=getMilli()
dic=[]
with open("dic.txt","r") as f:
    for line in f:
        dic.append(line.strip())
loade=getMilli()
print("Took "+str(loade-loadb)+" milliseconds to load dictionary into RAM!")
loadb=getMilli();
words=[]
count=0;
f=open('temp.txt','w')
for counter in range (minlen,len+1):
    print("Starting stage "+str(counter)+"!\n------------------")
    for i in product(chrs, repeat=counter):
            temp=''.join(i)
            words.append(temp)
            if temp in dic:
                print("Fround!")
                count+=1
                f.write(temp+"\n")
                f.flush()
    print("------------------\nStage "+str(counter)+" done!\n")
loade=getMilli();
f.close()

print("Removing Duplicates!")
lines_seen = set() 
outfile = open("output.txt", "w")
for line in open("temp.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
    else:
        count-=1
outfile.close()
os.remove("temp.txt")
print("Took "+str((loade-loadb)/1000)+" seconds to execute! \n"+str(count)+" item(s) found!")
