def divide_numbers(a, b):
    try:
        result = a / b
        print("Hasil pembagian:", result)
    except ZeroDivisionError:
        print("Error: Tidak dapat membagi dengan nol!")
    except TypeError:
        print("Error: Input harus berupa angka!")
    finally:
        print("Program selesai dijalankan.")

divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "a")