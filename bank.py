def szamit (osszeg, futamido):
    if futamido > 12:
        kamat = 0.12
    else:
        kamat = 0.05
    return osszeg * kamat

for i in range(4):
    osszeg = int(input("Adja meg a betenni kívánt összeget: "))
    futamido = int(input("Adja meg betét futamidejét (hónapban): "))
    print(f"A betett összeg után {round(szamit(osszeg,futamido),2)} Ft betéti kamat jár.")