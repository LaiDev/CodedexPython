""" Instructions 
We just got back from a trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

🇨🇴 Columbian pesos
🇵🇪 Peruvian soles
🇧🇷 Brazilian reais
Create a currency.py program that asks the user for the amount they have in peso, soles, and reais and calculates the total in USD.

Make sure to Google the current exchange rates! """

#Solution
peso = int(input("What do you have left in pesos? ")) * 0.0025
reais = int(input("What do you have left in reais? " )) *0.20364
soles = int(input("What do you have left in soles? ")) * 0.26704 

usd = peso + reais + soles
print(usd)
