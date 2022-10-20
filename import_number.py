def import_telephone(): 
    n = input("Введите данные:")+";"
    a=open("telephones.txt", "r", encoding="UTF-8")
    rec=""
    x=a.read()
    rec=open("telephones.txt", "a", encoding="UTF-8")
    rec=rec.write(n)
    print("Телефон записан в справочник")