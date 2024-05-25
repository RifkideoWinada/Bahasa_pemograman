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