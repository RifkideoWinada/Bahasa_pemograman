def main():
  """Fungsi utama untuk menjalankan program kalkulator."""
  while True:
    print("\nKalkulator Sederhana")
    print("1. Perkalian")
    print("2. Pengurangan")
    print("3. Penambahan")
    print("4. Pembagian")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan Anda (1-4/0): ")

    if pilihan == '0':
      break
    elif pilihan == '1':
      perkalian()
    elif pilihan == '2':
      pengurangan()
    elif pilihan == '3':
      penambahan()
    elif pilihan == '4':
      pembagian()
    else:
      print("Pilihan tidak valid. Silakan coba lagi.")

def perkalian():
  """Fungsi untuk melakukan operasi perkalian."""
  bil1 = float(input("Masukkan bilangan pertama: "))
  bil2 = float(input("Masukkan bilangan kedua: "))
  hasil = bil1 * bil2
  print(f"{bil1} * {bil2} = {hasil}")

def pengurangan():
  """Fungsi untuk melakukan operasi pengurangan."""
  bil1 = float(input("Masukkan bilangan pertama: "))
  bil2 = float(input("Masukkan bilangan kedua: "))
  hasil = bil1 - bil2
  print(f"{bil1} - {bil2} = {hasil}")

def penambahan():
  """Fungsi untuk melakukan operasi penambahan."""
  bil1 = float(input("Masukkan bilangan pertama: "))
  bil2 = float(input("Masukkan bilangan kedua: "))
  hasil = bil1 + bil2
  print(f"{bil1} + {bil2} = {hasil}")

def pembagian():
  """Fungsi untuk melakukan operasi pembagian."""
  bil1 = float(input("Masukkan bilangan pertama: "))
  bil2 = float(input("Masukkan bilangan kedua: "))
  if bil2 == 0:
    print("Pembagian dengan nol tidak diizinkan.")
  else:
    hasil = bil1 / bil2
    print(f"{bil1} / {bil2} = {hasil}")

if __name__ == "__main__":
  main()