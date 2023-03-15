food_times = [3, 1, 2]
k = 5

answer = 0
anw = 0

for i in range(1,k+1):
    # print('i'+str(i))

    if anw >= len(food_times):
        anw = 0

    if food_times[anw] > 0:
        food_times[anw] -= 1
    else:
        for j in range(len(food_times[anw:])):
            
            
            if food_times[j+anw] != 0:
                food_times[j+anw] -= 1
                
                break
    
    anw += 1

if anw >= len(food_times)-1:
    answer = 1
else:
    answer = anw+1 
print(answer)