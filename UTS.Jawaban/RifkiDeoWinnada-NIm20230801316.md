# 1.JELASKANN SECARA SINGKAT APA ITU PARADIGMA DALAM BAHASA PEMOGRAMAN?
"Paradigma pemrograman merupakan gaya, klasifikasi, dan pendekatan dalam penulisan program untuk memecahkan masalah dengan menggunakan bahasa pemrograman yang digunakan.
jenis jenis paradigma pemograman:
1. Pemrograman Fungsional
2. Pemograman Prosedural/Iteratif
3. Pemograman Berorientasi objek
4. Pemograman Deklaratif
# 2. JELASKAN APA YANG DIMAKSUD DENGAN MODEL DATA, OPERATOR, SELEKSI DAN FUNGSI ?
# Model Data
Model data dalam bahasa pemrograman merujuk pada cara struktur data diorganisasikan dan disimpan dalam memori. Ini mencakup tipe data dasar seperti integer, float, boolean, dan string, serta tipe data kompleks seperti array, list, dictionary, dan objek. Model data menentukan bagaimana data dapat diakses, dimanipulasi, dan dikelola dalam sebuah
program. 
# Operator: 
Operator adalah simbol yang digunakan untuk melakukan operasi pada data. Operator dapat diklasifikasikan berdasarkan jenis operasinya, seperti operator aritmatika, operator relasional, operator logis, dan operator bitwise.
# Seleksi:
Seleksi adalah proses memilih satu atau lebih pernyataan untuk dieksekusi berdasarkan kondisi tertentu. Pernyataan seleksi yang umum digunakan antara lain:
Pernyataan if-else: Digunakan untuk memilih satu dari dua pernyataan berdasarkan kondisi tertentu.
# Pernyataan switch-case: 
Digunakan untuk memilih satu dari beberapa pernyataan berdasarkan nilai variabel tertentu.
# Fungsi:
Fungsi adalah blok kode yang dirancang untuk melakukan tugas tertentu. Fungsi dapat dipanggil dari mana saja dalam program dan dapat mengembalikan nilai.
# Jelaskan konsep perulangan pernyataan (Looping Statement) di bawah ini:
int n = 1;
cout << "Masukkan jumlah baris: ";
cin >> n;

for (int i = 1; i < n; i++) {
    for (int j = 1; j <= i; j++) {
        cout << "*";
    }
    cout << endl;
}

# Penjelasan
Program di atas menggunakan dua perulangan for untuk menghasilkan pola segitiga bintang. Perulangan for pertama digunakan untuk mengulangi sebanyak jumlah baris yang dimasukkan oleh pengguna. Perulangan for kedua digunakan untuk mengulangi sebanyak jumlah kolom pada setiap baris.

Pada setiap iterasi perulangan for kedua, program mencetak karakter "*" sebanyak jumlah kolom pada baris tersebut. Kemudian, program mencetak karakter baris baru 
# NO 4
#include <iostream>
using namespace std;

int main() {
    int tahunLahir;
    const int tahunSekarang = 2024;

    // Meminta input dari pengguna
    cout << "Masukkan Tahun Lahir Kalian: ";
    cin >> tahunLahir;

    // Menghitung usia
    int usia = tahunSekarang - tahunLahir;

    // Menampilkan hasil
    cout << "Berarti Usia Kalian sekarang adalah " << usia << " Tahun" << endl;

    return 0;
}



# No 5
#include <iostream>
using namespace std;

int main() {
    int angka1, angka2;

    // Meminta input dari pengguna
    cout << "Masukkan Angka Pertama: ";
    cin >> angka1;
    cout << "Masukkan Angka Kedua: ";
    cin >> angka2;

    // Melakukan operasi aritmatika
    int penjumlahan = angka1 + angka2;
    int pengurangan = angka1 - angka2;
    int perkalian = angka1 * angka2;
    int pembagian = angka1 / angka2;

    // Menampilkan hasil
    cout << "Penjumlahan = " << penjumlahan << endl;
    cout << "Pengurangan = " << pengurangan << endl;
    cout << "Perkalian = " << perkalian << endl;
    cout << "Pembagian = " << pembagian << endl;

    return 0;

# NO 6
#include <iostream>
using namespace std;

// Deklarasi fungsi-fungsi
void menu();
void tambah();
void kurang();
void kali();
void bagi();

int main() {
    menu();
    tambah();
    kurang();
    kali();
    bagi();
    return 0;
}

void menu() {
    cout << "Pilih operasi aritmatika:" << endl;
    cout << "1. Penjumlahan" << endl;
    cout << "2. Pengurangan" << endl;
    cout << "3. Perkalian" << endl;
    cout << "4. Pembagian" << endl;
}

void tambah() {
    int a, b;
    cout << "Masukkan dua angka untuk penjumlahan:" << endl;
    cin >> a >> b;
    cout << "Hasil penjumlahan: " << a + b << endl;
}

void kurang() {
    int a, b;
    cout << "Masukkan dua angka untuk pengurangan:" << endl;
    cin >> a >> b;
    cout << "Hasil pengurangan: " << a - b << endl;
}

void kali() {
    int a, b;
    cout << "Masukkan dua angka untuk perkalian:" << endl;
    cin >> a >> b;
    cout << "Hasil perkalian: " << a * b << endl;
}

void bagi() {
    int a, b;
    cout << "Masukkan dua angka untuk pembagian:" << endl;
    cin >> a >> b;
    if (b != 0) {
        cout << "Hasil pembagian: " << a / b << endl;
    } else {
        cout << "Error: Pembagian dengan nol!" << endl;
    }
}

# No 7

Berikut adalah diagram alur (flowchart) untuk program yang telah kita buat:

Mulai (Start)
Tampilkan Menu
"Pilih operasi aritmatika:"
"1. Penjumlahan"
"2. Pengurangan"
"3. Perkalian"
"4. Pembagian"
Penjumlahan
Minta pengguna memasukkan dua angka (a dan b)
Hitung hasil penjumlahan (a + b)
Tampilkan hasil penjumlahan
Pengurangan
Minta pengguna memasukkan dua angka (a dan b)
Hitung hasil pengurangan (a - b)
Tampilkan hasil pengurangan
Perkalian
Minta pengguna memasukkan dua angka (a dan b)
Hitung hasil perkalian (a * b)
Tampilkan hasil perkalian
Pembagian
Minta pengguna memasukkan dua angka (a dan b)
Jika b != 0
Hitung hasil pembagian (a / b)
Tampilkan hasil pembagian
Jika b == 0
Tampilkan "Error: Pembagian dengan nol!"
Selesai (End)