""""Task: Shaxsiy Kitob Kutubxonasi Boshqaruvi
Maqsad: O‘zingizning kitoblaringiz ro‘yxatini boshqarish uchun dastur yarating. Bu dasturda turli ma'lumot turlari, operatorlar, shartlar, tsikllar va kolleksiyalardan foydalaning.
Vazifa:

Ma'lumotlarni yaratish:

Bir dictionary library yarating, unda kamida 5 ta kitob bo‘lsin. Har bir kitob quyidagi kalitlarni o‘z ichiga olsin:

title (string) – kitob nomi.
pages (int) – sahifa soni.
genres (list) – janrlar ro‘yxati (masalan, ["fiction", "mystery"]).
available (boolean) – kitob mavjudligi (True/False).
publish_date (tuple) – nashr sanasi (yil, oy, kun sifatida, masalan, (2020, 5, 15)).


Misol:
pythonlibrary = {
    "book1": {"title": "The Great Gatsby", "pages": 180, "genres": ["fiction", "classic"], "available": True, "publish_date": (1925, 4, 10)},
    ...
}



Foydalanuvchi kiritishi:

Foydalanuvchidan yangi kitob qo‘shish uchun input() yordamida title, pages, va genres (vergul bilan ajratilgan) ni oling. available ni True, publish_date ni (hozirgi yil, oy, kun) sifatida avtomatik belgilang (hozirgi sana: 2025, 10, 29).
Yangi kitobni library ga qo‘shing.


Shartli tekshirish (If...Else):

Foydalanuvchidan sahifa soni 200 dan katta bo‘lgan kitoblarni ko‘rsatishni so‘rang (yes/no).
Agar "yes" bo‘lsa, if sharti yordamida 200 dan katta sahifali kitoblarni chop eting.


Tsikl (For Loop):

Barcha kitob nomlarini va ularning mavjudligini for tsikli yordamida chiqaring.


Tsikl (While Loop):

Foydalanuvchidan kitob nomini so‘rang va while tsikli yordamida kitob topilmaguncha qidiruvni davom ettiring. Agar kitob topilsa, "Kitob topildi!" deb chiqaring va tsiklni break bilan to‘xtating.


Set ishlatish:

Barcha kitoblarning janrlarini (genres) bitta set ga joylashtiring va noyob janrlarni chiqaring.


Operatorlar va Casting:

Jami sahifa sonini hisoblang (barcha kitoblarning pages qiymatini yig‘ing) va natijani float ga aylantirib (casting), har bir sahifaning o‘rtacha hajmini (masalan, 0.5 kb deb hisoblang) chiqaring: total_pages / 2.0.



Talablar:

Barcha o‘rganilgan mavzularni (Variables, Data Types, Lists, Tuples, Sets, Dictionaries, If...Else, While Loops, For Loops, Operators, Casting) ishlatish.
Kodni izohlar bilan yozing (masalan, # Kitob qo'shish).
Natijalarni aniq yorliqlar bilan (print(f"...")) chiqaring.

Namuna kiritish va natija:

Kiritish:

Yangi kitob: title=Python Basics, pages=150, genres=fiction,education
200+ sahifali kitoblarni ko‘rish: yes
Kitob qidiruvi: The Great Gatsby


Kutilgan natija:
textAll books and availability:
- The Great Gatsby: True
- ...
Unique genres: {'fiction', 'classic', 'education', ...}
Books with more than 200 pages: ...
Total pages average size (kb): 450.0
Searching for book... Kitob topildi!


Maslahatlar:

Hozirgi sana uchun 2025, 10, 29 dan foydalaning.
Xatolarni tekshirish uchun try-except qo‘shish ixtiyoriy (keyingi mavzu).

Kodni yozib, natijani menga yuboring, men tekshiraman va fikr beraman. Agar savol yoki yordam kerak bo‘lsa, ayting! 🚀"""