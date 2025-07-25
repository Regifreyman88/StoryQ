import streamlit as st

st.set_page_config(
    page_title="Arquetipos de StoryQ",
    page_icon="🧠"
)

st.title("🧠 Explora los 12 Arquetipos")
st.write("Los arquetipos son modelos de ser que nos ayudan a entender a los personajes... y a nosotros mismos. Elige uno para conocerlo mejor.")

# Definimos los arquetipos usando la información de tu PDF y los nombres de tus archivos
arquetipos = {
    "El Inocente": {
        "descripcion": "Es el que siempre ve el lado bueno de las cosas y busca ser feliz. Es optimista, puro, bondadoso y confiado. Su debilidad es que puede ser ingenuo, soñador o dependiente.",
        "imagen": "13.png"
    },
    "El Héroe": {
        "descripcion": "Es el que se atreve a enfrentar los desafíos y a luchar por lo que quiere. Es valiente, decidido, competitivo y líder. Su debilidad es que puede ser arrogante, agresivo o temerario.",
        "imagen": "12.png"
    },
    "El Mago": {
        "descripcion": "Es el que tiene un gran poder e influencia sobre los demás y sobre la realidad. Es transformador, creativo, intuitivo y carismático. Su debilidad es que puede ser manipulador o engañoso.",
        "imagen": "2.png"
    },
    "El Sabio": {
        "descripcion": "Es el que tiene un gran conocimiento e inteligencia y le gusta aprender y enseñar. Es reflexivo, analítico y observador. Su debilidad es que puede ser pedante o desconectado de la realidad.",
        "imagen": "3.png"
    },
    "El Seductor": {
        "descripcion": "Es el que disfruta de la belleza, el placer y las relaciones afectivas. Es apasionado, sensual y romántico. Su debilidad es que puede ser dependiente, celoso o superficial.",
        "imagen": "4.png"
    },
    "El Nutridor": {
        "descripcion": "Es el que se preocupa por el bienestar de los demás y les ofrece su apoyo y protección. Es altruista, compasivo y generoso. Su debilidad es que puede ser sobreprotector o sacrificado.",
        "imagen": "7.png"
    },
    "El Rebelde": {
        "descripcion": "Es el que se rebela contra las normas y las autoridades y busca cambiar el mundo. Es inconformista, revolucionario y provocador. Su debilidad es que puede ser destructivo o irresponsable.",
        "imagen": "9.png"
    }
    # Puedes seguir añadiendo el resto de arquetipos aquí
}

# Creamos un menú para que el usuario elija
opcion = st.selectbox("Elige un arquetipo:", list(arquetipos.keys()))

# Mostramos la información del arquetipo seleccionado
carta = arquetipos[opcion]

st.header(opcion)
st.image(carta["imagen"])
st.subheader("Análisis del Arquetipo")
st.write(carta["descripcion"])