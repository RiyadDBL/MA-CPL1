# TP 13 – IA via API Ollama

Ce projet montre comment envoyer un message à une IA (Mistral via Ollama) et obtenir une réponse simple : Oui ou Non.

## Contenu
- tp_ollama.py : script Python qui envoie chaque email au serveur IA.
- emails.csv : dataset minimal contenant 4 emails.
- README.md : ce fichier.

## Exécution





## Exemple de sortie
Message : Pouvez-vous me rappeler ?
Réponse IA : Oui
Attendu : Oui
----------------------------------------
Message : Merci pour votre aide.
Réponse IA : Non
Attendu : Non
----------------------------------------

## Questions du TP
1. L’IA lit le message et décide s’il nécessite une réponse.
2. L’API sert à envoyer le texte au modèle IA et récupérer sa réponse.
3. L’IP est importante car l’IA tourne sur un serveur distant.
4. Si on change le texte, l’IA réanalyse et peut changer sa réponse.
