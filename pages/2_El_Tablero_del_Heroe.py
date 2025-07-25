import streamlit as st

st.set_page_config(
    page_title="El Viaje del Héroe",
    page_icon="🗺️"
)

# Definimos todas las etapas del viaje en una lista de diccionarios
etapas_del_viaje = [
    {"titulo": "1. La llamada a la aventura", "descripcion": "El protagonista descubre que su vida actual no es satisfactoria y busca una nueva dirección."},
    {"titulo": "2. La negativa a la llamada", "descripcion": "El protagonista se siente inseguro y temeroso ante los desafíos que le esperan."},
    {"titulo": "3. Encuentro con el mentor", "descripcion": "El protagonista encuentra a un guía que lo ayuda a superar sus miedos y lo prepara para la aventura."},
    {"titulo": "4. Cruzando el umbral", "descripcion": "El protagonista abandona su vida anterior y se adentra en el mundo desconocido de la aventura."},
    {"titulo": "5. Pruebas y aliados", "descripcion": "El protagonista enfrenta desafíos y encuentra nuevos amigos y aliados que lo ayudan en su viaje."},
    {"titulo": "6. Acercamiento a la cueva oscura", "descripcion": "El protagonista se acerca a la fuente de su mayor miedo o desafío."},
    {"titulo": "7. La crisis", "descripcion": "El protagonista se enfrenta a su mayor desafío y sufre una derrota significativa."},
    {"titulo": "8. La revelación", "descripcion": "El protagonista descubre una nueva comprensión sobre sí mismo y su camino."},
    {"titulo": "9. Transformación", "descripcion": "El protagonista se transforma a través de la comprensión y la aceptación de su verdadera naturaleza."},
    {"titulo": "10. El don", "descripcion": "El protagonista recibe un regalo o conocimiento especial que le permite avanzar en su viaje."},
    {"titulo": "11. El camino de regreso", "descripcion": "El protagonista emprende el viaje de regreso a casa, pero aún enfrenta desafíos."},
    {"titulo": "12. La resurrección", "descripcion": "El protagonista enfrenta su mayor desafío y emerge renovado y transformado."},
    {"titulo": "13. El regreso con el elixir", "descripcion": "El protagonista regresa a casa con un don o conocimiento especial para compartir con su comunidad."},
    {"titulo": "14. Integración de la vida cotidiana", "descripcion": "El protagonista aprende a integrar su experiencia de aventura en su vida cotidiana."},
    {"titulo": "15. Celebración", "descripcion": "El protagonista celebra su éxito con su comunidad."},
    {"titulo": "16. El llamado a compartir", "descripcion": "El protagonista comparte su don o conocimiento especial con aquellos que buscan aventuras similares."},
    {"titulo": "17. El nuevo comienzo", "descripcion": "El protagonista comienza una nueva etapa de su vida con una nueva perspectiva y una mayor comprensión de sí mismo y el mundo."}
]

# Interfaz de la Aplicación
st.title("🗺️ El Tablero Interactivo del Héroe")
st.write("Sigue el camino paso a paso para construir tu historia. Cada vez que avances, reflexiona y escribe la parte correspondiente de tu relato.")

st.image("tablero.jpg")
st.markdown("---")

# Lógica Interactiva
if 'paso_actual' not in st.session_state:
    st.session_state.paso_actual = 0

col1, col2 = st.columns(2)

if col1.button("Avanzar al siguiente paso ➡️"):
    if st.session_state.paso_actual < len(etapas_del_viaje) - 1:
        st.session_state.paso_actual += 1

if col2.button("Reiniciar Viaje ⏪"):
    st.session_state.paso_actual = 0

st.markdown("---")

# Mostrar la Etapa Actual
etapa_actual = etapas_del_viaje[st.session_state.paso_actual]
st.header(etapa_actual["titulo"])
st.info(etapa_actual["descripcion"])
st.text_area("Escribe aquí la parte de tu historia que corresponde a esta etapa:", height=200, key=f"texto_{st.session_state.paso_actual}")
