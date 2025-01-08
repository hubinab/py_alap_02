Lista = []
Fekete = 0
Feher = 0
Dontetlen = 0
with open("eredmenyek.txt","r",encoding="utf-8") as filebe:
    sorok = filebe.read().splitlines()
    for sor in sorok:
        if sor == "FK":
            Fekete += 1
        if sor == "FH":
            Feher += 1
        if sor == "XX":
            Dontetlen += 1
        Lista.append(sor)


with open("pontozotabla.txt","w",encoding="utf-8") as fileki:
    print(f"A 2040-es sakkolimpián a következő eredmények születtek:", file=fileki)
    print(f"Az olimpián összesen {len(sorok)} partit játszottak a versenyzők egymással.", file=fileki)
    print(f"Ezek lebontása a következő:", file=fileki)
    print(f"Fehér színben játszva összesen {Feher} partit nyertek.", file=fileki)
    print(f"Fekete színben játszva összesen {Fekete} partit nyertek.", file=fileki)
    print(f"Döntetlent pedig összesen {Dontetlen} esetben játszottak.", file=fileki)

print("Az állományba történt kiíratás megtörtént.")