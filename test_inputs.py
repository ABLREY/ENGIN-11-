import sys
import time

print(sys.argv)

if len(sys.argv) < 2:
  print("Script requires run_time(int) as an input")
  exit()
else:
  run_time = int(sys.argv[1])

count = 0
while count < run_time:
  print(count)
  count +=1
  time.sleep(1)
