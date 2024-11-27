def renters_rente_kalkulator():
    print("Velkommen til Renters Rente Kalkulator med månedlige innskudd!")
    
    # Brukerinput
    initial_belop = float(input("Hva er ditt initialbeløp (P)? "))
    manedlig_bidrag = float(input("Hva er ditt månedlige bidrag (M)? "))
    tids_horisont = float(input("Hvor mange år vil du spare (t)? "))
    arlig_rente = float(input("Hva er den årlige renten (%)? ")) / 100
    n = 12  # Månedlig sammensetning
    
    # Beregning av renters rente
    sluttbelop = initial_belop * (1 + arlig_rente / n) ** (n * tids_horisont)
    sluttbelop += manedlig_bidrag * (((1 + arlig_rente / n) ** (n * tids_horisont) - 1) / (arlig_rente / n))
    
    # Totalt beløp brukeren selv har satt inn
    totalt_innsatt = initial_belop + (manedlig_bidrag * 12 * tids_horisont)
    
    # Resultat
    print(f"\nEtter {tids_horisont} år:")
    print(f"- Totalt beløp spart (inkludert renter): {sluttbelop:,.2f} NOK")
    print(f"- Totalt beløp du selv har satt inn: {totalt_innsatt:,.2f} NOK")
    print(f"- Gevinst fra renter: {(sluttbelop - totalt_innsatt):,.2f} NOK")
    
# Kjør kalkulatoren
renters_rente_kalkulator()
