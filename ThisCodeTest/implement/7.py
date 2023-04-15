N = input()
total = len(str(N))

front = N[0:total//2]
rear = N[total//2:total]

frontTotal = 0
rearTotal = 0
for i in front:
  frontTotal += int(i)

for i in rear:
  rearTotal += int(i)

if frontTotal == rearTotal:
  print('LUCKY')
else:
  print('READY')