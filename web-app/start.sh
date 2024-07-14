#!/bin/sh

JSON_STRING='{"megafon":[{"url":"'$SMPP_URL'","user":"'$SMPP_USER'","password":"'$SMPP_PASSWORD'"}],"sms":[{"user":"'$SMS_USER'","password":"'$SMPP_USER'"}],"db":[{"user":"'$DB_USER'","password":"'$DB_PASS'","db":"'$SMS_DB'","host":"'$DB_HOST'"}]}'

echo $JSON_STRING > db.json

python3 web-app.py