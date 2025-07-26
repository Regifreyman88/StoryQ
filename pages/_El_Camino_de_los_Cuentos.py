import streamlit as st

st.set_page_config(
    page_title="El Camino de los Cuentos",
    page_icon="🧚"
)

st.title("🧚 El Camino de los Cuentos de Hadas")
st.write("Una estructura clásica para narrativas de encanto, pruebas y transformaciones inesperadas.")

# Mostramos la imagen del tablero
try:
    st.image("tablero_cuentos.jpg")
except Exception:
    st.error("No se encontró la imagen 'tablero_cuentos.jpg'. Asegúrate de que el archivo esté en el repositorio principal.")

st.markdown("---")

st.header("Las Etapas del Cuento")

with st.expander("1. Salida del hogar"):
    st.write("El protagonista, a menudo humilde o común, debe dejar su entorno familiar debido a un problema, una carencia o un deseo.")

with st.expander("2. Camino para restaurar el orden (Pruebas)"):
    st.write("Durante su viaje, el protagonista se enfrenta a una serie de pruebas y encuentra objetos o personajes que parecen insignificantes pero serán clave.")

with st.expander("3. Fragilidad y Ayuda"):
    st.write("El protagonista se encuentra con alguien vulnerable o en apuros y, a pesar de sus propias limitaciones, se detiene para ayudar.")

with st.expander("4. Acto heroico"):
    st.write("Usando su ingenio, bondad y a menudo la ayuda de un don mágico recibido por su acto de generosidad, el protagonista realiza un acto heroico.")

with st.expander("5. Reconexión"):
    st.write("El protagonista logra su objetivo, a menudo reconectando con aquello que había perdido o reparando el desorden inicial.")
    
with st.expander("6. Regreso a la pasividad (o a un nuevo orden)"):
    st.write("El protagonista regresa a su hogar, pero transformado. La 'pasividad' no es negativa, sino un retorno a un estado de paz y equilibrio, ahora enriquecido por la experiencia.")
