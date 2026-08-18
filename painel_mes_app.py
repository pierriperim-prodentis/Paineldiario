import streamlit as st
import os

st.set_page_config(
    page_title="Painel do Mês - Pródentis/ARP",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove Streamlit UI elements
st.markdown("""
<style>
    .block-container { padding: 0 !important; }
    header { display: none !important; }
    footer { display: none !important; }
    #MainMenu { display: none !important; }
    [data-testid="stToolbar"] { display: none !important; }
    [data-testid="stDecoration"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ── CHAVE SECRETA ──────────────────────────────────────────
CHAVE_SECRETA = "prodentis2026"  # altere aqui se quiser

params = st.query_params
chave_informada = params.get("chave", "")

if chave_informada != CHAVE_SECRETA:
    # Acesso negado
    st.markdown("""
    <style>
    body { margin: 0; }
    .denied {
        display: flex; align-items: center; justify-content: center;
        height: 100vh; background: linear-gradient(135deg, #4A148C, #9C27B0);
        font-family: 'Inter', sans-serif;
    }
    .box {
        background: #fff; border-radius: 16px; padding: 48px 40px;
        text-align: center; max-width: 400px; width: 90%;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    .icon { font-size: 56px; margin-bottom: 16px; }
    .title { font-size: 20px; font-weight: 700; color: #1A0A2E; margin-bottom: 8px; }
    .sub { font-size: 13px; color: #6B5B82; }
    .footer { font-size: 11px; color: #B0A0C0; margin-top: 24px; }
    </style>
    <div class="denied">
      <div class="box">
        <div class="icon">🔒</div>
        <div class="title">Acesso Restrito</div>
        <div class="sub">Você não tem permissão para acessar este dashboard.<br>Verifique o link com o administrador.</div>
        <div class="footer">Pródentis © 2026</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ── ACESSO LIBERADO ─────────────────────────────────────────
base_dir = os.path.dirname(__file__)
possiveis_nomes = ["relatorio.html", "painel_mes.html"]
html_path = None
for nome in possiveis_nomes:
    caminho = os.path.join(base_dir, nome)
    if os.path.exists(caminho):
        html_path = caminho
        break

if html_path is None:
    st.error(f"Arquivo HTML não encontrado. Procurei por: {', '.join(possiveis_nomes)} na pasta do app.")
    st.stop()

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=2200, scrolling=False)
