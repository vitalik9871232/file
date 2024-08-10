# Відкриваємо файл для читання

with open("quotes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)

answer = input("Хто написав ці рядки?: ")

# Відкриваємо файл для запису

with open("quotes.txt", "a", encoding="utf-8") as file:
    file.write("\n Шевченко (Т.Г.)")

while True:
    answer2 = input("Бажаєте додати ще одну цитату? (так/ні): ")
    answer2.lower()

    if answer2 == "так":
        quote = input("Введіть цитату: ")
        author = input("Введіть автора: ")

        with open("quotes.txt", "a", encoding="utf-8") as file:
            file.write("\n"+quote)
            file.write("\n"+author)
            file.write("\n")
            file.close()
    else:
        break

with open("quotes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)