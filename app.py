import streamlit as st
import os
import base64

# --- 1. CONFIGURAZIONE ---
st.set_page_config(
    page_title="TANGO POST",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- FUNZIONE PER CARICARE IMMAGINE LOCALE IN BASE64 ---
def get_img_as_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Tenta di caricare il logo se esiste
logo_html = ""
if os.path.exists("logo.jpg"):
    img_b64 = get_img_as_base64("logo.jpg")
    # Logo ridotto (width: 55%) come richiesto
    logo_html = f'<img src="data:image/jpeg;base64,{img_b64}" class="logo-img">'
else:
    # Fallback
    logo_html = '<div class="logo-placeholder">LOGO.JPG MISSING</div>'

# --- 2. CSS "MACRO TYPOGRAPHY" & LAYOUT ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');

    /* BACKGROUND - Antracite scuro */
    .stApp {
        background-color: #1a1a1a;
        font-family: 'Inter', sans-serif;
    }
    
    /* RESET STANDARD STREAMLIT */
    header, footer { visibility: hidden; }
    .block-container { 
        padding-top: 2rem; 
        max-width: 1400px; 
        margin: 0 auto;
    } 

    /* --- TITOLO E HEADER (COLONNA 1) --- */
    
    .header-wrapper {
        width: 100%;
        max-width: 350px; 
        display: flex;
        flex-direction: column;
        align-items: flex-end; /* MODIFICA: Allinea il logo a DESTRA */
    }

    /* 1. LOGO IMMAGINE - RIDOTTO */
    .logo-img {
        width: 55%;        
        height: auto;
        display: block;
        margin-bottom: 15px; 
        object-fit: contain;
    }
    
    .logo-placeholder {
        width: 55%; height: 80px; background: #333; color: #555; 
        display: flex; align-items: center; justify-content: center; 
        font-weight: 900; margin-bottom: 15px;
    }

    /* SPAZIATURA STANDARD VERTICALE */
    .standard-gap { height: 40px; display: block; }

    /* --- LA CASSA (TAG) --- */
    .tag-box {
        background-color: #0a0a0a; 
        border: 1px solid #333;
        aspect-ratio: 1 / 1; 
        position: relative;
        overflow: hidden; 
        transition: all 0.3s ease;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        padding: 25px;
        margin-bottom: 25px;
    }

    .tag-box:hover {
        border-color: #ff2a2a;
        background-color: #000;
        transform: translateY(-5px);
    }

    /* CONTENT LAYER */
    .content-layer {
        position: relative;
        z-index: 2; 
        align-self: flex-start; 
        width: 100%;
    }

    .status-dot {
        height: 8px; width: 8px; 
        background-color: #ff2a2a; 
        border-radius: 50%; 
        margin-bottom: 15px; 
        display: block;
    }

    .tag-title {
        color: #ffffff;
        font-size: 28px; 
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: -1px;
        line-height: 0.95;
        margin-bottom: 8px;
    }

    .tag-desc {
        font-size: 12px;
        color: #999;
        font-weight: 400;
        line-height: 1.2;
        max-width: 80%; 
    }

    /* IL NUMERO (Basso Destra) */
    .big-number {
        position: absolute;
        bottom: -60px;      
        right: -20px;       
        font-size: 280px;   
        font-weight: 900;
        color: #1a1a1a;     
        line-height: 1;
        z-index: 1;
        letter-spacing: -10px;
        pointer-events: none;
        text-align: right;  
    }

    /* SPACER PER COLONNE */
    .spacer-mid { height: 120px; }

    </style>
""", unsafe_allow_html=True)

# --- 3. FUNZIONE DRAW ---
def draw_tag(number, title, desc):
    return f"""
    <div class="tag-box">
        <div class="content-layer">
            <div class="status-dot"></div>
            <div class="tag-title">{title}</div>
            <div class="tag-desc">{desc}</div>
        </div>
        <div class="big-number">{number}</div>
    </div>
    """

# --- 4. LAYOUT ---
c1, c2, c3 = st.columns(3, gap="large")

# --- COLONNA 1 (SX) ---
with c1:
    # BLOCCO SOLO LOGO (Allineato a destra via CSS)
    st.markdown(f"""
    <div class="header-wrapper">
        {logo_html}
    </div>
    <div class="standard-gap"></div>
    """, unsafe_allow_html=True)

    # TAG 3 (Spostato qui al posto dell'1)
    st.markdown(draw_tag("3", "FREE IMF<br>PACKAGING", "Netflix / Amazon specs check."), unsafe_allow_html=True)
    
    # TAG 6 (Spostato qui al posto del 4)
    st.markdown(draw_tag("6", "CONTACT<br>REQUEST", "Direct line to engineering."), unsafe_allow_html=True)


# --- COLONNA 2 (CENTRO) ---
with c2:
    # TAG 1 (Spostato qui al posto del 2)
    st.markdown(draw_tag("1", "FREE DCP<br>CHECK", "Integrity & Hash verification."), unsafe_allow_html=True)
    
    # TAG 4 (Spostato qui al posto del 5)
    st.markdown(draw_tag("4", "COLOR<br>SCIENCE", "ACES Pipeline & SDR/HDR."), unsafe_allow_html=True)
    
    # TAG 7 (Resta qui)
    st.markdown(draw_tag("7", "DISPLAY<br>CALIBRATION", "Probe matching & 3D LUTs."), unsafe_allow_html=True)


# --- COLONNA 3 (DX) ---
with c3:
    # Spacer
    st.markdown('<div class="spacer-mid"></div>', unsafe_allow_html=True)

    # TAG 2 (Spostato qui al posto del 3)
    st.markdown(draw_tag("2", "FREE<br>MASTERING", "Conforming & Technical Analysis."), unsafe_allow_html=True)

    # TAG 5 (Spostato qui al posto del 6)
    st.markdown(draw_tag("5", "QUICK QC<br>DIAGNOSTIC", "Cloud link or File upload check."), unsafe_allow_html=True)
