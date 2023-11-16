#faktorials

skaitlis=int(input("Ievaadi skaitli:"))

faktorials=1

for i in range(1, skaitlis+1): #katrs nakamais skaitlis, kuru reizina par 1 lielāks neka ieprieksejais
    faktorials*=i

print('Skaitļa', skaitlis,'faktorials ir:',faktorials)