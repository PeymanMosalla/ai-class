age = int(input("سن: "))
day = input("روز: ")

if age < 5:
    price = 0
elif age <= 12:
    price = 50000
elif age >= 60:
    price = 60000
else:
    price = 100000

# حذف فاصله و نیم‌فاصله تا «سه شنبه» و «سه‌شنبه» هر دو قبول شوند
normalized_day = day.strip().replace(" ", "").replace("\u200c", "")
if normalized_day == "سهشنبه":
    price = price * 80 // 100

if price == 0:
    print("ورود رایگان!")
else:
    print(f"قیمت بلیط: {price} تومان")
