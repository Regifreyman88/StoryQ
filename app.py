import streamlit as st

st.set_page_config(
    page_title="StoryQ - Tu Aventura Narrativa",
    page_icon="🔮"
)

st.title("Bienvenida a StoryQ 🔮")

# Asegúrate de que el archivo se llame 'portada.png' en tu carpeta.
# Si usas el tablero para la portada de StoryQ, el archivo podría ser 'tablero.jpg'
try:
    st.image("portada.png") 
except Exception:
    st.warning("Asegúrate de tener un archivo 'portada.png' en tu repositorio.")


st.header("Somos las historias que contamos")
st.write(
    """
    StoryQ es una herramienta interactiva diseñada para despertar tu creatividad y
    ayudarte a construir narrativas poderosas. Explora los arquetipos de personajes,
    recorre los caminos del héroe y juega para darle vida a tu próxima gran historia.
    
    **Usa el menú de la izquierda para navegar por las diferentes herramientas.**
    """
)

# --- MÓDULO DE APOYO ---
# Este código añade la sección en la barra lateral.
st.sidebar.markdown("---")
st.sidebar.header("Apoya este Proyecto")
st.sidebar.write(
    """
    ¿Te ha gustado StoryQ? 
    Tu apoyo me ayuda a seguir creando y mejorando más juegos educativos y creativos.
    
    ¡Gracias por tu generosidad!
    """
)
st.sidebar.link_button("Invítame un café ☕", "https://coff.ee/regifreyman8")
