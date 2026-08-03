import streamlit as st

st.set_page_config(
    page_title="Sociedades AR",
    page_icon="§",
    layout="wide",
    initial_sidebar_state="expanded",
)

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', -apple-system, sans-serif !important; }

:root {
    --ink: #0a0a0a;
    --paper: #ffffff;
    --gray-50: #fafafa;
    --gray-200: #e5e5e5;
    --gray-300: #d4d4d4;
    --gray-600: #525252;
    --accent: #5c1a25;
}

.stApp { background: var(--paper); color: var(--ink); }

h1, h2, h3, h4 { font-weight: 800; letter-spacing: -0.02em; color: var(--ink); }

hr { border-color: var(--gray-300); }

section[data-testid="stSidebar"] {
    background: var(--gray-50);
    border-right: 1px solid var(--gray-300);
}
section[data-testid="stSidebar"] a { color: var(--ink) !important; font-weight: 500; }
section[data-testid="stSidebar"] a[aria-current="page"] {
    color: var(--accent) !important;
    font-weight: 700;
    border-left: 3px solid var(--accent);
}

div[data-testid="stExpander"], .stButton>button, .stTextInput>div>div>input {
    border-radius: 0 !important;
}

div[data-testid="stExpander"] {
    border: 1px solid var(--gray-300);
    background: var(--gray-50);
}

.stButton>button {
    background: var(--ink);
    color: var(--paper);
    border: 1px solid var(--ink);
    font-weight: 600;
}
.stButton>button:hover { background: var(--accent); border-color: var(--accent); color: var(--paper); }

a, .stMarkdown a { color: var(--accent) !important; }

.tag {
    display: inline-block;
    border: 1px solid var(--ink);
    padding: 2px 10px;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-right: 6px;
}
.tag-accent { border-color: var(--accent); color: var(--accent); }

.rule { border-top: 4px solid var(--ink); margin: 1.4rem 0; }

.module-box {
    border: 1px solid var(--gray-300);
    padding: 1.1rem 1.2rem;
    background: var(--gray-50);
    height: 100%;
}
.module-box h4 { margin-bottom: 0.3rem; }
.module-box p { color: var(--gray-600); font-size: 0.92rem; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<div class="tag tag-accent">CCCN · LGS 19.550 · LEY 27.349</div>', unsafe_allow_html=True)
st.title("SOCIEDADES CIVILES Y COMERCIALES EN ARGENTINA")
st.markdown("Plataforma de estudio jurídico — nivel universitario y profesional. Régimen legal, doctrina y jurisprudencia.")
st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

st.subheader("MÓDULOS")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """<div class="module-box">
        <h4>01 · FICHAS SOCIETARIAS</h4>
        <p>Los 8 tipos de la LGS: régimen legal, doctrina y jurisprudencia clave.</p>
        </div>""",
        unsafe_allow_html=True,
    )
    st.page_link("pages/1_Fichas_Societarias.py", label="Ingresar →", icon=None)

with col2:
    st.markdown(
        """<div class="module-box">
        <h4>02 · EN CONSTRUCCIÓN</h4>
        <p>Marco general, comparador, wizard, quiz y buscador — próximos módulos.</p>
        </div>""",
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """<div class="module-box">
        <h4>03 · EN CONSTRUCCIÓN</h4>
        <p>Reservado para futuros módulos.</p>
        </div>""",
        unsafe_allow_html=True,
    )
