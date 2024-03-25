def konversi_reamur(celcius):
    konversi_reamur = 4 * celcius / 5
    return konversi_reamur

def konversi_fahrenheit(celcius):
    konversi_fahrenheit = 9 * celcius / 5 + 32
    return konversi_fahrenheit

def konversi_kelvin(celcius):
    konversi_kelvin = celcius + 273
    return konversi_kelvin

print("=" * 25)
print("     Program Konversi Suhu      ")
print("=" * 25)
temperatur_suhu = int(input("Masukkan Skala Celcius: "))
print("=" * 35)
print(f"Hasil Konversi Suhu {temperatur_suhu} C adalah {konversi_reamur(temperatur_suhu)} Reamur")
print(f"Hasil Konversi Suhu {temperatur_suhu} C adalah {konversi_fahrenheit(temperatur_suhu)} Fahrenheit")
print(f"Hasil Konversi Suhu {temperatur_suhu} C adalah {konversi_kelvin(temperatur_suhu)} Kelvin")