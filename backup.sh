start=$1
startdate=$(date -d"$start" +%F)
today=$(date +%F)

while [ $startdate != $today ]
do
day_of_the_week=$(date -d"$startdate" +%a)


day_before=$(date -d"$startdate - 1 day" +%F)
#echo day_before$day_before
echo $startdate
cat paid/$startdate free_tree/$startdate userlist/$startdate |sort > /usr/share/nginx/html/$startdate

startdate=$(date -d"$startdate + 1 day" +%F)
done