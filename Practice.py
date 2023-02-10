import time
import time as _time

start_time = _time.time()
time.sleep(3)
end_time = _time.time()
print("sleep_time =", abs(end_time - start_time))

