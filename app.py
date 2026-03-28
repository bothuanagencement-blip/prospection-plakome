import streamlit as st
import pandas as pd

st.set_page_config(page_title="Prospection Plakome & Tanguy Design")

st.title("Prospection Plakome & Tanguy Design")

societe = st.selectbox(
    "Choisir la société",
    ["Plakome", "Tanguy Design"]
)

st.write(f"Société sélectionnée : {societe}")

st.divider()

st.subheader("Recherche de prospects")

metier = st.selectbox(
    "Type de prospect",
    [
        "Architectes",
        "Maîtres d'œuvre",
        "Architectes intérieur",
        "Promoteurs"
    ]
)

ville = st.text_input("Ville ou département", "Morbihan")

if st.button("Rechercher prospects"):

    data = {
        "Entreprise": [
            "Atelier Architecture Vannes",
            "MO Bretagne Auray",
            "Architecte Lorient"
        ],
        "Ville": [
            "Vannes",
            "Auray",
            "Lorient"
        ],
        "Email": [
            "contact@exemple1.fr",
            "contact@exemple2.fr",
            "contact@exemple3.fr"
        ],
        "Type": [
            metier,
            metier,
            metier
        ]
    }

    df = pd.DataFrame(data)

    st.success("Prospects trouvés")
    st.dataframe(df)

st.divider()

st.subheader("Campagne emailing")

objet = st.text_input("Objet du mail")

message = st.text_area("Message")

nb_mail = st.number_input(
    "Nombre de mails par jour",
    min_value=1,
    max_value=50,
    value=10
)

if st.button("Créer campagne"):
    st.success("Campagne créée")
    st.write("Société :", societe)
    st.write("Objet :", objet)
    st.write("Mails par jour :", nb_mail)
