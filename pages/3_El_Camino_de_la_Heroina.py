import streamlit as st

st.set_page_config(
    page_title="El Camino de la Heroína",
    page_icon="👑"
)

st.title("👑 El Camino de la Heroína")
st.write("Una estructura narrativa para explorar viajes de autodescubrimiento e integración.")

# Mostramos la imagen del tablero
try:
    st.image("tablero_heroina.jpg")
except Exception:
    st.error("No se encontró la imagen 'tablero_heroina.jpg'. Asegúrate de que el archivo esté en el repositorio principal.")

st.markdown("---")

st.header("Las Etapas del Viaje")

# Usamos expanders para mostrar las etapas del tablero
with st.expander("1. Separación de lo femenino"):
    st.write("La heroína siente una desconexión con los valores tradicionalmente femeninos que la rodean.")

with st.expander("2. Identificación con lo masculino"):
    st.write("Busca el éxito en un mundo dominado por reglas y valores masculinos, adoptándolos como propios.")

with st.expander("3. Pruebas, aliados y enemigos (Encuentro con ogros y dragones)"):
    st.write("En su búsqueda de éxito, enfrenta desafíos que ponen a prueba sus nuevas habilidades y se encuentra con aliados y adversarios.")

with st.expander("4. Éxito aparente y sentimiento de vacío (Muerte espiritual)"):
    st.write("Aunque puede alcanzar el éxito según los estándares del mundo exterior, siente una profunda insatisfacción o vacío interior.")

with st.expander("5. Iniciación y reconexión femenina"):
    st.write("Un evento o crisis la lleva a un punto de quiebre, iniciando un descenso para reconectar con su propia alma y los valores femeninos que rechazó.")

with st.expander("6. Cura de la herida masculino-femenina"):
    st.write("La heroína aprende a sanar la división interna entre sus lados masculino y femenino, aceptando e integrando ambos.")
    
with st.expander("7. Regreso e integración final"):
    st.write("Regresa al mundo con una nueva sabiduría, capaz de integrar su ser completo y actuar desde un lugar de autenticidad y equilibrio.")
