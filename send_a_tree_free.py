import csv
import random
from datetime import datetime
import sys

year=int(sys.argv[1])
month=int(sys.argv[2])
day=int(sys.argv[3])

#LOADING USERS
userlist=[]
outpute=[]
datelist=[]
sended=[]
send_list={}
number_of_sends=0

with open('userlist.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        userlist.append(row)

for i in range(0,len(userlist)):
    user_info=userlist[i]

    #WEIGHTS
    birth_weight={1970:1,1971:3,1972:5,1973:6,1974:21,1975:25,1976:68,1977:160,1978:244,1979:514,1980:868,1981:1490,1982:2336,1983:3292,1984:4490,1985:5951,1986:7247,1987:8698,1988:9429,1989:9679,1990:9517,1991:8749,1992:7530,1993:6181,1994:4660,1995:3410,1996:2200,1997:1471,1998:880,1999:463,2000:219}
    gender_weight={"male":3,"female":8,"not_provided":8}
    country_weight={"2.84.0.0":5, '1.72.0.0':2, "49.144.0.0":3, "41.0.0.0":1, "151.106.0.0":6}
    source_weight={"google":4,"invite_a_friend":10, "article":5,"paid":4}
    date_weight={0:26104,1:15660,2:7288,3:6387,4:6091,5:5813,6:5724,7:5549,8:5190,9:4953,10:4699,11:4579,12:4085,13:3994,14:3883,15:3489,16:3212,17:2808,18:2630,19:2532,20:2480,21:2423,22:2404,23:2236,24:2009,25:1971,26:1963,27:1931,28:1923,29:1904,30:1833,31:1681,32:1623,33:1614,34:1592,35:1584,36:1566,37:1515,38:1502,39:1441,40:1417,41:1402,42:1374,43:1293,44:1259,45:1245,46:1225,47:1183,48:1182,49:1122,50:1059,51:1049,52:1039,53:1025,54:967,55:964,56:958,57:953,58:905,59:870,60:849,61:848,62:826,63:808,64:789,65:785,66:736,67:708,68:656,69:656,70:639,71:623,72:617,73:612,74:606,75:552,76:532,77:519,78:508,79:505,80:488,81:459,82:430,83:423,84:383,85:376,86:367,87:340,88:320,89:317,90:314,91:289,92:250,93:247,94:242,95:222,96:199,97:189,98:175,99:120}

    #CALCULATION
    datediff=abs(datetime.strptime(user_info[0], "%Y-%m-%d")-datetime(year, month, day, 0, 0, 0, 0)).days
    if datediff > 79:
        date_weight[datediff]=500

    #a=send_a_tree
    a=date_weight[datediff]/203930
    b=birth_weight[int(user_info[4])]/99807
    c=gender_weight[user_info[5]]
    d=country_weight[user_info[6]]
    e=source_weight[user_info[7]]
    f=1+random.randint(-5,20)/10

    send_list[user_info[2]] = int(a*b*c*d*e*f)
    number_of_sends+=int(a*b*c*d*e*f)

#USER_IDs should appear as many times as many messages they have sent

for i in send_list:
    if send_list[i]>0:
        x=send_list[i]
        while x > 0:
            x = x - 1
            sended.append(i)

for i in range(0,number_of_sends):
    hour = random.randint(0,23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    final_date = datetime(year, month, day, hour, minute, second).strftime('%Y-%m-%d')
    print(final_date, sended[i], "sent_a_free_tree")
