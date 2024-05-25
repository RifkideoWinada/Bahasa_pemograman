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

    // Check for division by zero
    if (angka2 != 0) {
        int pembagian = angka1 / angka2;
        // Menampilkan hasil
        cout << "Penjumlahan = " << penjumlahan << endl;
        cout << "Pengurangan = " << pengurangan << endl;
        cout << "Perkalian = " << perkalian << endl;
        cout << "Pembagian = " << pembagian << endl;
    } else {
        // Menampilkan hasil tanpa pembagian
        cout << "Penjumlahan = " << penjumlahan << endl;
        cout << "Pengurangan = " << pengurangan << endl;
        cout << "Perkalian = " << perkalian << endl;
        cout << "Pembagian tidak dapat dilakukan karena pembagi adalah nol." << endl;
    }

    return 0;
}
