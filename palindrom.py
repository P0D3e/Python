ord = input("Testa ord om dom är en palindrom : ")

reversed_ord = ord[::-1]
if len(ord) < 2:
    print("Använd mer än 2 bokstäver tack!")
else:

    if ord.lower() == reversed_ord.lower():
        print("Korrekt")
    else:
        print("Fel")