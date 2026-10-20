playlist = ["Shape of You", "Blinding Lights", "Believer", "Perfect"]

# الف) تعداد آهنگ‌ها
print("تعداد آهنگ‌ها:", len(playlist))

# ب) اولین و آخرین آهنگ
print("اولین آهنگ:", playlist[0])
print("آخرین آهنگ:", playlist[-1])

# ج) اضافه کردن Dynamite به آخر لیست
playlist.append("Dynamite")

# د) حذف Believer از لیست
playlist.remove("Believer")

# هـ) مرتب‌سازی الفبایی
playlist.sort()
print("لیست مرتب‌شده:", playlist)

# و) چاپ شماره‌دار با حلقه for
for number, song in enumerate(playlist, start=1):
    print(f"{number}. {song}")
