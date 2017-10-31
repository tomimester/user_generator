#!/bin/bash
PATH=/opt/someApp/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

start=$1
end=$2
[ -z "$start" ] && start=$(date -d"yesterday" +%F)
[ -z "$end" ] && end=$(date +%F)
startdate=$(date -d"$start" +%F)
enddate=$(date -d"$end" +%F)

while [ $startdate != $enddate ]
do
day_of_the_week=$(date -d"$startdate" +%a)
weekend_multiplier=1
[[ $day_of_the_week = "Sun" ]] || [[ $day_of_the_week = "Sat" ]] && weekend_multiplier=$(python3 weekend.py)

growth=$(python3 growth.py)
#echo growth$growth

day_before=$(date -d"$startdate - 1 day" +%F)
#echo day_before$day_before

number_of_day_before=$(cat ~/number_of_users.csv)
[ -z "$number_of_day_before" ] && number_of_day_before=$(cat userlist.csv | grep $day_before |wc -l)
#echo number_of_day_before$number_of_day_before
[ "$number_of_day_before" == 0 ] && number_of_day_before=100
#echo number_of_day_before$number_of_day_before

number_of_users=$(echo "$number_of_day_before * $growth" |bc)
echo $number_of_users > ~/number_of_users.csv
number_of_users_weekend=$(echo "$number_of_users * $weekend_multiplier" |bc)
echo number_of_users": "$number_of_users_weekend $startdate

last_user=$(cat userlist.csv |tail -1 |cut -d' ' -f3)
[ -z "$last_user" ] && last_user=1000000
formatted_date=$(echo $startdate |tr '-' ' ')
python3 send_a_tree_users.py $number_of_users_weekend $formatted_date $last_user > ~/userlist/$startdate
cat ~/userlist/$startdate >> userlist.csv
python3 send_a_tree_free.py $formatted_date > ~/free_tree/$startdate
python3 send_a_tree_paid.py $formatted_date > ~/paid/$startdate
cat paid/$startdate free_tree/$startdate userlist/$startdate |sort > /usr/share/nginx/html/$startdate

startdate=$(date -d"$startdate + 1 day" +%F)
done