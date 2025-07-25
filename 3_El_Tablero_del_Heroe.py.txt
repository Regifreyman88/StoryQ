import streamlit as st

st.set_page_config(
    page_title="El Viaje del Héroe",
    page_icon="🗺️"
)

st.title("🗺️ El Tablero del Viaje del Héroe")
st.write("Usa este mapa como una guía para estructurar tu narrativa. Cada casilla representa una etapa clave en la transformación de tu personaje.")

# Mostramos la imagen principal del tablero
# Asegúrate de que el archivo 'tablero.jpg' esté en tu carpeta principal.
try:
    st.image("tablero.jpg")
except FileNotFoundError:
    st.error("No se encontró la imagen 'tablero.jpg'. Asegúrate de que el archivo esté en la carpeta principal de la aplicación.")

st.markdown("---")

st.header("Las 17 Etapas del Viaje")

# Usamos st.expander para que la lista no sea tan larga y el usuario pueda abrir cada etapa.
with st.expander("1. La llamada a la aventura"):
    st.write("El protagonista descubre que su vida actual no es satisfactoria y busca una nueva dirección.")

with st.expander("2. La negativa a la llamada"):
    st.write("El protagonista se siente inseguro y temeroso ante los desafíos que le esperan.")

with st.expander("3. Encuentro con el mentor"):
    st.write("El protagonista encuentra a un guía que lo ayuda a superar sus miedos y lo prepara para la aventura.")

with st.expander("4. Cruzando el umbral"):
    st.write("El protagonista abandona su vida anterior y se adentra en el mundo desconocido de la aventura.")

with st.expander("5. Pruebas y aliados"):
    st.write("El protagonista enfrenta desafíos y encuentra nuevos amigos y aliados que lo ayudan en su viaje.")

with st.expander("6. Acercamiento a la cueva oscura"):
    st.write("El protagonista se acerca a la fuente de su mayor miedo o desafío.")

with st.expander("7. La crisis"):
    st.write("El protagonista se enfrenta a su mayor desafío y sufre una derrota significativa.")

with st.expander("8. La revelación"):
    st.write("El protagonista descubre una nueva comprensión sobre sí mismo y su camino.")

with st.expander("9. Transformación"):
    st.write("El protagonista se transforma a través de la comprensión y la aceptación de su verdadera naturaleza.")

with st.expander("10. El don"):
    st.write("El protagonista recibe un regalo o conocimiento especial que le permite avanzar en su viaje.")

with st.expander("11. El camino de regreso"):
    st.write("El protagonista emprende el viaje de regreso a casa, pero aún enfrenta desafíos.")

with st.expander("12. La resurrección"):
    st.write("El protagonista enfrenta su mayor desafío y emerge renovado y transformado.")

with st.expander("13. El regreso con el elixir"):
    st.write("El protagonista regresa a casa con un don o conocimiento especial para compartir con su comunidad.")

with st.expander("14. Integración de la vida cotidiana"):
    st.write("El protagonista aprende a integrar su experiencia de aventura en su vida cotidiana.")

with st.expander("15. Celebración"):
    st.write("El protagonista celebra su éxito con su comunidad.")

with st.expander("16. El llamado a compartir"):
    st.write("El protagonista comparte su don o conocimiento especial con aquellos que buscan aventuras similares.")

with st.expander("17. El nuevo comienzo"):
    st.write("El protagonista comienza una nueva etapa de su vida con una nueva perspectiva y una mayor comprensión de sí mismo y el mundo.")