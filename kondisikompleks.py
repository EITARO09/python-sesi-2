a = int(input("masukan bilangan a :"))
b = int(input("masukan bilangan b :"))
c = int(input("masukan bilangan c :"))

kondisi_a = (a > b) or (a > c)
kondisi_b = (a % 2 == 0 or c % 2 != 0)
kondisi_c = (b != c)

if kondisi_a and kondisi_b and kondisi_c:
    print("kondisi terpenuhi")
else:
    print("kondisi tidak terpenuhi")

