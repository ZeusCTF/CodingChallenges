def findRelativeRanks(score):
    score2 = sorted(score, reverse=True)

    for i in range(len(score)):
        if score[i] == score2[0]:
  
            score[i] = "Gold Medal"
        elif score[i] == score2[1]:
            score[i] = "Silver Medal"

        elif score[i] == score2[2]:
            score[i] = "Bronze Medal"

        else:
            score[i] = str(score2.index(score[i]) + 1)
    return score

findRelativeRanks([5, 6, 3, 2, 1])