sayac=0
for x in range(102,988,1):
    a=int(x/100)
    b=int(x%100/10)
    c=int(x%10)


    if not a==b and not b==c and not a==c:
        print(str(a)+str(b)+str(c))
        sayac=sayac+1
print("Toplam ", sayac)


