import streamlit as st

st.set_page_config(
    page_title="Arquetipos de StoryQ",
    page_icon="🧠"
)

st.title("🧠 Explora los 12 Arquetipos")
st.write("Los arquetipos son modelos de ser que nos ayudan a entender a los personajes... y a nosotros mismos. Elige uno para conocerlo mejor.")

# CORREGIDO: Usando los nombres de archivo exactos de tu lista final
arquetipos = {
    "El Artista": {"imagen": "artista.jpg"},
    "El Aventurero": {"imagen": "aventurero.jpg"},
    "El Chico Común": {"imagen": "chico_comun.jpg"},
    "El Héroe": {"imagen": "heroe.jpg"},
    "El Inocente": {"imagen": "inocente.jpg"},
    "El Líder": {"imagen": "lider.jpg"},
    "El Mago": {"imagen": "mago.jpg"},
    "El Nutridor": {"imagen": "nutridor.jpg"},
    "El Rebelde": {"imagen": "rebelde.jpg"},
    "El Sabio": {"imagen": "sabio.jpg"},
    "La Sombra": {"imagen": "sombra.jpg"},
    # Faltan Seductor y Bufón, puedes añadirlos cuando tengas sus imágenes.
}

opcion = st.selectbox("Elige un arquetipo:", list(arquetipos.keys()))

if opcion:
    carta = arquetipos[opcion]
    st.header(opcion)
    
    # Intenta mostrar la imagen y si no la encuentra, da un error amigable.
    try:
        st.image(carta["imagen"])
    except Exception:
        st.error(f"Error: No se encontró la imagen '{carta['imagen']}'. Verifica que el archivo esté subido a GitHub con ese nombre exacto.")
