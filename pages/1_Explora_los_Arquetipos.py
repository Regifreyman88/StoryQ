import streamlit as st

st.set_page_config(
    page_title="Arquetipos de StoryQ",
    page_icon="🧠"
)

st.title("🧠 Explora los 12 Arquetipos")
st.write("Los arquetipos son modelos de ser que nos ayudan a entender a los personajes... y a nosotros mismos. Elige uno para conocerlo mejor.")

# --- Mazo de Arquetipos con Descripciones Detalladas ---
# La información fue extraída de tu instructivo.
arquetipos = {
    "El Héroe": {
        "imagen": "heroe.jpg",
        "descripcion": "Es el que se atreve a enfrentar los desafíos y a luchar por lo que quiere. Es valiente, decidido, competitivo y líder. Su debilidad es que puede ser arrogante, agresivo o temerario."
    },
    "El Inocente": {
        "imagen": "inocente.jpg",
        "descripcion": "Es el que siempre ve el lado bueno de las cosas y busca ser feliz. Es optimista, puro, bondadoso y confiado. Su debilidad es que puede ser ingenuo, soñador o dependiente de los demás."
    },
    "El Mago": {
        "imagen": "mago.jpg",
        "descripcion": "Es el que tiene un gran poder e influencia sobre los demás y sobre la realidad. Es transformador, creativo, intuitivo y carismático. Su debilidad es que puede ser manipulador o engañoso."
    },
    "El Sabio": {
        "imagen": "sabio.jpg",
        "descripcion": "Es el que tiene un gran conocimiento e inteligencia y le gusta aprender y enseñar. Es reflexivo, analítico, observador y consejero. Su debilidad es que puede ser pedante, dogmático o desconectado de la realidad."
    },
    "El Nutridor": {
        "imagen": "nutridor.jpg",
        "descripcion": "Es el que se preocupa por el bienestar de los demás y les ofrece su apoyo y su protección. Es altruista, compasivo, generoso y empático. Su debilidad es que puede ser sobreprotector, sacrificado o manipulador."
    },
    "El Rebelde": {
        "imagen": "rebelde.jpg",
        "descripcion": "Es el que se rebela contra las normas y las autoridades y busca cambiar el mundo. Es inconformista, revolucionario, provocador y liberador. Su debilidad es que puede ser destructivo, violento o irresponsable."
    },
    "El Artista": {
        "imagen": "artista.jpg",
        "descripcion": "Es el que tiene una gran imaginación y capacidad para crear cosas originales e innovadoras. Es artístico, expresivo, visionario e inspirador. Su debilidad es que puede ser perfeccionista, egocéntrico o impráctico."
    },
    "El Aventurero": {
        "imagen": "aventurero.jpg",
        "descripcion": "Es el que le gusta descubrir cosas nuevas y vivir aventuras. Es curioso, independiente, libre y viajero. Su debilidad es que puede ser inquieto, insatisfecho o escapista."
    },
    "El Chico Común": {
        "imagen": "chico_comun.jpg",
        "descripcion": "Es el que se lleva bien con todo el mundo y quiere ayudar a los demás. Es leal, honesto, justo y ético. Su debilidad es que puede ser demasiado idealista, moralista o conformista."
    },
    "El Líder": {
        "imagen": "lider.jpg",
        "descripcion": "Es el que tiene un gran sentido de la responsabilidad y la organización y le gusta tener el control de todo. Es poderoso, ambicioso, autoritario e influyente. Su debilidad es que puede ser tirano, dominante o inflexible."
    },
     "El Seductor": {
        "imagen": "seductor.jpg", # Asegúrate de tener este archivo
        "descripcion": "Es el que disfruta de la belleza, el placer y las relaciones afectivas. Es apasionado, sensual, romántico y atractivo. Su debilidad es que puede ser dependiente, celoso o superficial."
    },
    "La Sombra": {
        "imagen": "sombra.jpg",
        "descripcion": "Es la parte de nuestra personalidad que no queremos reconocer ni mostrar. Contiene nuestros miedos, defectos y deseos ocultos. Puede hacernos actuar de manera negativa o destructiva."
    }
    # Asegúrate de tener las imágenes para todos los arquetipos.
}

# --- Interfaz de la Aplicación ---

opcion = st.selectbox("Elige un arquetipo:", sorted(list(arquetipos.keys())))

if opcion:
    carta = arquetipos[opcion]
    
    st.header(opcion)
    
    # Usamos columnas para una mejor distribución
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(carta["imagen"])

    with col2:
        st.subheader("Análisis del Arquetipo")
        st.write(carta["descripcion"])
