# /usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import urllib
import requests
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import psycopg2

dbf = open('db.json')
db = json.load(dbf)


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def create_DataFromUrl(self, source):
        data = dict()
        for i in source:
            d = i.split('=')
            data[d[0]] = d.pop()
        return data
    def create_JsonMegafon(self, source):
        m = source['text']
        data = {
            "from": "BaltZavod",
            "to": int(source['to']),
            "message": source['text'].replace('+', ' ')
        }
        return data

    def do_GET(self):
        s = urllib.parse.unquote(self.path, 'utf-8')
        c = self.client_address[0]
        durl = s.strip('/').split('&')
        url_data = self.create_DataFromUrl(durl)
        json_data = self.create_JsonMegafon(url_data)
        
        try:
        # пытаемся подключиться к базе данных
            conn = psycopg2.connect(dbname=db['db'][0]['db'],
                                    user=db['db'][0]['user'],
                                    password=db['db'][0]['password'],
                                    host=db['db'][0]['host'])
            cursor = conn.cursor()
        except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
            print('Can`t establish connection to database')
        if url_data['user'] == db['sms'][0]['user'] and url_data['pass'] == db['sms'][0]['password']:
            logging.info("Success auth from Client - %s", c)
            requests.post(db['megafon'][0]['url'], data=json.dumps(json_data),
                          auth=(db['megafon'][0]['user'], db['megafon'][0]['password']),
                          headers={"Content-Type": "application/json"})
            logging.info("Phone - %s, Message: %s", json_data['to'], json_data['message'])

            cursor.execute("INSERT INTO sent_sms (host,username,message,phone) VALUES (%s, %s, %s, %s)", (c,url_data['user'],json_data['message'],json_data['to']))
            conn.commit()
            cursor.close()
            conn.close()
            self._set_response()
        else:
            logging.info("Wrong auth string from client - %s User - %s, Pass - %s, Message - %s", c, url_data['user'],
                         url_data['pass'], json_data['message'])
            
            cursor.execute("INSERT INTO fail_sms (host,username,message,phone) VALUES (%s, %s, %s, %s)", (c,url_data['user'],json_data['message'],json_data['to']))
            conn.commit()
            cursor.close()
            conn.close()
            self._set_response()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).decode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, port=8000):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                        handlers=[logging.FileHandler(filename='sms.log', mode= 'a+', encoding= 'utf-8')])
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    except Exception:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
