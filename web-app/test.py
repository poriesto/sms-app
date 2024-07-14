
import psycopg2

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='sms-db', user='sms', password='password', host='db')
    print('Zaebis')
    cursor = conn.cursor()
    data =  ("fsfsdf","234234","fdsfdsf","sdfsdfsdf")
   cursor.execute("INSERT INTO sent_sms (host,username,message,phone) VALUES (%s, %s, %s, %s)", ("fsfsdf","234234","fdsfdsf","sdfsdfsdf"))
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')
~                                                       