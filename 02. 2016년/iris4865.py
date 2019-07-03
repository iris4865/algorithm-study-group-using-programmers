def solution(month, day):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    
    total_day = sum(days[:month]) + day
    return week[total_day % len(week)]
