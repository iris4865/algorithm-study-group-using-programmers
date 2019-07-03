def solution(name):
    name = list(name)
    clear_name = ['A'] * len(name)
    
    answer = 0
    i = 0
    while clear_name != name:
        if name[i] != 'A':
            value = ord(name[i]) - ord('A')
            answer += min(26 - value, value) # 상하이동 가장짧은거
            name[i] = 'A'
        else:
            left = 1
            right = 1
            # 좌우이동 가장짧은거
            for d in range(1, len(name)):
                if name[i + d] == "A":
                    right += 1
                else:
                    break
                if name[i - d] == "A":
                    left += 1
                else:
                    break
            if left < right:
                answer += left
                i -= left
            else:
                answer += right
                i += right
    return answer
