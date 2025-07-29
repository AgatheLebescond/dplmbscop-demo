app_dplmbscop_mini_light.py
# Timport streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from textblob import TextBlob
from transformers import pipeline

# Résumeur HuggingFace
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

st.set_page_config(page_title="DplmbScop", layout="wide")
st.title("🧠 DplmbScop — Prototype Démo")
st.caption("Résumé automatique, nuage de mots, et tonalité d’un article controversé")

# Zone de texte
article = st.text_area("📰 Colle ici un article, un extrait ou une pétition :", height=300, placeholder="Colle ton texte ici...")

# Requête
requete = st.text_input("🔍 Requête thématique (optionnel) :", placeholder="Ex : danger pour la santé publique")

# Bouton
if st.button("Analyser"):
    if not article.strip():
        st.warning("Merci de coller un texte à analyser.")
    else:
        st.subheader("📝 Résumé de l’article")
        summary = summarizer(article, max_length=130, min_length=30, do_sample=False)
        st.success(summary[0]['summary_text'])

        st.subheader("💬 Analyse de sentiment")
        blob = TextBlob(article)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            st.info(f"Tonalité : **positive** ({sentiment:.2f})")
        elif sentiment < 0:
            st.error(f"Tonalité : **négative** ({sentiment:.2f})")
        else:
            st.warning("Tonalité : **neutre**")

        st.subheader("☁️ Nuage de mots")
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(article)
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)

st.markdown("---")
st.caption("Version simplifiée de démonstration sans connexion à X / Change.org / scraping.")


