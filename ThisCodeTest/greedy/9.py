# s = 'ababcdcdababcdcd'
s = 'aabbaccc'

plusCheck = 1
total = len(s)
totalStrLen = []

while plusCheck < total:
  # 1~끝까지 잘라줌
  first_n = s[0:plusCheck]
  n = s[0:plusCheck]
  num = 0
  newStr = ''
  checks = True
  
  for i in range(0, total):

    #시작 글자랑 똑같은게 없으면 종료 조건
    if first_n != s[i:i+plusCheck:plusCheck] and plusCheck == i and len(s[i:i+plusCheck:plusCheck]) == len(first_n):
      checks = False
      print("plusCheck:"+str(plusCheck), end=" ")
      print("i:"+str(i), end=" ")
      print("n:"+first_n, end=" ")
      print("s:"+s[i:i+plusCheck:plusCheck], end=" ")
      print(plusCheck)
      break

    if total == i+1: # 마지막
      
      if n == s[i:i+plusCheck:plusCheck]:
        num += 1
      if num > 1:
        newStr += str(num)+s[i:i+plusCheck:plusCheck]
      else:
        newStr += s[i:i+plusCheck:plusCheck]
      break
    
    if n == s[i:i+plusCheck:plusCheck]:
      num += 1
      
    else:
      
      if num > 1:
        newStr += str(num)+s[i:i+plusCheck:plusCheck]
      else:
        newStr += s[i:i+plusCheck:plusCheck]

      n = s[i]
      num = 0
      
  if checks == True:
    totalStrLen.append(len(newStr))

    
  print("plusCheck: "+str(plusCheck)+", newStr: "+newStr)
  # 끝날때마다 추가
  plusCheck += 1

print(totalStrLen)

if len(totalStrLen) > 0:
  totalStrLen.sort()
  print(totalStrLen[0])
else:
  print(len(s))
