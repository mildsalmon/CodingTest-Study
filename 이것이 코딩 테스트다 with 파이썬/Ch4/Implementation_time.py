n = input()
import time as ti

start = ti.time()


hh = "00"
mm = "00"
ss = "00"

time = str(hh) + str(mm) + str(ss)
count = 0

while time != (n + "5959"):
  for i in range(0, len(time)):
    # print(time[i])
    if time[i] == "3":
      # print(count)
      count = count + 1
      break

  hh = int(hh)
  mm = int(mm)
  ss = int(ss)

  ss = ss + 1

  if ss == 60:
    mm = mm + 1
    ss = ss - 60

  if mm == 60:
    hh = hh + 1
    mm = mm - 60

  time = str(hh) + str(mm) + str(ss)

end = ti.time()

print(end-start)

print(count)

