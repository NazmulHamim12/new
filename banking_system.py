import hamim_lib as hami
import json
f=hami.json_file()




def account():
    name=str(input("Enter Name:"))
    job=input("Enter your job:")
    age=input("Enter your age:")

    data={
        "name":name,
        "job":job,
        "age":age,
        "balance":0

    }

    f.file_open(name,data)

    print("\n Account add")


def update():
    name=str(input("Enter name:"))

    data=f.file_read(name)

    pre=data["balance"]

    bal=int(input("Enter new balance:"))

    pre+=bal
    data["balance"]=pre

    f.file_open(name,data)

    print("\n Add new balance")

def check():

    name =str(input("Enter your name:"))

    with open(f"{name}.json","r") as file:
        data=json.load(file)

    print("\n")
    print(f"Your balance is now--> {data["balance"]}tk")





print("\n                                   Banking System")




while True:
    print("\n 1.Acount open")
    print(" 2.Cash in")
    print(" 3.Check balance")
    print(" 4.Exit")

    print("\n")

    chose = int(input(" Enter your choice:"))





    if chose == 1:
        account()
    elif chose == 2:
        update()
    elif chose == 3:
        check()
    else:
        break


print("End")