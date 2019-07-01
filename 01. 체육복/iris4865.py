def solution(n, lost, reserve):
    have_two_cloth = [r for r in reserve if r not in lost] # 체육복 2벌 가지고 있는 학생리스트
    have_zero_cloth = [l for l in lost if l not in reserve] # 체육복 가지고 있지 않은 학생리스트
    for r in have_two_cloth: # 2벌 있는 학생만 반복
        front = r - 1
        back = r + 1
        if front in have_zero_cloth: # 앞 학생이 옷이 없는 경우
            have_zero_cloth.remove(front)
        elif back in have_zero_cloth: # 뒷 학생이 옷이 없는 경우
            have_zero_cloth.remove(back)
    return n - len(have_zero_cloth) # 전체 학생 - 체육복 못 빌린 학생
