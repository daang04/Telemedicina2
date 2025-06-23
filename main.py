import streamlit as st

# Cargar el correo permitido desde secrets.toml
allowed_email = st.secrets["access"]["allowed_email"]

# Configuración de la página
st.set_page_config(page_title="Plataforma de Trazabilidad", page_icon="🏥", layout="centered")

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
    
    # Validar que el correo sea el permitido desde secrets.toml
    if email != allowed_email:
        st.error("🚫 Acceso denegado. Tu cuenta no está autorizada.")
        st.info(f"📧 Cuenta utilizada: {email}")
        st.stop()

    st.title("Plataforma de Trazabilidad")

    st.success(f"Bienvenido {email}!")
    
    # Aquí puedes agregar el contenido de tu plataforma de trazabilidad
    st.write("Contenido de la Plataforma de Trazabilidad...")
    
    # Funcionalidad de cierre de sesión
    if st.button("Cerrar sesión"):
        st.session_state.clear()
        st.experimental_rerun()
