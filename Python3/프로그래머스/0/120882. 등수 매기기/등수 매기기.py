def solution(score):
    sum_score = sorted([sum(i) for i in score], reverse = True)
    return [sum_score.index(sum(i))+1 for i in score]