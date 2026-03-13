import time

total_seconds = time.time()

seconds_in_day = 86400
days_since_epoch = int(total_seconds // seconds_in_day)

remaining_seconds = total_seconds % seconds_in_day

hours = int(remaining_seconds // 3600)
minutes = int((remaining_seconds % 3600) // 60)
seconds = int(remaining_seconds % 60)

print(f"Days since epoch: {days_since_epoch}")
print(f"Current time (GMT): {hours}:{minutes:02d}:{seconds:02d}")