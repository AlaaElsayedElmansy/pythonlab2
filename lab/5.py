count =0
total=0
while True:
    number= input("enter number")
    if number == "done":
        break;
    elif number.isdigit():
        number=int(number)
        count=number+1
        total+=number
    else:
        print("not number")
avrage=total/count

print(f"total = {total}")
print (f"avrage = {avrage}")