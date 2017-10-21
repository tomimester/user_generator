start=$1
startdate=$(date -d"$start" +%F)
today=$(date +%F)

while [ $startdate != $today ]
do
day_of_the_week=$(date -d"$startdate" +%a)
weekend_multiplier=1
[[ $day_of_the_week = "Sun" ]] || [[ $day_of_the_week = "Sat" ]] && weekend_multiplier=$(python3 weekend.py)

growth=$(python3 growth.py)
#echo growth$growth

day_before=$(date -d"$startdate - 1 day" +%F)
#echo day_before$day_before

number_of_day_before=$(echo $number_of_users)
[ -z "$number_of_day_before" ] && number_of_day_before=$(cat userlist.csv | grep $day_before |wc -l)
#echo number_of_day_before$number_of_day_before
[ "$number_of_day_before" == 0 ] && number_of_day_before=100
#echo number_of_day_before$number_of_day_before

number_of_users=$(echo "$number_of_day_before * $growth" |bc)
number_of_users_weekend=$(echo "$number_of_users * $weekend_multiplier" |bc)
echo number_of_users_weekend": "$number_of_users_weekend

last_user=$(cat userlist.csv |tail -1 |cut -d' ' -f3)
[ -z "$last_user" ] && last_user=1000000
formatted_date=$(echo $startdate |tr '-' ' ')
python3 send_a_tree_users.py $number_of_users_weekend $formatted_date $last_user > ~/userlist/$startdate
cat ~/userlist/$startdate >> userlist.csv
python3 send_a_tree_free.py $formatted_date > ~/free_tree/$startdate
python3 send_a_tree_paid.py $formatted_date > ~/paid/$startdate

startdate=$(date -d"$startdate + 1 day" +%F)
done