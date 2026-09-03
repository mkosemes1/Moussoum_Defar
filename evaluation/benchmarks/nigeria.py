"""
Benchmark IA pour le Nigeria.
Tests de compréhension du contexte nigérian.
"""

NIGERIA_BENCHMARK = {
    "name": "Nigeria AI Benchmark v1",
    "description": "Évaluation de la compréhension du contexte nigérian pour les modèles IA",
    "country_code": "NG",
    "country_name": "Nigeria",
    "version": "1.0",
    "language_code": "en",
    "language_name": "English",
    "category": "mixed",
    "tests": [
        # Mobile Money / Fintech
        {
            "input_text": "How do I send money to someone in Lagos using OPay?",
            "expected_output": "To send money via OPay: Open the OPay app, tap 'Transfer', enter the recipient's OPay account number or phone number, input the amount, add a description if needed, and confirm with your PIN. The transfer is usually instant.",
            "context": "OPay is one of the leading fintech platforms in Nigeria, popular for quick transfers.",
            "category": "fintech",
            "difficulty": 1,
            "tags": ["opay", "transfer", "fintech"]
        },
        {
            "input_text": "What's the difference between Paga and Kuda Bank?",
            "expected_output": "Paga is primarily a mobile payment platform that allows cash-in/cash-out at agents, while Kuda is a fully digital bank with no physical branches. Kuda offers a debit card and savings features, while Paga focuses more on payments and bill payments.",
            "context": "Both are popular fintech solutions in Nigeria, but serve different primary functions.",
            "category": "fintech",
            "difficulty": 2,
            "tags": ["paga", "kuda", "comparison"]
        },
        {
            "input_text": "How do I buy airtime on my phone without going to a store?",
            "expected_output": "You can buy airtime through: USSD codes (like *904# for Airtel, *777# for MTN), mobile banking apps, fintech apps like OPay/PalmPay, or by dialing your bank's USSD code and selecting 'Airtime'. Most networks also allow direct top-up from your bank account.",
            "context": "Nigeria has multiple mobile networks: MTN, Airtel, Glo, and 9mobile.",
            "category": "fintech",
            "difficulty": 1,
            "tags": ["airtime", "ussd", "mobile_network"]
        },
        # Languages
        {
            "input_text": "How de? I dey find my way go Victoria Island.",
            "expected_output": "The user is speaking Nigerian Pidgin English. 'How de?' means 'How are you?' and 'I dey find my way go Victoria Island' means 'I'm trying to find my way to Victoria Island.' Victoria Island is an upscale area in Lagos.",
            "context": "Nigerian Pidgin is widely spoken across Nigeria, especially in informal settings.",
            "category": "linguistic",
            "difficulty": 3,
            "tags": ["pidgin", "lagos", "directions"]
        },
        {
            "input_text": "Abeg, how much be the transport for Ibadan?",
            "expected_output": "The user is asking in Nigerian Pidgin: 'Please, how much is the transport fare to Ibadan?' The bus fare from Lagos to Ibadan typically ranges from 3,000 to 5,000 Naira depending on the bus company and comfort level.",
            "context": "Ibadan is the capital of Oyo State and a major city in southwestern Nigeria.",
            "category": "linguistic",
            "difficulty": 2,
            "tags": ["pidgin", "ibadan", "transport"]
        },
        # Administratif
        {
            "input_text": "How do I get a voter's card in Nigeria?",
            "expected_output": "To get a voter's card in Nigeria: Register at the INEC (Independent National Electoral Commission) office or during registration drives. You need a valid ID (NIN, driver's license, or international passport). Visit INEC.gov.ng for registration centers and schedules.",
            "context": "INEC manages voter registration and elections in Nigeria.",
            "category": "administrative",
            "difficulty": 2,
            "tags": ["voter_card", "inec", "registration"]
        },
        {
            "input_text": "What documents do I need to register a business in Nigeria?",
            "expected_output": "To register a business in Nigeria with CAC (Corporate Affairs Commission): You need a business name reservation, completed registration form, identification documents (NIN or passport), and payment of registration fees. The process can be done online at cac.gov.ng.",
            "context": "CAC is the government agency responsible for business registration in Nigeria.",
            "category": "administrative",
            "difficulty": 3,
            "tags": ["business_registration", "cac", "documents"]
        },
        # Commercial
        {
            "input_text": "I want to buy property in Abuja. What should I know?",
            "expected_output": "When buying property in Abuja: Verify the property with the FCTA (Federal Capital Territory Administration), check for genuine Certificate of Occupancy (C of O), engage a verified lawyer, conduct a search at the land registry, and be aware of the area's development plan. Prices vary by district.",
            "context": "Abuja, the capital city, has strict land use regulations managed by FCTA.",
            "category": "commercial",
            "difficulty": 3,
            "tags": ["property", "abuja", "real_estate"]
        },
        {
            "input_text": "How much does it cost to ship goods from Lagos to Port Harcourt?",
            "expected_output": "Shipping costs from Lagos to Port Harcourt vary: By road, it costs approximately 5,000-15,000 Naira per item depending on size and weight. For bulk shipments, trucking companies charge between 200,000-500,000 Naira for a full container. Sea freight takes 2-3 days via the Lagos-Port Harcourt route.",
            "context": "Lagos and Port Harcourt are major commercial hubs in Nigeria.",
            "category": "commercial",
            "difficulty": 2,
            "tags": ["shipping", "logistics", "lagos"]
        },
        # Culturel
        {
            "input_text": "What is the significance of Aso Ebi in Nigerian weddings?",
            "expected_output": "Aso Ebi (meaning 'family cloth' in Yoruba) is a tradition where family members and friends wear matching fabrics at events, especially weddings. It symbolizes unity, support, and social solidarity. The host typically provides or suggests the fabric, and guests purchase it to show their participation.",
            "context": "Aso Ebi is a prominent cultural practice across Nigeria, especially among Yoruba people.",
            "category": "cultural",
            "difficulty": 2,
            "tags": ["aso_ebi", "wedding", "yoruba"]
        },
        {
            "input_text": "What is Jollof Rice and why is there a debate about it?",
            "expected_output": "Jollof Rice is a one-pot rice dish cooked with tomatoes, peppers, and spices, popular across West Africa. The 'Jollof Wars' is a friendly rivalry between Nigeria and Ghana over whose version is superior. Nigerian Jollof is known for its smoky flavor, while Ghanaian Jollof uses more spices.",
            "context": "The Jollof Rice debate is a cultural phenomenon in West Africa, especially on social media.",
            "category": "cultural",
            "difficulty": 1,
            "tags": ["jollof_rice", "food", "culture"]
        },
        # Médical
        {
            "input_text": "Where can I find a good hospital in Lagos?",
            "expected_output": "Lagos has several top hospitals: Lagos University Teaching Hospital (LUTH) in Idi-Araba, Reddington Hospital in Victoria Island, St. Nicholas Hospital in Lagos Island, and Evercare Hospital in Lekki. For specialized care, LUTH is a major public teaching hospital.",
            "context": "Lagos has both public and private hospitals, with private facilities generally offering shorter wait times.",
            "category": "medical",
            "difficulty": 1,
            "tags": ["hospital", "lagos", "healthcare"]
        },
        {
            "input_text": "How can I prevent malaria in Nigeria?",
            "expected_output": "To prevent malaria in Nigeria: Sleep under insecticide-treated mosquito nets, use insect repellent, wear long sleeves in the evening, eliminate stagnant water around your home, and consider prophylactic medication if traveling from a non-endemic area. Seek prompt treatment for fever.",
            "context": "Malaria is endemic in Nigeria and a leading cause of death, especially among children.",
            "category": "medical",
            "difficulty": 2,
            "tags": ["malaria", "prevention", "health"]
        },
        # Éducatif
        {
            "input_text": "How do I gain admission into University of Lagos?",
            "expected_output": "To gain admission into UNILAG: Score at least 200 in JAMB (UTME), choose UNILAG as first choice, pass the post-UTME screening, meet the departmental cut-off mark (varies by course), and have at least 5 O'Level credits including English and Mathematics. Applications are done through JAMB CAPS.",
            "context": "UNILAG is one of Nigeria's premier universities, located in Akoka, Lagos.",
            "category": "educational",
            "difficulty": 2,
            "tags": ["unilag", "admission", "jamb"]
        },
        {
            "input_text": "What is the difference between polytechnic and university in Nigeria?",
            "expected_output": "In Nigeria: Universities offer degree programs (B.Sc, B.A) and are more academic/research-focused. Polytechnics offer National Diploma (ND) and Higher National Diploma (HND) programs with more practical/technical training. University degrees are generally more recognized for postgraduate studies and some employers.",
            "context": "Both institutions play important roles in Nigeria's education system.",
            "category": "educational",
            "difficulty": 2,
            "tags": ["polytechnic", "university", "education"]
        },
        # Agricole
        {
            "input_text": "What are the main crops grown in Nigeria?",
            "expected_output": "Nigeria's main crops include: cassava (largest producer globally), yam, maize, rice, sorghum, millet, cocoa (mainly in the southwest), palm oil (southeast), rubber, and groundnuts. Agriculture employs about 35% of the Nigerian workforce.",
            "context": "Agriculture contributes about 24% to Nigeria's GDP.",
            "category": "agricultural",
            "difficulty": 1,
            "tags": ["crops", "agriculture", "nigeria"]
        },
        {
            "input_text": "How do I access farming loans in Nigeria?",
            "expected_output": "To access farming loans in Nigeria: Apply through the NIRSAL Microfinance Bank, Bank of Agriculture, commercial banks with agricultural lending programs, or the Anchor Borrowers Programme (ABP) by CBN. You'll need a business plan, land ownership documents, and BVN registration.",
            "context": "The Nigerian government has several agricultural financing programs to boost food security.",
            "category": "agricultural",
            "difficulty": 3,
            "tags": ["farming_loan", "agriculture", "finance"]
        },
        # Sécurité
        {
            "input_text": "How do I report a scam in Nigeria?",
            "expected_output": "To report a scam in Nigeria: File a report with the EFCC (Economic and Financial Crimes Commission) at efcc.gov.ng, contact the Nigeria Police Force Cybercrime Unit, or report to the NPF (Nigeria Police Force) at your nearest station. You can also report to your bank's fraud department for financial scams.",
            "context": "The EFCC is the primary agency fighting financial crimes in Nigeria.",
            "category": "security",
            "difficulty": 2,
            "tags": ["scam", "efcc", "report"]
        },
        {
            "input_text": "What should I do if my bank account is hacked?",
            "expected_output": "If your bank account is hacked: Immediately contact your bank's fraud department to freeze the account, change all passwords and PINs, file a police report, report to the CBN (Central Bank of Nigeria) consumer protection department, and keep all evidence of unauthorized transactions.",
            "context": "Nigerian banks have dedicated fraud departments and are required to investigate within 24 hours.",
            "category": "security",
            "difficulty": 2,
            "tags": ["hack", "bank", "security"]
        }
    ]
}


def get_nigeria_benchmark():
    """Retourne le benchmark Nigeria."""
    return NIGERIA_BENCHMARK
