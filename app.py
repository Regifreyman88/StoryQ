import streamlit as st

st.set_page_config(
    page_title="StoryQ - Tu Aventura Narrativa",
    page_icon="🔮"
)

st.title("Bienvenida a StoryQ 🔮")

# --- Cambio Principal ---
# Ahora usamos tu nueva imagen de portada.
# Asegúrate de que el archivo se llame 'portada.png' en tu carpeta.
st.image("portada.png") # <<< ¡Esta es la línea que cambiamos!

st.header("Somos las historias que contamos")
st.write(
    """
    StoryQ es una herramienta interactiva diseñada para despertar tu creatividad y
    ayudarte a construir narrativas poderosas. Explora los arquetipos de personajes,
    recorre los caminos del héroe y juega para darle vida a tu próxima gran historia.
    
    **Usa el menú de la izquierda para navegar por las diferentes herramientas.**
    """
)