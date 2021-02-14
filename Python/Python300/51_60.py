#51
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

#52
movie_rank.append("배트맨")

#53
movie_rank.insert(1, "슈퍼맨")

#54
del movie_rank[3]

#55
del movie_rank[2]
del movie_rank[2]

#56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2 

#57
nums = [1, 2, 3, 4, 5, 6, 7]
nums_min = min(nums)
nums_max = max(nums)

#58
nums = [1, 2, 3, 4, 5]
nums_sum  = sum(nums)

#59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
cook_num = len(cook)

#60
nums_avg = sum(nums) / len(nums)
print(nums_avg)