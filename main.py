import streamlit as st
from streamlit_option_menu import option_menu

# Función de login
def login_screen():
    st.title("Bienvenidos a la Plataforma de Trazabilidad de Insumos Médicos")
    st.write("Por favor, inicie sesión con su cuenta de Google para continuar.")
    if st.button("Iniciar sesión con Google"):
        st.login("google")

# Mostrar la pantalla de autenticación
if not st.session_state.get("user"):
    login_screen()
    st.stop()

# Si ya está logueado, mostrar la plataforma
email = st.session_state.user.get("email")

# Mostrar la plataforma
st.title("Plataforma de Trazabilidad de Insumos Médicos")

# Sidebar con el menu de opciones
with st.sidebar:
    menu = option_menu(
        menu_title="Menú Principal",
        options=["Inicio", "Base de Datos", "Mantenimientos", "Gestión de Pasantes", "Reportes"],
        icons=["house", "database", "tools", "person-badge", "file-earmark-text"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "width": "100%"},
            "icon": {"color": "#DC143C", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px", 
                "text-align": "left", 
                "margin": "0px",
                "padding": "15px 20px",
                "width": "100%"
            },
            "nav-link-selected": {"background-color": "#DC143C"},
        }
    )

# Mostrar el contenido según el menú seleccionado
if menu == "Inicio":
    st.write("Bienvenido a la plataforma de trazabilidad. Aquí gestionas los insumos médicos.")
elif menu == "Base de Datos":
    st.write("Aquí podrás consultar la base de datos de insumos médicos.")
elif menu == "Mantenimientos":
    st.write("En este módulo podrás gestionar los mantenimientos de equipos médicos.")
elif menu == "Gestión de Pasantes":
    st.write("Aquí puedes gestionar el estado y las tareas de los pasantes.")
elif menu == "Reportes":
    st.write("En este módulo puedes generar reportes de los insumos médicos y otros datos.")

# Funcionalidad de cierre de sesión
if st.button("Cerrar sesión"):
    st.session_state.clear()
    st.experimental_rerun()
