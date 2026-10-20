words = {
    "i": "من",
    "love": "دوست دارم",
    "python": "پایتون",
    "you": "تو",
    "book": "کتاب",
    "good": "خوب",
    "hello": "سلام",
    "computer": "کامپیوتر",
}

sentence = "I love python and AI"

result = []
translated = 0
not_translated = 0

for word in sentence.split():
    key = word.lower()
    if key in words:
        result.append(words[key])
        translated += 1
    else:
        result.append(f"[{key}]")
        not_translated += 1

print(" ".join(result))

# بخش اضافه
print("تعداد کلمات ترجمه‌شده:", translated)
print("تعداد کلمات ترجمه‌نشده:", not_translated)
