def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n - 1)


angka = int(input("Masukkan angka: "))
hasil = faktorial(angka)
print("Faktorial dari", angka, "adalah", hasil)
