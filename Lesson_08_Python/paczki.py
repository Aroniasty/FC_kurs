#dodać limit elementu w zakresie 1-10 kg

liczba_elementow = int(input("Podaj mi ilość elementów: "))
suma_wszystkich_kilogramow = 0
waga_paczki = 0
ilosc_paczek = 1
suma_pustych_kilogramow = 0
paczka_z_najwieksza_iloscia_pustcy_kg = 1
najwecej_pustych_kg = 0
for element in range(liczba_elementow):
    waga_elementu = float(input("Podaj mi wagę elementu: "))
    suma_wszystkich_kilogramow += waga_elementu
    if waga_elementu + waga_paczki < 20:
        waga_paczki += waga_elementu
    else:
        suma_pustych_kilogramow += (20 - waga_paczki)
        puste_kg_w_tej_paczce = 20 - waga_paczki
        if puste_kg_w_tej_paczce > najwecej_pustych_kg:
            paczka_z_najwieksza_iloscia_pustcy_kg = ilosc_paczek
            najwecej_pustych_kg = puste_kg_w_tej_paczce
        ilosc_paczek += 1
        waga_paczki = waga_elementu
puste_kg_w_ostatniej_paczce = 20 - waga_paczki
suma_pustych_kilogramow += (20 -waga_paczki)
if puste_kg_w_ostatniej_paczce > najwecej_pustych_kg:
    paczka_z_najwieksza_iloscia_pustcy_kg = ilosc_paczek
    najwecej_pustych_kg = puste_kg_w_ostatniej_paczce

print(f"Suma wszystkich kg wysłanych to: {suma_wszystkich_kilogramow}")
print(f"Ilość paczek to: {ilosc_paczek}")
print(f"Liczba pustch kg w paczkach to: {suma_pustych_kilogramow}")
print(f"Najmniej kg było w paczce {paczka_z_najwieksza_iloscia_pustcy_kg}, było to: {najwecej_pustych_kg}")