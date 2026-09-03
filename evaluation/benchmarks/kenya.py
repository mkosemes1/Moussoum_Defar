"""
Benchmark IA pour le Kenya.
Tests de compréhension du contexte kényan.
"""

KENYA_BENCHMARK = {
    "name": "Kenya AI Benchmark v1",
    "description": "Évaluation de la compréhension du contexte kényan pour les modèles IA",
    "country_code": "KE",
    "country_name": "Kenya",
    "version": "1.0",
    "language_code": "en",
    "language_name": "English",
    "category": "mixed",
    "tests": [
        # Mobile Money
        {
            "input_text": "How do I send money to someone in Mombasa using M-Pesa?",
            "expected_output": "To send money via M-Pesa: Open the M-Pesa app or dial *334#, select 'Send Money', enter the recipient's Safaricom number, input the amount, add an optional reference, and confirm with your M-Pesa PIN. The money is sent instantly.",
            "context": "M-Pesa is the dominant mobile money service in Kenya, operated by Safaricom.",
            "category": "mobile_money",
            "difficulty": 1,
            "tags": ["mpesa", "safaricom", "transfer"]
        },
        {
            "input_text": "What is the difference between M-Pesa and Airtel Money in Kenya?",
            "expected_output": "M-Pesa (Safaricom) has the largest market share in Kenya with extensive agent network. Airtel Money (Airtel) typically offers lower transaction fees and competitive rates. M-Pesa has more features like M-Shwari and KCB M-Pesa, while Airtel Money focuses on affordability.",
            "context": "Safaricom M-Pesa dominates with over 80% market share in Kenya's mobile money.",
            "category": "mobile_money",
            "difficulty": 2,
            "tags": ["mpesa", "airtel_money", "comparison"]
        },
        {
            "input_text": "How do I pay my electricity bill using M-Pesa?",
            "expected_output": "To pay KPLC electricity bill via M-Pesa: Dial *334#, select 'Lipa Na M-Pesa', then 'Pay Bill', enter KPLC business number (887660), enter your prepaid meter number as the account number, input the amount, confirm with your PIN, and you'll receive a confirmation message.",
            "context": "Kenya Power and Lighting Company (KPLC) accepts M-Pesa payments for electricity.",
            "category": "mobile_money",
            "difficulty": 1,
            "tags": ["electricity", "kplc", "bill_payment"]
        },
        # Languages
        {
            "input_text": "Niko aje? Poa sana, niko home.",
            "expected_output": "The user is speaking Sheng (Kenyan slang combining Swahili and English). 'Niko aje?' means 'How am I?' (rhetorical greeting), 'Poa sana' means 'Very cool/good', and 'niko home' means 'I'm at home'. Sheng is widely used by urban youth in Kenya.",
            "context": "Sheng is a creole language widely spoken in urban areas of Kenya, especially Nairobi.",
            "category": "linguistic",
            "difficulty": 3,
            "tags": ["sheng", "swahili", "slang"]
        },
        {
            "input_text": "Ningependa kwenda Uhuru Park,omba,nionyeshe njia.",
            "expected_output": "The user is asking in Swahili: 'I would like to go to Uhuru Park, please show me the way.' Uhuru Park is a public park in Nairobi, near the city center. It's a popular recreational area with a lake and green spaces.",
            "context": "Uhuru Park is an iconic public park in Nairobi's central business district.",
            "category": "linguistic",
            "difficulty": 2,
            "tags": ["swahili", "uhuru_park", "directions"]
        },
        # Administratif
        {
            "input_text": "How do I get a national ID card in Kenya?",
            "expected_output": "To get a Kenyan national ID: Visit your nearest Huduma Center with your birth certificate and passport photos. Fill out the application form, provide biometric data (fingerprints and photo), and pay the required fee. Processing takes 10-30 days. You must be 18+ years old.",
            "context": "Huduma Centers are one-stop service centers for government services in Kenya.",
            "category": "administrative",
            "difficulty": 2,
            "tags": ["national_id", "huduma", "registration"]
        },
        {
            "input_text": "How do I register a business in Kenya?",
            "expected_output": "To register a business in Kenya: Search for business name availability at eCitizen, reserve the name, complete the registration form, provide KRA PIN, pay the registration fee, and receive your certificate of registration. The process takes 1-7 working days through eCitizen platform.",
            "context": "Kenya uses the eCitizen platform for most government services including business registration.",
            "category": "administrative",
            "difficulty": 3,
            "tags": ["business_registration", "ecitizen", "kra"]
        },
        # Commercial
        {
            "input_text": "I want to rent an apartment in Nairobi. What are the typical prices?",
            "expected_output": "Apartment rental prices in Nairobi vary by area: Studios in CBD: 15,000-25,000 KES/month. 1-bedroom in Westlands: 25,000-45,000 KES. 2-bedroom in Kilimani: 35,000-60,000 KES. 3-bedroom in Karen: 80,000-150,000 KES. Prices include or exclude service charges.",
            "context": "Nairobi has diverse neighborhoods with varying price ranges for housing.",
            "category": "commercial",
            "difficulty": 2,
            "tags": ["rent", "nairobi", "housing"]
        },
        {
            "input_text": "How much does it cost to ship goods from Mombasa to Nairobi?",
            "expected_output": "Shipping from Mombasa to Nairobi: By road, trucking costs approximately 30,000-80,000 KES for a 20ft container. Railway transport via SGR costs less but takes longer. For individual items, courier services charge 500-2,000 KES per kg. The journey takes 8-12 hours by road.",
            "context": "Mombasa is Kenya's main port city, and most imports pass through it to Nairobi.",
            "category": "commercial",
            "difficulty": 2,
            "tags": ["shipping", "mombasa", "logistics"]
        },
        # Culturel
        {
            "input_text": "What is the significance of the Maasai Moran ceremony?",
            "expected_output": "The Maasai Moran (warrior) ceremony, known as 'Eunoto', marks the transition of junior warriors to senior warriors. It involves shaving the warriors' long hair, a celebration feast, and the warriors receiving new responsibilities. It's a key rite of passage in Maasai culture.",
            "context": "The Maasai are a Nilotic ethnic group inhabiting northern Kenya and Tanzania.",
            "category": "cultural",
            "difficulty": 2,
            "tags": ["maasai", "ceremony", "tradition"]
        },
        {
            "input_text": "What is Nyama Choma and where is it popular?",
            "expected_output": "Nyama Choma is roasted meat, Kenya's most popular social food. It's typically goat or beef, seasoned with salt and served with ugali, kachumbari (tomato-onion salad), and sometimes chapati. It's popular at social gatherings, restaurants, and roadside joints, especially in Nairobi and rural areas.",
            "context": "Nyama Choma is an integral part of Kenyan social life and celebrations.",
            "category": "cultural",
            "difficulty": 1,
            "tags": ["nyama_choma", "food", "culture"]
        },
        # Médical
        {
            "input_text": "Where can I find a good hospital in Nairobi?",
            "expected_output": "Nairobi has several top hospitals: Kenyatta National Hospital (KNH) is the largest public hospital, Nairobi Hospital in Argwings Kodhek Road is a leading private facility, Aga Khan University Hospital in Parklands, and MP Shah Hospital in Shivaji Nagar. For specialized care, KNH and Nairobi Hospital are recommended.",
            "context": "Nairobi is Kenya's medical hub with both public and private healthcare facilities.",
            "category": "medical",
            "difficulty": 1,
            "tags": ["hospital", "nairobi", "healthcare"]
        },
        {
            "input_text": "How do I prevent cholera in Kenya?",
            "expected_output": "To prevent cholera in Kenya: Drink only treated or boiled water, wash hands with soap before eating and after using the toilet, eat food that is thoroughly cooked and served hot, avoid raw vegetables and fruits that can't be peeled, and use properly treated water for brushing teeth.",
            "context": "Cholera outbreaks occur periodically in Kenya, especially during rainy seasons.",
            "category": "medical",
            "difficulty": 2,
            "tags": ["cholera", "prevention", "health"]
        },
        # Éducatif
        {
            "input_text": "How do I get admission to University of Nairobi?",
            "expected_output": "To gain admission to UoN: Score at least C+ in KCSE, apply through KUCCPS (Kenya Universities and Colleges Central Placement Service), meet the specific course requirements (some require B plain or above), and accept the placement offer. Direct applications are also possible for some programs.",
            "context": "UoN is Kenya's largest university, established in 1970.",
            "category": "educational",
            "difficulty": 2,
            "tags": ["uon", "admission", "kuccps"]
        },
        {
            "input_text": "What is the difference between public and private universities in Kenya?",
            "expected_output": "In Kenya: Public universities (like UoN, Kenyatta University, Moi University) are government-funded with lower fees but limited slots. Private universities (like USIU, Strathmore, Catholic University) have higher fees but often better facilities and smaller class sizes. Both offer accredited degrees.",
            "context": "Kenya has over 30 public and 50 private universities accredited by CUE.",
            "category": "educational",
            "difficulty": 2,
            "tags": ["universities", "public_private", "education"]
        },
        # Agricole
        {
            "input_text": "What are the main crops grown in Kenya?",
            "expected_output": "Kenya's main crops include: tea (largest export), coffee, maize (staple food), wheat, sugarcane, pyrethrum, horticultural products (flowers, vegetables, fruits), and cotton. Agriculture contributes about 22% to Kenya's GDP and employs over 70% of the rural population.",
            "context": "Agriculture is the backbone of Kenya's economy.",
            "category": "agricultural",
            "difficulty": 1,
            "tags": ["crops", "agriculture", "kenya"]
        },
        {
            "input_text": "How do I access agricultural loans in Kenya?",
            "expected_output": "To access agricultural loans in Kenya: Apply through Kenya Agricultural and Livestock Research Organization (KALRO), Kenya Women Finance Trust, Equity Bank agricultural loans, Co-operative Bank farming products, or government programs like the Agricultural Finance Corporation (AFC). You'll need a farm business plan and land documents.",
            "context": "Kenya has several agricultural financing options through banks and government agencies.",
            "category": "agricultural",
            "difficulty": 3,
            "tags": ["agricultural_loan", "finance", "kenya"]
        },
        # Financier
        {
            "input_text": "How do I open a bank account in Kenya?",
            "expected_output": "To open a bank account in Kenya: Visit a bank branch with your national ID or passport, KRA PIN certificate, passport photos, and proof of address. Some banks allow online registration through their apps. Most banks require a minimum deposit (usually 500-1,000 KES). M-Banking is widely available.",
            "context": "Kenya has a well-developed banking sector with both local and international banks.",
            "category": "financial",
            "difficulty": 2,
            "tags": ["bank_account", "banking", "kenya"]
        },
        {
            "input_text": "What is M-Shwari and how does it work?",
            "expected_output": "M-Shwari is a mobile savings and loan product by Safaricom and CBA (now NCBA). Users can save money through M-Pesa and access instant loans. Savings earn interest, and loan limits increase with consistent saving. To access: Dial *334# and select M-Shwari. No paperwork required.",
            "context": "M-Shwari has over 30 million users in Kenya and has disbursed billions in loans.",
            "category": "financial",
            "difficulty": 2,
            "tags": ["mshwari", "savings", "loans"]
        },
        # Sécurité
        {
            "input_text": "How do I report a crime in Kenya?",
            "expected_output": "To report a crime in Kenya: Call 999 or 112 for emergencies. For non-emergencies, visit your nearest police station. You can also report through the DCI (Directorate of Criminal Investigations) hotline or the National Police Service website. For gender-based violence, call 1195 (Gender Violence Recovery Centre).",
            "context": "Kenya has a national emergency response system and various hotlines for different crimes.",
            "category": "security",
            "difficulty": 2,
            "tags": ["crime_report", "police", "emergency"]
        },
        {
            "input_text": "What should I do if my phone is stolen in Nairobi?",
            "expected_output": "If your phone is stolen in Nairobi: Report to the nearest police station immediately, report to Safaricom/Airtel to block the SIM card, report to the DCI's Crime Research and Intelligence Bureau, change all passwords and PINs, and report to your bank if financial apps were on the phone. Keep the police abstract for insurance claims.",
            "context": "Phone theft is a common crime in urban areas of Kenya.",
            "category": "security",
            "difficulty": 2,
            "tags": ["phone_theft", "nairobi", "security"]
        }
    ]
}


def get_kenya_benchmark():
    """Retourne le benchmark Kenya."""
    return KENYA_BENCHMARK
