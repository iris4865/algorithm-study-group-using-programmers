def solution(skill, skill_trees):
    count = 0
    
    for tree in skill_trees:
        idx = [tree.find(s) for s in skill]
        while idx and idx[-1] == -1:
            idx.pop()
        if not idx or idx[0] > -1 and idx == sorted(idx):
            count += 1

    return count
