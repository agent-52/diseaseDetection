import streamlit as st
import tensorflow as tf
import numpy as np
import streamlit as st
import streamlit.components.v1 as components





# Language dictionaries for translation (Example in Hindi, Tamil, Telugu)
translations = {
    "english": {
        "title": "🌿 Plant Disease Recognition System",
        "intro": """
            Welcome to the Plant Disease Recognition System! 🌿🔍

            Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

            ### How It Works
            1. **Upload Image:** Use the option below to upload an image of a plant with suspected diseases.
            2. **Analysis:** Our system will process the image using advanced machine learning techniques to identify potential diseases.
            3. **Results:** View the predicted disease and recommendations for further action.

            ### Why Choose Us?
            - **Accuracy:** State-of-the-art machine learning algorithms for accurate disease detection.
            - **User-Friendly:** Simple and intuitive interface for seamless user experience.
            - **Fast Results:** Receive predictions within seconds, allowing for quick decisions.
        """,
        "disease_recognition": "Disease Recognition",
        "predict_btn": "Predict Disease",
        "choose_image": "Choose an Image of a Plant:",
        "prediction_result": "Prediction: This plant seems to have **{}** disease!",
        "next_steps": """
            ### Next Steps:
            1. Identify the disease from the list above.
            2. Consult an expert or use appropriate remedies.
            3. Monitor the plant for further symptoms.
        """
    },
    "hindi": {
        "title": "🌿 पौधों की बीमारी पहचान प्रणाली",
        "intro": """
            पौधों की बीमारी पहचान प्रणाली में आपका स्वागत है! 🌿🔍

            हमारा मिशन पौधों की बीमारियों की पहचान करना है। एक पौधे की छवि अपलोड करें, और हमारी प्रणाली उसे बीमारियों के संकेतों को पहचानने के लिए विश्लेषण करेगी। चलिए मिलकर हमारी फसलों को सुरक्षित बनाते हैं और बेहतर उत्पादन सुनिश्चित करते हैं!

            ### यह कैसे काम करता है
            1. **चित्र अपलोड करें:** नीचे दिए गए विकल्प का उपयोग करके एक पौधे की छवि अपलोड करें, जिसमें बीमारी हो सकती है।
            2. **विश्लेषण:** हमारी प्रणाली इस छवि का विश्लेषण करेगी और संभावित बीमारियों की पहचान करेगी।
            3. **परिणाम:** बीमारियों का अनुमान और आगे की कार्रवाई के लिए सिफारिशें प्राप्त करें।

            ### क्यों चुनें हमें?
            - **सटीकता:** अत्याधुनिक मशीन लर्निंग तकनीकों के माध्यम से सटीक बीमारी पहचान।
            - **उपयोगकर्ता के अनुकूल:** एक साधारण और सहज इंटरफेस।
            - **तेज़ परिणाम:** कुछ ही सेकंड्स में परिणाम प्राप्त करें, ताकि आप जल्द से जल्द निर्णय ले सकें।
        """,
        "disease_recognition": "बीमारी पहचान",
        "predict_btn": "बीमारी का अनुमान लगाएं",
        "choose_image": "पौधे की छवि चुनें:",
        "prediction_result": "अनुमान: यह पौधा **{}** बीमारी से प्रभावित प्रतीत होता है!",
        "next_steps": """
            ### अगला कदम:
            1. ऊपर सूचीबद्ध बीमारियों में से बीमारी की पहचान करें।
            2. एक विशेषज्ञ से सलाह लें या उचित उपचार का उपयोग करें।
            3. पौधे की और निगरानी करें।
        """
    },
    "tamil": {
        "title": "🌿 வேளாண் நோய் அறிதல் அமைப்பு",
        "intro": """
            வேளாண் நோய் அறிதல் அமைப்புக்கு வரவேற்கின்றேன்! 🌿🔍

            நமது குறிக்கோள் விவசாய நோய்களை துல்லியமாக கண்டறிதல் ஆகும். ஒரு செடியின் படத்தை பதிவேற்றுங்கள், எங்கள் அமைப்பு அதை நோய்களுக்கான அடையாளங்களை கண்டறிந்திடுகிறது. நம் விவசாயிகளை காப்பாற்றி ஆரோக்கியமான வருமானத்தை உறுதி செய்வோம்!

            ### இது எப்படி வேலை செய்கிறது
            1. **படம் பதிவேற்றுங்கள்:** கீழே உள்ள தேர்வு வழிமுறையை பயன்படுத்தி ஒரு செடியின் படத்தை பதிவேற்றுங்கள்.
            2. **பரிசோதனை:** எங்கள் அமைப்பு அந்த படத்தை பரிசோதித்து நோய்களின் அடையாளங்களை கண்டறியும்.
            3. **பரிந்துரைகள்:** நோய் அறிதல் முடிவுகள் மற்றும் தொடரும் நடவடிக்கைகள்.

            ### ஏன் நம்மை தேர்வு செய்வது?
            - **துல்லியம்:** கணினி கற்றல் தொழில்நுட்பங்களால் துல்லியமான நோய் அறிதல்.
            - **பயன்பாட்டுக்கு எளிதானது:** எளிமையான மற்றும் பயனர் நட்பு இடைமுகம்.
            - **மிகவும் வேகமான முடிவுகள்:** சில நொடிகளில் முடிவுகளை பெறுங்கள்.
        """,
        "disease_recognition": "நோய் அறிதல்",
        "predict_btn": "நோயை கணிக்கவும்",
        "choose_image": "ஒரு செடியின் படத்தை தேர்வு செய்க:",
        "prediction_result": "கணிப்பு: இந்த செடி **{}** நோயால் பாதிக்கப்படுவது போல உள்ளது!",
        "next_steps": """
            ### அடுத்த படிகள்:
            1. மேலே கொடுக்கப்பட்டுள்ள நோய்களில் ஒன்றை அடையாளம் காண்க.
            2. ஒரு நிபுணரிடம் ஆலோசனை பெறவும் அல்லது சரியான சிகிச்சையை பயன்படுத்தவும்.
            3. செடியை தொடர்ந்து கவனிக்கவும்.
        """
    },
    "telugu": {
        "title": "🌿 పంటల రోగం గుర్తింపు సిస్టమ్",
        "intro": """
            పంటల రోగం గుర్తింపు సిస్టమ్ లోకి స్వాగతం! 🌿🔍

            మా లక్ష్యం పంటల రోగాలను సులభంగా గుర్తించడం. ఒక పంట యొక్క చిత్రం అప్‌లోడ్ చేయండి, మరియు మా సిస్టమ్ దానిని రోగాల యొక్క సంకేతాలను గుర్తించడానికి విశ్లేషిస్తుంది. మన పంటలను రక్షించుకోవడం మరియు మంచి పంటను సాధించడం కోసం మనం కలిసి పని చేద్దాం!

            ### ఇది ఎలా పనిచేస్తుంది
            1. **చిత్రం అప్‌లోడ్ చేయండి:** క్రింది ఎంపికను ఉపయోగించి ఒక పంట యొక్క చిత్రాన్ని అప్‌లోడ్ చేయండి.
            2. **విశ్లేషణ:** మా సిస్టమ్ ఆ చిత్రాన్ని విశ్లేషించి రోగాలను గుర్తిస్తుంది.
            3. **ఫలితాలు:** అనుమానిత రోగం మరియు తదుపరి చర్యల కోసం సిఫార్సులు చూడండి.

            ### ఎందుకు మమ్మల్ని ఎంచుకోవాలి?
            - **తులనాత్మకత:** ఆధునిక మెషిన్ లర్నింగ్ అల్గోరిథమ్స్ ద్వారా సరిగ్గా రోగాలను గుర్తించడం.
            - **ఉపయోగకర్త స్నేహపూర్వకమైనది:** సులభమైన మరియు సమర్థమైన ఇంటర్‌ఫేస్.
            - **వేగవంతమైన ఫలితాలు:** కొన్ని సెకన్లలో ఫలితాలను పొందండి.
        """,
        "disease_recognition": "రోగం గుర్తింపు",
        "predict_btn": "రోగాన్ని అంచనా వేయండి",
        "choose_image": "ఒక పంట చిత్రాన్ని ఎంచుకోండి:",
        "prediction_result": "అంచనా: ఈ పంట **{}** రోగంతో బాధపడుతోంది!",
        "next_steps": """
            ### తదుపరి దశలు:
            1. పై లిస్ట్‌లో ఉన్న రోగాల నుండి ఒకదాన్ని గుర్తించండి.
            2. ఒక నిపుణిని సంప్రదించండి లేదా సరైన చికిత్సను ఉపయోగించండి.
            3. పంటను మళ్లీ పర్యవేక్షించండి.
        """
    }
}
# Streamlit configuration
st.set_page_config(page_title=translations["english"]["title"], page_icon="🌿", layout="centered")

# Inject Google Translate widget
components.html("""
    <div id="google_translate_element"></div>
    <script type="text/javascript">
      function googleTranslateElementInit() {
        new google.translate.TranslateElement(
          {pageLanguage: 'en'},
          'google_translate_element'
        );
      }
    </script>
    <script type="text/javascript" 
      src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit">
    </script>
""", height=100)



@st.cache_resource
def load_model():
    return tf.keras.models.load_model("trained_plant_disease_model.keras")

model = load_model()







def model_prediction(image_file):
    image = tf.keras.preprocessing.image.load_img(image_file, target_size=(128, 128))
    arr = tf.keras.preprocessing.image.img_to_array(image)
    arr = np.expand_dims(arr, axis=0)
    preds = model.predict(arr)
    return int(np.argmax(preds))



# Language selection
language = st.selectbox("Choose Language", ["English", "Hindi", "Tamil", "Telugu"])

# Set the correct language for translation
lang = "english" if language == "English" else language.lower()

# Apply colors
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #4A5D23;
    }}
    .stButton > button {{
        background-color: #7b7f3d;
        color: white;
    }}
    .stTextInput > input {{
        background-color: #fff7e6;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# Structured labels and metadata
class_labels = [
    'Apple – Scabby Patches on Leaves/Fruit',  # Apple___Apple_scab
    'Apple – Black Spots on Fruit',             # Apple___Black_rot
    'Apple – Rusty Orange Spots on Leaves',     # Apple___Cedar_apple_rust
    'Apple – Healthy',
    'Blueberry – Healthy',
    'Cherry – White Powder on Leaves',          # Cherry___Powdery_mildew
    'Cherry – Healthy',
    'Corn – Gray Leaf Spots',                   # Corn___Cercospora_leaf_spot_Gray_leaf_spot
    'Corn – Rusty Reddish Patches on Leaves',   # Common_rust
    'Corn – Long Brown Leaf Blight',            # Northern_Leaf_Blight
    'Corn – Healthy',
    'Grape – Black Rotten Spots',               # Black_rot
    'Grape – Black Patches on Leaves',          # Esca (Black Measles)
    'Grape – Light Brown Leaf Spots',           # Isariopsis Leaf Spot
    'Grape – Healthy',
    'Orange – Yellowing Leaves (Citrus Greening)',  # Haunglongbing
    'Peach – Dark Spots on Leaves',             # Bacterial Spot
    'Peach – Healthy',
    'Bell Pepper – Leaf Spots',                 # Bacterial Spot
    'Bell Pepper – Healthy',
    'Potato – Early Brown Spots on Leaves',     # Early blight
    'Potato – Late Black/Brown Rot',            # Late blight
    'Potato – Healthy',
    'Raspberry – Healthy',
    'Soybean – Healthy',
    'Squash – White Powdery Coating',           # Powdery mildew
    'Strawberry – Leaf Burning or Scorching',   # Leaf scorch
    'Strawberry – Healthy',
    'Tomato – Leaf and Fruit Spots',            # Bacterial Spot
    'Tomato – Early Brown Leaf Spots',          # Early Blight
    'Tomato – Late Black Rot',                  # Late Blight
    'Tomato – Moldy Leaves',                    # Leaf Mold
    'Tomato – Tiny Circular Spots on Leaves',   # Septoria Leaf Spot
    'Tomato – Tiny Web and Yellowing Leaves',   # Spider mites
    'Tomato – Round Yellow-Brown Spots',        # Target Spot
    'Tomato – Curled Yellow Leaves',            # Tomato Yellow Leaf Curl Virus
    'Tomato – Patchy Yellow/Green Leaves',      # Tomato Mosaic Virus
    'Tomato – Healthy'
]

class_metadata = [
    {   # 0: Apple – Scabby Patches on Leaves/Fruit
         "cause": "Caused by the fungus *Venturia inaequalis*, especially during cool, wet spring weather. It leads to dark, scabby spots on leaves and fruit.",
        "avoid": "Avoid overhead watering and excessive nitrogen fertilizers. Don’t leave fallen leaves or infected fruit on the ground.",
        "do": "Prune trees to improve air circulation. Use disease-resistant apple varieties. Clean up debris and fallen fruit regularly.",
        "pesticides": "Use fungicides like *Captan or Mancozeb* during early leaf stages. Apply at regular intervals during wet weather.",
        "organic_remedies": "Spray neem oil or a mixture of baking soda (1 tsp), mild soap (few drops), and water (1 liter) weekly during the early season."
    },
    {   # 1: Apple – Black Spots on Fruit
        "cause": "Caused by *Botryosphaeria obtusa* fungus, commonly known as black rot. It infects through wounds and spreads in humid conditions.",
        "avoid": "Do not leave pruned branches or infected fruit on the ground. Avoid overcrowding trees.",
        "do": "Prune dead or infected branches. Keep the area clean and dry. Apply protective sprays early in the season.",
        "pesticides": "Use fungicides like Thiophanate-methyl or copper-based sprays.",
        "organic_remedies": "Apply compost tea or neem oil as a preventative. Remove and burn infected fruit immediately."
    },
    {   # 2: Apple – Rusty Orange Spots on Leaves
        "cause": "Caused by *Gymnosporangium juniperi-virginianae* fungus (Cedar Apple Rust). Requires both apple and juniper trees to complete its lifecycle.",
        "avoid": "Avoid planting apples near juniper trees. Do not allow wet leaves to persist.",
        "do": "Remove nearby wild junipers. Use rust-resistant varieties. Apply fungicides during early spring.",
        "pesticides": "Use fungicides like Myclobutanil or Mancozeb starting at bud break.",
        "organic_remedies": "Use sulfur sprays or garlic extract. Remove infected leaves promptly."
    },
    {
        "cause": "No visible signs of disease. Leaves and fruits appear fresh and unblemished.",
        "avoid": "Avoid overwatering, excessive fertilizer use, and planting in poorly drained soils.",
        "do": "Regularly inspect for pests and diseases. Maintain good airflow by pruning. Apply organic compost.",
        "pesticides": "Not needed.",
        "organic_remedies": "Not required, but neem oil can be used as a preventive measure."
    },  # 3: Apple – Healthy
    {
        "cause": "No signs of disease or pests. Leaves are green, and fruits are firm and ripe.",
        "avoid": "Avoid waterlogging and poor soil nutrition.",
        "do": "Mulch the base, maintain soil acidity (pH 4.5–5.5), and water evenly.",
        "pesticides": "Not required.",
        "organic_remedies": "Use neem oil or compost tea once a month for general prevention."
    },  # 4: Blueberry – Healthy
    {   # 5: Cherry – White Powder on Leaves
         "name": "Cherry – White Powder on Leaves",
        "cause": "Powdery mildew caused by *Podosphaera clandestina*. Thrives in warm, dry days and cool nights.",
        "avoid": "Avoid excessive nitrogen. Don’t water leaves directly.",
        "do": "Improve air circulation by pruning. Plant in sunny areas. Water at the base.",
        "pesticides": "Apply sulfur-based fungicides or potassium bicarbonate during early growth.",
        "organic_remedies": "Use a mix of 1 tsp baking soda + 1 liter water + few drops of oil/soap. Spray weekly."
    },
    {
        "cause": "No infection or pest damage. Growth appears normal.",
        "avoid": "Avoid waterlogging and overfertilization.",
        "do": "Prune in late winter. Monitor for early pest signs. Keep the area clean.",
        "pesticides": "Not needed.",
        "organic_remedies": "Periodic neem oil spray can help prevent future infestations."
    },  # 6: Cherry – Healthy
    {   # 7: Corn – Gray Leaf Spots
         "cause": "Caused by the fungus *Cercospora zeae-maydis*. Leads to rectangular gray-brown lesions on leaves.",
        "avoid": "Avoid monocropping and overwatering. Don’t use infected seeds.",
        "do": "Use disease-resistant varieties. Rotate crops every season.",
        "pesticides": "Spray fungicides like Propiconazole or Azoxystrobin at the first sign of infection.",
        "organic_remedies": "Use compost tea and neem cake in the soil. Improve soil health with organic matter."
    },
    {   # 8: Corn – Rusty Reddish Patches on Leaves
        "name": "Corn – Rusty Reddish Patches on Leaves",
        "cause": "Common rust caused by *Puccinia sorghi*. Occurs in warm, humid climates.",
        "avoid": "Avoid excessive irrigation and overcrowding.",
        "do": "Plant rust-resistant corn varieties. Ensure proper spacing between plants.",
        "pesticides": "Use fungicides like Mancozeb or Tebuconazole when symptoms first appear.",
        "organic_remedies": "Apply neem oil or diluted cow urine. Maintain soil health with compost."
    },
    {   # 9: Corn – Long Brown Leaf Blight
        "cause": "Caused by the fungus *Exserohilum turcicum* (Northern Leaf Blight). Elongated brown lesions develop on leaves.",
        "avoid": "Avoid dense planting and poor field drainage.",
        "do": "Use resistant hybrids. Rotate crops. Remove infected plant residues.",
        "pesticides": "Spray fungicides like Azoxystrobin or Mancozeb early in disease cycle.",
        "organic_remedies": "Use Trichoderma-based biocontrol. Maintain field hygiene and organic mulching."
    },
    {
        "cause": "No signs of fungal or pest issues. Uniform growth with green, upright leaves.",
        "avoid": "Avoid water stagnation and poor nutrient balance.",
        "do": "Apply well-rotted manure. Regularly weed and inspect crop.",
        "pesticides": "Not necessary.",
        "organic_remedies": "Use vermicompost and neem spray monthly.",
    },  # 10: Corn – Healthy
    {   # 11: Grape – Black Rotten Spots
        "cause": "Common rot caused by *Guignardia bidwellii*. It leads to circular black spots on leaves and fruit, causing berries to shrivel.",
        "avoid": "Avoid overhead irrigation and overcrowding. Don't leave pruned parts on the ground.",
        "do": "Prune infected parts, improve air circulation, and use resistant varieties.",
        "pesticides": "Use Mancozeb or Myclobutanil when symptoms appear.",
        "organic_remedies": "Spray neem oil weekly. Use garlic oil or horsetail tea as antifungal sprays."
    },
    {   # 12: Grape – Black Patches on Leaves (Esca)
         "cause": "Esca or Black Measles disease caused by fungi like *Phaeomoniella* and *Phaeoacremonium*.",
        "avoid": "Avoid mechanical injury to vines and use clean planting material.",
        "do": "Remove infected wood, maintain field hygiene, and avoid excessive irrigation.",
        "pesticides": "Apply Copper oxychloride when symptoms show.",
        "organic_remedies": "Apply neem cake to the base. Use Trichoderma-based biocontrols."
    },
    {   # 13: Grape – Light Brown Leaf Spots
        "cause": "Leaf spots caused by *Isariopsis clavispora*. Results in angular, light brown to gray leaf spots.",
        "avoid": "Avoid dense planting and overwatering.",
        "do": "Remove infected leaves and spray at early stages.",
        "pesticides": "Spray Mancozeb or Zineb during early infection stages.",
        "organic_remedies": "Spray a mixture of baking soda, water, and mild soap weekly."
    },
    {
         "cause": "No signs of disease. Leaves are green, and fruits are firm.",
        "avoid": "Avoid poor drainage and using infected tools.",
        "do": "Regularly prune the vines and apply compost tea or neem oil monthly.",
        "pesticides": "Not required.",
        "organic_remedies": "Neem or cow urine can be used monthly as prevention."
    },  # 14: Grape – Healthy
    {   # 15: Orange – Yellowing Leaves (Citrus Greening)
         "cause": "Caused by the bacteria *Candidatus Liberibacter*, spread by citrus psyllid insects.",
        "avoid": "Avoid planting infected saplings and control the psyllid population.",
        "do": "Remove infected trees, apply foliar micronutrients, and use pest nets.",
        "pesticides": "Imidacloprid or Thiamethoxam can be used to control psyllids.",
        "organic_remedies": "Spray neem oil mixed with garlic extract and use yellow sticky traps to control psyllids."
    },
    {   # 16: Peach – Dark Spots on Leaves
        "name": "Peach – Dark Spots on Leaves",
        "cause": "Bacterial Spot caused by *Xanthomonas campestris*. It results in dark, water-soaked spots on leaves and fruit.",
        "avoid": "Avoid overhead watering and avoid working on plants when wet to reduce bacterial spread.",
        "do": "Remove infected leaves and destroy them. Use resistant peach varieties.",
        "pesticides": "Apply copper-based fungicides like Copper hydroxide or Copper oxychloride.",
        "organic_remedies": "Spray with garlic and neem oil solution or use compost tea."
    },
    {
        "cause": "No disease symptoms. The leaves are green and the fruit is healthy.",
        "avoid": "Avoid poor drainage and ensure proper spacing between plants.",
        "do": "Regularly prune to remove dead branches and apply organic fertilizers like compost.",
        "pesticides": "Not required.",
        "organic_remedies": "Use neem oil or cow urine for monthly applications as a preventative measure."
    },  # 17: Peach – Healthy
    {   # 18: Bell Pepper – Leaf Spots
         "cause": "Bacterial Spot caused by *Xanthomonas vesicatoria*. Small water-soaked spots appear on the leaves.",
        "avoid": "Avoid overhead irrigation and high humidity. Don’t handle plants when they’re wet.",
        "do": "Remove and destroy infected leaves. Use resistant varieties and maintain proper spacing.",
        "pesticides": "Use copper-based fungicides like Copper oxychloride or Copper sulfate.",
        "organic_remedies": "Spray neem oil solution and compost tea to control bacterial spread."
    },
    {
       "cause": "No signs of disease. The leaves are firm and the fruit is smooth.",
        "avoid": "Avoid excessive watering and overcrowding. Ensure proper air circulation around the plants.",
        "do": "Apply organic compost or mulch to support healthy growth.",
        "pesticides": "Not required.",
        "organic_remedies": "Monthly application of neem oil can help prevent diseases."
    },  # 19: Bell Pepper – Healthy
    {   # 20: Potato – Early Brown Spots on Leaves
         "cause": "Early Blight caused by *Alternaria solani*. Characterized by dark brown or black lesions with concentric rings.",
        "avoid": "Avoid dense planting and overwatering. Ensure good drainage.",
        "do": "Remove and destroy infected leaves. Spray with copper fungicide.",
        "pesticides": "Apply Mancozeb or Chlorothalonil during the early stages of infection.",
        "organic_remedies": "Spray neem oil or use a mixture of baking soda and water as a preventive measure."
    },
    {   # 21: Potato – Late Black/Brown Rot
         "cause": "Late Blight caused by *Phytophthora infestans*. Leads to large brown to black lesions on leaves and tubers.",
        "avoid": "Avoid wet and humid conditions. Remove infected plants promptly.",
        "do": "Remove and destroy infected plants. Spray with mancozeb or copper-based fungicides.",
        "pesticides": "Use Metalaxyl or Mancozeb to control the disease.",
        "organic_remedies": "Spray a mixture of neem oil and water regularly to control late blight."
    },
    {
        "cause": "No symptoms of disease. The leaves are firm and green, and tubers are free from infection.",
        "avoid": "Maintain proper spacing between plants to ensure air circulation.",
        "do": "Apply organic mulch and compost for soil health.",
        "pesticides": "Not needed.",
        "organic_remedies": "Regular use of neem oil can help protect plants from early and late blight."
    },  # 22: Potato – Healthy
    {
         "cause": "No disease signs. The plant shows healthy green leaves and fruit.",
        "avoid": "Ensure proper drainage and space between plants to prevent waterlogging.",
        "do": "Prune regularly and mulch to retain moisture.",
        "pesticides": "Not required.",
        "organic_remedies": "Apply a compost tea solution monthly to keep plants healthy."
    },  # 23: Raspberry – Healthy
    {
         "cause": "No signs of disease. Leaves are green, and pods are well-formed.",
        "avoid": "Avoid overcrowding and poor drainage.",
        "do": "Provide proper spacing between plants and use crop rotation.",
        "pesticides": "Not necessary.",
        "organic_remedies": "Use compost and neem oil as a natural fertilizer and pest deterrent."
    },  # 24: Soybean – Healthy
    {   # 25: Squash – White Powdery Coating
        "cause": "Powdery mildew caused by *Erysiphe cichoracearum*. It forms a white powdery coating on leaves and stems.",
        "avoid": "Avoid dense planting and ensure good air circulation.",
        "do": "Remove infected leaves and use fungicides.",
        "pesticides": "Use sulfur-based fungicides or Neem oil.",
        "organic_remedies": "Spray a mixture of baking soda and water to control powdery mildew."
    },
    {   # 26: Strawberry – Leaf Burning or Scorching
        "cause": "Leaf scorch caused by environmental stress, excessive sunlight, or lack of water. Can also be caused by fungal infections.",
        "avoid": "Avoid prolonged exposure to intense sunlight and ensure consistent watering.",
        "do": "Mulch around the plants and provide partial shade during the hottest part of the day.",
        "pesticides": "Use copper-based fungicides if fungal infection is the cause.",
        "organic_remedies": "Spray with diluted neem oil or compost tea to promote healthy foliage."
    },
    { "cause": "No disease signs. Healthy leaves and fruits, free from pests and fungal infections.",
        "avoid": "Avoid overcrowding, provide adequate spacing, and maintain proper drainage.",
        "do": "Regularly water, apply organic compost, and mulch to retain moisture.",
        "pesticides": "Not required.",
        "organic_remedies": "Spray neem oil or compost tea to keep pests at bay."},  # 27: Strawberry – Healthy
    {   # 28: Tomato – Leaf and Fruit Spots
        "cause": "Bacterial Spot caused by *Xanthomonas* species. Water-soaked spots appear on leaves and fruits.",
        "avoid": "Avoid overhead irrigation and ensure good air circulation.",
        "do": "Remove and destroy infected plant parts. Use resistant tomato varieties.",
        "pesticides": "Use copper-based fungicides like Copper oxychloride or Copper sulfate.",
        "organic_remedies": "Spray a solution of garlic extract and neem oil as a natural fungicide."
    },
    {   # 29: Tomato – Early Brown Leaf Spots
        "cause": "Early Blight caused by *Alternaria solani*. Dark brown lesions appear with concentric rings on leaves.",
        "avoid": "Avoid dense planting and ensure good air circulation.",
        "do": "Remove infected leaves, and apply fungicides like Mancozeb or Chlorothalonil.",
        "pesticides": "Use Copper oxychloride or Mancozeb during early infection stages.",
        "organic_remedies": "Spray with neem oil or compost tea to reduce disease spread."
    },
    {   # 30: Tomato – Late Black Rot
        "cause": "Late Blight caused by *Phytophthora infestans*. Characterized by large black lesions, often affecting both leaves and fruits.",
        "avoid": "Avoid wet, humid conditions. Prune infected plants promptly.",
        "do": "Remove infected plants and apply fungicides like Mancozeb or Ridomil Gold.",
        "pesticides": "Use Mancozeb or Metalaxyl to control the spread.",
        "organic_remedies": "Use neem oil or a mixture of garlic and water to prevent fungal growth."
    },
    {   # 31: Tomato – Moldy Leaves (Leaf Mold)
         "cause": "Leaf Mold caused by *Cladosporium fulvum*. White, powdery mold grows on the underside of leaves.",
        "avoid": "Avoid wetting the leaves during irrigation and provide adequate spacing.",
        "do": "Prune infected leaves and increase air circulation around plants.",
        "pesticides": "Use fungicides like Chlorothalonil or Propiconazole.",
        "organic_remedies": "Spray with neem oil or a mix of baking soda and water."
    },
    {   # 32: Tomato – Tiny Circular Spots on Leaves (Septoria Leaf Spot)
        "cause": "Septoria Leaf Spot caused by *Septoria lycopersici*. It causes tiny, circular spots with dark edges on the leaves.",
        "avoid": "Avoid overcrowding plants and ensure proper spacing.",
        "do": "Remove and dispose of infected leaves. Apply copper-based fungicides.",
        "pesticides": "Spray Mancozeb or Chlorothalonil for control.",
        "organic_remedies": "Spray neem oil and ensure proper plant care."
    },
    {   # 33: Tomato – Tiny Web and Yellowing Leaves (Spider mites)
       "cause": "Spider Mites. Small webs and yellowing of leaves are signs of mite infestation.",
        "avoid": "Avoid high heat and humidity. Inspect plants regularly for mites.",
        "do": "Use a strong stream of water to remove mites, and apply insecticidal soap.",
        "pesticides": "Use Spinosad or Insecticidal soap for control.",
        "organic_remedies": "Spray with garlic oil or neem oil solution to control mites."
    },
    {   # 34: Tomato – Round Yellow-Brown Spots (Target Spot)
        "cause": "Target Spot caused by *Alternaria solani*. Circular yellow-brown spots with dark borders appear on the leaves.",
        "avoid": "Ensure proper drainage and space between plants.",
        "do": "Remove infected leaves and apply fungicides to control the disease.",
        "pesticides": "Use Mancozeb or Chlorothalonil to manage the infection.",
        "organic_remedies": "Spray a mixture of neem oil and water to reduce fungal spread."
    },
    {   # 35: Tomato – Curled Yellow Leaves (Tomato Yellow Leaf Curl Virus)
        "cause": "Tomato Yellow Leaf Curl Virus (TYLCV) caused by a virus transmitted by whiteflies.",
        "avoid": "Avoid planting in areas with high whitefly populations.",
        "do": "Remove infected plants and control whitefly populations using insecticides or organic methods.",
        "pesticides": "Use imidacloprid or other whitefly-targeting insecticides.",
        "organic_remedies": "Use yellow sticky traps to control whiteflies and apply neem oil."
    },
    {   # 36: Tomato – Patchy Yellow/Green Leaves (Tomato Mosaic Virus)
        "cause": "Tomato Mosaic Virus (ToMV) causes yellow and green patchy leaves.",
        "avoid": "Avoid planting tomatoes near infected crops and control aphids.",
        "do": "Remove infected plants and control aphids using insecticides.",
        "pesticides": "Use insecticides like Imidacloprid for aphid control.",
        "organic_remedies": "Use neem oil and maintain plant health with regular care."
    },
    {"cause": "No signs of disease. The plant is growing strong with no visible pests or infections.",
    "avoid": "Avoid overcrowding, maintain proper spacing between plants, and ensure good airflow.",
    "do": "Regularly water, apply organic fertilizers, and prune dead or yellow leaves to promote healthy growth.",
    "pesticides": "Not needed, as the plant is healthy.",
    "organic_remedies": "Use compost or organic fertilizers to maintain soil health. Mulch around the base to retain moisture."}   # 37: Tomato – Healthy
]



# Header and introduction text
st.title(translations[lang]["title"])
st.markdown(translations[lang]["intro"], unsafe_allow_html=True)

st.markdown("---")

# Disease recognition
st.header(translations[lang]['disease_recognition'])

# File upload or camera input
img_file = st.file_uploader(translations[lang]['choose_image'], type=['jpg','jpeg','png'])
camera_img = st.camera_input("Or take a photo using your camera")

# Preview image
image_to_use = img_file if img_file else camera_img
if image_to_use:
    st.image(image_to_use, caption='Selected Image', use_column_width=True)

# Predict button
if st.button(translations[lang]['predict_btn']):
    if not image_to_use:
        st.warning('Please upload or capture an image first.')
    else:
        idx = model_prediction(image_to_use)
        label = class_labels[idx]
        meta = class_metadata[idx] if idx < len(class_metadata) else {}

        st.success(f"Prediction: {label}")

        # Display next-step info
        if meta:
            st.markdown(f"<div style='font-size:22px'><b>Cause:</b> {meta['cause']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:22px'><b>Avoid:</b> {meta['avoid']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:22px'><b>Do:</b> {meta['do']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:22px'><b>Recommended Pesticides:</b> {meta['pesticides']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:22px'><b>Organic Remedies:</b> {meta['organic_remedies']}</div>", unsafe_allow_html=True)
        else:
            st.info('No action needed. Plant appears healthy.')





