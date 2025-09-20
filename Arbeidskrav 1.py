"""
Arbeidskrav 1

@author: peerapas
"""

'Variabler'
km_per_år = 10000 #km per år (km/år)
f_el = 5000 #forsikring elbil (kr/år)
f_bensin = 7500 #forsikring bensinbil (kr/år)
tfa = 8.38 #trafikkforsikringavgift (kr/dag)
d_el = 0.2 #driftstoffbruk elbil (kWh/km)
d_bensin = 1 #driftstoffbruk bensinbil (kr/km)
strømpris = 2 #strømpris (kr/kWh)
b_el = 0.1 #bomavgifter elbil (kr/km)
b_bensin = 0.3 #bomavgifter bensinbil (kr/km)

'Elbil'
total_el = f_el + tfa*365 + km_per_år*d_el*strømpris + km_per_år*b_el
print("Totalkostnad for elbil = ", total_el, "kr/år")

'Bensin'
total_bensin = f_bensin + tfa*365 + km_per_år*d_bensin + km_per_år*b_bensin
print("Totalkostnad for bensinbil = ", total_bensin, "kr/år")

'Kostnadsdifferanse'
diff = total_bensin - total_el
print("Kostnadsdifferanse =", diff, "kr/år")
