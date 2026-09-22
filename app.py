import streamlit as st
import pandas as pd

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
                "Sala": "",
            },
            {
                "Bloque": "2.º y 3.º",
                "Curso": "2.º B",
                "Profesor": "Félix Ormázabal",
                "Sala": "",
            },
            {
                "Bloque": "3.º y 4.º",
                "Curso": "2.º A",
                "Profesor": "Fernando Tatter",
                "Sala": "",
            },
        ],
        "cambios": [
            {
                "Bloque": "1.º",
                "Docente": "Jorge Berríos",
                "Reemplaza a": "Cristian Gutierrez",
                "Curso que toma": "2.º D",
                "Sala": "",
            },
            {
                "Bloque": "2.º",
                "Docente": "María Eliana Astudillo",
                "Reemplaza a": "Félix Ormázabal",
                "Curso que toma": "Electivo de 3.º Medio",
                "Sala": "",
            },
            {
                "Bloque": "2.º",
                "Docente": "Marcelo Ortiz",
                "Reemplaza a": "Cristian Gutierrez",
                "Curso que toma": "4.º A",
                "Sala": "",
            },
            {
                "Bloque": "4.º",
                "Docente": "María José Arévalo",
                "Reemplaza a": "Fernando Tatter",
                "Curso que toma": "1.º D",
                "Sala": "",
            },
            {
                "Bloque": "3.º",
                "Docente": "Cristian Gutierrez",
                "Reemplaza a": "Félix Ormázabal",
                "Curso que toma": "Electivo de 4.º Medio",
                "Sala": "",
            },
            {
                "Bloque": "3.º",
                "Docente": "Raquel Vera",
                "Reemplaza a": "Fernando Tatter",
                "Curso que toma": "Electivo de 3.º Medio",
                "Sala": "",
            },
        ],
    },
    "Jueves 01/10": {
        "evaluaciones": [
            {
                "Bloque": "1.º y 2.º",
                "Curso": "2.º A",
                "Profesor": "Sebastián Fuentes",
                "Sala": "",
            },
            {
                "Bloque": "2.º y 3.º",
                "Curso": "1.º C",
                "Profesor": "Alejandro",
                "Sala": "",
            },
            {
                "Bloque": "3.º y 4.º",
                "Curso": "4.º A",
                "Profesor": "Isma",
                "Sala": "",
            },
        ],
        "cambios": [
            {
                "Bloque": "1.º",
                "Docente": "Lissete Caravantes",
                "Reemplaza a": "Sebastián Fuentes",
                "Curso que toma": "4.º E",
                "Sala": "",
            },
            {
                "Bloque": "2.º",
                "Docente": "Francisca Larraín",
                "Reemplaza a": "Sebastián Fuentes",
                "Curso que toma": "1.º D",
                "Sala": "",
            },
            {
                "Bloque": "2.º",
                "Docente": "Alejandro Mondaca",
                "Reemplaza a": "Alejandro",
                "Curso que toma": "1.º C",
                "Sala": "",
            },
            {
                "Bloque": "3.º",
                "Docente": "María Eliana Astudillo",
                "Reemplaza a": "Alejandro",
                "Curso que toma": "1.º B",
                "Sala": "",
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
                "Profesor": "Carlitos",
                "Sala": "",
            },
            {
                "Bloque": "2.º y 3.º",
                "Curso": "2.º A",
                "Profesor": "Ariel Moraga",
                "Sala": "",
            },
            {
                "Bloque": "3.º y 4.º",
                "Curso": "4.º A",
                "Profesor": "Patricio Quinteros",
                "Sala": "",
            },
        ],
        "cambios": [
            {
                "Bloque": "1.º",
                "Docente": "Cristian Gutierrez",
                "Reemplaza a": "Carlitos",
                "Curso que toma": "2.º D",
                "Sala": "",
            },
            {
                "Bloque": "2.º",
                "Docente": "Lissete Caravantes",
                "Reemplaza a": "Carlitos",
                "Curso que toma": "Libre",
                "Sala": "",
            },
            {
                "Bloque": "2.º",
                "Docente": "Marcelo Ortiz",
                "Reemplaza a": "Ariel Moraga",
                "Curso que toma": "Electivo Tercero",
                "Sala": "",
            },
            {
                "Bloque": "3.º",
                "Docente": "Seba",
                "Reemplaza a": "Ariel Moraga",
                "Curso que toma": "1.º C",
                "Sala": "",
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
                "Sala": "",
            },
            {
                "Bloque": "2.º y 3.º",
                "Curso": "2.º B",
                "Profesor": "Franco Gálvez",
                "Sala": "",
            },
            {
                "Bloque": "3.º y 4.º",
                "Curso": "1.º D",
                "Profesor": "Marcelo Ortiz",
                "Sala": "",
            },
        ],
        "cambios": [
            {
                "Bloque": "1.º",
                "Docente": "Francisca Larraín",
                "Reemplaza a": "María José Arévalo",
                "Curso que toma": "1.º A",
                "Sala": "",
            },
            {
                "Bloque": "2.º",
                "Docente": "Ariel Moraga",
