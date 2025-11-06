# ...existing code...
def c_to_f(c): return c * 9/5 + 32
def c_to_k(c): return c + 273.15
def c_to_re(c): return c * 4/5
def c_to_rn(c): return (c + 273.15) * 9/5

def format_val(v):
    return f"{v:.2f}"

def convert_all(c):
    return {
        "Fahrenheit": format_val(c_to_f(c)),
        "Kelvin": format_val(c_to_k(c)),
        "Réaumur": format_val(c_to_re(c)),
        "Rankine": format_val(c_to_rn(c))
    }

def menu():
    print("Konversi suhu dari Celsius")
    print("1) Konversi semua")
    print("2) Ke Fahrenheit")
    print("3) Ke Kelvin")
    print("4) Ke Réaumur")
    print("5) Ke Rankine")
    print("0) Keluar")

def main():
    while True:
        try:
            menu()
            choice = input("Pilih (0-5): ").strip()
            if choice == "0":
                print("Selesai.")
                break
            val = input("Masukkan suhu dalam Celsius: ").strip()
            c = float(val)
        except ValueError:
            print("Input tidak valid. Masukkan angka (mis. 36.6).\n")
            continue

        if choice == "1":
            res = convert_all(c)
            for k, v in res.items():
                print(f"{k}: {v}")
        elif choice == "2":
            print("Fahrenheit:", format_val(c_to_f(c)))
        elif choice == "3":
            print("Kelvin:", format_val(c_to_k(c)))
        elif choice == "4":
            print("Réaumur:", format_val(c_to_re(c)))
        elif choice == "5":
            print("Rankine:", format_val(c_to_rn(c)))
        else:
            print("Pilihan tidak dikenal.")
        print()

if __name__ == "__main__":
    main()
# ...existing code...