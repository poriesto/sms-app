Веб сервис для отправки sms сообщений двухфакторной авторизации.
 Основное предназначение принять get запрос, сформировать json запрос на сервер оператора мобильной связи и отправить его.
 Введется логирование на предмет корректности ссылки и записывается в БД.
 В качестве клиента к бд используется временно adminer.

Развертывание:
 - назначить бит исполнения для файла build.sh:
    - chmod +x build.sh
 - запустить скрипт build.sh:
    - ./build.sh
 Для корректного развертывания скрипта требуется доступ к Dockerhub.
 Резервная ссылка для файла "astra-python.tar" https://1drv.ms/u/s!Aic8RIOhSb1wo6drmG62SULxVeQSDQ?e=3QwgK9

Использование:
   - URL для отправки SMS: http://HOST_IP:PORT/to=PHONE-NUMBER&text=MESSAGE&user=USER&pass=PASS
   - Пример: http://HOST_IP:PORT/to=87764348887234123&text=fsdfsdf%20dsfsdf%fdsfdsf:%20bz47328947hsdf&user=sms&pass=smppusr