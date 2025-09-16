from datetime import timedelta
from datetime import date 
def update_streak( last_day, today, current_streak):
    if last_day is None:
        return 1
    
    if today == last_day:
        return current_streak
    
    if today == last_day + timedelta(days = 1):
        return current_streak + 1
    
    return 1 

if __name__ == "__main__":
    streak = 0
    last_day = None 

    print("=== Streak demo ===")

    # Day 1: first practice today
    today = date.today()
    streak = update_streak(last_day, today, streak)
    last_day = today
    print(f"Day 1 ({today}): streak = {streak}")

    # Practicing again the same day
    streak = update_streak(last_day, today, streak)
    print(f"Day 1 again ({today}): streak = {streak}")

    # Next day (consecutive)
    next_day = today + timedelta(days=1)
    streak = update_streak(last_day, next_day, streak)
    last_day = next_day
    print(f"Day 2 ({next_day}): streak = {streak}")

    # Skip a day (jump 2 days ahead)
    skipped_day = next_day + timedelta(days=2)
    streak = update_streak(last_day, skipped_day, streak)
    last_day = skipped_day
    print(f"Day 4 after skip ({skipped_day}): streak = {streak}")


