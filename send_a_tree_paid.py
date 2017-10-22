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
    birth_weight={1970:0,1971:0,1972:0,1973:0,1974:0,1975:0.1,1976:0.2,1977:0.3,1978:0.4,1979:0.5,1980:0.6,1981:0.7,1982:0.8,1983:0.9,1984:1,1985:1.1,1986:1.2,1987:2.4,1988:3,1989:3.1,1990:4.9,1991:6.5,1992:7.1,1993:8,1994:6,1995:4.5,1996:3.9,1997:3.4,1998:2.5,1999:2.4,2000:2.1}
    gender_weight={"male":2,"female":4,"not_provided":4}
    country_weight={"2.84.0.0":3, '1.72.0.0':10, "49.144.0.0":2, "41.0.0.0":1, "151.106.0.0":8}
    source_weight={"google":5,"invite_a_friend":7, "article":3,"paid":1}
    date_weight={0:26104,1:15660,2:7288,3:6387,4:6091,5:5813,6:5724,7:5549,8:5190,9:4953,10:4699,11:4579,12:4085,13:3994,14:3883,15:3489,16:3212,17:2808,18:2630,19:2532,20:2480,21:2423,22:2404,23:2236,24:2009,25:1971,26:1963,27:1931,28:1923,29:1904,30:1833,31:1681,32:1623,33:1614,34:1592,35:1584,36:1566,37:1515,38:1502,39:1441,40:1417,41:1402,42:1374,43:1293,44:1259,45:1245,46:1225,47:1183,48:1182,49:1122,50:1059,51:1049,52:1039,53:1025,54:967,55:964,56:958,57:953,58:905,59:870,60:849,61:848,62:826,63:808,64:789,65:785,66:736,67:708,68:656,69:656,70:639,71:623,72:617,73:612,74:606,75:552,76:532,77:519,78:508,79:505,80:488,81:459,82:430,83:423,84:383,85:376,86:367,87:340,88:320,89:317,90:314,91:289,92:250,93:247,94:242,95:222,96:199,97:189,98:175,99:120}
    supertree_multiplier=random.randint(40,60)/100

    #CALCULATION
    datediff=abs(datetime.strptime(user_info[0], "%Y-%m-%d")-datetime(year, month, day, 0,0,0,0)).days
    if datediff > 79:
        date_weight[datediff]=500

    #a=send_a_tree
    a=date_weight[datediff]/203930
    b=birth_weight[int(user_info[4])]/67.6
    c=gender_weight[user_info[5]]
    d=country_weight[user_info[6]]
    e=source_weight[user_info[7]]
    f=1+random.randint(-5,20)/10
    g=supertree_multiplier

    send_list[user_info[2]] = int(a*b*c*d*e*f*g)
    number_of_sends+=int(a*b*c*d*e*f*g)

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
    print(final_date, sended[i], "sent_a_super_tree")
