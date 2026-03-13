# Câu 1
r = 5
pi = 3.14159
volume = (4/3) * pi * (r**3)

print(f"The volume of the sphere is: {volume:.2f}")

# Câu 2
cover_price = 24.95
discount_price = cover_price * 0.6
total_books = 60

total_book_cost = discount_price * total_books

shipping_cost = 3 + (total_books - 1) * 0.75

total_wholesale_cost = total_book_cost + shipping_cost

print(f"Total wholesale cost for 60 copies: ${total_wholesale_cost:.2f}")

# Câu 3
easy_pace_sec = 8 * 60 + 15
tempo_pace_sec = 7 * 60 + 12

total_seconds = (easy_pace_sec * 2) + (tempo_pace_sec * 3)

total_minutes = total_seconds // 60
extra_seconds = total_seconds % 60

end_minutes = 52 + total_minutes
arrival_hour = 6 + (end_minutes // 60)
arrival_minute = end_minutes % 60

print(f"Time for breakfast: {arrival_hour}:{arrival_minute:02d} am")