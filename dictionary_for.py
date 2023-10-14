python_words = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "boolean": "Mantiqiy qiymat",
    "for": "Biror amalni qayta-qayta bajarish tsikli",
    "if": "Shartlarni tekshirish operatori",
}

for key, value in sorted(python_words.items()):
    print(f"{key.title()} - {value}")
