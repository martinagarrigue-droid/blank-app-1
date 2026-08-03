# -*- coding: utf-8 -*-
"""
Banco de preguntas para el módulo de autoevaluación.
Cada pregunta indica el tema, el enunciado, las opciones, el índice de la
opción correcta y una explicación con cita normativa.
"""

QUIZ = [
    {
        "tema": "Marco General",
        "pregunta": "¿Qué ocurrió con la 'sociedad civil' a partir de la unificación de 2015?",
        "opciones": [
            "Se mantuvo intacta como tipo autónomo en el nuevo CCCN",
            "Se derogó su régimen y quedó absorbida por la LGS (tipos previstos o Sección IV)",
            "Se transformó automáticamente en SRL",
            "Pasó a llamarse 'sociedad simple' y sigue en el Código Civil",
        ],
        "correcta": 1,
        "explicacion": "La Ley 26.994 derogó los arts. 1648 a 1788 bis del Código Civil de Vélez y unificó el régimen bajo la LGS. Las ex sociedades civiles hoy deben adoptar un tipo de la LGS o caen en el régimen residual de la Sección IV (arts. 21 a 26 LGS).",
    },
    {
        "tema": "Marco General",
        "pregunta": "Según el art. 1° LGS, ¿cuántas personas se necesitan como mínimo para constituir una sociedad?",
        "opciones": ["Siempre dos", "Una, en los casos que la ley admite sociedad unipersonal", "Tres", "No hay sociedad sin al menos cinco socios"],
        "correcta": 1,
        "explicacion": "Desde la reforma de la Ley 26.994, el art. 1° LGS admite que la sociedad se constituya por una o más personas (SAU y, luego con la Ley 27.349, SAS unipersonal).",
    },
    {
        "tema": "Marco General",
        "pregunta": "La 'inoponibilidad de la personalidad jurídica' (art. 54, 3er párr. LGS) permite...",
        "opciones": [
            "Disolver la sociedad automáticamente",
            "Imputar la actuación societaria directamente a los socios o controlantes que la hicieron posible, cuando encubre fines extrasocietarios o viola la ley/buena fe",
            "Que un socio se retire sin consecuencias",
            "Que la sociedad cambie de tipo social sin trámite",
        ],
        "correcta": 1,
        "explicacion": "Es la doctrina del 'disregard' o 'corrimiento del velo': permite responsabilizar solidaria e ilimitadamente a quienes usaron la sociedad como mero recurso para fines extrasocietarios o para violar la ley, el orden público o la buena fe, o para frustrar derechos de terceros.",
    },
    {
        "tema": "Sección IV",
        "pregunta": "¿Cómo responden, en principio, los socios de una sociedad de la Sección IV frente a terceros?",
        "opciones": [
            "Solidaria e ilimitadamente siempre",
            "Como obligados simplemente mancomunados y por partes iguales, salvo estipulación o tipo social en juego",
            "No responden nunca",
            "Sólo responde el administrador",
        ],
        "correcta": 1,
        "explicacion": "Art. 24 LGS: los socios responden mancomunadamente y por partes iguales, salvo que exista solidaridad pactada, o que resulte de las reglas del tipo que manifestaron adoptar y no cumplieron.",
    },
    {
        "tema": "Colectiva",
        "pregunta": "¿Cómo responden los socios de una Sociedad Colectiva por las obligaciones sociales?",
        "opciones": ["Limitada al aporte", "Ilimitada, solidaria y subsidiaria (con beneficio de excusión)", "Sólo con las ganancias no percibidas", "No responden"],
        "correcta": 1,
        "explicacion": "Art. 125 y 56 LGS: la responsabilidad es subsidiaria (el acreedor debe primero agotar el patrimonio social), ilimitada y solidaria entre los socios.",
    },
    {
        "tema": "Comandita Simple",
        "pregunta": "En la Sociedad en Comandita Simple, ¿puede el socio comanditario ejercer la administración?",
        "opciones": [
            "Sí, sin restricciones",
            "No puede administrar ni ser mandatario de la sociedad; si lo hace, compromete su responsabilidad limitada",
            "Sólo si es el socio mayoritario",
            "Sólo los fines de semana",
        ],
        "correcta": 1,
        "explicacion": "Arts. 136-138 LGS: la administración está reservada a los comanditados; el comanditario que se inmiscuye en la administración responde ilimitada y solidariamente por los actos en que hubiera participado.",
    },
    {
        "tema": "Capital e Industria",
        "pregunta": "En la Sociedad de Capital e Industria, ¿hasta qué límite responde el socio industrial?",
        "opciones": ["Ilimitadamente, igual que el capitalista", "Hasta las ganancias no percibidas", "No responde nunca por deudas sociales", "Limitada al valor de su aporte dinerario"],
        "correcta": 1,
        "explicacion": "Art. 141 LGS: el socio industrial (que aporta su trabajo) responde sólo hasta la concurrencia de las ganancias no percibidas.",
    },
    {
        "tema": "SRL",
        "pregunta": "¿Cuál es el número máximo de socios permitido en una SRL?",
        "opciones": ["No tiene límite", "50 socios", "20 socios", "5 socios"],
        "correcta": 1,
        "explicacion": "Art. 146 LGS: la SRL no puede tener más de 50 socios.",
    },
    {
        "tema": "SRL",
        "pregunta": "¿Qué es la 'garantía solidaria' del art. 150 LGS en la SRL?",
        "opciones": [
            "Los socios responden ilimitadamente por todas las deudas sociales",
            "Los socios garantizan solidariamente frente a terceros la integración total de los aportes de todos los socios",
            "El Estado garantiza el capital social",
            "No existe tal garantía en la SRL",
        ],
        "correcta": 1,
        "explicacion": "Art. 150 LGS: aunque cada socio limita su responsabilidad al capital que suscribe, todos los socios garantizan solidariamente a los terceros la integración de los aportes comprometidos por el resto.",
    },
    {
        "tema": "SA",
        "pregunta": "¿Qué es la Sociedad Anónima Unipersonal (SAU)?",
        "opciones": [
            "Una SA que sólo puede tener hasta 5 accionistas",
            "Una SA constituida por un único accionista, con integración del 100% del capital al constituirse y fiscalización estatal permanente",
            "Un tipo social eliminado por el CCCN",
            "Lo mismo que una SAS",
        ],
        "correcta": 1,
        "explicacion": "Art. 1° LGS (modif. Ley 26.994): la SAU exige un único accionista, capital totalmente integrado al momento de constituirse, y queda comprendida en la fiscalización estatal permanente del art. 299 LGS.",
    },
    {
        "tema": "SA",
        "pregunta": "¿Qué órgano de gobierno tiene la Sociedad Anónima?",
        "opciones": ["Reunión de socios", "Asamblea de accionistas", "Directorio", "Sindicatura"],
        "correcta": 1,
        "explicacion": "Arts. 233-254 LGS: el órgano de gobierno de la SA es la Asamblea de Accionistas (ordinaria y extraordinaria). El Directorio es el órgano de administración.",
    },
    {
        "tema": "Comandita por Acciones",
        "pregunta": "En la Sociedad en Comandita por Acciones, la parte del capital de los socios comanditarios se representa por...",
        "opciones": ["Cuotas", "Acciones", "Partes de interés", "Bonos de participación"],
        "correcta": 1,
        "explicacion": "Art. 315 LGS: el capital comanditario se divide en acciones, aplicándose supletoriamente las normas de la SA.",
    },
    {
        "tema": "SAS",
        "pregunta": "¿En qué norma se regula la Sociedad por Acciones Simplificada (SAS)?",
        "opciones": ["En la LGS 19.550, arts. 163 a 190", "En la Ley 27.349, Título III", "En el CCCN, arts. 148 a 224", "En un decreto reglamentario de la AFIP"],
        "correcta": 1,
        "explicacion": "La SAS fue creada por la Ley 27.349 (2017), por fuera de la LGS, aplicándose la LGS y el CCCN de manera supletoria (art. 33, Ley 27.349).",
    },
    {
        "tema": "SAS",
        "pregunta": "¿Cuál es el capital social mínimo exigido para constituir una SAS?",
        "opciones": ["$100.000 fijos", "El equivalente a 2 veces el Salario Mínimo Vital y Móvil", "No se exige ningún mínimo", "U$S 10.000"],
        "correcta": 1,
        "explicacion": "Art. 40, Ley 27.349: el capital social no puede ser inferior al importe equivalente a dos veces el Salario Mínimo Vital y Móvil vigente.",
    },
    {
        "tema": "Disolución y Liquidación",
        "pregunta": "¿La disolución de una sociedad extingue inmediatamente su personalidad jurídica?",
        "opciones": [
            "Sí, de forma inmediata",
            "No, la personalidad subsiste al solo efecto de la liquidación (art. 101 LGS)",
            "Sólo en las SRL",
            "Sólo si lo decide un juez",
        ],
        "correcta": 1,
        "explicacion": "Art. 101 LGS: la sociedad disuelta conserva su personalidad a los efectos de la liquidación, hasta la cancelación de su inscripción registral (art. 112).",
    },
    {
        "tema": "Transformación/Fusión/Escisión",
        "pregunta": "¿Qué diferencia principal hay entre transformación y fusión?",
        "opciones": [
            "Son sinónimos",
            "La transformación cambia el tipo social sin disolverse; la fusión une patrimonios de dos o más sociedades, disolviéndose sin liquidarse",
            "La fusión sólo aplica a sociedades civiles",
            "La transformación siempre requiere quiebra previa",
        ],
        "correcta": 1,
        "explicacion": "Arts. 74-81 (transformación) y 82-87 (fusión) LGS. La transformación mantiene la misma persona jurídica bajo otro tipo; la fusión puede crear una nueva sociedad o incorporar otra(s) que se disuelven sin liquidarse.",
    },
    {
        "tema": "Sociedades extranjeras",
        "pregunta": "Según el art. 124 LGS, una sociedad constituida en el extranjero con sede o principal objeto en Argentina...",
        "opciones": [
            "Puede operar libremente sin ningún requisito local",
            "Se considera sociedad local a los efectos del cumplimiento de las formalidades de constitución, reforma y contralor",
            "Debe disolverse obligatoriamente",
            "Se rige únicamente por la ley del país de origen, sin excepciones",
        ],
        "correcta": 1,
        "explicacion": "Art. 124 LGS: es una norma de orden público que evita el uso de sociedades 'off shore' para eludir el régimen societario argentino cuando la sede o el objeto principal está en el país.",
    },
]
