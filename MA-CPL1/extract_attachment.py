"""
TP_12 - Étape 2 : Extraction de la pièce jointe d'un fichier .eml
Usage : python extract_attachment.py <fichier.eml>
"""

import email
import os
import sys


def extract_image_from_eml(
    eml_path: str, output_dir: str = "attachments"
) -> str | None:
    """
    Ouvre un fichier .eml, parcourt les pièces jointes,
    trouve la première image et l'enregistre dans output_dir/.
    Retourne le chemin du fichier sauvegardé, ou None si aucune image trouvée.
    """
    # Créer le dossier de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)

    # Lire et parser le fichier .eml
    with open(eml_path, "rb") as f:
        msg = email.message_from_bytes(f.read())

    # Parcourir toutes les parties du message
    for part in msg.walk():
        content_type = part.get_content_type()

        # On cherche uniquement les images (image/jpeg, image/png, etc.)
        if content_type.startswith("image/"):
            # Récupérer le nom de fichier depuis les headers
            filename = part.get_filename()
            if not filename:
                # Générer un nom par défaut selon le type MIME
                ext = content_type.split("/")[1]  # ex: "jpeg" -> "jpeg"
                filename = f"image.{ext}"

            output_path = os.path.join(output_dir, filename)

            # Décoder et sauvegarder l'image
            with open(output_path, "wb") as img_file:
                img_file.write(part.get_payload(decode=True))

            print(f"[OK] Image extraite : {output_path}")
            return output_path

    print("[ERREUR] Aucune image trouvée dans le fichier .eml.")
    return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python extract_attachment.py <fichier.eml>")
        sys.exit(1)

    eml_file = sys.argv[1]

    if not os.path.exists(eml_file):
        print(f"[ERREUR] Fichier introuvable : {eml_file}")
        sys.exit(1)

    result = extract_image_from_eml(eml_file)

    if result is None:
        sys.exit(1)
