#!/bin/bash
PATH=/opt/someApp/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

cp /home/tomi/private/$(date -d"yesterday" +%F) /usr/share/nginx/html/