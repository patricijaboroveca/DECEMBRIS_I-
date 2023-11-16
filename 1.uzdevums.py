skaitlis = int(input("Ievadiet skaitli: ")) #Komanda, kura prasa ievadīt skaitli

summa = 0
for i in range(1, skaitlis+1):
    summa += i

print("Summa no 1 līdz", skaitlis, "ir:", summa)