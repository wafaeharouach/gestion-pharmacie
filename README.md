# 💊 Gestion de Pharmacie

## 📌 Présentation du projet

Gestion de Pharmacie est une application web développée avec Python et Streamlit. Elle permet de gérer les médicaments d'une pharmacie à travers une interface simple et intuitive.

Le projet utilise MongoDB pour stocker les données et Docker pour faciliter le déploiement de l'application.

## 🛠️ Technologies utilisées

- Python
- Streamlit
- MongoDB
- Docker
- Docker Compose

## ✨ Fonctionnalités

- 🔍 Rechercher un médicament.
- ➕ Ajouter un nouveau médicament.
- ✏️ Modifier les informations d'un médicament.
- 🗑️ Supprimer un médicament.
- 💾 Stocker les données dans MongoDB.

## 📁 Structure du projet

```text
gestion-pharmacie/
│
├── docker-compose.yml
│
└── webapp/
    ├── app.py
    ├── init_db.py
    ├── Dockerfile
    └── requirements.txt
```

## 🚀 Installation et lancement

### 1. Cloner le dépôt

```bash
git clone https://github.com/wafaeharouach/gestion-pharmacie.git
```

### 2. Accéder au dossier

```bash
cd gestion-pharmacie
```

### 3. Lancer l'application avec Docker Compose

```bash
docker compose up --build
```

### 4. Accéder à l'application

Ouvrir le navigateur et accéder à :

```text
http://localhost:8501
```

## 👩‍💻 Auteur

**Wafae Harouach**

Étudiante en deuxième année en Intelligence Artificielle – Option Big Data.
