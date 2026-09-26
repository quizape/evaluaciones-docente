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
