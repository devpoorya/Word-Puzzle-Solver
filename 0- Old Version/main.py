from itertools import product
from string import ascii_letters, digits
import csv

len=int(input("Lenght : "))
chrs=input("Enter Combo : ")
f=open("output.txt","w")
minlen=3
for counter in range(minlen,len+1):
    for i in product(chrs, repeat=len):
        city=''.join(i)
        with open('dic.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            try:
                for row in reader:
                    # print("**"+row['farsi']+"**"+city+"**")
                    if row['farsi'] == city or row['farsi'].replace('ي','ی')==city:
                        f.write(city+"\n")
                        f.flush()
                        print("Fround !")
                        break
            except ValueError:
                print ('incorrect value')
    f.close()
print("Done!")
