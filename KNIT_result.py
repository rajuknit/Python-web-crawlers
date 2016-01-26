from bs4 import BeautifulSoup
import operator
import urllib
'''
    Author-- Raju Varshney 13228
'''
def year2():
    url="http://knit.ac.in/coe/even2014/btreg_457ddla57.asp?reqsem=4&rollno="
    d={}
    print ""
    print("2nd year Result")
    print("Roll no. Based")
    roll =13201
    while roll<13251:
        #print(roll)
        web=urllib.urlopen(url+str(roll))
        html_content=web.read()
        soup = BeautifulSoup(html_content) # making soup
        n=soup.select('td[width="50%"]')[1]
        #print(n.text)
        m=soup.select('td')[-5]  
        #print(m.text)
        m=str(m.text)
        ll=m.index("/")
        ll=int(m[:ll])
        d[roll]=[ll,n.text]
        print(str(roll)+" "+str(n.text)+" "+str(m))
        roll+=1 
        if roll==13212 or roll==13225 or roll==13243:
            roll+=1   
    print ""
    print("Rank Based")
    print ""        
    d=sorted(d.items(), key=operator.itemgetter(1),reverse=True)
   
    for i in range(len(d)):
        print (str(d[i][0])+" "+str(d[i][1][1])+" "+str(d[i][1][0]))
    return d     
def sem5():
    url="http://knit.ac.in/coe/odd_2015/odx51fsp758g.asp?rollno="
    d={}
    print ""
    print("5th sem Result")
    print("Roll no. Based")
    roll =13201
    while roll<13251:
        #print(roll)
        web=urllib.urlopen(url+str(roll))
        html_content=web.read()
        soup = BeautifulSoup(html_content) # making soup
        n=soup.select('td[width="50%"]')[1]
        #print(n.text)
        m=soup.select('td')[-3]  
        #print(m.text)
        m=str(m.text)
        ll=m.index("/")
        ll=int(m[:ll])
        d[roll]=[ll,n.text]
        print(str(roll)+" "+str(n.text)+" "+str(m))
        roll+=1 
        if roll==13212 or roll==13225 or roll==13243:
            roll+=1   
    print ""
    print("Rank Based")
    print ""         
    d=sorted(d.items(), key=operator.itemgetter(1),reverse=True)
   
    for i in range(len(d)):
        print (str(d[i][0])+" "+str(d[i][1][1])+" "+str(d[i][1][0]))
    return d    
 
def year1():
    url="http://knit.ac.in/coe/even_2013_14/btIst.asp?rollno="
    d={}
    print ""
    print("1st year Result")
    print("Roll no. Based")
    roll =13201
    while roll<13251:
        #print(roll)
        web=urllib.urlopen(url+str(roll))
        html_content=web.read()
        soup = BeautifulSoup(html_content) # making soup
        n=soup.select('td[width="50%"]')[1]
        #print(n.text)
        m=soup.select('td')[-5]  
        #print(m.text)
        m=str(m.text)
        ll=m.index("/")
        ll=int(m[:ll])
        d[roll]=[ll,n.text]
        print(str(roll)+" "+str(n.text)+" "+str(m))
        roll+=1 
        #if roll==13212 or roll==13225 or roll==13243:
        #    roll+=1   
    print""
    print("Rank Based")
    print""       
    d=sorted(d.items(), key=operator.itemgetter(1),reverse=True)
   
    for i in range(len(d)):
        print (str(d[i][0])+" "+str(d[i][1][1])+" "+str(d[i][1][0]))
    return d    

s="""
Enter 1 for 1st year result
Enter 2 for 2nd year result
Enter 3 for 5th sem result
Enter 4 for overall result
"""
print(s)                       
n=int(raw_input())
if n==1:
    d1=year1()
if n==2:
   d2=year2()
if n==3:
   d3=sem5() 
if n==4:
    d1=year1()
    d2=year2()
    d3=sem5()
    d={}
    for i in range(len(d1)):
        d[d1[i][0]]=[d1[i][1][0],d1[i][1][1]]
    for i in range(len(d2)):
        d[d2[i][0]][0]+=d2[i][1][0]
    for i in range(len(d2)):
        d[d3[i][0]][0]+=d3[i][1][0] 
    d=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
    print ""
    print ""
    print "Result till 5th sem"
    for i in range(len(d)):
        print (str(d[i][0])+" "+str(d[i][1][1])+" "+str(d[i][1][0]))  
             
