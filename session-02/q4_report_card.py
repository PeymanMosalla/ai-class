scores = {"Ali": 18, "Sara": 20, "Reza": 9, "Mina": 14, "Omid": 11.5}

# الف) نمره و رتبه هر دانشجو
for name, score in scores.items():
    if score >= 17:
        grade = "عالی"
    elif score >= 14:
        grade = "خوب"
    elif score >= 10:
        grade = "قبول"
    else:
        grade = "مردود"
    print(f"{name}: {score} → {grade}")

# ب) لیست قبول‌شده‌ها
passed = []
for name, score in scores.items():
    if score >= 10:
        passed.append(name)
print("قبول‌شده‌ها:", passed)

# ج) میانگین کلاس
average = sum(scores.values()) / len(scores)
print("میانگین کلاس:", average)

# د) نفر اول کلاس
top_student = max(scores, key=scores.get)
print("نفر اول:", top_student)
