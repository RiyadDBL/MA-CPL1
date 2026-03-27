import csv
import requests

API_URL = "http://gpu.cpnv.me:11434/api/generate"


def analyse_message(texte):
    prompt = f"""
Analyse le message et réponds seulement par :
- Oui si c'est une demande qui nécessite une réponse,
- Non sinon.

Message : {texte}
"""

    r = requests.post(API_URL, json={"model": "mistral:latest", "prompt": prompt})

    r.raise_for_status()
    data = r.json()
    return data["response"].strip()


with open("emails.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        message = row["email_text"]
        attendu = row["label_attendu"]
        resultat = analyse_message(message)

        print("Message :", message)
        print("Réponse IA :", resultat)
        print("Attendu :", attendu)
        print("-" * 40)
