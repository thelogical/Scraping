import json
import urllib2
import re
import requests
import os
import sys

if(len(sys.argv) < 0):
    print("Usage: python /path/to/final.py pages city")
    quit()

p = int(sys.argv[1])
if(p < 0 or p > 100):
    print("Error: page range(0 - 100),exiting")
    quit()

pages=sys.argv[1]

cities = ['ahmedabad','bangalore','mumbai','nagpur','delhi','kolkata','surat','jaipur']

if(sys.argv[2] not in cities):
    print("valid cities=>",cities)
    quit()

city = sys.argv[1]

os.chdir("data")

f = open("bwdata.txt",'w')
f2 = open("burls.txt",'w')
base = "https://photographers.canvera.com"                             
for i in range(0,pages):
    url="https://photographers.canvera.com/getphjson?photographer_url=/"+city+"&location=&categoryFilter=&budget=&tab=all&isCategory=false&categoryName=wedding&withoutimage=false&withoutbudget=false&sortbyprice=&sortbydefault=false&sortbytopview=false&sortbypopularity=false&sortbyuserratings=true&p="+str(i)+"&includeVideographer=no"
    response = urllib2.urlopen(url)
    data = json.load(response)
    for j in range(0,20):
        f.write(data['photographers'][j]['company']+",")
        f.write(data['photographers'][j]['businessAddress']['city']['cityName']+',')
        f.write(data['photographers'][j]['businessAddress']['mobileNum'] + '\n')
        f2.write(base+data['photographers'][j]['companyUrl']+'\n')
f.close()
f2.close()
'''
'''
f = open("burls.txt",'r')
f6 = open("burls2.txt",'w')
urls = f.readlines()

for url in urls:
    try:
        res = urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        print(url)
        continue
    except urllib2.URLError, e:
        print(url)
        continue
    a = res.read()
    z = re.findall(r"<a.*href.*\"\n", a)
    q = z[-1].split(" ")[-1][6:-2]
    if "void(0)" in q:
        f6.write("N/A\n")
        continue
    f6.write(q+'\n')
    print(q)

f.close()
f6.close()

f3 = open("burls2.txt",'r')
f5 = open("bemails.txt",'w')
urls = f3.readlines()
f3.close()
i = 1
for url in urls:
    try:
        print(str(i)+"/200")
        i=i+1
        if(url=='N/A\n'):
            f5.write("N/A\n")
            continue
        res = urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        f5.write("N/A\n")
        continue
    except urllib2.URLError, e:
        f5.write("N/A\n")
        continue
    except ValueError, e:
        f5.write("N/A\n")
        continue
    a = res.read()
    m = re.findall(r"\w+\.?\w+@[a-z|A-Z]+\.[a-z|A-Z]+", a)
    if not m:
        f5.write("N/A\n")
        continue
    f5.write(m[0]+'\n')

f5.close()

f = open(city+'.txt','w')
f2 = open('bwdata.txt','r')
f3 = open('bemails.txt','r')
rows = f2.readlines()
emails = f3.readlines()
for i in range(0,len(rows) - 1):
    f.write(rows[i][:-1]+","+emails[i][:-1]+'\n')

f.close()
os.remove('bwdata.txt')
os.remove('bemails.txt')
os.remove('urls.txt')
os.remove('urls2.txt')


