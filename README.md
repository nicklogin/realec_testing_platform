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


Пользовател нужно создавать с нативным паролем MySQL, это делается так:
CREATE USER 'PlatformAdmin'@'localhost' IDENTIFIED WITH mysql_native_password BY 'rnY79gbE43!';

Можно восстановить данные базы из дампа (файл db_dump.json), чтобы все работали с одними и теми же данными:

python manage.py loaddata --exclude auth.permission --exclude contenttypes db_dump.json

ИЛИ

python3 manage.py loaddata --exclude auth.permission --exclude contenttypes db_dump.json (если вариант выше ругается
на InvalidSyntax)


(Источник: https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata)




СПИСОК ЗАДАЧ:
 - В функции edit_quiz из main_app/views.py написать код, который действительно изменяет вопросы и правильные ответы в базе данных
 (под if request.POST) - СДЕЛАНО
 - В файлах реалека отредактировать файл visualiser_ui.js так, чтобы работала кнопка "Generate test" - 
 СДЕЛАНО, на локалхосте у nicklogin
 - Сделать так, чтобы страница "/editQuiz/" была доступна только администраторам (user.rights = 'A')
 или учителям(user.rights = 'T'), этот квиз создавшим - СДЕЛАНО, пусть и криво
 - Добавить дедлайе к квизам и чтобы после дедлайна форма не принималась
 - Сделать так, чтобы кнопки Delete и Restore to default на страницах generateQuestions/ и 
 editQuiz работали, причём перед удалением пользователя бы спрашивали, точно ли он хочет это сделать:
     - Отредактировать файл question_editor.js
     - В main_app/views.py отредактировать функцию edit_quiz так, чтобы в render передавались также и индексы "вынутых" из базы правильных ответов
     - Отредактировать файлы templates/editquiz.html и templates/generquestions.html (как я думаю это сделать):
        - Сделать так, чтобы в ответы тоже записывался их id в поле "id" html-элемента в формате "answer_question.id_answer.id" (сейчас там просто 
        "answer_question.id_1" для всех правильных ответов к одному вопросу, что, конечно, неправильно)
        - Сделать так, чтобы ответы с вопросами были в одном div'е, id которого будет передаваться в функцию deleteQuestion() (однако, непонятно как это будет сочетаться - с display:grid из CSS - действует ли это свойство на вложенные дивы? - И если да, то как можно сделать, чтобы оно
        на них не действовало?)
 - Добавить в /editQuiz возможность вручную создавать новые вопросы и ответы
 - Сделать страницу, на которой можно вруную составлять квиз из имеющихся в базе вопросов - CДЕЛАНО, но пока кое-как
 - Сделать главную страницу, чтобы при заходе на "index" она показывала, что-то нормальное, а не тупо текст "Here will be the index page"
 - Желательно было бы заменить все присутствующие сейчас в коде вызовы main_app/views.py вызовы HttpResponse() на редиректы
 - Создать страницу /Users, на которую могут заходить только админы и где можно добавлять новых пользователей и редактировать/удалять старых
 - Создать страницу /Grades, на которой:
     - Ученик видит свои оценки за тесты
     - Учитель и админ видят оценки и тесты учеников и могут редактировать оценку за конкретный ответ ученика
 - Улучшить дизайн страниц - всегда кстати!
 - Сделать так, чтобы при создании вопроса из текста эссе в таблицу Question в поле error_tag добавлялся настоящий тег ошибки, а не "Suggestion", а в поля
 folder_addr и essay_addr добавлялись соответственнл адрес папки и адрес текста соответственно



