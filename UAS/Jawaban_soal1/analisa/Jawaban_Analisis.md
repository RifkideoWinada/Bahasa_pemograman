#  SOAL
Jelaskan menurut anda apa itu function and recursive di python, dan berikan contoh codingannya serta capture hasilnya

# Function
Function adalah sebuah blok kode yang dapat dipanggil berulang kali dengan nama yang sama. Fungsi dapat menerima argumen dan mengembalikan nilai. Fungsi digunakan untuk mengurangi duplikasi kode, membuat kode lebih modular, dan memudahkan penggunaan kode.

Analisis:

1. Fungsi greet menerima satu argumen name.
2. Fungsi greet mencetak pesan "Halo, " + name + "!".
3. Fungsi greet dipanggil dua kali dengan argumen yang berbeda, yaitu "John" dan "Jane".
4. Hasilnya adalah pesan "Halo, John!" dan "Halo, Jane!" yang dicetak di layar.

Berikut adalah beberapa kelebihan dari menggunakan function:

1. Modularitas: Fungsi memungkinkan kita untuk memecahkan masalah yang kompleks menjadi bagian-bagian yang lebih kecil dan lebih mudah diatur.
2. Reusability: Fungsi dapat dipanggil berulang kali dengan argumen yang berbeda, sehingga kita tidak perlu menulis kode yang sama berulang kali.
3. Readability: Fungsi membuat kode lebih mudah dibaca dan dipahami, karena kita dapat memberikan nama yang deskriptif kepada fungsi dan argumennya.
4. Maintainability: Fungsi memungkinkan kita untuk memperbarui kode dengan lebih mudah, karena kita hanya perlu memperbarui kode di dalam fungsi.
Jenis-jenis Function

Berikut adalah beberapa jenis function di Python:

1. Function dengan argumen: Fungsi yang menerima argumen dan mengembalikan nilai.
2. Function tanpa argumen: Fungsi yang tidak menerima argumen dan mengembalikan nilai.
3. Function dengan default value: Fungsi yang menerima argumen dengan nilai default.
Function dengan variable arguments: Fungsi yang menerima argumen yang jumlahnya tidak tetap.

Berikut adalah beberapa best practice untuk menggunakan function di Python:

1. Gunakan nama yang deskriptif: Berikan nama yang deskriptif kepada fungsi dan argumennya, sehingga kode lebih mudah dibaca dan dipahami.
2. Jaga kode di dalam fungsi: Pastikan kode di dalam fungsi tidak terlalu panjang dan kompleks, sehingga lebih mudah dipahami dan diperbarui.
3. Gunakan fungsi untuk mengurangi duplikasi kode: Fungsi dapat membantu mengurangi duplikasi kode, sehingga kode lebih efisien dan lebih mudah diperbarui.

Dengan demikian, function adalah sebuah konsep yang sangat penting di Python, dan dapat membantu kita untuk menulis kode yang lebih efisien, lebih mudah dibaca, dan lebih mudah diperbarui.

# Recursive
Recursive adalah sebuah teknik pemrograman di mana sebuah fungsi memanggil dirinya sendiri. Fungsi recursive digunakan untuk menyelesaikan masalah yang dapat dipecah menjadi sub-masalah yang lebih kecil, dan kemudian menyelesaikan sub-masalah tersebut dengan cara yang sama.

Analisis:
1. Fungsi factorial menerima satu argumen n dan mengembalikan hasil perkalian dari n dan hasil factorial dari n-1.
2. Fungsi factorial memanggil dirinya sendiri dengan argumen n-1 sampai n menjadi 0.
3. Ketika n menjadi 0, fungsi factorial mengembalikan nilai 1.
4. Hasilnya adalah hasil perkalian dari n dan hasil factorial dari n-1, yaitu 5 * 4 * 3 * 2 * 1 = 120.

Kelebihan dari recursive adalah:
1. Dapat menyelesaikan masalah yang kompleks dengan cara yang lebih sederhana.
2. Dapat mengurangi jumlah kode yang dibutuhkan.

Kekurangan dari recursive adalah:

1. Dapat menyebabkan stack overflow jika fungsi recursive dipanggil terlalu banyak kali.
2. Dapat memperlambat kinerja program jika fungsi recursive dipanggil terlalu banyak kali.

Dalam menggunakan recursive, perlu diingat bahwa:

1. Fungsi recursive harus memiliki kondisi dasar yang menghentikan proses recursive.
2. Fungsi recursive harus memiliki argumen yang berubah dalam setiap panggilan.

Dengan demikian, recursive dapat menjadi alat yang efektif dalam menyelesaikan masalah yang kompleks, tetapi perlu digunakan dengan hati-hati dan bijak.

