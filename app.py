import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Evaluaciones y cambios docentes",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Evaluaciones y cambios docentes")
st.caption("Aplicación de consulta. Los datos no se pueden editar desde la interfaz.")

agenda = {
    "Lunes 28": {
        "evaluaciones": [
            {"Bloque": "1.º y 2.º", "Curso": "3.º C", "Profesor": "Cristian"},
            {"Bloque": "2.º y 3.º", "Curso": "2.º B", "Profesor": "Félix"},
            {"Bloque": "3.º y 4.º", "Curso": "2.º A", "Profesor": "Fernando"},
        ],
        "cambios": [
            {"Bloque": "1.º", "Docente": "Berríos", "Reemplaza a": "Cristian", "Curso que toma": "2.º D"},
            {"Bloque": "2.º", "Docente": "María Eliana", "Reemplaza a": "Félix", "Curso que toma": "Electivo de 3.º Medio"},
            {"Bloque": "2.º", "Docente": "Marcelo", "Reemplaza a": "Cristian", "Curso que toma": "4.º A"},
            {"Bloque": "4.º", "Docente": "Pepa", "Reemplaza a": "Fernando", "Curso que toma": "1.º D"},
            {"Bloque": "3.º", "Docente": "Cristian", "Reemplaza a": "Félix", "Curso que toma": "Electivo de 4.º Medio"},
            {"Bloque": "3.º", "Docente": "Raquel", "Reemplaza a": "Fernando", "Curso que toma": "Electivo de 3.º Medio"},
        ],
    },
    "Jueves 01/10": {
        "evaluaciones": [
            {"Bloque": "1.º y 2.º", "Curso": "2.º A", "Profesor": "Sebita"},
            {"Bloque": "2.º y 3.º", "Curso": "1.º C", "Profesor": "Alejandro"},
            {"Bloque": "3.º y 4.º", "Curso": "4.º A", "Profesor": "Isma"},
        ],
        "cambios": [
            {"Bloque": "1.º", "Docente": "Caravantes", "Reemplaza a": "Sebita", "Curso que toma": "4.º E"},
            {"Bloque": "2.º", "Docente": "Francisca", "Reemplaza a": "Sebita", "Curso que toma": "1.º D"},
            {"Bloque": "2.º", "Docente": "Mondaca", "Reemplaza a": "Alejandro", "Curso que toma": "1.º C"},
            {"Bloque": "3.º", "Docente": "María Eliana", "Reemplaza a": "Alejandro", "Curso que toma": "1.º B"},
            {"Bloque": "3.º", "Docente": "Ismael", "Reemplaza a": "Isma", "Curso que toma": "4.º A"},
            {"Bloque": "4.º", "Docente": "Electivo", "Reemplaza a": "Isma", "Curso que toma": "Libre"},
        ],
    },
    "Viernes 02/10": {
        "evaluaciones": [
            {"Bloque": "1.º y 2.º", "Curso": "2.º B", "Profesor": "Carlitos"},
            {"Bloque": "2.º y 3.º", "Curso": "2.º A", "Profesor": "Ariel"},
            {"Bloque": "3.º y 4.º", "Curso": "4.º A", "Profesor": "Pato"},
        ],
        "cambios": [
            {"Bloque": "1.º", "Docente": "Cristian", "Reemplaza a": "Carlitos", "Curso que toma": "2.º D"},
            {"Bloque": "2.º", "Docente": "Caravantes", "Reemplaza a": "Carlitos", "Curso que toma": "Libre"},
            {"Bloque": "2.º", "Docente": "Marcelo", "Reemplaza a": "Ariel", "Curso que toma": "Electivo Tercero"},
            {"Bloque": "3.º", "Docente": "Seba", "Reemplaza a": "Ariel", "Curso que toma": "1.º C"},
            {"Bloque": "3.º", "Docente": "Electivo", "Reemplaza a": "Pato", "Curso que toma": "Libre"},
            {"Bloque": "4.º", "Docente": "Electivo", "Reemplaza a": "Pato", "Curso que toma": "Libre"},
        ],
    },
    "Lunes 05/10": {
        "evaluaciones": [
            {"Bloque": "1.º y 2.º", "Curso": "2.º C", "Profesor": "Pepa"},
            {"Bloque": "2.º y 3.º", "Curso": "2.º B", "Profesor": "Franco"},
            {"Bloque": "3.º y 4.º", "Curso": "1.º D", "Profesor": "Marcelo"},
        ],
        "cambios": [
            {"Bloque": "1.º", "Docente": "Fran", "Reemplaza a": "Pepa", "Curso que toma": "1.º A"},
            {"Bloque": "2.º", "Docente": "Ariel", "Reemplaza a": "Pepa", "Curso que toma": "1.º D"},
            {"Bloque": "2.º", "Docente": "María Eliana", "Reemplaza a": "Franco", "Curso que toma": "4.º B"},
            {"Bloque": "3.º", "Docente": "Cristian", "Reemplaza a": "Franco", "Curso que toma": "1.º C"},
            {"Bloque": "3.º", "Docente": "Alfredo", "Reemplaza a": "Marcelo", "Curso que toma": "Libre"},
            {"Bloque": "4.º", "Docente": "Fernando", "Reemplaza a": "Marcelo", "Curso que toma": "3.º D (45 min) y 3.º C (45 min)"},
        ],
    },
}

fecha = st.selectbox("Selecciona una fecha", list(agenda.keys()))
datos = agenda[fecha]

tab_evaluaciones, tab_cambios = st.tabs(["Docentes a evaluar", "Cambios"])

with tab_evaluaciones:
    st.subheader(f"Docentes a evaluar — {fecha}")
    st.dataframe(
        pd.DataFrame(datos["evaluaciones"]),
        use_container_width=True,
        hide_index=True,
    )

with tab_cambios:
    st.subheader(f"Cambios — {fecha}")
    st.dataframe(
        pd.DataFrame(datos["cambios"]),
        use_container_width=True,
        hide_index=True,
    )

st.info("Selecciona otra fecha para consultar su programación.")
