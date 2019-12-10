Системные требования:
 - Python 3.6.4
 - Django 2.1.3
 - MySQL 8.0.13
 - mysqlclient для Python36 отсюда: https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
 - django-annoying для Python36: https://github.com/skorokithakis/django-annoying

Туториал по MySQL:
http://www.ntu.edu.sg/home/ehchua/programming/sql/mysql_howto.html


Туториал по Django, пройти тем кто не знаком с Django скорее обязательно:
https://docs.djangoproject.com/en/2.1/intro/



Для того, чтобы соединиться с базой данных на локалхосте, нужно создать
на локальном MySQL-сервере базу testing_platform,
пользователя с логином и паролем как в testing_platform/settings.py,
дать ему доступ на все опреации ко всем базам.


Можно восстановить данные базы из дампа (файл db_dump.json), чтобы все работали с одними и теми же данными:

python manage.py loaddata --exclude auth.permission --exclude contenttypes db_dump.json

ИЛИ

python3 manage.py loaddata --exclude auth.permission --exclude contenttypes db_dump.json (если вариант выше ругается
на InvalidSyntax)


(Источник: https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata)
