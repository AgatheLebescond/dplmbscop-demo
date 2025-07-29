# DplmbScop – Mini Prototype IA Citoyenne

Ce prototype Streamlit permet de :
- Scraper les tweets sur un sujet (ex: #LoiDuplomb)
- Générer un nuage de mots en temps réel
- Résumer un article de presse à partir de son URL

## ⚙️ Lancer en local

```bash
pip install -r requirements.txt
streamlit run app_dplmbscop_mini.py
```

## 🚀 Déploiement Streamlit Cloud

- Dépôt GitHub requis avec :
  - app_dplmbscop_mini.py
  - requirements.txt
  - README.md
- Aller sur [streamlit.io/cloud](https://streamlit.io/cloud), connecter votre GitHub
- Sélectionner ce dépôt et déployer

## Exemple de requête :
```
#LoiDuplomb lang:fr since:2025-07-01
```

## Exemple d’article :
```
https://www.lemonde.fr/politique/article/2025/07/22/la-loi-duplomb-enflamme-le-parlement_6184521_823448.html
```
