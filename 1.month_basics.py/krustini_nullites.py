#izprintē sākumu
sk = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sp1 = input('Izvēlise kas tu būsi par simbolu (O, X): ')
print('\nSAKAM SPĒLI!')
print(f" {sk[0]} | {sk[1]} | {sk[2]} ")
print(f'___|___|___')
print(f" {sk[3]} | {sk[4]} | {sk[5]} ")
print(f'___|___|___')
print(f" {sk[6]} | {sk[7]} | {sk[8]}")

i = 0
def uzvara(uzvar):
    for g in uzvar:
        global chek
        chek = len(set(g)) 
        if chek == 1:
            return True
#gājieni un uzvara        
while i < 9:
    #uzvara
    uzvar = [[sk[0], sk[1], sk[2]],[sk[3], sk[4], sk[5]], [sk[6], sk[7], sk[8]],
             [sk[0], sk[3], sk[6]], [sk[1], sk[4], sk[7]], [sk[2], sk[6], sk[8]],
             [sk[0], sk[4], sk[8]], [sk[2], sk[4], sk[6]]]
    if uzvara(uzvar) == True:
        print('yepee, Tu uzvarēji!')
        break
    
    #gājieni
    if i % 2 == 0:
        spX = int(input('\nspēlētājs O ievadi skaitli no 1 - 9: '))
        sk[spX - 1] = 'O'
    else:
        spX = int(input('\nspēlētājs X ievadi skaitli no 1 - 9: '))
        sk[spX - 1] = 'X'
    print(f" {sk[0]} | {sk[1]} | {sk[2]} ")
    print(f'___|___|___')
    print(f" {sk[3]} | {sk[4]} | {sk[5]} ")              
    print(f'___|___|___')
    print(f" {sk[6]} | {sk[7]} | {sk[8]}")
    i+=1

#input can be just int
#nevar ievadīt divus vienādus skaitļus spēles laikā
