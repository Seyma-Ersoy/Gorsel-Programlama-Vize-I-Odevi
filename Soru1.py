eMail="seymaersoy1@gmail.com"
for x in range(0,len(eMail)):
    if (eMail[x] == "@"):
        print("Bu bir eMaildir.")
        break
else:
    print("Bu bir eMail değildir.")
