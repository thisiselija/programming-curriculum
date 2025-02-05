annual = input("Ievadi gada ienākumus: ")
housing = input("Ievadi saimniecības izdevumus mēnesī: ")
bill = input("Ievadi ikmēneša rēķīnus: ")
food = input("Ievadi nedēļas ēdiena naudu: ")
travel = input("Gadā patērētā nauda ceļošanai: ")

chek = [annual, housing, bill, food, travel]
i = 0

while i < 5:
    if chek[i].isnumeric():
       i += 1
    else:
        print("Ievades kļūda")
        break
housingPro = float(housing)/ float(annual) * 100
hesh = "#" * int(housingPro)
print('housing | $ ' +housing+ ' | '+str(housingPro)+'% | ' +hesh)