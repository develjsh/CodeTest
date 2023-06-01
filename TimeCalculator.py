import time
import datetime

start = time.time()
end = time.time()
sec = (end - start)

result_list = str(datetime.timedelta(seconds=sec)).split(".")
print(result_list[0])