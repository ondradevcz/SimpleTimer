import time

timer = 0
starttime = time.time()
print("TIMER STARTS")
while True:
  timer += 1
  print(timer)
  # Remove the Time taken by code to execute
  time.sleep(1.0 - ((time.time() - starttime) % 1.0))
