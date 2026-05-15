import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def temizle(metin):
    metin = metin.lower()
    metin = re.sub(r'[^a-zA-Z\s]', '', metin)
    stop_words = set(stopwords.words('english'))
    kelimeler = metin.split()
    temiz_kelimeler = [k for k in kelimeler if k not in stop_words]
    return ' '.join(temiz_kelimeler)

model = joblib.load('spam.model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title('SMS Spam Dedektörü')

mesaj = st.text_area('Mesajı Gir:')

if st.button('Kontrol Et'):
    temiz_mesaj = temizle(mesaj)
    X = vectorizer.transform([temiz_mesaj])
    sonuc = model.predict(X)
    if sonuc == 1:
        st.write('Spam')
    else:
        st.write('Ham')