import smtplib
import os
from dotenv import load_dotenv



load_dotenv()

login = os.getenv('login')
password = os.getenv('password')

server = smtplib.SMTP_SSL('smtp.yandex.com', 465)
server.login(login, password)

website = "https://dvmn.org/profession-ref-program/boss.qwerzxcv/yeP30/"
friend_name = 'Кирилл'
my_name = 'Павел'
email_from = 'chepik.pasha@yandex.ru'
email_to = 'qew.qweqwe.2016@mail.ru'

letter = """\
From: {email_from}
To: {email_to}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
      """.format(email_from=email_from, email_to=email_to)

letter = letter.replace('%website%', website)
letter = letter.replace('%friend_name%', friend_name)
letter = letter.replace('%my_name%', my_name)
letter = letter.encode("UTF-8")

server.sendmail(email_from, email_to, letter)
server.quit()