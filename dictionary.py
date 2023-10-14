python_izohli_lugati = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "string": "Matn",
    "list": "Ro'yxat",
    "tuple": "O'zgarmas ro'yxat"}
kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit, "Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")

    
