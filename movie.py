import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

date_year = datetime.today().year
date_month = datetime.today().month
date_day = datetime.today().day

date = str(date_year)+str(date_month)+str(date_day)


bot = telegram.Bot(token = '845840045:AAG8gmv7KOyQ7j2B6mBxzdB_NE8l62-6mJE')
url1 = 'http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0088&date='
url2 = date

url = url1+url2

def job_function():
    html = requests.get(url)
    # print(html.text)
    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup.select_one('body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie > a > strong'))
    title_list1 = soup.select('div.info-movie')
    title_list2 = soup.select('div.info-timetable')

    title_list = []
    time_list = []
    seat_list = []
    message_list = []

    for i in title_list1:
        title = i.select_one('a > strong').text.strip()
        title_list.append(title)
    for i in title_list2:
        time = i.select_one('em').text.strip()
        time_list.append(time)
        seat = i.select_one('span').text.strip()
        seat_list.append(seat)

    size = len(title_list)
    # print(size)
    # bot.sendMessage(chat_id=994690178, text='test')
    for i in range(size):
        message = title_list[i] + " " + time_list[i] + " " + seat_list[i]
        message_list.append(message)
        # bot.sendMessage(chat_id=994690178, text = time_list[i])
        # bot.sendMessage(chat_id=994690178, text = seat_list[i])
    for i in range(size):
        bot.sendMessage(chat_id=994690178, text=message_list[i])

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=86400)
sched.start()