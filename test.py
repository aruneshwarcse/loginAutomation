import schedule 
import time

def test():
    print("working")


schedule.every(10).seconds.do(test)

while True:
    schedule.run_pending()
    time.sleep(1)