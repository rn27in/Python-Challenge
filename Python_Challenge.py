from  urllib2 import Request
import urllib2
import re
req = Request("http://www.pythonchallenge.com/pc/def/equality.html")
html = urllib2.urlopen(req).read().decode()

comments = re.findall("<!--(.*?)-->", html, re.DOTALL)
comments = comments[0]
temp = re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", comments)

''.join(temp)
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
###http://www.pythonchallenge.com/pc/def/linkedlist.html

#The page will redirect you to linkedlist.php

#http://www.pythonchallenge.com/pc/def/linkedlist.php

#####Problem 4###########################################################################
temp = Request("http://www.pythonchallenge.com/pc/def/linkedlist.php")
init = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044"
init = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
for elem in range(400):
    print elem
    #print html
    temp = Request(init)
    html = urllib2.urlopen(temp).read().decode()
    match = re.search(r'and the next nothing is ([0-9]+)', html).group(1) if not '16044' in html else str(16044/2)
    if match is not None:
        init = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+match



temp = Request("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
temp1 = urllib2.urlopen(temp)
html = temp1.read()

###Problem 5 peak.html

###http://www.pythonchallenge.com/pc/def/peak.html

###Problem 6##############################################################
#http://www.pythonchallenge.com/pc/def/peak.html
req = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
import pickle
temp = pickle.load(req)
for line in temp:
    print "".join([k*v for k,v in line])

#http://www.pythonchallenge.com/pc/def/channel.html
