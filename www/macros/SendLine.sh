#!/bin/bash
echo "Sending Line Notify"
curl -X POST -H "Authorization: Bearer WzZweyeasnB7JKPBbHZ11dOEytNlExPOGJiNjqouANk" -F "message=Motion Detect" -F "imageFile=@$1" https://notify-api.line.me/api/notify
echo "Sending Email"
/usr/bin/python3 /var/www/html/macros/SendEmail.py $1
