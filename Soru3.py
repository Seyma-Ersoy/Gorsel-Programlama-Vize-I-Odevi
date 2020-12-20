a="Şeyma Ersoy"
e="Ers"
b=a.find(e)

if b>-1:
    baslangic=b-1
    bitis=baslangic+(len(e)+2)
    print(a[baslangic:bitis])
