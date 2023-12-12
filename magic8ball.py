import random
print("Skriv en fråga så kommer magic 8 ball att svara!")
input()

Ja_lista = ("Ja", "Självklart", "Absolut", "Utan Tvekan")
Nej_lista = ("Nej", "Inte En Chans", "Absolut Inte", "Icke San Icke")
Kanske_lista = ("Kanske", "Möjligtvis", "Ibland", "Osäker")


result = random.randint(0,2)
if result == 1:
    print(random.choice(Ja_lista))

elif result == 2:
    print(random.choice(Nej_lista))

else:
    print(random.choice(Kanske_lista))
