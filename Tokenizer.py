# tokenizer.py – Version élève (squelette)

import re
import sys

# -----------------------------------------------------------
# 1) MODE 1 : découpe naïve par espaces
# -----------------------------------------------------------

def tokenize_whitespace(text):
    """
    TODO : retourner une liste de tokens découpés par espaces.
    """
    
    return text.split()
# permet de diviser le résultat obtenu par les espaces

# -----------------------------------------------------------
# 2) MODE 2 : découpe avec regex
# -----------------------------------------------------------

# Regex fournie (simplifiée)
TOKEN_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+|\d+|[.,;:!?()\"]")

def tokenize_regex(text):
    """
    TODO : retourner une liste de tokens basés sur la regex.
    """

    return TOKEN_RE.findall(text)
    # Indice : utiliser TOKEN_RE.findall(text)


# -----------------------------------------------------------
# 3) Interface en ligne de commande (CLI)
# -----------------------------------------------------------

# Usage attendu :
# python tokenizer.py whitespace "Bonjour le monde !"
# python tokenizer.py regex "J'aime les maths !"

# 1) Récupérer le mode depuis sys.argv[1]
# 2) Récupérer le texte depuis sys.argv[2:]
# 3) Appeler la bonne fonction selon le mode
# # 4) Afficher les tokens un par un

if __name__ == "__main__":
    # TODO :
    system_mode = sys.argv[1]  # Récupérer le mode (whitespace ou regex)
    system_text = " ".join(sys.argv[2:])  # Récupérer le texte à tokeniser
        # Appeler la fonction de tokenisation appropriée   
    if system_mode == "whitespace":
        tokens = tokenize_whitespace(system_text)
    elif system_mode == "regex":
        tokens = tokenize_regex(system_text)
    else:
        print("Mode inconnu. Utilisez 'whitespace' ou 'regex'.")
        sys.exit(1)
    # Afficher les tokens un par un
    for token in tokens:
        print(token)