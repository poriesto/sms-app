FROM astra:175-python3-pg

ADD start.sh /
ADD web-app.py /
RUN chmod +x /start.sh

ENTRYPOINT [ "/start.sh" ]