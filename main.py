import streamlit as st
import json

# Cargar roles desde secrets.toml
roles_data = json.loads(st.secrets["roles_autorizados"]["data"])

# Configuración de la página
st.set_page_config(page_title="Plataforma de Trazabilidad", page_icon="🏥", layout="wide")

# Verificar si el usuario está logueado
if 'user' not in st.session_state:
    # Mostrar mensaje de bienvenida antes del login
    st.title("Bienvenidos a la Plataforma de Trazabilidad de Insumos Médicos")
    st.write("Por favor, inicia sesión con tu cuenta de Google para continuar.")
    
    if st.button("Iniciar sesión con Google"):
        st.login("google")
else:
    # Cuando el usuario esté logueado, cambiamos el título
    email = st.session_state.user["email"]
    
    # Validar que el correo esté en roles_autorizados
    if email not in roles_data:
        st.error("🚫 Acceso denegado. Tu cuenta no está autorizada.")
        st.info(f"📧 Cuenta utilizada: {email}")
        st.stop()

    # Obtener el rol y las funciones del correo autenticado
    rol_info = roles_data[email]
    rol_nombre = rol_info[0]
    rol_nivel = rol_info[1]
    funciones = rol_info[2]
        
    st.title("Plataforma de Trazabilidad")
    st.success(f"Bienvenido {rol_nombre} ({email})")

    # Mostrar las funciones del rol
    st.write(f"**Funciones asignadas:**")
    for funcion in funciones:
        st.write(f"• {funcion}")

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
