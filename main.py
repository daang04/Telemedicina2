import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Login", page_icon="🔑", layout="centered")

# Verifica si el usuario está autenticado
user = st.session_state.get("user")

# Si el usuario no está autenticado, mostramos el login
if not user:
    st.title("🔐 Iniciar sesión")
    st.write("Por favor, inicia sesión con tu cuenta de Google para continuar.")
    
    if st.button("Iniciar sesión con Google"):
        st.login("google")
    st.stop()  # Detenemos la ejecución hasta que el usuario se autentique

# Si el usuario está autenticado
email = user.get("email")
st.success(f"Bienvenido {email}!")

# Aquí puedes añadir el contenido de tu app después de que el usuario se haya autenticado
st.write("Acceso concedido, ahora puedes continuar con la app.")

