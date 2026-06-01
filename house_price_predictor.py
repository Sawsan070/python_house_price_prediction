# Project 3: Huizenprijzen voorspellen met PANDAS!
import pandas as pd

# 1. We maken een nette tabel (DataFrame) met Pandas
data = {
    'Kamers': [1, 2, 3, 4, 5],
    'Prijs': [150000, 250000, 350000, 450000, 550000]
}
df = pd.DataFrame(data)

print("--- De data in Pandas-tabelvorm: ---")
print(df)
print("------------------------------------")

# 2. De computer berekent het gemiddelde met een Pandas-functie
gemiddelde_prijs = df['Prijs'].mean()
print(f"De gemiddelde huizenprijs is: €{gemiddelde_prijs},-")

# 3. Voorspelling voor een huis met 6 kamers
def voorspel_prijs(nieuwe_kamers):
    return 50000 + (nieuwe_kamers * 100000)

voorspelling = voorspel_prijs(6)
print(f"Voorspelling: Een huis met 6 kamers kost ongeveer €{voorspelling},-")