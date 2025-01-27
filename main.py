# Оригінальний текст
text = "Робота в ІТ передбачає постійне навчання та розвиток. Спеціалісти повинні\
 володіти технічними знаннями, вирішувати проблеми та ефективно співпрацювати в\
 командах для досягнення успіху в проєктах."

# (Стешенко Станіслав)
# 1. Використання функції lower() для переведення всіх символів у нижній регістр
lowercase_text = text.lower()
print("Текст у нижньому регістрі:")
print(lowercase_text, "\n")

# 2. Використання функції count() для підрахунку кількості входжень слова "та"
count_of_word_ta = text.count("та")
print("Кількість входжень слова 'та':", count_of_word_ta, "\n")

# 3. Використання функції replace() для заміни слова "співпрацювати" на "взаємодіяти"
replaced_text = text.replace("співпрацювати", "взаємодіяти")
print("Текст після заміни слова 'співпрацювати':")
print(replaced_text)