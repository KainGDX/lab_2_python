# Задание 4: Регулярные выражения

import re

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Email
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
with open("emails.txt", "w") as f:
    f.write("\n".join(emails))

# Телефоны
phones = re.findall(r'\+7-\d{3}-\d{3}-\d{2}-\d{2}', text)
with open("phones.txt", "w") as f:
    f.write("\n".join(phones))

# Слова с заглавной
cap_words = re.findall(r'\b[А-ЯA-Z][а-яa-z]+\b', text)
with open("capital_words.txt", "w") as f:
    f.write("\n".join(cap_words))
