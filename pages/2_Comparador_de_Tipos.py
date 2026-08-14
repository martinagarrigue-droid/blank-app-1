import os
import sys

import pandas as pd
import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sociedades_data import SOCIEDADES, ORDEN_TIPOS  # noqa: E402

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

.rule { border-top: 4px solid var(--ink); margin: 1rem 0 1.4rem 0; }

.field-label {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--gray-600);
    margin-bottom: 0.1rem;
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.title("COMPARADOR DE TIPOS SOCIETARIOS")
st.markdown("Filtrá y compará los distintos tipos societarios según tus criterios.")
st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

grupos_disponibles = sorted(set(d["grupo"] for d in SOCIEDADES.values()))
filtro_grupo = st.multiselect("Filtrar por grupo societario", grupos_disponibles, default=grupos_disponibles)

filas = []
for key in ORDEN_TIPOS:
    d = SOCIEDADES[key]
    if d["grupo"] not in filtro_grupo:
        continue
    filas.append(
        {
            "Tipo": f'{d["nombre"]} ({d["sigla"]})' if d["sigla"] else d["nombre"],
            "Grupo": d["grupo"],
            "Socios (mín-máx)": f'{d["socios"]["min"]}–{d["socios"]["max"] or "∞"}',
            "Responsabilidad": d["responsabilidad"],
            "Capital mínimo": d["capital"]["minimo"],
            "Administración": d["organos"]["administracion"],
            "Gobierno": d["organos"]["gobierno"],
            "Artículos": d["articulos"],
        }
    )

df = pd.DataFrame(filas)
st.dataframe(df, use_container_width=True, hide_index=True)

st.markdown('<div class="rule"></div>', unsafe_allow_html=True)
st.subheader("COMPARACIÓN RÁPIDA UNO A UNO")

col1, col2 = st.columns(2)
nombres = {k: SOCIEDADES[k]["nombre"] for k in ORDEN_TIPOS}
with col1:
    tipo_a = st.selectbox("Tipo A", ORDEN_TIPOS, format_func=lambda k: nombres[k], index=0)
with col2:
    tipo_b = st.selectbox("Tipo B", ORDEN_TIPOS, format_func=lambda k: nombres[k], index=min(1, len(ORDEN_TIPOS) - 1))

da, db = SOCIEDADES[tipo_a], SOCIEDADES[tipo_b]
campos = [
    ("Responsabilidad", "responsabilidad"),
    ("Capital mínimo", lambda d: d["capital"]["minimo"]),
    ("Administración", lambda d: d["organos"]["administracion"]),
    ("Gobierno", lambda d: d["organos"]["gobierno"]),
    ("Fiscalización", lambda d: d["organos"]["fiscalizacion"]),
]
ca, cb = st.columns(2)
for label, accessor in campos:
    val_a = accessor(da) if callable(accessor) else da[accessor]
    val_b = accessor(db) if callable(accessor) else db[accessor]
    ca.markdown(f'<div class="field-label">{label} — {da["nombre"]}</div>', unsafe_allow_html=True)
    ca.write(val_a)
    cb.markdown(f'<div class="field-label">{label} — {db["nombre"]}</div>', unsafe_allow_html=True)
    cb.write(val_b)
