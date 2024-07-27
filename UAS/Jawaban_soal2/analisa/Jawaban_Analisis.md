# Apa itu Exception Handling?
Exception Handling adalah sebuah mekanisme di dalam bahasa pemrograman yang memungkinkan kita untuk menangani kesalahan atau exception yang terjadi saat kode dijalankan. Exception adalah sebuah kondisi yang tidak diharapkan terjadi saat kode dijalankan, seperti kesalahan sintaks, kesalahan logika, atau kesalahan input.

# Tujuan Exception Handling
Tujuan dari Exception Handling adalah untuk:

1. Menangani kesalahan yang terjadi saat kode dijalankan
2. Mencegah program dari crash atau berhenti secara tiba-tiba
3. Memberikan pesan error yang lebih informatif kepada pengguna
4. Memungkinkan program untuk melanjutkan eksekusi setelah kesalahan terjadi
Function of Exception Handling

Function of Exception Handling adalah untuk menangani kesalahan yang terjadi saat kode dijalankan. Berikut adalah beberapa function of Exception Handling:

1. Try: Blok kode yang berisi kode yang mungkin menghasilkan kesalahan
2. Except: Blok kode yang berisi kode yang akan dijalankan jika kesalahan terjadi
3. Raise: Menghasilkan kesalahan yang akan ditangani oleh Except block
4. Finally: Blok kode yang akan dijalankan baik kesalahan terjadi atau tidak

# Analisa Lengkap

Berikut adalah analisa lengkap dari contoh codingan di atas:

# Try Block
1. try block berisi kode yang mungkin menghasilkan kesalahan, yaitu result = a / b.
2. Kode ini akan menghasilkan kesalahan jika b adalah nol atau jika input tidak berupa angka.

# Except Block
1. except block berisi kode yang akan dijalankan jika kesalahan terjadi.
2. except ZeroDivisionError: akan menangani kesalahan jika b adalah nol.
3. print("Error: Tidak dapat membagi dengan nol!") akan dijalankan jika kesalahan terjadi.
4. except TypeError: akan menangani kesalahan jika input tidak berupa angka.
5. print("Error: Input harus berupa angka!") akan dijalankan jika kesalahan terjadi.

# Finally Block
1. finally block berisi kode yang akan dijalankan baik kesalahan terjadi atau tidak.
2. print("Program selesai dijalankan.") akan dijalankan setelah try block dan except block selesai dijalankan.
Kelebihan Exception Handling

Berikut adalah beberapa kelebihan dari menggunakan Exception Handling:

1. Mencegah program dari crash: Exception Handling memungkinkan kita untuk menangani kesalahan yang terjadi saat kode dijalankan, sehingga program tidak akan crash atau berhenti secara tiba-tiba.
2. Memberikan pesan error yang lebih informatif: Exception Handling memungkinkan kita untuk memberikan pesan error yang lebih informatif kepada pengguna, sehingga pengguna dapat memahami apa yang terjadi.
3. Memungkinkan program untuk melanjutkan eksekusi: Exception Handling memungkinkan kita untuk melanjutkan eksekusi program setelah kesalahan terjadi, sehingga program dapat melanjutkan eksekusi dengan lebih stabil dan lebih aman.

Dengan demikian, Exception Handling adalah sebuah mekanisme yang sangat penting di dalam bahasa pemrograman, karena memungkinkan kita untuk menangani kesalahan yang terjadi saat kode dijalankan dan membuat program lebih stabil dan lebih aman.