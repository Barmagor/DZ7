def export_telephone(): 
    n = input("Введите фамилию: ")
    a=open("telephones.txt", "r", encoding="UTF-8")
    x=a.read()
    y=x.split(";")   
    print(y)
    for i in y:
        if n in i:
            print(i)