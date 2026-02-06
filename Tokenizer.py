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
    # Indice : utiliser TOKEN_RE.findall(text)
    pass


# -----------------------------------------------------------
# 3) Interface en ligne de commande (CLI)
# -----------------------------------------------------------

# Usage attendu :
# python tokenizer.py whitespace "Bonjour le monde !"
# python tokenizer.py regex "J'aime les maths !"

if __name__ == "__main__":
    # TODO :
    # 1) Récupérer le mode depuis sys.argv[1]
    # 2) Récupérer le texte depuis sys.argv[2:]
    # 3) Appeler la bonne fonction selon le mode
    # 4) Afficher les tokens un par un

    pass