import pandas as pd
import matplotlib.pyplot as plt

# Memuat data dari file CSV
df = pd.read_csv('data_dokumen.csv')

# Menampilkan lima baris pertama dari data
print("Data Dokumen:")
print(df.head())

# Analisis sederhana: jumlah dokumen per kata kunci
keyword_counts = df['kata_kunci'].value_counts()

# Menampilkan hasil analisis
print("\nJumlah Dokumen per Kata Kunci:")
print(keyword_counts)

# Visualisasi hasil analisis
plt.figure(figsize=(10, 6))
keyword_counts.plot(kind='bar')
plt.title('Jumlah Dokumen per Kata Kunci')
plt.xlabel('Kata Kunci')
plt.ylabel('Jumlah Dokumen')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
