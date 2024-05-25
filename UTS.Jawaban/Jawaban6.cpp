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
