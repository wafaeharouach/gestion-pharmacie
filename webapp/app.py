
import streamlit as st
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://mongodb:27017/")
db = client["pharmacie_db"]
collection = db["medicaments"]

st.title("🏥 Gestion de Pharmacie")

# Menu
menu = st.sidebar.selectbox(
    "Choisir une opération",
    [
        "🔎 Rechercher médicament",
        "➕ Ajouter médicament",
        "✏️ Modifier médicament",
        "🗑️ Supprimer médicament"
    ]
)

# =========================================================
# 1. RECHERCHER
# =========================================================

if menu == "🔎 Rechercher médicament":

    st.header("🔎 Rechercher un médicament")

    nom = st.text_input("Nom du médicament")

    if st.button("Rechercher"):
        medicament = collection.find_one({"nom": nom})

        if medicament:
            st.success("Médicament trouvé !")
            st.write("💊 Nom :", medicament["nom"])
            st.write("💰 Prix :", medicament["prix"], "MAD")
            st.write("📦 Quantité :", medicament["quantite"])
            st.write("📂 Catégorie :", medicament["categorie"])
            st.write("📅 Date d'expiration :", medicament["date_expiration"])
        else:
            st.error("Médicament introuvable.")


# =========================================================
# 2. AJOUTER
# =========================================================

elif menu == "➕ Ajouter médicament":

    st.header("➕ Ajouter un médicament")

    nom = st.text_input("Nom")
    prix = st.number_input("Prix (MAD)", min_value=0.0)
    quantite = st.number_input("Quantité", min_value=0, step=1)
    categorie = st.text_input("Catégorie")
    date_expiration = st.date_input("Date d'expiration")

    if st.button("Ajouter"):

        existe = collection.find_one({"nom": nom})

        if existe:
            st.warning("Ce médicament existe déjà.")
        elif nom == "":
            st.warning("Veuillez entrer le nom du médicament.")
        else:
            collection.insert_one({
                "nom": nom,
                "prix": prix,
                "quantite": quantite,
                "categorie": categorie,
                "date_expiration": str(date_expiration)
            })

            st.success("✅ Médicament ajouté avec succès !")


# =========================================================
# 3. MODIFIER
# =========================================================

elif menu == "✏️ Modifier médicament":

    st.header("✏️ Modifier un médicament")

    nom = st.text_input("Nom du médicament à modifier")

    if st.button("Chercher"):

        medicament = collection.find_one({"nom": nom})

        if medicament:

            st.success("Médicament trouvé.")

            nouveau_prix = st.number_input(
                "Nouveau prix (MAD)",
                value=float(medicament["prix"])
            )

            nouvelle_quantite = st.number_input(
                "Nouvelle quantité",
                value=int(medicament["quantite"]),
                step=1
            )

            nouvelle_categorie = st.text_input(
                "Nouvelle catégorie",
                value=medicament["categorie"]
            )

            nouvelle_date = st.text_input(
                "Nouvelle date d'expiration",
                value=medicament["date_expiration"]
            )

            if st.button("Enregistrer les modifications"):

                collection.update_one(
                    {"nom": nom},
                    {
                        "$set": {
                            "prix": nouveau_prix,
                            "quantite": nouvelle_quantite,
                            "categorie": nouvelle_categorie,
                            "date_expiration": nouvelle_date
                        }
                    }
                )

                st.success("✅ Médicament modifié avec succès !")

        else:
            st.error("Médicament introuvable.")


# =========================================================
# 4. SUPPRIMER
# =========================================================

elif menu == "🗑️ Supprimer médicament":

    st.header("🗑️ Supprimer un médicament")

    nom = st.text_input("Nom du médicament à supprimer")

    if st.button("Supprimer"):

        resultat = collection.delete_one({"nom": nom})

        if resultat.deleted_count > 0:
            st.success("✅ Médicament supprimé avec succès !")
        else:
            st.error("Médicament introuvable.")