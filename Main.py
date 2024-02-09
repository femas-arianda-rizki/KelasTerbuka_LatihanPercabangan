# kalkulator sederhana
print("="*20)
print("Kalkulator Sederhana")
print("="*20, "\n")

angka_ke1 = float(input('masukkan angka ke1 :'))
operator = input("operator (+,-,x,/) :")
angka_ke2 = float(input("masukkan angka ke2 :"))

# percabangannya
if operator == "+":
  hasil = angka_ke1 + angka_ke2
  print(f"hasilnya adalah {hasil}")
elif operator == "-":
  hasil = angka_ke1 - angka_ke2
  print(f"hasilnya adalah {hasil}")
elif operator == "x" or operator == "*":
  hasil = angka_ke1 * angka_ke2
  print(f"hasilnya adalah {hasil}")
elif operator == "/":
  hasil = angka_ke1 / angka_ke2
  print(f"hasilnya adalah {hasil}")
else:
  print("Maaf ada kesalahan, periksa lagi masukkannya")

print("="*20)