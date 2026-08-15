import os
import sys

import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unidad_1_data import UNIDAD_1  # noqa: E402

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

div[data-testid="stExpander"] { border-radius: 0 !important; border: 1px solid var(--gray-300); background: var(--gray-50); }
div[data-testid="stExpander"] summary { font-weight: 600; }

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
.rule { border-top: 4px solid var(--ink); margin: 1rem 0 1.4rem 0; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.title("UNIDAD 1")
st.markdown("Derecho Comercial: categoría histórica, transformación regulatoria, tecnologías disruptivas y personas jurídicas privadas.")
st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

for tema in UNIDAD_1:
    with st.expander(tema["titulo"], expanded=False):
        st.markdown(f'<span class="tag tag-accent">{tema["articulos"]}</span>', unsafe_allow_html=True)
        st.markdown(tema["contenido"])
