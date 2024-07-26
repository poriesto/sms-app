FROM astra:175-python3-pg

ADD web-app/start.sh /
ADD web-app/web-app.py /
RUN chmod +x /start.sh

ENTRYPOINT [ "/start.sh" ]