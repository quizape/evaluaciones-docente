import unicodedata

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Evaluaciones y cambios docentes",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Evaluaciones y cambios docentes")
st.caption(
    "Aplicación de consulta. Los datos no se pueden editar desde la interfaz."
)


agenda = {
    "Lunes 28": {
        "evaluaciones": [
            {
                "Bloque": "1.º y 2.º",
                "Curso": "3.º C",
                "Profesor": "Cristian Gutierrez",
                "Sala": "32",
            },
            {
                "Bloque": "2.º y 3.º",
                "Curso": "2.º B",
                "Profesor": "Félix Ormázabal",
                "Sala": "15",
            },
            {
                "Bloque": "3.º y 4.º",
                "Curso": "2.º A",
                "Profesor": "Fernando Tatter",
                "Sala": "22",
            },
        ],
        "cambios": [
            {
                "Bloque": "1.º",
                "Docente": "Jorge Berríos",
                "Reemplaza a": "Cristian Gutierrez",
                "Curso que toma": "2.º D",
                "Sala": "27",
            },
            {
                "Bloque": "2.º",
                "Docente": "María Eliana Astudillo",
                "Reemplaza a": "Félix Ormázabal",
                "Curso que toma": "Electivo de 3.º Medio",
                "Sala": "16",
            },
            {
                "Bloque": "2.º",
                "Docente": "Marcelo Ortiz",
                "Reemplaza a": "Cristian Gutierrez",
                "Curso que toma": "4.º A",
                "Sala": "17",
            },
            {
                "Bloque": "4.º",
                "Docente": "María José Arévalo",
                "Reemplaza a": "Fernando Tatter",
                "Curso que toma": "1.º D",
                "Sala": "29",
            },
            {
                "Bloque": "3.º",
                "Docente": "Cristian Gutierrez",
                "Reemplaza a": "Félix Ormázabal",
                "Curso que toma": "Electivo de 4.º Medio",
                "Sala": "32",
            },
            {
                "Bloque": "3.º",
                "Docente": "Raquel Vera",
                "Reemplaza a": "Fernando Tatter",
                "Curso que toma": "Electivo de 3.º Medio",
                "Sala": "18",
            },
        ],
    },

    "Jueves 01/10": {
        "evaluaciones": [
            {
                "Bloque": "1.º y 2.º",
                "Curso": "2.º A",
                "Profesor": "Sebastián Fuentes",
                "Sala": "21",
            },
            {
                "Bloque": "2.º y 3.º",
                "Curso": "1.º C",
                "Profesor": "Alejandro",
                "Sala": "34",
            },
            {
                "Bloque": "3.º y 4.º",
                "Curso": "4.º A",
                "Profesor": "Isma",
                "Sala": "19",
            },
        ],
        "cambios": [
            {
                "Bloque": "1.º",
                "Docente": "Lissete Caravantes",
                "Reemplaza a": "Sebastián Fuentes",
                "Curso que toma": "4.º E",
                "Sala": "34",
            },
            {
                "Bloque": "2.º",
                "Docente": "Francisca Larraín",
                "Reemplaza a": "Sebastián Fuentes",
                "Curso que toma": "1.º D",
                "Sala": "23",
            },
            {
                "Bloque": "2.º",
                "Docente": "Alejandro Mondaca",
                "Reemplaza a": "Alejandro",
                "Curso que toma": "1.º C",
                "Sala": "26",
            },
            {
                "Bloque": "3.º",
                "Docente": "María Eliana Astudillo",
                "Reemplaza a": "Alejandro",
                "Curso que toma": "1.º B",
                "Sala": "16",
            },
            {
                "Bloque": "3.º",
                "Docente": "Ismael Oyarce",
                "Reemplaza a": "Isma",
                "Curso que toma": "4.º A",
                "Sala": "",
            },
            {
                "Bloque": "4.º",
                "Docente": "Electivo",
                "Reemplaza a": "Isma",
                "Curso que toma": "Libre",
                "Sala": "",
            },
        ],
    },

    "Viernes 02/10": {
        "evaluaciones": [
            {
                "Bloque": "1.º y 2.º",
                "Curso": "2.º B",
                "Profesor": "Carlos Gómez",
                "Sala": "20",
            },
            {
                "Bloque": "2.º y 3.º",
                "Curso": "2.º A",
                "Profesor": "Ariel Moraga",
                "Sala": "31",
            },
            {
                "Bloque": "3.º y 4.º",
                "Curso": "4.º A",
                "Profesor": "Patricio Quinteros",
                "Sala": "23",
            },
        ],
        "cambios": [
            {
                "Bloque": "1.º",
                "Docente": "Cristian Gutierrez",
                "Reemplaza a": "Carlos Gómez",
                "Curso que toma": "2.º D",
                "Sala": "32",
            },
            {
                "Bloque": "2.º",
                "Docente": "Lissete Caravantes",
                "Reemplaza a": "Carlos Gómez",
                "Curso que toma": "Libre",
                "Sala": "34",
            },
            {
                "Bloque": "2.º",
                "Docente": "Marcelo Ortiz",
                "Reemplaza a": "Ariel Moraga",
                "Curso que toma": "Electivo Tercero",
                "Sala": "17",
            },
            {
                "Bloque": "3.º",
                "Docente": "Sebastián Fuentes",
                "Reemplaza a": "Ariel Moraga",
                "Curso que toma": "1.º C",
                "Sala": "20",
            },
            {
                "Bloque": "3.º",
                "Docente": "Electivo",
                "Reemplaza a": "Patricio Quinteros",
                "Curso que toma": "Libre",
                "Sala": "",
            },
            {
                "Bloque": "4.º",
                "Docente": "Electivo",
                "Reemplaza a": "Patricio Quinteros",
                "Curso que toma": "Libre",
                "Sala": "",
            },
        ],
    },

    "Lunes 05/10": {
        "evaluaciones": [
            {
                "Bloque": "1.º y 2.º",
                "Curso": "2.º C",
                "Profesor": "María José Arévalo",
                "Sala": "29",
            },
            {
                "Bloque": "2.º y 3.º",
                "Curso": "2.º B",
                "Profesor": "Franco Gálvez",
                "Sala": "Cancha",
            },
            {
                "Bloque": "3.º y 4.º",
                "Curso": "1.º D",
                "Profesor": "Marcelo Ortiz",
                "Sala": "17",
            },
        ],
        "cambios": [
            {
                "Bloque": "1.º",
                "Docente": "Francisca Larraín",
                "Reemplaza a": "María José Arévalo",
                "Curso que toma": "1.º A",
                "Sala": "23",
            },
            {
                "Bloque": "2.º",
                "Docente": "Ariel Moraga",
                "Reemplaza a": "María José Arévalo",
                "Curso que toma": "1.º D",
                "Sala": "31",
            },
            {
                "Bloque": "2.º",
                "Docente": "María Eliana Astudillo",
                "Reemplaza a": "Franco Gálvez",
                "Curso que toma": "4.º B",
                "Sala": "16",
            },
            {
                "Bloque": "3.º",
                "Docente": "Cristian Gutierrez",
                "Reemplaza a": "Franco Gálvez",
                "Curso que toma": "1.º C",
                "Sala": "32",
            },
            {
                "Bloque": "3.º",
                "Docente": "Alfredo Oyarzún",
                "Reemplaza a": "Marcelo Ortiz",
                "Curso que toma": "Libre",
                "Sala": "",
            },
            {
                "Bloque": "4.º",
                "Docente": "Fernando Tatter",
                "Reemplaza a": "Marcelo Ortiz",
                "Curso que toma": "3.º D (45 min) y 3.º C (45 min)",
                "Sala": "22",
            },
        ],
    },
}


def normalizar(texto):
    texto_nfd = unicodedata.normalize("NFD", str(texto))

    texto_sin_tildes = "".join(
        caracter
        for caracter in texto_nfd
        if unicodedata.category(caracter) != "Mn"
    )

    return texto_sin_tildes.lower().strip()


def crear_registros(datos_agenda):
    registros_globales = []

    for fecha_registro, programacion in datos_agenda.items():
        for evaluacion in programacion["evaluaciones"]:
            fila = {
                "Fecha": fecha_registro,
                "Tipo": "Evaluación",
                "Bloque": evaluacion.get("Bloque", ""),
                "Curso": evaluacion.get("Curso", ""),
                "Profesor": evaluacion.get("Profesor", ""),
                "Docente": "",
                "Reemplaza a": "",
                "Curso que toma": "",
                "Sala": evaluacion.get("Sala", ""),
            }
            registros_globales.append(fila)

        for cambio in programacion["cambios"]:
            fila = {
                "Fecha": fecha_registro,
                "Tipo": "Cambio",
                "Bloque": cambio.get("Bloque", ""),
                "Curso": "",
                "Profesor": "",
                "Docente": cambio.get("Docente", ""),
                "Reemplaza a": cambio.get("Reemplaza a", ""),
                "Curso que toma": cambio.get("Curso que toma", ""),
                "Sala": cambio.get("Sala", ""),
            }
            registros_globales.append(fila)

    return registros_globales


registros = crear_registros(agenda)


busqueda = st.text_input(
    "🔎 Buscar en todas las fechas",
    placeholder="Ej.: quint, 2.º A, sala 23...",
)


if busqueda.strip():
    termino = normalizar(busqueda)
    resultados = []

    for registro in registros:
        contenido = " ".join(
            str(valor)
            for valor in registro.values()
        )

        if termino in normalizar(contenido):
            resultados.append(registro)

    if resultados:
        st.subheader(f"Resultados para: {busqueda}")
        st.caption(
            f"Se encontraron {len(resultados)} coincidencias."
        )

        tabla_resultados = pd.DataFrame(resultados)

        columnas_visibles = [
            columna
            for columna in tabla_resultados.columns
            if tabla_resultados[columna]
            .fillna("")
            .astype(str)
            .str.strip()
            .ne("")
            .any()
        ]

        tabla_resultados = tabla_resultados[columnas_visibles]

        st.dataframe(
            tabla_resultados,
            use_container_width=True,
            hide_index=True,
        )

    else:
        st.warning("No se encontraron coincidencias.")

else:
    fecha = st.selectbox(
        "Selecciona una fecha",
        list(agenda.keys()),
    )

    datos = agenda[fecha]

    tab_evaluaciones, tab_cambios = st.tabs(
        ["Docentes a evaluar", "Cambios"]
    )

    with tab_evaluaciones:
        st.subheader(f"Docentes a evaluar — {fecha}")

        tabla_evaluaciones = pd.DataFrame(
            datos["evaluaciones"]
        )

        st.dataframe(
            tabla_evaluaciones,
            use_container_width=True,
            hide_index=True,
        )

    with tab_cambios:
        st.subheader(f"Cambios — {fecha}")

        tabla_cambios = pd.DataFrame(
            datos["cambios"]
        )

        st.dataframe(
            tabla_cambios,
            use_container_width=True,
            hide_index=True,
        )

    st.info(
        "Escribe en el buscador para consultar todas las fechas."
    )
