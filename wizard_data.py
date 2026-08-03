# -*- coding: utf-8 -*-
"""
Preguntas del wizard "¿Qué sociedad me conviene?".
Cada opción de respuesta suma puntaje a determinados tipos societarios
(claves iguales a las de SOCIEDADES en sociedades_data.py). Al final se
recomienda el/los tipos con mayor puntaje, con las salvedades pedagógicas
correspondientes (esto es una guía educativa, no asesoramiento profesional).
"""

WIZARD_PREGUNTAS = [
    {
        "id": "socios",
        "pregunta": "¿Cuántos socios/as van a integrar la sociedad?",
        "opciones": [
            {
                "texto": "Voy a emprender solo/a (unipersonal)",
                "puntajes": {"sas": 3, "sa": 2, "seccion_iv": 1},
            },
            {
                "texto": "Entre 2 y 5 personas",
                "puntajes": {"srl": 3, "sas": 2, "colectiva": 1, "seccion_iv": 1, "sa": 1},
            },
            {
                "texto": "Entre 6 y 50 personas",
                "puntajes": {"srl": 3, "sa": 2, "sas": 1},
            },
            {
                "texto": "Más de 50, o busco abrir el capital a muchos inversores",
                "puntajes": {"sa": 4, "comandita_acciones": 1},
            },
        ],
    },
    {
        "id": "responsabilidad",
        "pregunta": "¿Qué nivel de exposición patrimonial personal estás dispuesto/a a asumir?",
        "opciones": [
            {
                "texto": "Quiero limitar mi responsabilidad al capital que aporto",
                "puntajes": {"srl": 3, "sa": 3, "sas": 3},
            },
            {
                "texto": "No me preocupa asumir responsabilidad ilimitada si a cambio tengo control total",
                "puntajes": {"colectiva": 3, "comandita_simple": 1, "capital_industria": 1},
            },
            {
                "texto": "Prefiero un esquema mixto: algunos socios gestionan y responden más, otros sólo ponen capital",
                "puntajes": {"comandita_simple": 3, "comandita_acciones": 3, "capital_industria": 2},
            },
            {
                "texto": "Todavía no lo sé / quiero la opción más flexible y económica para arrancar",
                "puntajes": {"seccion_iv": 3},
            },
        ],
    },
    {
        "id": "capital",
        "pregunta": "¿Cómo pensás financiar el proyecto?",
        "opciones": [
            {
                "texto": "Capital propio, chico, para arrancar rápido y barato",
                "puntajes": {"seccion_iv": 2, "sas": 3, "srl": 1},
            },
            {
                "texto": "Busco inversores ángeles / fondos de venture capital",
                "puntajes": {"sas": 3, "sa": 2},
            },
            {
                "texto": "Planeo salir a Oferta Pública / cotizar en bolsa en el futuro",
                "puntajes": {"sa": 4},
            },
            {
                "texto": "Aporte de trabajo de una parte y de capital de otra",
                "puntajes": {"capital_industria": 4},
            },
        ],
    },
    {
        "id": "velocidad",
        "pregunta": "¿Qué tan urgente es constituir la sociedad?",
        "opciones": [
            {
                "texto": "La necesito ya, quiero trámites 100% digitales y rápidos",
                "puntajes": {"sas": 4},
            },
            {
                "texto": "Puedo esperar el trámite tradicional (semanas)",
                "puntajes": {"srl": 2, "sa": 2, "colectiva": 1},
            },
            {
                "texto": "No tengo apuro y prefiero evitar trámites formales por ahora",
                "puntajes": {"seccion_iv": 3},
            },
        ],
    },
    {
        "id": "escala",
        "pregunta": "¿Cuál es la escala / ambición del proyecto?",
        "opciones": [
            {
                "texto": "Startup tecnológica escalable",
                "puntajes": {"sas": 4, "sa": 1},
            },
            {
                "texto": "PyME familiar o profesional de escala media",
                "puntajes": {"srl": 4},
            },
            {
                "texto": "Gran empresa, potencial cotización, muchos accionistas",
                "puntajes": {"sa": 4},
            },
            {
                "texto": "Proyecto chico, informal o de confianza entre pocas personas",
                "puntajes": {"seccion_iv": 3, "colectiva": 2},
            },
        ],
    },
]

DISCLAIMER_WIZARD = (
    "Este wizard es una herramienta **educativa** para practicar el razonamiento "
    "jurídico de elección de tipo societario. No reemplaza el asesoramiento de un/a "
    "abogado/a o contador/a matriculado/a para un caso concreto."
)
