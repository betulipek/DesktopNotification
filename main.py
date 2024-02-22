import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(title="ALERT ALERT", message="You should take a break", timeout=15)

        time.sleep(60)


