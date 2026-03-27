# TP_12 – YOLO & Analyse d'image jointe à un e-mail
## Étape 4 – Réponses aux questions

---

### 1. Quels sont les types d'objets détectés dans l'image ?

Le fichier `.eml` contient une image (`objet.jpg`) dont le contenu visuel déterminera les classes détectées.  
YOLOv8n reconnaît **80 classes COCO** : personnes, voitures, chaises, téléphones, animaux, etc.  
Les résultats exacts sont listés dans `runs/detect/predict/detections.json` après exécution du script.

---

### 2. Le niveau de confiance est-il élevé ou faible ?

- Un score **≥ 0.70** (70 %) est considéré comme **élevé** : YOLO est très confiant dans sa détection.  
- Un score entre **0.50 et 0.70** est **moyen** : la détection est plausible mais incertaine.  
- Un score **< 0.50** est **faible** : l'objet est peut-être mal éclairé, partiellement caché ou hors des classes connues.

Les scores de confiance de chaque détection sont visibles dans `detections.json` (champ `"confidence"`).

---

### 3. YOLO a-t-il commis des erreurs visibles ? Explique.

YOLO peut commettre plusieurs types d'erreurs :

- **Faux positifs** : il détecte un objet qui n'existe pas réellement (ex. une texture confondue avec une personne).  
- **Faux négatifs** : il rate un objet présent dans l'image (ex. objet trop petit ou trop flou).  
- **Mauvaise classe** : il détecte bien un objet mais lui attribue la mauvaise étiquette (ex. confondre un chat et un chien).  
- **Bounding box imprécise** : la boîte englobante est décalée ou trop grande/petite.

Ces erreurs se vérifient visuellement en comparant l'image annotée (`runs/detect/predict/`) avec l'image originale.

---

### 4. Quel serait un cas où YOLO ne fonctionnerait pas bien ?

Plusieurs situations limitent les performances de YOLO :

- **Image très floue ou de mauvaise résolution** : les features visuelles sont trop dégradées.  
- **Objets inconnus du modèle** : YOLO (entraîné sur COCO) ne connaît que 80 classes. Un objet rare ou spécifique (ex. outil médical, pièce industrielle) ne sera pas reconnu.  
- **Fort encombrement visuel** : beaucoup d'objets superposés ou très petits peuvent être manqués.  
- **Conditions d'éclairage extrêmes** : image trop sombre, surexposée, ou avec reflets.  
- **Vue partielle** : objet fortement tronqué ou vu sous un angle inhabituel.  
- **Images aériennes ou satellites** : YOLO est entraîné sur des photos "terrestres", les perspectives aériennes donnent de mauvais résultats.
