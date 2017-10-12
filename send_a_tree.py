import random
import sys
from numpy.random import choice
from datetime import timedelta
from datetime import datetime

number_of_new_users=int(sys.argv[1])

geoips = ["2.84.0.0", "1.72.0.0", "49.144.0.0", "41.0.0.0", "151.106.0.0"]
source = ["google", "invite_a_friend", "article", "paid"]
gender = ["male", "female", "not_provided"]
birth = [1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000]

#ATTRIBUTES
country_weight=[3,5,2,2,10]
source_weight=[3,9,2,1]
gender_weight=[4,10,9]
birth_weight=[2,1,5,17,41,86,142,290,543,962,1537,2330,3510,4637,6123,7305,8445,9335,9523,9232,8497,7362,6062,4689,3398,2317,1566,920,554,299,162]

#WEIGHTS
rand_min=-1
rand_max=1

country_weight=[i*(1+random.randint(rand_min,rand_max)/10) for i in country_weight]
source_weight=[i*(1+random.randint(rand_min,rand_max)/10) for i in source_weight]
gender_weight=[i*(1+random.randint(rand_min,rand_max)/10) for i in gender_weight]
birth_weight=[i*(1+random.randint(rand_min,rand_max)/10) for i in birth_weight]

probability_gender=[]
for i in gender_weight:
    probability_gender.append(i/sum(gender_weight))

probability_source=[]
for i in source_weight:
    probability_source.append(i/sum(source_weight))

probability_geoips=[]
for i in country_weight:
    probability_geoips.append(i/sum(country_weight))

probability_birth=[]
for i in birth_weight:
    probability_birth.append(i/sum(birth_weight))

#USERID
userid = 1000000

#DATETIMES
datelist=[]

for i in range(0,number_of_new_users):
    hour = random.randint(0,23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    final_date = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour, minute, second).strftime('%Y-%m-%d %H:%M:%S')
    datelist.append(final_date)

datelist.sort()

#GENERATE
for i in range(0,number_of_new_users):
    userid += 1
    generated_gender=choice(gender, 1, p=probability_gender)[0]
    generated_birth=choice(birth, 1, p=probability_birth)[0]
    generated_geoips=choice(geoips, 1, p=probability_geoips)[0]
    generated_source=choice(source, 1, p=probability_source)[0]
    print(datelist[i],userid,"registration",generated_birth,generated_gender,generated_geoips,generated_source)