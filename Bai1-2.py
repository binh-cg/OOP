total_seconds = 42 * 60 + 42
miles = 10 / 1.61

pace_seconds_per_mile = total_seconds / miles
pace_minutes = int(pace_seconds_per_mile // 60)
pace_seconds = int(pace_seconds_per_mile % 60)
print(f"Average Pace: {pace_minutes}:{pace_seconds} per mile")

total_hours = total_seconds / 3600
average_speed = miles / total_hours
print(f"Average Speed: {average_speed} miles per hour")