import time
import datetime

start = time.time()

end = time.time()
sec = (end - start)
sec = datetime.timedelta(seconds=sec)
print(sec)