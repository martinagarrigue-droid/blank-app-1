# -*- coding: utf-8 -*-
"""
Datos estructurados sobre los tipos societarios regulados por la
Ley General de Sociedades (Ley 19.550, t.o. 1984, modif. por Ley 26.994
y normativa complementaria) y la Ley 27.349 (SAS).

Fuente de referencia normativa: Código Civil y Comercial de la Nación (CCCN,
Ley 26.994), Ley General de Sociedades (LGS, Ley 19.550), Ley 27.349 (SAS),
Resoluciones Generales IGJ.

IMPORTANTE (nota metodológica para la app):
Desde la unificación de 2015 (Ley 26.994) la "sociedad civil" dejó de existir
como tipo autónomo del Código Civil derogado (arts. 1648 a 1788 bis, C.Civ.).
Las sociedades que antes se constituían como "civiles" hoy quedan comprendidas,
según el caso, dentro de los tipos de la LGS o -si no adoptan un tipo o no
cumplen los requisitos- dentro del régimen residual de la Sección IV
(sociedades simples, arts. 21 a 26 LGS).
"""

SOCIEDADES = {
    "seccion_iv": {
        "nombre": "Sociedad de la Sección IV (Sociedad Simple / Residual)",
        "sigla": "S. Secc. IV",
        "articulos": "Arts. 21 a 26, LGS",
        "grupo": "Régimen residual / libre",
        "definicion": (
            "Régimen aplicable a las sociedades que no adoptan uno de los tipos "
            "previstos en el Capítulo II de la LGS, que omiten requisitos esenciales "
            "o que incumplen formalidades exigidas por la ley. También comprende a las "
            "sociedades atípicas y, en la práctica, absorbió el espacio que antes "
            "ocupaban las sociedades civiles del Código Civil derogado y las llamadas "
            "'sociedades de hecho' e 'irregulares' del régimen anterior a 2015."
        ),
        "constitucion": (
            "El contrato social puede hacerse por instrumento público o privado, "
            "e incluso probarse por cualquier medio de prueba (art. 23, 3er párr.). "
            "No requiere inscripción registral para existir como sujeto de derecho, "
            "aunque la falta de inscripción tiene consecuencias sobre su oponibilidad."
        ),
        "socios": {
            "min": 1,
            "max": None,
            "detalle": "No hay mínimo ni máximo específico distinto del régimen general; puede ser unipersonal de hecho, aunque lo usual es la pluripersonalidad.",
        },
        "responsabilidad": (
            "Los socios responden frente a terceros como obligados simplemente "
            "mancomunados y por partes iguales, salvo que la solidaridad con la "
            "sociedad o entre ellos, o una distinta proporción, resulten de una "
            "estipulación expresa respecto de una relación o conjunto de relaciones, "
            "o de las reglas del tipo que manifestaron adoptar y respecto del cual "
            "se dejaron de cumplir requisitos sustanciales o formales (art. 24 LGS)."
        ),
        "capital": {
            "minimo": "No hay capital mínimo legal.",
            "aportes": "Flexibles; el régimen de bienes registrables está facilitado por el art. 23 LGS.",
        },
        "organos": {
            "administracion": "Libremente pactada en el contrato; a falta de pacto, cualquier socio representa a la sociedad (art. 23).",
            "gobierno": "Reunión de socios o pacto libre entre partes.",
            "fiscalizacion": "No obligatoria.",
        },
        "representacion": (
            "Las cláusulas del contrato son oponibles entre los socios y también "
            "frente a terceros si se prueba que las conocían efectivamente al "
            "tiempo de la contratación o del nacimiento de la relación obligacional (art. 22)."
        ),
        "ventajas": [
            "Máxima flexibilidad y bajo costo de constitución.",
            "No exige instrumento público ni inscripción para existir.",
            "Útil para emprendimientos incipientes o acuerdos entre pocas personas de confianza.",
        ],
        "desventajas": [
            "Responsabilidad de los socios más expuesta (mancomunada, en principio no limitada).",
            "Menor protección y oponibilidad de cláusulas frente a terceros.",
            "Dificultades prácticas para operar con bancos, licitaciones o adquirir inmuebles.",
        ],
        "normativa": ["Arts. 21 a 26, LGS 19.550 (según Ley 26.994)", "CCCN: arts. 148 y 141 (persona jurídica privada)"],
    },
    "colectiva": {
        "nombre": "Sociedad Colectiva",
        "sigla": "S.C.",
        "articulos": "Arts. 125 a 133, LGS",
        "grupo": "Sociedades de personas (por interés)",
        "definicion": (
            "Sociedad de tipo personalista en la que los socios contraen "
            "responsabilidad subsidiaria, ilimitada y solidaria por las "
            "obligaciones sociales (art. 125 LGS). Es el tipo históricamente "
            "más antiguo de la LGS y refleja fuertemente el 'intuitu personae'."
        ),
        "constitucion": "Instrumento público o privado, inscripto en el Registro Público (arts. 4, 5, 6 LGS).",
        "socios": {"min": 2, "max": None, "detalle": "Sin tope máximo legal, pero por su naturaleza suele integrarse con pocos socios."},
        "responsabilidad": "Subsidiaria (beneficio de excusión, art. 56), ilimitada y solidaria entre los socios.",
        "capital": {"minimo": "No hay mínimo legal.", "aportes": "Pueden ser obligaciones de dar o de hacer."},
        "organos": {
            "administracion": "A cargo de uno o varios socios o de terceros, conforme el contrato (art. 127); a falta de regulación, todos los socios administran indistintamente.",
            "gobierno": "Reunión de socios; mayoría absoluta de capital, salvo pacto distinto (art. 131).",
            "fiscalizacion": "No obligatoria; puede pactarse.",
        },
        "ventajas": ["Simplicidad de funcionamiento.", "Fuerte control personal entre los socios.", "Sin capital mínimo."],
        "desventajas": ["Responsabilidad ilimitada y solidaria: alto riesgo patrimonial personal.", "Poco usada en la práctica moderna por ese motivo."],
        "normativa": ["Arts. 125 a 133, LGS"],
    },
    "comandita_simple": {
        "nombre": "Sociedad en Comandita Simple",
        "sigla": "S.C.S.",
        "articulos": "Arts. 134 a 140, LGS",
        "grupo": "Sociedades de personas (por interés)",
        "definicion": (
            "Coexisten dos categorías de socios: los 'comanditados', que responden "
            "como los socios de la sociedad colectiva (ilimitada y solidariamente), "
            "y los 'comanditarios', que sólo responden con el capital que se "
            "obligaron a aportar (art. 134)."
        ),
        "constitucion": "Instrumento público o privado, inscripto en el Registro Público.",
        "socios": {"min": 2, "max": None, "detalle": "Al menos un comanditado y un comanditario."},
        "responsabilidad": "Comanditados: ilimitada y solidaria. Comanditarios: limitada al capital aportado.",
        "capital": {"minimo": "No hay mínimo legal.", "aportes": "Comanditarios sólo pueden aportar obligaciones de dar (art. 135)."},
        "organos": {
            "administracion": "Reservada a los socios comanditados o terceros que designen (art. 136); el comanditario no puede administrar ni ser mandatario (art. 137).",
            "gobierno": "Reunión de socios.",
            "fiscalizacion": "No obligatoria.",
        },
        "ventajas": ["Permite combinar 'capitalistas pasivos' (comanditarios) con gestores (comanditados).", "Sin capital mínimo."],
        "desventajas": ["Poco frecuente en la práctica actual.", "El comanditario pierde el beneficio de responsabilidad limitada si se inmiscuye en la administración (art. 137, 138)."],
        "normativa": ["Arts. 134 a 140, LGS"],
    },
    "capital_industria": {
        "nombre": "Sociedad de Capital e Industria",
        "sigla": "S.C.I.",
        "articulos": "Arts. 141 a 145, LGS",
        "grupo": "Sociedades de personas (por interés)",
        "definicion": (
            "El o los socios 'capitalistas' responden como los socios de la "
            "sociedad colectiva; el o los socios 'industriales' responden hasta la "
            "concurrencia de las ganancias no percibidas (art. 141)."
        ),
        "constitucion": "Instrumento público o privado, inscripto en el Registro Público.",
        "socios": {"min": 2, "max": None, "detalle": "Al menos un socio capitalista y un socio industrial (que aporta sólo su trabajo)."},
        "responsabilidad": "Capitalistas: ilimitada y solidaria. Industriales: limitada a las ganancias no percibidas.",
        "capital": {"minimo": "No hay mínimo legal.", "aportes": "El industrial aporta trabajo/industria, no bienes."},
        "organos": {
            "administracion": "Puede ejercerla cualquiera de los socios, sujeto a las reglas de la sociedad colectiva (art. 143).",
            "gobierno": "Reunión de socios; el voto del industrial se computa según art. 144.",
            "fiscalizacion": "No obligatoria.",
        },
        "ventajas": ["Permite formalizar sociedades entre un aportante de capital y un aportante de trabajo.", "Sin capital mínimo."],
        "desventajas": ["Escasamente utilizada; poco desarrollo jurisprudencial y práctico.", "Responsabilidad ilimitada del capitalista."],
        "normativa": ["Arts. 141 a 145, LGS"],
    },
    "srl": {
        "nombre": "Sociedad de Responsabilidad Limitada",
        "sigla": "S.R.L.",
        "articulos": "Arts. 146 a 162, LGS",
        "grupo": "Sociedades de responsabilidad limitada (mixtas)",
        "definicion": (
            "El capital se divide en cuotas; los socios limitan su responsabilidad "
            "a la integración de las cuotas que suscriben o adquieren, sin perjuicio "
            "de la garantía solidaria e ilimitada por la integración de los aportes "
            "de los demás socios (arts. 146 y 150)."
        ),
        "constitucion": "Instrumento público o privado, inscripto en el Registro Público.",
        "socios": {"min": 2, "max": 50, "detalle": "Tope legal de 50 socios (art. 146)."},
        "responsabilidad": "Limitada al capital suscripto, con garantía solidaria entre socios por la integración total de los aportes (art. 150).",
        "capital": {
            "minimo": (
                "La LGS no fija un piso en pesos: solo exige que el capital sea "
                "'adecuado al objeto social'. En la práctica, los registros (IGJ y "
                "registros provinciales) verifican que el monto guarde relación "
                "razonable con la actividad declarada, pudiendo observar capitales "
                "manifiestamente insuficientes."
            ),
            "aportes": "Deben ser obligaciones de dar, integrados en dinero o en especie; el dinerario debe integrarse en un 25% al constituir y el resto en 2 años.",
        },
        "organos": {
            "administracion": "Gerencia, unipersonal o plural; puede ser indistinta, conjunta o colegiada (arts. 157-158).",
            "gobierno": "Reunión de socios / asamblea (según el contrato); art. 159-160.",
            "fiscalizacion": "Optativa, salvo que el capital alcance el monto del art. 299 inc. 2° (fiscalización estatal obligatoria y sindicatura obligatoria).",
        },
        "ventajas": [
            "Responsabilidad limitada de los socios.",
            "Estructura simple y económica de administrar.",
            "Buena para PyMEs y sociedades familiares.",
        ],
        "desventajas": [
            "Tope de 50 socios.",
            "Cesión de cuotas sujeta a mayores formalidades que las acciones de una SA.",
            "Menor prestigio/uso en operaciones de gran escala o financiamiento vía mercado de capitales.",
        ],
        "normativa": ["Arts. 146 a 162, LGS"],
    },
    "sa": {
        "nombre": "Sociedad Anónima",
        "sigla": "S.A.",
        "articulos": "Arts. 163 a 307, LGS",
        "grupo": "Sociedades por acciones",
        "definicion": (
            "El capital se representa por acciones; los socios limitan su "
            "responsabilidad a la integración de las acciones suscriptas (art. 163). "
            "Puede constituirse también como Sociedad Anónima Unipersonal (SAU, art. 1° LGS, "
            "modif. Ley 26.994), con un único accionista, sujeta a fiscalización estatal "
            "permanente y a que el capital se integre totalmente en el acto constitutivo."
        ),
        "constitucion": "Instrumento público, por acto único o por suscripción pública (arts. 165 a 168), inscripto en el Registro Público.",
        "socios": {"min": 1, "max": None, "detalle": "Puede ser unipersonal (SAU) o pluripersonal, sin tope máximo de accionistas."},
        "responsabilidad": "Limitada a la integración de las acciones suscriptas.",
        "capital": {
            "minimo": "Determinado por la reglamentación (IGJ / autoridad local); históricamente $100.000, actualizado por resoluciones.",
            "aportes": "El capital se divide en acciones; el dinerario debe integrarse en un 25% al constituir y el saldo en 2 años (art. 187), salvo SAU, que exige integración del 100%.",
        },
        "organos": {
            "administracion": "Directorio (uno o más directores), art. 255.",
            "gobierno": "Asamblea de accionistas (ordinaria y extraordinaria), arts. 233 a 254.",
            "fiscalizacion": "Sindicatura o consejo de vigilancia; obligatoria en los supuestos del art. 299 (SAU, oferta pública, capital social elevado, concesionarias de servicios públicos, etc.).",
        },
        "ventajas": [
            "Responsabilidad limitada.",
            "Estructura ideal para grandes emprendimientos, atraer inversores y acceder al mercado de capitales.",
            "Libre transmisibilidad de las acciones (salvo restricciones estatutarias).",
        ],
        "desventajas": [
            "Mayores costos y formalidades de constitución y funcionamiento.",
            "Órganos más complejos (directorio, sindicatura, asamblea).",
            "Fiscalización estatal más intensa en ciertos supuestos (art. 299).",
        ],
        "normativa": ["Arts. 163 a 307, LGS", "Art. 1°, LGS (SAU)", "Normas de la IGJ (Res. Gral. IGJ 7/2015 y modif.)"],
    },
    "comandita_acciones": {
        "nombre": "Sociedad en Comandita por Acciones",
        "sigla": "S.C.A.",
        "articulos": "Arts. 315 a 324, LGS",
        "grupo": "Sociedades por acciones",
        "definicion": (
            "El o los socios comanditados responden como en la sociedad colectiva "
            "(ilimitada y solidariamente); el o los comanditarios limitan su "
            "responsabilidad al capital suscripto, que se representa por acciones (art. 315)."
        ),
        "constitucion": "Instrumento público, inscripto en el Registro Público; se aplican subsidiariamente las normas de la SA.",
        "socios": {"min": 2, "max": None, "detalle": "Al menos un comanditado y un comanditario."},
        "responsabilidad": "Comanditados: ilimitada y solidaria. Comanditarios: limitada a las acciones suscriptas.",
        "capital": {"minimo": "Se aplican, en lo pertinente, las reglas de capital de la SA para la porción representada en acciones.", "aportes": "El comanditario aporta capital representado en acciones; el comanditado puede aportar su gestión."},
        "organos": {
            "administracion": "Reservada a los socios comanditados o terceros (art. 318); se aplican las normas del directorio de la SA en lo compatible.",
            "gobierno": "Asamblea, con las particularidades de los arts. 321-322 respecto del voto del socio administrador.",
            "fiscalizacion": "Según reglas de la SA en lo pertinente.",
        },
        "ventajas": ["Combina control de gestión (comanditado) con aporte de capital diversificado (comanditarios vía acciones)."],
        "desventajas": ["Tipo social poco utilizado en la práctica argentina actual.", "Complejidad de articular dos regímenes de responsabilidad distintos."],
        "normativa": ["Arts. 315 a 324, LGS"],
    },
    "sas": {
        "nombre": "Sociedad por Acciones Simplificada",
        "sigla": "S.A.S.",
        "articulos": "Ley 27.349, Título III (arts. 33 a 62)",
        "grupo": "Sociedades por acciones (régimen especial)",
        "definicion": (
            "Tipo societario creado por la Ley 27.349 (2017) por fuera de la LGS, "
            "pensado para agilizar la constitución de startups y pequeños "
            "emprendimientos. Puede constituirse por una o más personas humanas o "
            "jurídicas, que limitan su responsabilidad a la integración de las "
            "acciones suscriptas (art. 38, Ley 27.349)."
        ),
        "constitucion": (
            "Instrumento público o privado, incluso digital, con firma digital, "
            "e inscripción registral por medios digitales en un plazo de 24 horas "
            "si se usa el modelo tipo (art. 38, Ley 27.349)."
        ),
        "socios": {"min": 1, "max": None, "detalle": "Unipersonal o pluripersonal, sin tope máximo."},
        "responsabilidad": "Limitada al capital suscripto.",
        "capital": {
            "minimo": (
                "Equivalente a 2 veces el Salario Mínimo Vital y Móvil (SMVM) vigente "
                "al momento de la constitución (art. 40, Ley 27.349). ⚠️ Este monto es "
                "variable: se actualiza automáticamente cada vez que el Consejo Nacional "
                "del Empleo, la Productividad y el SMVM modifica el salario mínimo "
                "(varias veces al año). No tomes el valor en pesos de ningún artículo "
                "o app como definitivo: verificá el SMVM vigente en igj.gob.ar o en el "
                "Boletín Oficial antes de constituir la sociedad."
            ),
            "aportes": "Igual que en la SA en cuanto a integración de dinerarios (25% al constituir); admite aportes irrevocables y capital en distintas clases de acciones con gran flexibilidad estatutaria.",
        },
        "organos": {
            "administracion": "Órgano de administración flexible, unipersonal o plural, según el instrumento constitutivo (art. 49-51, Ley 27.349).",
            "gobierno": "Reunión de socios, incluso a distancia / por medios digitales (art. 53).",
            "fiscalizacion": "No obligatoria salvo pacto o los supuestos generales de fiscalización estatal.",
        },
        "ventajas": [
            "Constitución rápida y 100% digital.",
            "Gran libertad estatutaria (objeto plural, capital variable, acciones con derechos diversos).",
            "Ideal para startups y emprendimientos tecnológicos; acceso más simple al régimen de FONDES/inversores.",
        ],
        "desventajas": [
            "Menor 'trayectoria' institucional que la SA para grandes inversores tradicionales o bancos.",
            "Ciertas restricciones (p. ej. no puede ser controlada por ni controlar a sociedades del art. 299, ni ser SAU, sin perder el régimen SAS - art. 39 Ley 27.349).",
        ],
        "normativa": ["Ley 27.349, arts. 33 a 62", "Aplicación supletoria de la LGS y del CCCN (art. 33, Ley 27.349)"],
    },
}

# Orden sugerido para mostrar los tipos en la app (de menor a mayor "formalidad")
ORDEN_TIPOS = [
    "seccion_iv",
    "colectiva",
    "comandita_simple",
    "capital_industria",
    "srl",
    "sa",
    "comandita_acciones",
    "sas",
]

GRUPOS = {
    "Régimen residual / libre": "Sociedades que no adoptan un tipo, lo hacen defectuosamente, o son atípicas.",
    "Sociedades de personas (por interés)": "Predomina el elemento personal ('intuitu personae'); responsabilidad total o parcialmente ilimitada.",
    "Sociedades de responsabilidad limitada (mixtas)": "Combinan elementos personalistas y capitalistas; responsabilidad limitada al aporte.",
    "Sociedades por acciones": "El capital se representa en títulos negociables (acciones); responsabilidad limitada; estructura orgánica más compleja.",
    "Sociedades por acciones (régimen especial)": "Régimen especial fuera de la LGS, orientado a agilidad y simplicidad (SAS).",
}
