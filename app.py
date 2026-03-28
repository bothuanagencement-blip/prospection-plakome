import streamlit as st

st.title("Prospection Plakome & Tanguy Design")

societe = st.selectbox(
    "Choisir la société",
    ["Plakome", "Tanguy Design"]
)

st.write(f"Société sélectionnée : {societe}")

st.button("Rechercher prospects")
st.button("Créer campagne")
