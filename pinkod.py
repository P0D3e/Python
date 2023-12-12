pin = input(int)

pin_length = len(pin)

if pin.isdigit():
    if (pin_length >4):
         print("Invalid input, please use 4 numbers only!")
             
    if (pin_length <4):
         print("Invalid input, please use 4 numbers only!")

    else: print(pin)


else:
     print("Use only numbers")
