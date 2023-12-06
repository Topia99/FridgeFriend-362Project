import schedule
import time
import datetime
from .models import Item, Fridge
import requests
from . import secret_keys
import threading

def send_warning_email(item):
    user_email = Fridge.objects.filter(id=item.fridge_id)[0].users.first().email
   
    return requests.post(
		"https://api.mailgun.net/v3/fridgefriendapp.com/messages",
		auth=("api", secret_keys.get_mailgun_key()),
		data={"from": "System <system@fridgefriendapp.com>",
			"to": ["" + user_email],
			"subject": "Food Expiration Notice: " + item.item_name,
			"text": "You have some food that's expiring soon! Please check on your " + item.item_name})
        
def check_date():
    try:
        for item in Item.objects.filter(notified=False):
            currentDate = datetime.datetime.now()
            expiryDate = datetime.datetime.combine(item.expiry_date, datetime.datetime.min.time())
            timeLeft = currentDate - expiryDate
            timeCutOff = datetime.timedelta(hours=24)
            if timeLeft < timeCutOff:
                send_warning_email(item)
                print(item.item_name)
                item.notified = True
                item.save()
                
    except Exception as e:
        print(e)
        time.sleep(100)
    #time.sleep(60)

def run_continuously(interval=30):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.daemon = True
    continuous_thread.start()
    return cease_continuous_run

def start_scheduler():
    schedule.every(10).seconds.do(check_date)
    stop_run_continously = run_continuously()