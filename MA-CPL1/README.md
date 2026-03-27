# TP14 – Connexion n8n & Connecteur Outlook
**Étudiant :** Ryiad KATTAR  
**Filière :** Informatique – CPNV

## Objectif
Se connecter à n8n et configurer un connecteur Microsoft Outlook OAuth2 pour détecter les emails entrants.

## Configuration du connecteur OAuth2

| Paramètre | Valeur |
|---|---|
| Authorization URL | `https://login.microsoftonline.com/040c3629-dddb-4198-89fe-5af26d933b01/oauth2/v2.0/authorize` |
| Access Token URL | `https://login.microsoftonline.com/040c3629-dddb-4198-89fe-5af26d933b01/oauth2/v2.0/token` |
| Client ID | `c52c8d7e-8d8f-4859-a6a3-fd504a4315e0` |
| OAuth Redirect URL | `https://n8n.cpnv.me/rest/oauth2-credential/callback` |

## Workflow
Le workflow contient un seul node : **Microsoft Outlook Trigger**
- Poll : Every Minute
- Trigger On : Message Received
- Output : Simplified

## Résultat attendu
Lors de la réception d'un email, n8n affiche les champs suivants :

```json
{
  "id": "AAMkADIz...",
  "subject": "Test",
  "from": "ryiad.kattar@eduvaud.ch",
  "to": ["Ryiad.Kattar@cpnv.me"],
  "bodyPreview": "Hello World\nMeilleures salutations,\nRyiad Kattar",
  "hasAttachments": false,
  "categories": []
}
```

## Validation
- [x] Compte n8n créé
- [x] Connecteur Outlook configuré
- [x] Connexion Microsoft fonctionnelle
- [x] Email détecté depuis @eduvaud.ch

## Questions
1. **Quel événement déclenche le Microsoft Outlook Trigger ?** L'événement `Message Received` déclenche le workflow dès qu'un nouvel email arrive dans la boîte.
2. **Pourquoi le polling est-il configuré Every Minute ?** Outlook ne supporte pas les webhooks natifs dans n8n ; le polling toutes les minutes permet de vérifier régulièrement les nouveaux messages.
3. **Quelles informations pourraient être utilisées pour automatiser un traitement ?** Le sujet (`subject`), l'expéditeur (`from`), le corps du message (`bodyPreview`), et la présence de pièces jointes (`hasAttachments`).
