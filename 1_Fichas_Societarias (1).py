import os
import sys

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

div[data-testid="stExpander"] { border-radius: 0 !important; border: 1px solid var(--gray-300); background: var(--gray-50); }
div[data-testid="stExpander"] summary { font-weight: 600; }

.stTabs [data-baseweb="tab-list"] { border-bottom: 2px solid var(--ink); gap: 0; }
.stTabs [data-baseweb="tab"] {
    border: 1px solid var(--gray-300);
    border-bottom: none;
    background: var(--gray-50);
    color: var(--gray-600);
    font-weight: 600;
    border-radius: 0 !important;
}
.stTabs [aria-selected="true"] { background: var(--ink) !important; color: var(--paper) !important; }

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

st.title("FICHAS SOCIETARIAS")
st.markdown("Los 8 tipos societarios de la Ley General de Sociedades y la Ley 27.349, con doctrina y jurisprudencia.")
st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

tab_labels = [f'{SOCIEDADES[k]["sigla"] or SOCIEDADES[k]["nombre"][:14]}' for k in ORDEN_TIPOS]
tabs = st.tabs(tab_labels)

for tab, key in zip(tabs, ORDEN_TIPOS):
    d = SOCIEDADES[key]
    with tab:
        st.markdown(
            f'<span class="tag">{d["articulos"]}</span><span class="tag tag-accent">{d["grupo"]}</span>',
            unsafe_allow_html=True,
        )
        st.header(f'{d["nombre"]}  ·  {d["sigla"] or ""}')
        st.write(d["definicion"])

        st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

        with st.expander("RÉGIMEN LEGAL — Socios, responsabilidad, capital y órganos", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="field-label">Socios</div>', unsafe_allow_html=True)
                soc = d["socios"]
                rango = f'Mínimo: {soc["min"]}' + (f' · Máximo: {soc["max"]}' if soc["max"] else " · Sin máximo")
                st.write(rango)
                st.caption(soc["detalle"])

                st.markdown('<div class="field-label">Responsabilidad</div>', unsafe_allow_html=True)
                st.write(d["responsabilidad"])

                st.markdown('<div class="field-label">Capital</div>', unsafe_allow_html=True)
                st.write(f'Mínimo: {d["capital"]["minimo"]}')
                st.write(f'Aportes: {d["capital"]["aportes"]}')

            with col2:
                st.markdown('<div class="field-label">Órganos</div>', unsafe_allow_html=True)
                org = d["organos"]
                st.write(f'Administración: {org["administracion"]}')
                st.write(f'Gobierno: {org["gobierno"]}')
                st.write(f'Fiscalización: {org["fiscalizacion"]}')

                st.markdown('<div class="field-label">Constitución</div>', unsafe_allow_html=True)
                st.write(d["constitucion"])

        with st.expander("VENTAJAS Y DESVENTAJAS"):
            col3, col4 = st.columns(2)
            with col3:
                st.markdown('<div class="field-label">Ventajas</div>', unsafe_allow_html=True)
                for v in d["ventajas"]:
                    st.markdown(f"- {v}")
            with col4:
                st.markdown('<div class="field-label">Desventajas</div>', unsafe_allow_html=True)
                for x in d["desventajas"]:
                    st.markdown(f"- {x}")

        if d.get("debate_doctrinario"):
            with st.expander("DEBATE DOCTRINARIO"):
                st.markdown(d["debate_doctrinario"])

        if d.get("jurisprudencia_clave"):
            with st.expander("JURISPRUDENCIA CLAVE"):
                for caso in d["jurisprudencia_clave"]:
                    st.markdown(f"**{caso['caso']}**")
                    if caso.get("tribunal"):
                        st.caption(caso["tribunal"])
                    st.write(caso["sintesis"])
                    st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

        if d.get("conflictos_frecuentes"):
            with st.expander("CONFLICTOS SOCIETARIOS FRECUENTES"):
                for c in d["conflictos_frecuentes"]:
                    st.markdown(f"- {c}")

        if d.get("inoponibilidad_velo"):
            with st.expander("INOPONIBILIDAD Y VELO SOCIETARIO (ART. 54, 3ER PÁRR. LGS)"):
                st.markdown(d["inoponibilidad_velo"])

        with st.expander("NORMATIVA APLICABLE"):
            for n in d["normativa"]:
                st.markdown(f"- {n}")
