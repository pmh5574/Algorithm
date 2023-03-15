S = input()

result = 0
count = 0
j = 1

answer = []



for i in range(len(S)):
        
    if len(S) > j:
        if S[i] != S[j]:
            count += 1
        
    j+=1

print((count+1)//2)