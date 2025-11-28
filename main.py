import requests

name = "amadou"
print(f"Hello {name}")


nb = 42
print("hyna -> 42 %x" % nb)  # entier en hexadécimal minuscule
print(f"hyna -> 42 : {nb:x}")  # entier en hexadécimal avec les f-string

price = 20.457
print("Prix: %10.2f" % price)  # largeur minimal de 10 caractères, 2 décimal
print(f"Prix: {price:8.2f}")  # meme résultat avec les f-string
print("*" * 50)
response = requests.get("https://www.pyton.org")
print("Statut de la réponse :", response.status_code)
