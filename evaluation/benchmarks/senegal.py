"""
Benchmark IA pour le Sénégal.
Tests de compréhension du contexte sénégalais.
"""

SENEGAL_BENCHMARK = {
    "name": "Sénégal AI Benchmark v1",
    "description": "Évaluation de la compréhension du contexte sénégalais pour les modèles IA",
    "country_code": "SN",
    "country_name": "Sénégal",
    "version": "1.0",
    "language_code": "fr",
    "language_name": "Français",
    "category": "mixed",
    "tests": [
        # Mobile Money
        {
            "input_text": "Je veux envoyer 50000 FCFA à ma mère à Thiès via Wave. Comment faire ?",
            "expected_output": "Pour envoyer 50000 FCFA via Wave, ouvrez l'application Wave, sélectionnez 'Envoyer', entrez le numéro de téléphone de votre mère à Thiès, saisissez le montant de 50000 FCFA et confirmez la transaction avec votre code PIN.",
            "context": "Wave est le service de mobile money le plus utilisé au Sénégal, disponible dans tout le pays.",
            "category": "mobile_money",
            "difficulty": 1,
            "tags": ["wave", "mobile_money", "transfert"]
        },
        {
            "input_text": "Quelle est la différence entre Orange Money et Wave au Sénégal ?",
            "expected_output": "Orange Money et Wave sont deux services de mobile money au Sénégal. Wave est généralement consideré comme moins cher pour les transferts, tandis qu'Orange Money bénéficie du réseau Orange plus étendu dans les zones rurales.",
            "context": "Les deux services sont populaires au Sénégal avec des commissions différentes.",
            "category": "mobile_money",
            "difficulty": 2,
            "tags": ["orange_money", "wave", "comparaison"]
        },
        {
            "input_text": "Comment retirer de l'argent de mon compte Wave dans un point de vente ?",
            "expected_output": "Pour retirer de l'argent Wave, rendez-vous dans un point de vente Wave, sélectionnez 'Retrait' sur l'application, entrez le montant, et présentez le code de retrait au commerçant.",
            "context": "Les points de Wave sont des kiosques ou commerces partenaires dans tout le Sénégal.",
            "category": "mobile_money",
            "difficulty": 1,
            "tags": ["wave", "retrait", "point_de_vente"]
        },
        # Langues
        {
            "input_text": "Nanga def ? Je vais bien, tanne ci.",
            "expected_output": "La personne salué en wolof 'Nanga def' (comment vas-tu ?) et répond en français 'Je vais bien, merci'. C'est un mélange courant de wolof et de français au Sénégal.",
            "context": "Le code-switching wolof-français est très courant au Sénégal, surtout à Dakar.",
            "category": "linguistic",
            "difficulty": 3,
            "tags": ["wolof", "code_switching", "salutation"]
        },
        {
            "input_text": "Jërejëf, je cherche un taxi pour aller à la Médina.",
            "expected_output": "Le mot 'Jërejëf' signifie 'merci' en wolof. La personne cherche un taxi pour se rendre au quartier de la Médina, un quartier populaire de Dakar.",
            "context": "La Médina est l'un des quartiers les plus peuplés de Dakar.",
            "category": "linguistic",
            "difficulty": 2,
            "tags": ["wolof", "taxi", "dakar"]
        },
        {
            "input_text": "Mangi fi rekk, duñu fi xam-xam.",
            "expected_output": "Cette phrase en wolof signifie 'Je suis juste ici, on ne nous connaît pas ici'. C'est une expression d'un sentiment d'anonymat ou d'inconnu dans un lieu.",
            "context": "Le wolof est la langue la plus parlée au Sénégal, utilisé par environ 80% de la population.",
            "category": "linguistic",
            "difficulty": 4,
            "tags": ["wolof", "expression", "sentiment"]
        },
        # Administratif
        {
            "input_text": "Comment obtenir un acte de naissance à Dakar ?",
            "expected_output": "Pour obtenir un acte de naissance à Dakar, rendez-vous à la mairie de votre quartier avec votre carte d'identité ou celle de vos parents. Le coût est généralement de 500 FCFA et le délai est de 24 à 48 heures.",
            "context": "Les actes de naissance sont délivrés par les mairies d'arrondissement à Dakar.",
            "category": "administratif",
            "difficulty": 2,
            "tags": ["acte_naissance", "mairie", "dakar"]
        },
        {
            "input_text": "Quels documents faut-il pour créer une entreprise au Sénégal ?",
            "expected_output": "Pour créer une entreprise au Sénégal, vous avez besoin de : statuts de la société, accusé de réception du guichet unique (CFCE), publication au journal officiel, et inscription au RCCM. Le coût varie selon le type d'entreprise.",
            "context": "Le Centre de Formalités des Créations d'Entreprises (CFCE) est le guichet unique pour la création d'entreprise.",
            "category": "administratif",
            "difficulty": 3,
            "tags": ["entreprise", "creation", "formalites"]
        },
        # Commercial
        {
            "input_text": "Je cherche un fournisseur de mangues à Thiès pour exporter en Europe.",
            "expected_output": "Thiès est une importante zone de production de mangues au Sénégal. Vous pouvez contacter les coopératives agricoles de la région, comme la Coopérative des Producteurs de Mangues de Thiès. Pour l'export, vous aurez besoin de certifications phytosanitaires.",
            "context": "Thiès est la deuxième ville du Sénégal et un important centre agricole.",
            "category": "commercial",
            "difficulty": 3,
            "tags": ["mangues", "export", "agriculture"]
        },
        {
            "input_text": "Quel est le prix moyen d'un terrain à Diamniadio ?",
            "expected_output": "Diamniadio est une ville nouvelle en développement rapide près de Dakar. Les prix des terrains varient entre 5 et 20 millions de FCFA selon la localisation et la superficie. La zone est en pleine expansion avec de nombreux projets immobiliers.",
            "context": "Diamniadio est le nouveau pôle urbain de Dakar avec la construction de la Diamniadio Plateforme.",
            "category": "commercial",
            "difficulty": 2,
            "tags": ["immobilier", "diamniadio", "prix"]
        },
        # Culturel
        {
            "input_text": "Qu'est-ce que le Grand Magal de Touba ?",
            "expected_output": "Le Grand Magal de Touba est un pèlerinage religieux annuel de la confrérie des Mourides, commémorant l'exil du fondateur Cheikh Ahmadou Bamba. C'est l'un des plus grands rassemblements religieux au monde, attirant des millions de fidèles.",
            "context": "Touba est la sainte ville des Mourides, la plus grande confrérie religieuse du Sénégal.",
            "category": "cultural",
            "difficulty": 2,
            "tags": ["mourides", "touba", "religion"]
        },
        {
            "input_text": "C'est quoi le Teranga ?",
            "expected_output": "Le Teranga est un concept sénégalais qui signifie 'hospitalité'. C'est une valeur fondamentale de la culture sénégalaise qui se manifeste par l'accueil chaleureux des invités, le partage de nourriture et la générosité. C'est aussi le mot de ralliement des Sénégalais.",
            "context": "Le Teranga est au cœur de l'identité sénégalaise et influence tous les aspects de la vie sociale.",
            "category": "cultural",
            "difficulty": 1,
            "tags": ["teranga", "hospitalite", "culture"]
        },
        # Médical
        {
            "input_text": "Où trouver un centre de santé à Dakar pour une consultation ?",
            "expected_output": "Dakar dispose de nombreux centres de santé, dont le Centre Hospitalier National (CHN) de Fann, l'Hôpital Principal de Dakar, et plusieurs cliniques privées. Les centres de santé communautaires sont disponibles dans chaque arrondissement.",
            "context": "Le système de santé sénégalais comprend des structures publiques et privées.",
            "category": "medical",
            "difficulty": 1,
            "tags": ["sante", "hopital", "dakar"]
        },
        {
            "input_text": "Comment prévenir le paludisme au Sénégal ?",
            "expected_output": "Pour prévenir le paludisme au Sénégal : utilisez des moustiquaires imprégnées, appliquez des répulsifs, portez des vêtements couvrants le soir, éliminez les eaux stagnantes près de chez vous, et consultez un professionnel de santé en cas de fièvre.",
            "context": "Le paludisme est endémique au Sénégal, surtout pendant la saison des pluies.",
            "category": "medical",
            "difficulty": 2,
            "tags": ["paludisme", "prevention", "sante"]
        },
        # Éducatif
        {
            "input_text": "Quel est le système éducatif au Sénégal ?",
            "expected_output": "Le système éducatif sénégalais comprend : l'enseignement préscolaire, le primaire (6 ans), le secondaire (4+3 ans), et l'enseignement supérieur. La langue d'enseignement est le français, avec l'introduction du wolof comme langue d'apprentissage en primaire.",
            "context": "Le Sénégal a mis en place la gratuité de l'enseignement primaire depuis 2013.",
            "category": "educational",
            "difficulty": 2,
            "tags": ["education", "ecole", "systeme"]
        },
        {
            "input_text": "Comment s'inscrire à l'Université Cheikh Anta Diop ?",
            "expected_output": "Pour s'inscrire à l'UCAD : le candidat doit avoir le baccalauréat, se connecter sur le portail d'inscription en ligne, constituer son dossier, et se présenter à la faculté choisie. Les inscriptions se font généralement entre août et octobre.",
            "context": "L'UCAD est la plus grande université du Sénégal, située à Dakar.",
            "category": "educational",
            "difficulty": 2,
            "tags": ["universite", "ucad", "inscription"]
        },
        # Agricole
        {
            "input_text": "Quelles sont les principales cultures au Sénégal ?",
            "expected_output": "Les principales cultures au Sénégal sont : l'arachide (premier produit d'exportation), le mil, le sorgho, le maïs, le riz (surtout dans le delta du Sénégal et la Casamance), et les fruits (mangues, bananes, citrus).",
            "context": "L'agriculture emploie environ 60% de la population active sénégalaise.",
            "category": "agricultural",
            "difficulty": 1,
            "tags": ["agriculture", "cultures", "arachide"]
        },
        {
            "input_text": "Comment obtenir des semences certifiées au Sénégal ?",
            "expected_output": "Pour obtenir des semences certifiées au Sénégal, contactez le SNSMS (Service National des Semences et Matériel Semencier), les centres de recherche agronomique, ou les coopératives agricoles agréées. Le SNSMS délivre les certificaux de qualité.",
            "context": "Le SNSMS est l'organisme national de certification des semences au Sénégal.",
            "category": "agricultural",
            "difficulty": 3,
            "tags": ["semences", "certification", "agriculture"]
        },
        # Financier
        {
            "input_text": "Comment ouvrir un compte bancaire au Sénégal ?",
            "expected_output": "Pour ouvrir un compte bancaire au Sénégal, vous avez besoin de : pièce d'identité en cours de validité, justificatif de domicile, et un minimum de dépôt (généralement 10 000 à 50 000 FCFA). Les banques populaires comme la BCEAO offrent des conditions plus accessibles.",
            "context": "Le Sénégal dispose de nombreuses banques commerciales et de microfinance.",
            "category": "financial",
            "difficulty": 2,
            "tags": ["banque", "compte", "finance"]
        },
        {
            "input_text": "Qu'est-ce que le REV目前 ?",
            "expected_output": "Le REV (Réseau d'Épargne et de Vulgarisation) est un système d'épargne et de crédit populaire au Sénégal, organisé en groupes. Les membres cotisent régulièrement et peuvent obtenir des prêts à taux avantageux pour des projets de microfinance.",
            "context": "Les REV sont largement utilisés en milieu rural au Sénégal pour l'inclusion financière.",
            "category": "financial",
            "difficulty": 3,
            "tags": ["rev", "epargne", "microfinance"]
        },
        # Sécurité
        {
            "input_text": "Que faire en cas de vol de téléphone à Dakar ?",
            "expected_output": "En cas de vol de téléphone à Dakar : portez plainte au commissariat le plus proche, contactez votre opérateur pour bloquer la carte SIM et le téléphone, et signalez le vol sur le portail de l'ARTP si nécessaire.",
            "context": "L'ARTP (Agence de Régulation des Télécommunications) gère les plaintes liées aux télécommunications.",
            "category": "security",
            "difficulty": 2,
            "tags": ["vol", "telephone", "securite"]
        },
        {
            "input_text": "Comment signaler une escroquerie en ligne au Sénégal ?",
            "expected_output": "Pour signaler une escroquerie en ligne au Sénégal : contactez la Police des Fraudes Numériques au 117, déposez plainte au commissariat, et signalez l'escroquerie sur le site de la Direction de la Police Judiciaire. Conservez toutes les preuves numériques.",
            "context": "La Police des Fraudes Numériques est spécialisée dans la cybercriminalité au Sénégal.",
            "category": "security",
            "difficulty": 2,
            "tags": ["escroquerie", "cybercriminalite", "signalement"]
        }
    ]
}


def get_senegal_benchmark():
    """Retourne le benchmark Sénégal."""
    return SENEGAL_BENCHMARK
