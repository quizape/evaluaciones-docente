import streamlit as st
import pandas as pd
import unicodedata


st.set_page_config(
    page_title="Evaluaciones y cambios docentes",
    page_icon="📚",
    layout="wide",
)


st.title("📚 Evaluaciones y cambios docentes")
st.caption(
    "Consulta evaluaciones y reemplazos docentes por fecha, "
    "curso, profesor o sala. La información es de solo lectura."
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
                "Profesor": "Alejandro Mondaca",
                "Sala": "34",
            },
            {
                "Bloque": "3.º y 4.º",
                "Curso": "4.º A",
                "Profesor": "Ismael Oyarce",
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
                "Docente": "Héctor Garrido",
                "Reemplaza a": "Alejandro Mondaca",
                "Curso que toma": "1.º C",
                "Sala": "26",
            },
            {
                "Bloque": "3.º",
                "Docente": "María Eliana Astudillo",
                "Reemplaza a": "Alejandro Mondaca",
                "Curso que toma": "1.º B",
                "Sala": "16",
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

    return "".join(
        caracter
        for caracter in texto_nfd
        if unicodedata.category(caracter) != "Mn"
    ).strip().casefold()


# Validación de la estructura de la agenda
for fecha_registro, programacion in agenda.items():
    if not all(
        clave in programacion
        for clave in ("evaluaciones", "cambios")
    ):
        st.error(
            f"Faltan datos obligatorios en {fecha_registro}."
        )
        st.stop()


# Construcción de la lista general para el buscador
registros = []

for fecha_registro, programacion in agenda.items():
    for evaluacion in programacion["evaluaciones"]:
        fila = {
            "Fecha": fecha_registro,
            "Tipo": "Evaluación",
        }
        fila.update(evaluacion)
        registros.append(fila)

    for cambio in programacion["cambios"]:
        fila = {
            "Fecha": fecha_registro,
            "Tipo": "Cambio",
        }
        fila.update(cambio)
        registros.append(fila)


busqueda = st.text_input(
    "🔎 Buscar en todas las fechas",
    placeholder="Ej.: Carlos Gómez, 2.º A, sala 23...",
)


if busqueda.strip():
    termino = normalizar(busqueda)

    resultados = [
        registro
        for registro in registros
        if termino
        in normalizar(
            " ".join(
                str(valor)
                for valor in registro.values()
            )
        )
    ]

    if resultados:
        st.success(
            f"Se encontraron {len(resultados)} coincidencias."
        )

        tabla_resultados = pd.DataFrame(resultados)

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
        [
            "Docentes a evaluar",
            "Cambios",
        ]
    )

    with tab_evaluaciones:
        st.subheader(
            f"Docentes a evaluar — {fecha}"
        )

        tabla_evaluaciones = pd.DataFrame(
            datos["evaluaciones"]
        )

        st.dataframe(
            tabla_evaluaciones,
            use_container_width=True,
            hide_index=True,
        )

    with tab_cambios:
        st.subheader(
            f"Cambios — {fecha}"
        )

        tabla_cambios = pd.DataFrame(
            datos["cambios"]
        )

        st.dataframe(
            tabla_cambios,
            use_container_width=True,
            hide_index=True,
        )

    st.info(
        "Selecciona otra fecha para consultar su programación."
    )
