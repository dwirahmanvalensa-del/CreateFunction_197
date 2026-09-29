def converts_temperature(value, unit) :
    if unit.upper() == 'C' :
        return (value * 9/5) + 32
    elif unit.upper() == 'F' :
        return (value - 32) * 5/9
    else:
        print("tidak ada unit selain 'C' atau 'F' ")

print("===== converts temperature =====")

value = int(input("masukkan value:"))
unit = input("masukkan unit: ")








