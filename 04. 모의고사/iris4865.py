def solution(answers):
    solve = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    score = [0, 0, 0]
    
    for number, answer in enumerate(answers):
        for i, s in enumerate(solve):
            if answer == s[number % len(s)]: # 정답과 찍기가 같은경우
                score[i] += 1

    return [i + 1 for i, s in enumerate(score) if s == max(score)]
