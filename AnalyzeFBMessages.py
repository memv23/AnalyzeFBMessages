# Import necessary modules
##################################################
import json
import csv
from itertools import zip_longest
import re
##################################################


# Load JSON file
##################################################
with open('messages.json') as f:
    data = json.load(f)
##################################################


# Initialize lists
##################################################
xsender = []
xtime = []
xmessage = []
xtype = []
##################################################


# Separate JSON file into lists
##################################################
for i in range(len(data['messages'])):
    a = data['messages'][i]
    xl = []
    for j in a:
        b = a[j]
        xl.append(b)
        if len(xl) == 4:
            xsender.append(xl[0])
            xtime.append(xl[1])
            xmessage.append(xl[2])
            xtype.append(xl[3])
##################################################


# Reverse all lists so they are in chron. order
##################################################
xsender.reverse()
xtime.reverse()
xmessage.reverse()
xtype.reverse()
##################################################


# Delete messages that are not "Generic" type
##################################################
klist = []
for k in range(len(xsender)):
    if xtype[k] != 'Generic':
        klist.append(k)
        
cntk = 0
for m in klist:        
    del xsender[m-cntk]
    del xtime[m-cntk]
    del xmessage[m-cntk]
    del xtype[m-cntk]
    cntk = cntk+1
##################################################
    

# Delete messages that are not strings
##################################################
ulist = []
for u in range(len(xsender)):
    if type(xmessage[u]) != type("abcd"):
        ulist.append(u)
        
cntu = 0
for n in ulist:
    del xsender[n-cntu]
    del xtime[n-cntu]
    del xmessage[n-cntu]
    del xtype[n-cntu]
    cntu = cntu+1
##################################################


# Prepare data for CSV file
##################################################
x = [xsender,xtime,xmessage,xtype]
zpdat = zip_longest(*x,fillvalue = '')
##################################################


# Write data to CSV file
##################################################
with open('csvfile.csv','w',encoding="utf8",newline='') as f2:
    wr = csv.writer(f2)
    wr.writerow(("Sender","Time","Message","Type"))
    wr.writerows(zpdat)
f2.close()
##################################################
