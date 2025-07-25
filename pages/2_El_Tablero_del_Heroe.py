import streamlit as st

st.set_page_config(
    page_title="Arquetipos de StoryQ",
    page_icon="🧠"
)

st.title("🧠 Explora los 12 Arquetipos")
st.write("Los arquetipos son modelos de ser que nos ayudan a entender a los personajes... y a nosotros mismos. Elige uno para conocerlo mejor.")

# CORREGIDO: Usando los nombres de archivo exactos de tu lista
arquetipos = {
    "El Artista": {"imagen": "artista.jpg"},
    "El Aventurero": {"imagen": "aventurero.jpg"},
    "El Chico Común": {"imagen": "chico_comun.jpg"}, # Con guion bajo
    "El Héroe": {"imagen": "heroe.jpg"},
    "El Inocente": {"imagen": "inocente.jpg"},
    "El Líder": {"imagen": "lider.jpg"},
    "El Mago": {"imagen": "mago.jpg"},
    "El Nutridor": {"imagen": "nutridor.jpg"},
    "El Rebelde": {"imagen": "rebelde.jpg"},
    "El Sabio": {"imagen": "sabio.jpg"},
    "La Sombra": {"imagen": "sombra.jpg"},
    # Falta el Seductor y el Bufón en tu lista, añádelos cuando los tengas.
}

opcion = st.selectbox("Elige un arquetipo:", list(arquetipos.keys()))

if opcion:
    carta = arquetipos[opcion]
    st.header(opcion)
    st.image(carta["imagen"])
