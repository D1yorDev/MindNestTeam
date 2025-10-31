# I start
# Bir dictionary library yarating, unda kamida 5 ta kitob bo‘lsin. Har bir kitob quyidagi kalitlarni o‘z ichiga olsin:~~~
# title (string) – kitob nomi.
# pages (int) – sahifa soni.
# genres (list) – janrlar ro‘yxati (masalan, ["fiction", "mystery"]).
# available (boolean) – kitob mavjudligi (True/False).
# Epublish_date (tuple) – nashr sanasi (yil, oy, kun sifatida, masalan, (2020, 5, 15)).


library = {
    "book1": {
        "title": "Harry Potter",
        "pages": 429,
        "genres": ["finction", "mystery"],
        "available": bool(True),
        "publish_date": (2020, 5, 15),
    },
    "book2": {
        "title": "Amir Temur",
        "pages": 929,
        "genres": ["Autobiography", "Historical"],
        "available": bool(True),
        "publish_date": (2000, 2, 5),
    },
    "book3": {
        "title": "Alamut",
        "pages": 529,
        "genres": ["Religious", "mystery"],
        "available": bool(False),
        "publish_date": (2010, 6, 25),
    },
    "book4": {
        "title": "Hunger Games",
        "pages": 300,
        "genres": ["Adventure", "mystery"],
        "available": bool(True),
        "publish_date": (2014, 7, 15),
    }, "book5": {
        "title": "Shumbola",
        "pages": 429,
        "genres": ["ROMAN"],
        "available": bool(False),
        "publish_date": (1988, 3, 15),
    }

}
for x in library.items():
    print(x)

# Foydalanuvchi kiritishi:

# Foydalanuvchidan yangi kitob qo‘shish uchun input() yordamida title, pages, va genres (vergul bilan ajratilgan) ni oling.
# available ni True, publish_date ni (hozirgi yil, oy, kun) sifatida avtomatik belgilang (hozirgi sana: 2025, 10, 29).
# Yangi kitobni library ga qo‘shing.

new_key = str(input("Please write new book's key name: "))
new_title = str(input("Enter book name: "))
new_pages = int(input("Page of book: "))
new_genres = (input("Enter genres of book: "))

new_book = {
    "title": new_title,
    "pages": new_pages,
    "genres": new_genres,
    "available": bool(True),
    "publish_date": (2025, 11, 31),
}

library[new_key] = new_book

for x in library.items():
    print(x)
