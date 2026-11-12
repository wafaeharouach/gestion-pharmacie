from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017/")

db = client["pharmacie_db"]
collection = db["medicaments"]

medicaments = [
    {
        "nom": "Paracetamol",
        "prix": 25,
        "quantite": 50,
        "categorie": "Antalgique",
        "date_expiration": "2027-05-10"
    },
    {
        "nom": "Doliprane",
        "prix": 30,
        "quantite": 35,
        "categorie": "Antalgique",
        "date_expiration": "2027-08-15"
    },
    {
        "nom": "Amoxicilline",
        "prix": 45,
        "quantite": 20,
        "categorie": "Antibiotique",
        "date_expiration": "2027-03-20"
    },
    {
        "nom": "Ibuprofene",
        "prix": 28,
        "quantite": 60,
        "categorie": "Anti-inflammatoire",
        "date_expiration": "2028-01-10"
    },
    {
        "nom": "Vitamine C",
        "prix": 40,
        "quantite": 15,
        "categorie": "Vitamine",
        "date_expiration": "2027-11-05"
    },
    {
        "nom": "Aspirine",
        "prix": 22,
        "quantite": 45,
        "categorie": "Antalgique",
        "date_expiration": "2027-09-12"
    },
    {
        "nom": "Sirop Toux",
        "prix": 55,
        "quantite": 10,
        "categorie": "Sirop",
        "date_expiration": "2027-06-18"
    },
    {
        "nom": "Omeprazole",
        "prix": 35,
        "quantite": 25,
        "categorie": "Digestif",
        "date_expiration": "2028-02-28"
    }
]

if collection.count_documents({}) == 0:
    collection.insert_many(medicaments)
    print("✅ Données insérées dans MongoDB")
else:
    print("ℹ️ Les données existent déjà")