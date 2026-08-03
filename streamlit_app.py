# -*- coding: utf-8 -*-
"""
Sociedades en Argentina — App interactiva sobre sociedades civiles y
comerciales según el CCCN, la Ley General de Sociedades (19.550) y la
Ley 27.349 (SAS).

Nivel: universitario / profesional.
"""

import random

import pandas as pd
import streamlit as st

from data.sociedades_data import SOCIEDADES, ORDEN_TIPOS, GRUPOS
from data.general_data import MARCO_GENERAL
from data.quiz_data import QUIZ
from data.wizard_data import WIZARD_PREGUNTAS, DISCLAIMER_WIZARD

# --------------------------------------------------------------------------
# Configuración general de la página
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="Sociedades en Argentina | CCCN & LGS",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------------------------------
# Estilos
# --------------------------------------------------------------------------
CUSTOM_CSS = """
<style>
:root {
    --acc: #7c3aed;
    --acc-soft: #ede9fe;
    --ink: #1e1b2e;
}
html, body, [class*="css"]  {
    font-family: "Source Sans Pro", "Segoe UI", sans-serif;
}
h1, h2, h3 {
    color: var(--ink);
}
.hero {
    background: linear-gradient(135deg, #4c1d95 0%, #7c3aed 55%, #a78bfa 100%);
    padding: 2.2rem 2.4rem;
    border-radius: 18px;
    color: white;
    margin-bottom: 1.4rem;
}
.hero h1 {
    color: white;
    margin-bottom: 0.3rem;
    font-size: 2.1rem;
}
.hero p {
    color: #ede9fe;
    font-size: 1.02rem;
    margin-bottom: 0;
}
.badge {
    display: inline-block;
    background: var(--acc-soft);
    color: #4c1d95;
    border-radius: 999px;
    padding: 0.15rem 0.75rem;
    font-size: 0.8rem;
    font-weight: 600;
    margin-right: 0.4rem;
    margin-bottom: 0.3rem;
}
.card {
    border: 1px solid #e5e0f5;
    border-radius: 14px;
    padding: 1.1rem 1.3rem;
    background: #ffffff;
    margin-bottom: 0.9rem;
}
.article-tag {
    background: #f3f0fb;
    color: #4c1d95;
    border-left: 4px solid var(--acc);
    padding: 0.5rem 0.8rem;
    border-radius: 6px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 0.6rem;
    display: inline-block;
}
.disclaimer {
    background: #fff7ed;
    border-left: 4px solid #f59e0b;
    padding: 0.8rem 1rem;
    border-radius: 8px;
    font-size: 0.9rem;
    color: #7c2d12;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --------------------------------------------------------------------------
# Sidebar / navegación
# --------------------------------------------------------------------------
st.sidebar.markdown("## ⚖️ Sociedades AR")
st.sidebar.caption("CCCN · Ley General de Sociedades · Ley 27.349 (SAS)")

SECCIONES = [
    "🏠 Inicio",
    "📚 Marco general",
    "📊 Comparador de tipos",
    "🗂️ Fichas por tipo societario",
    "🧭 Wizard: ¿qué sociedad me conviene?",
    "❓ Autoevaluación (Quiz)",
    "🔍 Buscador de artículos",
]
seccion = st.sidebar.radio("Navegación", SECCIONES, label_visibility="collapsed")

st.sidebar.divider()
st.sidebar.caption(
    "⚠️ Contenido con fines educativos. No constituye asesoramiento "
    "jurídico para un caso concreto. Verificá siempre el texto vigente "
    "en el [Sistema Argentino de Información Jurídica (SAIJ)](http://www.saij.gob.ar/)."
)

# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def hero(title, subtitle):
    st.markdown(
        f"""<div class="hero"><h1>{title}</h1><p>{subtitle}</p></div>""",
        unsafe_allow_html=True,
    )


def ficha_societaria(key, data):
    st.markdown(f'<span class="article-tag">{data["articulos"]}</span>', unsafe_allow_html=True)
    st.subheader(f'{data["nombre"]}  ·  {data["sigla"] or ""}')
    st.markdown(f'<span class="badge">{data["grupo"]}</span>', unsafe_allow_html=True)
    st.write(data["definicion"])

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**👥 Socios**")
        soc = data["socios"]
        rango = f'Mínimo: {soc["min"]}' + (f' · Máximo: {soc["max"]}' if soc["max"] else " · Sin máximo")
        st.write(rango)
        st.caption(soc["detalle"])

        st.markdown("**🛡️ Responsabilidad**")
        st.write(data["responsabilidad"])

        st.markdown("**💰 Capital**")
        st.write(f'*Mínimo:* {data["capital"]["minimo"]}')
        st.write(f'*Aportes:* {data["capital"]["aportes"]}')

    with col2:
        st.markdown("**🏛️ Órganos**")
        org = data["organos"]
        st.write(f'*Administración:* {org["administracion"]}')
        st.write(f'*Gobierno:* {org["gobierno"]}')
        st.write(f'*Fiscalización:* {org["fiscalizacion"]}')

        st.markdown("**📝 Constitución**")
        st.write(data["constitucion"])

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("**✅ Ventajas**")
        for v in data["ventajas"]:
            st.markdown(f"- {v}")
    with col4:
        st.markdown("**⚠️ Desventajas**")
        for d in data["desventajas"]:
            st.markdown(f"- {d}")

    st.markdown("**⚖️ Normativa aplicable**")
    for n in data["normativa"]:
        st.markdown(f"- {n}")


# --------------------------------------------------------------------------
# SECCIÓN: INICIO
# --------------------------------------------------------------------------
if seccion == "🏠 Inicio":
    hero(
        "Sociedades Civiles y Comerciales en Argentina",
        "Una guía interactiva basada en el Código Civil y Comercial de la Nación, "
        "la Ley General de Sociedades (19.550) y la Ley 27.349 (SAS), pensada para "
        "estudio universitario y práctica profesional.",
    )

    st.info(
        "**Punto de partida clave:** desde la unificación de 2015 (Ley 26.994), la "
        "categoría autónoma de 'sociedad civil' **desapareció**. Hoy toda sociedad se "
        "rige por la Ley General de Sociedades, adoptando un tipo previsto o quedando "
        "en el régimen residual de la Sección IV. Explorá la sección **Marco general** "
        "para entender este cambio en profundidad."
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Tipos societarios cubiertos", len(SOCIEDADES))
    c2.metric("Temas de marco general", len(MARCO_GENERAL))
    c3.metric("Preguntas de autoevaluación", len(QUIZ))
    c4.metric("Normas centrales", "CCCN · LGS · Ley 27.349")

    st.markdown("### 🗺️ Cómo recorrer la app")
    cols = st.columns(3)
    tarjetas = [
        ("📚 Marco general", "Personalidad jurídica, contrato de sociedad, responsabilidad, disolución, transformación."),
        ("📊 Comparador", "Tabla filtrable para contrastar todos los tipos societarios lado a lado."),
        ("🗂️ Fichas por tipo", "Desarrollo completo de cada tipo: SRL, SA, SAS, Colectiva, Comanditas, Sección IV, etc."),
        ("🧭 Wizard", "Respondé preguntas y recibí una recomendación razonada de tipo societario."),
        ("❓ Quiz", "Autoevaluación con explicación normativa de cada respuesta."),
        ("🔍 Buscador", "Encontrá rápido en qué tema o tipo societario se trata un artículo o concepto."),
    ]
    for i, (t, d) in enumerate(tarjetas):
        with cols[i % 3]:
            st.markdown(f'<div class="card"><b>{t}</b><br><span style="font-size:0.9rem;color:#555">{d}</span></div>', unsafe_allow_html=True)

    st.markdown("### 🧬 Línea de tiempo normativa")
    st.markdown(
        """
- **1972** — Sanción de la Ley 19.550 (Ley de Sociedades Comerciales).
- **1984** — Texto ordenado de la Ley 19.550.
- **2015 (1° ago.)** — Entrada en vigencia del CCCN (Ley 26.994): se deroga la sociedad civil, se renombra la LGS y se crean la SAU y la Sección IV.
- **2017** — Ley 27.349: crea la SAS y el marco de "Emprendedores".
        """
    )

# --------------------------------------------------------------------------
# SECCIÓN: MARCO GENERAL
# --------------------------------------------------------------------------
elif seccion == "📚 Marco general":
    hero("Marco General", "Los conceptos comunes a toda sociedad, antes de entrar en cada tipo particular.")

    for tema in MARCO_GENERAL:
        with st.expander(tema["titulo"], expanded=False):
            st.markdown(f'<span class="article-tag">{tema["articulos"]}</span>', unsafe_allow_html=True)
            st.markdown(tema["contenido"])

# --------------------------------------------------------------------------
# SECCIÓN: COMPARADOR
# --------------------------------------------------------------------------
elif seccion == "📊 Comparador de tipos":
    hero("Comparador de Tipos Societarios", "Filtrá y compará los distintos tipos según tus criterios.")

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

    st.markdown("### 📎 Comparación rápida uno a uno")
    col1, col2 = st.columns(2)
    nombres = {k: SOCIEDADES[k]["nombre"] for k in ORDEN_TIPOS}
    with col1:
        tipo_a = st.selectbox("Tipo A", ORDEN_TIPOS, format_func=lambda k: nombres[k], index=4)
    with col2:
        tipo_b = st.selectbox("Tipo B", ORDEN_TIPOS, format_func=lambda k: nombres[k], index=5)

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
        ca.markdown(f"**{label} — {da['nombre']}**")
        ca.write(val_a)
        cb.markdown(f"**{label} — {db['nombre']}**")
        cb.write(val_b)

# --------------------------------------------------------------------------
# SECCIÓN: FICHAS POR TIPO
# --------------------------------------------------------------------------
elif seccion == "🗂️ Fichas por tipo societario":
    hero("Fichas por Tipo Societario", "Desarrollo completo de cada tipo previsto en la LGS y en la Ley 27.349.")

    nombres_tabs = [f'{SOCIEDADES[k]["sigla"] or SOCIEDADES[k]["nombre"][:12]}' for k in ORDEN_TIPOS]
    tabs = st.tabs(nombres_tabs)
    for tab, key in zip(tabs, ORDEN_TIPOS):
        with tab:
            ficha_societaria(key, SOCIEDADES[key])

# --------------------------------------------------------------------------
# SECCIÓN: WIZARD
# --------------------------------------------------------------------------
elif seccion == "🧭 Wizard: ¿qué sociedad me conviene?":
    hero("¿Qué tipo societario me conviene?", "Respondé estas preguntas para recibir una recomendación razonada.")
    st.markdown(f'<div class="disclaimer">{DISCLAIMER_WIZARD}</div>', unsafe_allow_html=True)
    st.write("")

    respuestas = {}
    with st.form("wizard_form"):
        for p in WIZARD_PREGUNTAS:
            opciones_texto = [o["texto"] for o in p["opciones"]]
            respuestas[p["id"]] = st.radio(p["pregunta"], opciones_texto, key=p["id"])
        enviado = st.form_submit_button("🔎 Ver recomendación")

    if enviado:
        puntajes = {k: 0 for k in SOCIEDADES}
        for p in WIZARD_PREGUNTAS:
            elegido = respuestas[p["id"]]
            opcion = next(o for o in p["opciones"] if o["texto"] == elegido)
            for tipo, pts in opcion["puntajes"].items():
                puntajes[tipo] += pts

        ranking = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
        top = [t for t in ranking if t[1] > 0][:3]

        st.markdown("### 🏆 Resultado")
        if not top:
            st.warning("No se pudo determinar una recomendación; revisá tus respuestas.")
        else:
            medallas = ["🥇", "🥈", "🥉"]
            for i, (key, pts) in enumerate(top):
                d = SOCIEDADES[key]
                with st.container():
                    st.markdown(
                        f'<div class="card"><b>{medallas[i]} {d["nombre"]} ({d["sigla"] or ""})</b> '
                        f'— puntaje de afinidad: {pts}<br>'
                        f'<span style="font-size:0.9rem;color:#555">{d["definicion"]}</span></div>',
                        unsafe_allow_html=True,
                    )
            st.caption(
                "Consultá la ficha completa del tipo recomendado en la sección "
                "'🗂️ Fichas por tipo societario' para ver responsabilidad, capital, "
                "órganos y normativa aplicable."
            )

# --------------------------------------------------------------------------
# SECCIÓN: QUIZ
# --------------------------------------------------------------------------
elif seccion == "❓ Autoevaluación (Quiz)":
    hero("Autoevaluación", "Poné a prueba tus conocimientos sobre sociedades civiles y comerciales.")

    if "quiz_orden" not in st.session_state:
        st.session_state.quiz_orden = random.sample(range(len(QUIZ)), len(QUIZ))
        st.session_state.quiz_idx = 0
        st.session_state.quiz_score = 0
        st.session_state.quiz_respondida = False

    temas_disponibles = sorted(set(q["tema"] for q in QUIZ))
    with st.sidebar:
        pass

    colf1, colf2 = st.columns([3, 1])
    with colf2:
        if st.button("🔄 Reiniciar quiz"):
            st.session_state.quiz_orden = random.sample(range(len(QUIZ)), len(QUIZ))
            st.session_state.quiz_idx = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_respondida = False
            st.rerun()

    idx = st.session_state.quiz_idx
    total = len(QUIZ)

    if idx >= total:
        st.success(f"🎉 ¡Completaste el quiz! Puntaje final: {st.session_state.quiz_score} / {total}")
        pct = st.session_state.quiz_score / total
        if pct >= 0.8:
            st.balloons()
            st.write("Excelente dominio del tema. 🏆")
        elif pct >= 0.5:
            st.write("Buen nivel, pero repasá los temas donde fallaste. 📖")
        else:
            st.write("Te recomendamos repasar el 'Marco general' y las 'Fichas por tipo societario' antes de reintentar. 📚")
    else:
        pregunta_idx = st.session_state.quiz_orden[idx]
        q = QUIZ[pregunta_idx]

        st.progress(idx / total, text=f"Pregunta {idx + 1} de {total}")
        st.markdown(f'<span class="badge">{q["tema"]}</span>', unsafe_allow_html=True)
        st.markdown(f"#### {q['pregunta']}")

        elegido = st.radio("Elegí una opción:", q["opciones"], key=f"quiz_{idx}", index=None)

        if st.button("Confirmar respuesta", disabled=(elegido is None)):
            st.session_state.quiz_respondida = True
            st.session_state.quiz_correcta = q["opciones"].index(elegido) == q["correcta"]
            if st.session_state.quiz_correcta:
                st.session_state.quiz_score += 1

        if st.session_state.get("quiz_respondida"):
            if st.session_state.quiz_correcta:
                st.success("✅ ¡Correcto!")
            else:
                st.error(f"❌ Incorrecto. La respuesta correcta era: **{q['opciones'][q['correcta']]}**")
            st.info(f"📖 {q['explicacion']}")

            if st.button("Siguiente pregunta ➡️"):
                st.session_state.quiz_idx += 1
                st.session_state.quiz_respondida = False
                st.rerun()

# --------------------------------------------------------------------------
# SECCIÓN: BUSCADOR
# --------------------------------------------------------------------------
elif seccion == "🔍 Buscador de artículos":
    hero("Buscador", "Buscá por palabra clave, número de artículo o concepto en toda la app.")

    query = st.text_input("🔎 Escribí un término (ej: 'comanditario', 'art. 54', 'affectio societatis', 'SAS')")

    if query:
        q_lower = query.lower()
        resultados = []

        # Buscar en tipos societarios
        for key in ORDEN_TIPOS:
            d = SOCIEDADES[key]
            bloque_texto = " ".join(
                [
                    d["nombre"], d["sigla"] or "", d["articulos"], d["definicion"],
                    d["constitucion"], d["responsabilidad"],
                    str(d["capital"]), str(d["organos"]),
                    " ".join(d["ventajas"]), " ".join(d["desventajas"]),
                    " ".join(d["normativa"]),
                ]
            ).lower()
            if q_lower in bloque_texto:
                resultados.append(("Fichas por tipo societario", d["nombre"], d["articulos"], d["definicion"][:220] + "…"))

        # Buscar en marco general
        for tema in MARCO_GENERAL:
            bloque_texto = (tema["titulo"] + " " + tema["articulos"] + " " + tema["contenido"]).lower()
            if q_lower in bloque_texto:
                resultados.append(("Marco general", tema["titulo"], tema["articulos"], tema["contenido"].strip()[:220] + "…"))

        # Buscar en quiz (para practicar sobre el tema)
        for q_item in QUIZ:
            bloque_texto = (q_item["tema"] + " " + q_item["pregunta"] + " " + q_item["explicacion"]).lower()
            if q_lower in bloque_texto:
                resultados.append(("Quiz relacionado", q_item["tema"], "", q_item["pregunta"]))

        st.write(f"**{len(resultados)}** resultado(s) para *'{query}'*")
        for seccion_r, titulo_r, art_r, extracto in resultados:
            with st.container():
                art_tag_html = f'<span class="article-tag">{art_r}</span>' if art_r else ""
                st.markdown(
                    f'<div class="card">'
                    f'<span class="badge">{seccion_r}</span>'
                    f'{art_tag_html}'
                    f'<br><b>{titulo_r}</b><br>'
                    f'<span style="font-size:0.9rem;color:#555">{extracto}</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
    else:
        st.caption("Ejemplos para probar: `sociedad civil`, `Sección IV`, `SAU`, `art. 54`, `comanditario`, `affectio societatis`, `SAS`.")
