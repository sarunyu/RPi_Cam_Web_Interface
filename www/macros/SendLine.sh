#!/bin/bash

line_token=

echo "Sending Line Notify"
curl -X POST -H "Authorization: Bearer $line_token" -F "message=Motion Detect" -F "imageFile=@$1" https://notify-api.line.me/api/notify
echo "Sending Email"
/usr/bin/python3 /var/www/html/macros/SendEmail.py $1
