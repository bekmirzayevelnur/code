dasturchilar = {
    "ali": ["python", "c++"],
    "javoxir": ["html", "css", "js"],
    "mexroj": ["php", "sql"]
}

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end="")
    for til in tillar:
        print(f"{til.upper()} ", end="")
