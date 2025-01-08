rekesz = int(input("Adja meg a rendelt rekeszek darabszámát (5-20): "))
darab = int(input("Adja meg a mai napon leszüretelt almák darabszámot (100-200): "))

if rekesz * 12 <= darab:
    print("A rendelt mennyiség teljesíthető.")
else:
    print(f"A rendelt mennyiség nem teljesíthető, max. {darab//12} rekeszt lehet értékesíteni.")
