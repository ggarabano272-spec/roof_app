import streamlit as st
from datetime import datetime

# Configuración móvil y pestaña
st.set_page_config(page_title="The Roof Bar App", page_icon="🍸", layout="centered")

# Estilo Premium Dark & Gold
st.markdown("""
    <style>
    .main { background-color: #050505; color: white; }
    .stApp { max-width: 450px; margin: 0 auto; }
    
    /* Estilo de Tarjetas */
    .card {
        background: #111;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 15px;
        border: 1px solid #222;
    }
    .gold-text { color: #bfa100; font-weight: bold; }
    
    /* Botones */
    .stButton>button {
        background: linear-gradient(45deg, #8a6d3b, #bfa100);
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        height: 3em !important;
        width: 100%;
        font-weight: bold !important;
    }
    
    /* Menú Accordion Custom */
    .menu-item { display: flex; justify-content: space-between; border-bottom: 1px solid #222; padding: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: #bfa100; margin-bottom: 0;'>THE ROOF</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>PLAYA DEL CARMEN • EST. 2021</p>", unsafe_allow_html=True)

# SECCIÓN 1: EVENTOS (LINE-UP)
st.write("### 🎧 Line-up de la Semana")
eventos = [
    {"dia": "Hoy", "nombre": "Sunset Session", "dj": "Warmup: El Discípulo", "tag": "Melodic House"},
    {"dia": "Sábado", "nombre": "Peak Time Night", "dj": "Main: Special Guest", "tag": "Techno Vibes"},
]

for ev in eventos:
    with st.container():
        st.markdown(f"""
        <div class="card">
            <span class="gold-text">{ev['dia']}</span>
            <div style="font-size: 18px; font-weight: bold;">{ev['nombre']}</div>
            <div style="color: #888; font-size: 14px;">{ev['dj']} • {ev['tag']}</div>
        </div>
        """, unsafe_allow_html=True)

# SECCIÓN 2: MENÚ DIGITAL
with st.expander("📖 VER MENÚ DE BEBIDAS"):
    st.markdown("""
    <div class="menu-item"><span>Signature Cocktail (The Roof)</span><span class="gold-text">$250</span></div>
    <div class="menu-item"><span>Mezcalita de Maracuyá</span><span class="gold-text">$220</span></div>
    <div class="menu-item"><span>Gin Tonic Premium</span><span class="gold-text">$280</span></div>
    <div class="menu-item"><span>Cerveza Artesanal Local</span><span class="gold-text">$120</span></div>
    <br>
    <p style='font-size: 12px; color: #666;'>*Precios en MXN. Servicio no incluido.</p>
    """, unsafe_allow_html=True)

st.divider()

# SECCIÓN 3: RESERVAS (Tus datos ya están integrados)
st.write("### 📅 Reserva tu Mesa")
with st.container():
    nombre = st.text_input("Nombre para la lista")
    pax = st.number_input("Invitados", min_value=1, max_value=15, value=2)
    
    # Botón dinámico
    if st.button("RESERVAR AHORA"):
        if nombre:
            st.balloons()
            st.success(f"¡Hecho, {nombre}! Solo falta un paso.")
            # Link de reserva que me pediste recordar
            st.link_button("👉 CONFIRMAR EN SORTS.ONE", "https://sorts.one/hCu")
        else:
            st.warning("Por favor, ingresa un nombre.")

# Footer con tu info de DJ
st.markdown("""
    <div style='text-align: center; margin-top: 30px; opacity: 0.5; font-size: 12px;'>
        <p>Calle 8 entre 5ta y 10ma Av.<br>
        Open 18:00 - 01:00</p>
    </div>
""", unsafe_allow_html=True)
