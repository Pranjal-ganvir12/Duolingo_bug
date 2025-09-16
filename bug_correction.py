from datetime import timedelta

def update_streak( last_day, today, current_streak):
    if last_day is None:
        return 1
    
    if today == last_day:
        return current_streak
    
    if today == last_day + timedelta(days = 1):
        return current_streak + 1
    
    return 1 



