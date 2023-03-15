def solution(K, user_scores):

    answer = 0

    ranking = []
    score_dict = {}

    for i in user_scores:
        user, score = i.split()
        score = int(score)

        if user not in score_dict: # 처음 진입시

            score_dict[user] = score 
            # print(score_dict)

            if len(ranking) > K: # 표시된 개수보다 많으면 
                # if user == ranking[K]: # 마지막 유저랑 체크해서 이름 같으면
                #     continue
                if score == int(score_dict[ranking[-1]]): #마지막 유저랑 점수 같으면 
                    continue
                ranking.pop()
                ranking.append(user)
                ranking.sort(key=lambda x: (-score_dict[x], x))
                answer+= 1
            else:
                print(score_dict)
                print(ranking)
                # print(score_dict[ranking[-1]])
                if len(ranking) > 0:
                    if score == int(score_dict[ranking[-1]]): #마지막 유저랑 정수 같으면 
                        continue
                # 랭킹 페이지에 저장하고 내림차순으로
                ranking.append(user)
                if len(ranking) > K: # 표시된 개수보다 많으면 
                    ranking.sort(key=lambda x: (-score_dict[x], x))
                    ranking.pop()

                ranking.sort(key=lambda x: (-score_dict[x], x))
                answer+= 1

        else: # 현재 유저가 이미 있을때

            if score == int(score_dict[user]): #마지막 유저랑 점수 같으면 
                continue

            if int(score_dict[user]) < score: #기존 점수보다 높으면
                score_dict[user] = score
                # print(score_dict[user].index())

                nScore = 0
                for j in score_dict:

                    if nScore == 0:
                        nScore = score_dict[j]
                    if nScore < score:
                        answer+=1
                        break

                ranking.sort(key=lambda x: (-score_dict[x], x))

                # while ranking.index(user) >= K:
                #     ranking.pop()
                #     answer += 1
                if ranking.index(user) >= K:
                    answer += 1
                ranking = ranking[:K]
        # print(ranking)
        print(answer)
    return answer