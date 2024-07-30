FROM python:3.9.19-bookworm
 
COPY web-app/requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
ADD web-app/start.sh /
ADD web-app/web-app.py /
RUN chmod +x /start.sh

ENTRYPOINT [ "/start.sh" ]
