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

# Generazione HTML del Logo
logo_html = ""
if os.path.exists("logo.jpg"):
    img_b64 = get_img_as_base64("logo.jpg")
    logo_html = f'<img src="data:image/jpeg;base64,{img_b64}" class="logo-img">'
else:
    logo_html = '<div class="logo-placeholder">LOGO MISSING</div>'

# --- 2. CSS AVANZATO (GRID + FLEX ORDER + SPACING) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');

    /* BACKGROUND */
    .stApp {
        background-color: #1a1a1a;
        font-family: 'Inter', sans-serif;
    }
    
    /* NASCONDE HEADER/FOOTER STREAMLIT */
    header, footer { visibility: hidden; }
    .block-container { 
        padding-top: 2rem; 
        max-width: 1400px; 
        margin: 0 auto;
    } 

    /* --- LAYOUT GENERALE (DESKTOP) --- */
    /* Flexbox per le 3 colonne desktop */
    .main-container {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        gap: 40px; 
    }

    /* Wrapper delle colonne */
    .column-wrapper {
        display: flex;
        flex-direction: column;
        width: 32%; 
        gap: 25px; /* Spazio standard tra i box su Desktop */
    }

    /* Allineamento Logo nella Colonna 1 */
    .col-1-align {
        align-items: flex-end; 
    }
    
    .spacer-mid { height: 120px; display: block; }

    /* --- STILE BOX (TAG) --- */
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
        box-sizing: border-box;
    }

    .tag-box:hover {
        border-color: #ff2a2a;
        background-color: #000;
        transform: translateY(-5px);
    }

    .content-layer {
        position: relative; z-index: 2; align-self: flex-start; width: 100%;
    }

    .status-dot {
        height: 8px; width: 8px; background-color: #ff2a2a; 
        border-radius: 50%; margin-bottom: 15px; display: block;
    }

    .tag-title {
        color: #ffffff; font-size: 28px; font-weight: 700;
        text-transform: uppercase; letter-spacing: -1px; line-height: 0.95; margin-bottom: 8px;
    }

    .tag-desc {
        font-size: 12px; color: #999; font-weight: 400; line-height: 1.2; max-width: 80%;
    }

    .big-number {
        position: absolute; bottom: -60px; right: -20px;       
        font-size: 280px; font-weight: 900; color: #1a1a1a;     
        line-height: 1; z-index: 1; letter-spacing: -10px;
        pointer-events: none; text-align: right;  
    }

    /* STILE LOGO */
    .logo-container {
        width: 100%; display: flex; justify-content: flex-end; 
        margin-bottom: 15px;
    }
    .logo-img {
        width: 55%; height: auto; object-fit: contain;
    }
    .logo-placeholder {
        width: 55%; height: 80px; background: #333; color: #555; 
        display: flex; align-items: center; justify-content: center; font-weight: 900;
    }

    /* --- MOBILE OPTIMIZATION (Android/iOS) --- */
    @media only screen and (max-width: 768px) {
        
        .main-container {
            display: flex;
            flex-direction: column;
            gap: 25px; /* Spazio standard tra i box su Mobile */
        }

        /* Scompatta le colonne desktop */
        .column-wrapper {
            display: contents;
        }

        /* --- ORDINE MOBILE PERSONALIZZATO (1-7) --- */
        .mobile-order-logo { order: 0; }
        .mobile-order-1 { order: 1; }
        .mobile-order-2 { order: 2; }
        .mobile-order-3 { order: 3; }
        .mobile-order-4 { order: 4; }
        .mobile-order-5 { order: 5; }
        .mobile-order-6 { order: 6; }
        .mobile-order-7 { order: 7; }

        /* --- SPAZIATURE EXTRA SU MOBILE --- */
        .mobile-gap-large {
            margin-bottom: 50px !important; 
        }

        .spacer-mid { display: none; }

        /* Grafica Mobile */
        .big-number { font-size: 140px; bottom: -30px; right: -10px; }
        .tag-title { font-size: 22px; }
        
        .tag-box {
            width: 100%;
            aspect-ratio: auto;
            min-height: 180px;
        }

        .logo-container { justify-content: flex-end; margin-bottom: 10px; }
        .logo-img { width: 40%; }
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. GENERAZIONE HTML DEI TAG ---
def make_tag_html(number, title, desc, mobile_order_class, extra_class=""):
    return f"""
    <div class="tag-box {mobile_order_class} {extra_class}">
        <div class="content-layer">
            <div class="status-dot"></div>
            <div class="tag-title">{title}</div>
            <div class="tag-desc">{desc}</div>
        </div>
        <div class="big-number">{number}</div>
    </div>
    """

# --- 4. COSTRUZIONE LAYOUT ---

# Tag 1: FREE DCP CHECK (Mobile: 1°)
tag_1 = make_tag_html("1", "FREE DCP<br>CHECK", "Integrity & Hash verification.", "mobile-order-1")

# Tag 2: FREE MASTERING (Mobile: 2°) -> HA SPAZIO EXTRA SOTTO
tag_2 = make_tag_html("2", "FREE<br>MASTERING", "Conforming & Technical Analysis.", "mobile-order-2", "mobile-gap-large")

# Tag 3: FREE IMF PACKAGING (Mobile: 3°)
tag_3 = make_tag_html("3", "FREE IMF<br>PACKAGING", "Netflix / Amazon specs check.", "mobile-order-3")

# Tag 4: COLOR SCIENCE (Mobile: 4°)
tag_4 = make_tag_html("4", "COLOR<br>SCIENCE", "ACES Pipeline & SDR/HDR.", "mobile-order-4")

# Tag 5: QUICK QC DIAGNOSTIC (Mobile: 5°) -> HA SPAZIO EXTRA SOTTO
tag_5 = make_tag_html("5", "QUICK QC<br>DIAGNOSTIC", "Cloud link or File upload check.", "mobile-order-5", "mobile-gap-large")

# Tag 6: DISPLAY CALIBRATION (Mobile: 6°)
tag_6 = make_tag_html("6", "DISPLAY<br>CALIBRATION", "Probe matching & 3D LUTs.", "mobile-order-6")

# Tag 7: CONTACT REQUEST (Mobile: 7°)
tag_7 = make_tag_html("7", "CONTACT<br>REQUEST", "Direct line to engineering.", "mobile-order-7")

# Spacer (Desktop: Col 3)
spacer = '<div class="spacer-mid"></div>'

# HTML FINALE STRUTTURATO
# Nota: Nessuna indentazione a sinistra per evitare che venga letto come codice
full_html = f"""
<div class="main-container">
    
    <div class="column-wrapper col-1-align">
        <div class="logo-container mobile-order-logo">{logo_html}</div>
        <div class="standard-gap"></div>
        {tag_3}
        {tag_7}
    </div>

    <div class="column-wrapper">
        {tag_1}
        {tag_4}
        {tag_6}
    </div>

    <div class="column-wrapper">
        {spacer}
        {tag_2}
        {tag_5}
    </div>

</div>
"""

st.markdown(full_html, unsafe_allow_html=True)
