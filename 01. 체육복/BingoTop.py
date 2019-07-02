import sys



def solution(n,lost,reserve):
    for i in reserve: # 우선 빌려줄 수 있는 리스트를 반복문으로 돌려
        l = i - 1 # 왼쪽
        r = i + 1 # 오른쪽
        if l in lost: # reserve 리스트 중 l(왼쪽)이 있는지
            lost.remove(l) # 있으면 remove r과 중복되지 않게
        elif r in lost:
            lost.remove(r)
    return n - len(lost) # 입력된 n와 lost의 길이를 뺀다.


# main 코드 부분
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    lost = list(map(int,input().split()))
    reserve = list(map(int,input().split()))
    print(solution(n,lost,reserve))


