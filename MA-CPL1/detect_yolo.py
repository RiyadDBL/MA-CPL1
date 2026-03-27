"""
TP_12 - Étape 3 : Détection d'objets avec YOLOv8
Usage : python detect_yolo.py <chemin_image>
Génère :
  - Une image annotée dans runs/detect/predict/
  - Un fichier detections.json dans runs/detect/predict/
"""

import json
import os
import sys

from ultralytics import YOLO


def detect_objects(image_path: str, output_dir: str = "runs/detect/predict") -> None:
    """
    Charge YOLOv8n, effectue la détection sur l'image,
    sauvegarde l'image annotée et un fichier detections.json.
    """
    if not os.path.exists(image_path):
        print(f"[ERREUR] Image introuvable : {image_path}")
        sys.exit(1)

    # Créer le dossier de sortie
    os.makedirs(output_dir, exist_ok=True)

    # Charger le modèle YOLOv8n pré-entraîné (téléchargé automatiquement)
    print("[INFO] Chargement du modèle YOLOv8n...")
    model = YOLO("yolov8n.pt")

    # Effectuer la détection
    print(f"[INFO] Analyse de l'image : {image_path}")
    results = model(image_path, save=True, project="runs/detect", name="predict", exist_ok=True)

    # ---- Construire le fichier detections.json ----
    detections = []

    for result in results:
        boxes = result.boxes

        if boxes is None or len(boxes) == 0:
            print("[AVERTISSEMENT] Aucun objet détecté dans l'image.")
        else:
            for box in boxes:
                class_id = int(box.cls[0])
                class_name = model.names[class_id]
                confidence = float(box.conf[0])
                x1, y1, x2, y2 = box.xyxy[0].tolist()

                detection = {
                    "class_id": class_id,
                    "class_name": class_name,
                    "confidence": round(confidence, 4),
                    "bounding_box": {
                        "x1": round(x1, 2),
                        "y1": round(y1, 2),
                        "x2": round(x2, 2),
                        "y2": round(y2, 2),
                    },
                }
                detections.append(detection)
                print(
                    f"  -> {class_name} | confiance : {confidence:.2%} "
                    f"| box : [{x1:.0f}, {y1:.0f}, {x2:.0f}, {y2:.0f}]"
                )

    # Sauvegarder le JSON
    json_path = os.path.join(output_dir, "detections.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "image": image_path,
                "model": "yolov8n",
                "total_detections": len(detections),
                "detections": detections,
            },
            f,
            indent=2,
            ensure_ascii=False,
        )

    print(f"\n[OK] {len(detections)} objet(s) détecté(s).")
    print(f"[OK] Image annotée sauvegardée dans : {output_dir}/")
    print(f"[OK] Fichier JSON sauvegardé : {json_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python detect_yolo.py <chemin_image>")
        print("Exemple : python detect_yolo.py attachments/objet.jpg")
        sys.exit(1)

    detect_objects(sys.argv[1])
