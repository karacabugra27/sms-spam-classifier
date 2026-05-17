# SMS Spam Sınıflandırıcı

## Amaç
Kısa mesajların spam mı yoksa normal mi olduğunu tahmin eden 
bir sınıflandırıcı. Naive Bayes modeli %98 doğrulukla çalışıyor.

## Teknolojiler
- Python
- Pandas
- Scikit-learn
- NLTK
- Streamlit

## Nasıl Çalıştırılır
1. Kütüphaneleri kur:
pip install pandas scikit-learn nltk streamlit joblib
2. Jupyter'da `notebook.ipynb` dosyasını çalıştır — model ve vectorizer kaydedilir
3. Uygulamayı başlat:
streamlit run app.py

## Öğrendiklerim
- Veri temizleme: küçük harf, noktalama, stopwords
- TF-IDF ile metinleri sayısal vektöre dönüştürme
- Veri dengesizliğini tespit etme ve recall metriğinin önemi
- Naive Bayes ve Logistic Regression karşılaştırması
- Streamlit ile model deployment
