def toliq_ism_yasa(ism, familiya):
    """Toliq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism


talaba1 = toliq_ism_yasa("olim", "hakimov")
talaba2 = toliq_ism_yasa("hakim", "olimov")
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
print(f"{talaba1} darsga kechikib keldi")
