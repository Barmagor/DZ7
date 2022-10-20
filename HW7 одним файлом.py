def export_telephone(): 
    n = input("Введите фамилию: ")
    a=open("telephones.txt", "r", encoding="UTF-8")
    x=a.read()
    y=x.split(";")   
    print(y)
    for i in y:
        if n in i:
            print(i)

def import_telephone(): 
    n = input("Введите данные:")+";"
    a=open("telephones.txt", "r", encoding="UTF-8")
    rec=""
    x=a.read()
    rec=open("telephones.txt", "a", encoding="UTF-8")
    rec=rec.write(n)
    print("Телефон записан в справочник")

u = int(input("Введите 1, если хотите ввести данные, 2 - если получить: "))
while u<1 or u>2:
        print("Введите число от 1 до 2")
        try:
            u = int(input("Введите 1, если хотите ввести данные, 2 - если получить: "))
        except ValueError:
            print("Введите корректное число")

if u ==1:
    import_telephone()
    print("Телефон записан в справочник")
if u ==2:
    export_telephone()
