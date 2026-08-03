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

NOTA SOBRE DOCTRINA Y JURISPRUDENCIA (uso académico):
Las secciones "debate_doctrinario" y "jurisprudencia_clave" de cada tipo
societario son resúmenes pedagógicos elaborados a partir de fuentes públicas
(artículos académicos, comentarios de fallos y obras de referencia) y buscan
introducir al lector en las principales líneas de discusión doctrinaria y
jurisprudencial de la materia. No reemplazan la lectura del texto completo de
los fallos citados ni de las obras originales de los autores mencionados.
Antes de citar cualquier fallo o postura doctrinaria en un examen, trabajo
práctico o dictamen profesional, se recomienda verificar la fuente primaria
(el texto íntegro de la sentencia en la base de jurisprudencia
correspondiente, o la obra doctrinaria original).
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
        "debate_doctrinario": """
La reforma de la Ley 26.994 a la Sección IV es, junto con la sociedad unipersonal,
el cambio más discutido de la unificación 2015 en materia societaria.

- **Ricardo A. Nissen**, uno de los autores que más impulsó esta línea de reforma
  (junto con Pilar Rodríguez Acquarone), defendió la eliminación de la vieja
  categoría de "sociedad irregular" -con su severo régimen de responsabilidad
  solidaria y disolución anticipada a pedido de cualquier socio- y celebró que la
  Sección IV reconociera expresamente la capacidad de estas sociedades para
  adquirir bienes registrables, algo que antes generaba abusos cuando los socios
  invocaban la falta de personalidad para excluir inmuebles de la quiebra social.
- Sin embargo, el propio Nissen -y con él buena parte de la doctrina societaria-
  advirtió sobre el "costo" de la reforma: al eliminar la responsabilidad
  solidaria automática de los socios (que preveía el viejo art. 23) y
  reemplazarla por la mancomunión simple del art. 24, la ley debilitó la
  protección de los terceros que contratan con sociedades no regularizadas,
  generando un incentivo a no inscribirse.
- **Efraín Hugo Richard**, desde su enfoque funcional de la empresa y su
  desarrollo doctrinario sobre infracapitalización societaria, enfatiza que la
  Sección IV no debe leerse como un "premio" a la informalidad: la ausencia de
  tipicidad no exime a los socios y administradores de responder por los daños
  derivados de una gestión negligente o de la actuación en insolvencia.
""",
        "jurisprudencia_clave": [
            {
                "caso": "\"Banco de Ultramar S.A. c/ Diseños Eggo y otros\" y \"Romero, M.J. c/ Freeway S.R.L. y otros\"",
                "tribunal": "CNCom. (diversas salas)",
                "sintesis": (
                    "Precedentes citados por la doctrina (Balonas, entre otros) sobre la "
                    "responsabilidad de los integrantes de sociedades no regularizadas frente a "
                    "títulos de crédito librados por la sociedad; reflejan el criterio, previo a la "
                    "reforma de 2015, que restringía el beneficio de excusión a las sociedades "
                    "regularmente constituidas."
                ),
            },
            {
                "caso": "\"Safer S.A. c/ Organización Lococo S.A.\" (CNCom., Sala C, 24/2/1972) y \"Castaño, R. c/ Figueroa de Kelly\" (CNCom., Sala A, 7/9/1973)",
                "tribunal": "CNCom.",
                "sintesis": (
                    "Precedentes clásicos, anteriores a la reforma de 2015, sobre reconocimiento y "
                    "prueba de la existencia de una sociedad de hecho, hoy encuadrable en el régimen "
                    "de la Sección IV. ⚠️ Se recomienda verificar el texto completo antes de citarlos "
                    "en un trabajo, dada su antigüedad y el cambio de régimen legal posterior."
                ),
            },
        ],
        "conflictos_frecuentes": [
            "Prueba de la existencia y términos del contrato social: al no requerirse instrumento escrito, los conflictos sobre 'quién es socio' y en qué proporción son frecuentes; se resuelven por cualquier medio de prueba (art. 23, 3er párr. LGS).",
            "Representación: cualquier socio obliga a la sociedad frente a terceros (art. 23), lo que genera conflictos internos cuando uno de ellos contrata sin consentimiento de los demás.",
            "Subsanación (art. 25 LGS): los socios pueden subsanar la omisión de requisitos en cualquier momento, pero la falta de acuerdo unánime obliga a resolverlo judicialmente, lo que es fuente de litigios cuando algunos socios quieren regularizar y otros no.",
            "Relación entre acreedores sociales y particulares (art. 26 LGS): la falta de un patrimonio claramente diferenciado potencia los conflictos entre los acreedores de la sociedad y los acreedores personales de cada socio.",
        ],
        "inoponibilidad_velo": """
Paradójicamente, en la Sección IV la inoponibilidad del art. 54, 3er párrafo,
LGS tiene menor protagonismo práctico que en la SA o la SRL: como los socios ya
responden (mancomunada o solidariamente, según el caso) con su propio
patrimonio, el "premio" de correr el velo es menor. Donde sí se aplica con
fuerza es para imputar responsabilidad a quienes se ocultan detrás de una
sociedad de la Sección IV para aparentar insolvencia, o para fragmentar un
mismo negocio en múltiples sociedades informales con el objetivo de eludir a
acreedores laborales o fiscales -supuesto en el que se combinan el art. 54 LGS
con el art. 144 CCCN (inoponibilidad de la persona jurídica en general).
""",
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
        "debate_doctrinario": """
Existe consenso doctrinario (Nissen, Vítolo) en que la sociedad colectiva es,
en la práctica argentina actual, un tipo social "en extinción": su
responsabilidad ilimitada y solidaria la vuelve poco atractiva frente a la SRL
y la SAS, que ofrecen protección patrimonial sin renunciar a estructuras
simples. Se la sigue estudiando por su valor dogmático como "tipo puro"
personalista, que sirve de referencia comparativa para explicar tanto la
comandita simple como el régimen de la Sección IV.
""",
        "jurisprudencia_clave": [
            {
                "caso": "Nota metodológica",
                "tribunal": "-",
                "sintesis": (
                    "Dado su escaso uso actual, la sociedad colectiva genera poca litigiosidad "
                    "reciente; la jurisprudencia relevante suele remitir a los principios generales "
                    "del beneficio de excusión (art. 56 LGS) y de la responsabilidad solidaria de "
                    "los socios, antes que a fallos específicos y recientes sobre este tipo en "
                    "particular."
                ),
            }
        ],
        "conflictos_frecuentes": [
            "Remoción del socio administrador: salvo pacto en contrario o justa causa, requiere mayoría (art. 129 LGS) y puede derivar en acción judicial de remoción con intervención cautelar de la administración.",
            "Determinación de la mayoría para decisiones sociales: a falta de pacto, se computa por mayoría absoluta de capital (art. 131 LGS), lo que en sociedades de pocos socios con participaciones desiguales genera conflictos de bloqueo.",
            "Ingreso de nuevos socios o cesión de la parte social: requiere el consentimiento de todos los demás socios (art. 131, in fine, LGS), por el fuerte carácter intuitu personae del tipo.",
        ],
        "inoponibilidad_velo": """
Al ser ya ilimitada y solidaria la responsabilidad de los socios, el art. 54,
3er párrafo, LGS tiene aquí un rol secundario: rara vez hace falta 'correr el
velo' para llegar al patrimonio de los socios, porque la ley ya se los exige
directamente. Su aplicación se reserva a supuestos de sociedades colectivas
usadas, a su vez, como instrumento de otra persona (por ejemplo, un socio
formal que actúa por cuenta de un tercero oculto), en cuyo caso la
inoponibilidad permite imputar la actuación a ese tercero no declarado.
""",
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
        "debate_doctrinario": """
La doctrina (Nissen, Vítolo) coincide en señalar que la comandita simple
combina, para el uso empresarial moderno, las desventajas de dos regímenes:
exige un socio con responsabilidad ilimitada (el comanditado) y limita
severamente al comanditario, que ni siquiera puede participar de la gestión
sin arriesgar su beneficio de responsabilidad limitada (arts. 137-138 LGS).
Por eso se la considera, junto con la sociedad de capital e industria, uno de
los tipos "residuales" del Capítulo II, en la práctica reemplazados por la
SRL y la SAS.
""",
        "jurisprudencia_clave": [
            {
                "caso": "Nota metodológica",
                "tribunal": "-",
                "sintesis": (
                    "Al igual que la sociedad colectiva, la comandita simple tiene escaso uso "
                    "práctico actual y, en consecuencia, escasa jurisprudencia reciente y "
                    "específica. Los casos que existen suelen versar sobre la inmisión del "
                    "comanditario en la administración (arts. 137-138 LGS); se recomienda buscar "
                    "jurisprudencia actualizada en bases especializadas antes de citar un caso "
                    "puntual."
                ),
            }
        ],
        "conflictos_frecuentes": [
            "Inmiscusión del comanditario en la administración (arts. 137 y 138 LGS): es la fuente de litigio más típica del tipo, ya que el comanditario que administra -o incluso solo aparenta hacerlo, por ejemplo mediante poderes amplios- puede perder su responsabilidad limitada y quedar equiparado al comanditado.",
            "Uso de un comanditado 'hombre de paja' que formalmente administra mientras el comanditario real controla la sociedad tras bambalinas: la doctrina discute si corresponde correr el velo para hacer responder ilimitadamente al comanditario oculto.",
            "Cesión de la parte del comanditario y del comanditado: mientras el comanditario puede transmitir su parte con mayor libertad si el contrato lo permite, el cambio de comanditado suele requerir la conformidad de los demás socios, dada la naturaleza intuitu personae de su rol.",
        ],
        "inoponibilidad_velo": """
El supuesto más citado por la doctrina es precisamente el del 'comanditario
oculto que administra': si se prueba que el comanditario ejerce de hecho la
administración, prevaliéndose de la apariencia de que sólo el comanditado
administra, corresponde tanto la sanción específica de los arts. 137-138 LGS
(pérdida del límite de responsabilidad) como, en los casos más graves de
utilización fraudulenta de la estructura societaria, la aplicación del
art. 54, 3er párrafo, LGS.
""",
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
        "debate_doctrinario": """
Este es uno de los puntos de mayor coincidencia crítica entre Nissen y Vítolo:
ambos autores señalan -según se recoge en la literatura comparativa de sus
obras de referencia ("Ley de Sociedades Comerciales" de Nissen y "Manual de
Derecho Comercial" de Vítolo)- que históricamente la sociedad de capital e
industria fue utilizada como mecanismo de fraude laboral, disfrazando de
"socio industrial" a quien en los hechos era un trabajador dependiente, y de
"socio capitalista" a quien en los hechos era su empleador, para eludir las
cargas de la legislación laboral y de la seguridad social. Por ese motivo, la
doctrina y los tribunales del trabajo miran con particular desconfianza los
contratos de sociedad de capital e industria vinculados a la prestación de
servicios personales subordinados.
""",
        "jurisprudencia_clave": [
            {
                "caso": "Nota metodológica",
                "tribunal": "Fuero laboral (diversos)",
                "sintesis": (
                    "La jurisprudencia laboral argentina ha declarado, en numerosos casos, la "
                    "existencia de una relación de trabajo encubierta bajo la apariencia de una "
                    "sociedad de capital e industria, aplicando el principio de primacía de la "
                    "realidad (art. 14, LCT) para desestimar la forma societaria y reconocer los "
                    "derechos laborales del socio 'industrial'. Se recomienda buscar jurisprudencia "
                    "actualizada del fuero del trabajo de la jurisdicción correspondiente para casos "
                    "concretos, dado que este tipo de litigios es muy casuístico."
                ),
            }
        ],
        "conflictos_frecuentes": [
            "Determinación del valor del aporte de industria (trabajo) para fijar la proporción de ganancias del socio industrial, ante la ausencia de un aporte dinerario de referencia (art. 144 LGS).",
            "Calificación de la relación como sociedad genuina o como relación laboral encubierta (ver 'Jurisprudencia clave').",
            "Cómputo del voto del socio industrial en las decisiones sociales, cuya proporción exige integración con la del socio capitalista según las reglas supletorias del art. 144 LGS.",
        ],
        "inoponibilidad_velo": """
Aquí la inoponibilidad del art. 54 LGS dialoga con el art. 14 de la Ley de
Contrato de Trabajo (LCT), que sanciona con nulidad cualquier contrato que
tenga por objeto encubrir una relación laboral. Cuando un juez laboral
determina que el "socio industrial" era en realidad un trabajador
subordinado, no necesariamente aplica el art. 54 LGS en sentido estricto
-porque, técnicamente, no habría una sociedad válida que desestimar-, sino
que directamente recalifica el vínculo como laboral; sin embargo, cuando
existen terceros o socios capitalistas que se beneficiaron del fraude, la
inoponibilidad societaria puede sumarse para extender la responsabilidad
patrimonial a su respecto.
""",
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
        "debate_doctrinario": """
La SRL concentra buena parte del debate doctrinario sobre la "sociedad
cerrada" en Argentina:

- **Ricardo A. Nissen** defiende a la SRL como el vehículo más eficiente para
  la PyME y la empresa familiar argentina, por su equilibrio entre
  responsabilidad limitada y simplicidad estructural; en su obra "Ley de
  Sociedades Comerciales" analiza extensamente el funcionamiento de la
  gerencia y el rol de la garantía solidaria del art. 150 LGS como mecanismo
  que compensa, frente a terceros, la ausencia de un capital mínimo legal.
- **Daniel R. Vítolo**, en su "Manual de Derecho Comercial" y en sus trabajos
  sobre responsabilidad de administradores, señala la escasa regulación
  legal de los mecanismos de resolución de conflictos entre socios de la SRL
  cuando ésta tiene solo dos integrantes al 50%, apuntando que la ley no
  prevé, a diferencia del directorio de la SA (art. 260 LGS, doble voto del
  presidente), un mecanismo de desempate expreso para la gerencia o la
  reunión de socios de la SRL.
- **Efraín Hugo Richard** analiza a la SRL desde la responsabilidad de sus
  gerentes por infracapitalización material: para Richard, la ausencia de un
  capital mínimo legal traslada al gerente -y, eventualmente, a los socios
  que consintieron una subcapitalización manifiesta respecto del objeto
  social- el riesgo de responder personalmente frente a los acreedores
  sociales por los daños derivados de operar con un patrimonio insuficiente
  para el giro de la empresa (en conexión con el art. 99 LGS y el deber de
  prevención del daño de los arts. 1710 y ss. CCCN).
""",
        "jurisprudencia_clave": [
            {
                "caso": "Doctrina sobre 'sociedades de dos socios al 50%'",
                "tribunal": "Doctrina y práctica de los tribunales comerciales",
                "sintesis": (
                    "La doctrina nacional (entre otros, Favier Dubois y Spagnolo) sistematiza las "
                    "herramientas que utilizan los tribunales comerciales argentinos frente al "
                    "bloqueo societario en SRL de dos socios: (i) la impugnación del voto que causó "
                    "el empate, (ii) la acción de exclusión del socio que ejerce el bloqueo de forma "
                    "abusiva y contraria al interés social (arts. 91 a 93 LGS), y (iii) -como última "
                    "instancia- la disolución por 'imposibilidad sobreviniente de lograr el objeto "
                    "social' (art. 94, inc. 4°, LGS), interpretada extensivamente para abarcar los "
                    "casos de parálisis funcional de los órganos sociales por enfrentamiento "
                    "irreconciliable entre los socios. A diferencia de otras legislaciones (p. ej. "
                    "España o Uruguay), la LGS argentina no prevé una causal de disolución expresa "
                    "por 'empate' o 'parálisis de los órganos sociales', por lo que estos casos se "
                    "encuadran por vía interpretativa en el art. 94, inc. 4°."
                ),
            },
            {
                "caso": "\"Carballo, Atilano c/ Kanmar S.A. (en liquidación) y otros\"",
                "tribunal": "CSJN, Fallos 325:2817 (2002)",
                "sintesis": (
                    "Aunque referido a una SA, es un precedente troncal también invocado en materia "
                    "de responsabilidad de administradores de la SRL: la Corte remarcó que la "
                    "personalidad diferenciada de la sociedad respecto de sus administradores es la "
                    "base del derecho societario, y que la extensión de responsabilidad exige "
                    "probar una conducta fraudulenta o abusiva concreta, no bastando la mera "
                    "invocación genérica del art. 54 LGS."
                ),
            },
        ],
        "conflictos_frecuentes": [
            "Empate en sociedades de dos socios al 50%: al no existir en la LGS una causal expresa de disolución por 'parálisis de los órganos sociales', la doctrina y la práctica encuadran estos casos en la 'imposibilidad sobreviniente de lograr el objeto social' (art. 94, inc. 4° LGS) o habilitan la exclusión del socio bloqueante (arts. 91-93 LGS).",
            "Gerencia plural: conflictos frecuentes entre la gerencia 'indistinta' (cualquier gerente obliga a la sociedad) y la 'conjunta' (se requieren varias firmas), sobre todo cuando el contrato social no define con precisión el régimen aplicable (art. 157 LGS).",
            "Cesión de cuotas sociales: el derecho de preferencia de los demás socios (si está pactado) y las mayorías exigidas para aprobar el ingreso de un nuevo socio (art. 152 LGS) generan litigios frecuentes en sociedades familiares al momento de una sucesión o de un conflicto entre herederos.",
            "Exclusión de socio gerente por mal desempeño: se solapan las reglas de exclusión del art. 91 LGS con el régimen de responsabilidad del gerente (art. 157 LGS, que remite en lo pertinente a los arts. 59 y 274 LGS).",
        ],
        "inoponibilidad_velo": """
En la SRL, el art. 54, 3er párrafo, LGS suele activarse en dos escenarios
típicos: (i) cuando se utiliza la sociedad para vaciar patrimonialmente un
negocio familiar en perjuicio de acreedores (p. ej., transferencia de activos
a una nueva SRL constituida por los mismos socios, dejando a la sociedad
original sin bienes para responder), y (ii) en materia laboral, cuando se
constituye o se utiliza una SRL con capital nominal reducido para eludir el
cumplimiento de obligaciones frente a trabajadores.

Sin embargo, tras "Palomeque, Aldo René c/ Benemeth S.A. y otro" (CSJN,
Fallos 326:1062, 2003) y "Carballo, Atilano c/ Kanmar S.A." (CSJN, Fallos
325:2817, 2002) -ambos referidos a sociedades anónimas, pero de aplicación
analógica a la SRL-, la Corte Suprema fijó un criterio restrictivo: no basta
la mera falta de registración laboral o el incumplimiento de obligaciones
fiscales para correr el velo; es necesario acreditar que la sociedad fue
constituida o utilizada en fraude a la ley, de forma ficticia, o como recurso
para violar el orden público. Este criterio, muy discutido por la doctrina
laboralista -que lo consideró un retroceso en la protección del trabajador-,
sigue siendo el estándar de referencia para aplicar el art. 54 LGS a socios y
gerentes de una SRL.
""",
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
        "debate_doctrinario": """
La SA es el tipo con mayor desarrollo doctrinario y el terreno donde se
libran las discusiones más intensas del derecho societario argentino
contemporáneo:

- Sobre la **Sociedad Anónima Unipersonal (SAU)**, introducida en 2015: un
  sector relevante de la doctrina (entre otros, Vítolo) ha señalado que el
  legislador la diseñó con exigencias tan estrictas -integración del 100%
  del capital al constituirse y fiscalización estatal permanente (art. 299,
  inc. 7°, LGS)- que terminó siendo poco utilizada en la práctica, en
  contraste con la más flexible SAS unipersonal creada por la Ley 27.349
  apenas dos años después, que en los hechos desplazó a la SAU como
  alternativa preferida por el emprendedor individual.
- Sobre la **responsabilidad de los directores** (art. 274 LGS), el estándar
  del "buen hombre de negocios" (art. 59 LGS) se interpreta de manera
  dispar: **Efraín Hugo Richard**, uno de sus máximos exponentes en la
  materia, propugna extender la responsabilidad de los administradores en
  casos de infracapitalización societaria y de continuación de la actividad
  en estado de insolvencia; otro sector, más alineado con la jurisprudencia
  restrictiva de la CSJN en materia laboral (ver 'Jurisprudencia clave'),
  exige un estándar más estricto de prueba del dolo o la culpa grave antes de
  responsabilizar personalmente a un director.
- **Ricardo A. Nissen** ha sido uno de los críticos doctrinarios más
  constantes de la insuficiente regulación de la protección de accionistas
  minoritarios en la SA cerrada y de los grupos económicos, abogando por una
  interpretación amplia del art. 54, 3er párrafo, LGS frente a maniobras de
  vaciamiento entre sociedades de un mismo grupo.
""",
        "jurisprudencia_clave": [
            {
                "caso": "\"Compañía Swift de La Plata S.A.\" (\"Swift-Deltec\")",
                "tribunal": "Juzgado Nac. de 1ª Inst. en lo Comercial (Dr. Salvador M. Lozada), 8/11/1971; confirmado por la CSJN en 1973",
                "sintesis": (
                    "El leading case histórico de la doctrina de la inoponibilidad de la "
                    "personalidad jurídica en Argentina. El juez rechazó el concordato preventivo "
                    "de Swift y extendió la quiebra a las demás sociedades del grupo económico "
                    "multinacional Deltec, al comprobar que más del 80% de las ventas de Swift se "
                    "hacían a otras sociedades del mismo grupo a precios artificialmente bajos, lo "
                    "que evidenció que no existía una verdadera separación patrimonial ni de "
                    "voluntad entre las distintas personas jurídicas del grupo."
                ),
            },
            {
                "caso": "\"Palomeque, Aldo René c/ Benemeth S.A. y otro\"",
                "tribunal": "CSJN, Fallos 326:1062 (3/4/2003)",
                "sintesis": (
                    "La Corte revocó la extensión de condena a los directores y socios de una SA "
                    "por el pago parcial de salarios 'en negro', al no haberse acreditado que la "
                    "sociedad fuera ficticia o fraudulenta, constituida en abuso del derecho y con "
                    "el propósito de violar la ley. Fijó el criterio de que la responsabilidad "
                    "solidaria de socios y controlantes en materia societaria es de carácter "
                    "excepcional, marcando un giro restrictivo respecto de la jurisprudencia "
                    "laboral previa, que había tendido a aplicar el art. 54 LGS de forma más laxa "
                    "ante irregularidades registrales."
                ),
            },
            {
                "caso": "\"Carballo, Atilano c/ Kanmar S.A. (en liquidación) y otros\"",
                "tribunal": "CSJN, Fallos 325:2817 (2002)",
                "sintesis": (
                    "Precedente coetáneo a 'Palomeque': la Corte revocó la extensión de condena a "
                    "un director sin que se hubieran acreditado los extremos del art. 59 LGS, "
                    "remarcando que la personalidad diferenciada de la sociedad respecto de sus "
                    "administradores es la base sobre la que se asienta el derecho societario."
                ),
            },
            {
                "caso": "\"Oviedo [...] c/ Telecom [...]\"",
                "tribunal": "CSJN, 10/7/2025",
                "sintesis": (
                    "Fallo reciente que, según la doctrina laboral especializada que lo comentó, "
                    "reafirma la vigencia del criterio restrictivo de 'Palomeque' y 'Carballo' "
                    "respecto de la responsabilidad personal del administrador societario. ⚠️ Al "
                    "tratarse de un precedente muy reciente al momento de esta edición, se "
                    "recomienda verificar su texto completo y los comentarios doctrinarios "
                    "actualizados antes de citarlo en un trabajo académico o profesional."
                ),
            },
        ],
        "conflictos_frecuentes": [
            "Quórum y mayorías en asamblea: la distinción entre asamblea ordinaria y extraordinaria (arts. 234-244 LGS) y el cómputo del quórum en segunda convocatoria son fuente constante de impugnaciones de decisiones asamblearias (acción de nulidad del art. 251 LGS).",
            "Empate en el directorio: a diferencia de la SRL, la LGS sí prevé expresamente en el art. 260 que el estatuto puede otorgar 'doble voto' al presidente del directorio en caso de empate, mecanismo habitual pero cuestionable si se usa de forma abusiva contra el interés social.",
            "Abuso de la mayoría / opresión de la minoría: decisiones asamblearias que benefician sistemáticamente al socio de control en perjuicio del interés social o de los minoritarios habilitan la acción de nulidad (art. 251 LGS) y, en casos graves, la responsabilidad de los accionistas que votaron en interés contrario al social (art. 254 LGS).",
            "Remoción de directores (arts. 256 y 265 LGS): la remoción 'sin causa' es un derecho de la asamblea, pero su ejercicio arbitrario en sociedades cerradas de pocos accionistas suele derivar en litigios por daños y perjuicios o por abuso de derecho.",
            "Conflictos de interés del director (art. 272 LGS): la obligación de abstenerse de votar en asuntos en que tenga un interés contrario al de la sociedad es una fuente recurrente de acciones de responsabilidad.",
        ],
        "inoponibilidad_velo": """
La SA es el terreno donde la tensión doctrinaria y jurisprudencial sobre el
art. 54, 3er párrafo, LGS es más visible. Puede reconstruirse una línea
evolutiva útil para el análisis académico:

1. **Etapa expansiva (años 70)**: inaugurada por "Swift-Deltec", la
   jurisprudencia aplicó la desestimación de la personalidad de forma
   relativamente amplia frente a grupos económicos y maniobras de vaciamiento
   patrimonial.
2. **Etapa restrictiva (2002-2003 en adelante)**: con "Carballo" y
   "Palomeque", la CSJN fijó un estándar mucho más exigente, acorde al
   carácter "excepcional" que la ley atribuye a la responsabilidad solidaria
   societaria: se exige prueba concreta de que la sociedad fue constituida o
   utilizada en fraude a la ley, de forma ficticia, o para violar el orden
   público -no basta la mera insolvencia, el incumplimiento de obligaciones
   laborales o fiscales, ni una confusión patrimonial leve.
3. **Reafirmaciones recientes**: fallos posteriores (con antecedentes en 2025
   como "Oviedo c/ Telecom", según referencias doctrinarias) continuaron
   remitiendo a "Carballo" y "Palomeque" como precedentes rectores,
   consolidando el criterio restrictivo como estándar dominante en materia de
   responsabilidad de socios y administradores de la SA -sin perjuicio de que
   en el fuero concursal la aplicación pueda seguir siendo más flexible frente
   a grupos económicos.

Para un examen de nivel universitario, es clave poder explicar esta tensión
entre la letra amplia del art. 54 LGS y la lectura restrictiva que de él hizo
la CSJN, y contrastarla con la aplicación más flexible que suele hacer la
jurisprudencia y doctrina concursal en casos de grupos económicos (línea que
arranca, precisamente, en "Swift-Deltec").
""",
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
        "debate_doctrinario": """
La doctrina argentina (Nissen, entre otros) coincide en calificar a la
comandita por acciones como un tipo social en franco desuso, cuya combinación
de responsabilidad ilimitada del comanditado con capital representado en
acciones no ofrece, en la práctica, ninguna ventaja que no brinden mejor la SA
(para quien busca capitalizarse) o la SRL/SAS (para quien busca simplicidad
con responsabilidad limitada). Se lo mantiene vigente por tradición histórica
y para casos muy puntuales de estructuras de control familiar, donde se busca
combinar el control de gestión de un socio fundador (comanditado) con el
ingreso de capital externo representado en acciones.
""",
        "jurisprudencia_clave": [
            {
                "caso": "Nota metodológica",
                "tribunal": "-",
                "sintesis": (
                    "Su escasísimo uso práctico actual hace que no existan precedentes judiciales "
                    "recientes y específicos sobre este tipo societario en particular; los "
                    "principios aplicables se derivan, por reenvío normativo (art. 316 LGS), de la "
                    "jurisprudencia general sobre sociedades anónimas."
                ),
            }
        ],
        "conflictos_frecuentes": [
            "Cómputo del voto del socio administrador (comanditado) en la asamblea respecto de su propia gestión, regulado especialmente por los arts. 321-322 LGS para evitar que se autoapruebe sin control de los comanditarios.",
            "Remoción del socio comanditado administrador: por su carácter de socio con responsabilidad ilimitada, exige mayorías agravadas y, en ciertos casos, causa justificada (art. 319 LGS, con remisión a las reglas de la sociedad colectiva).",
        ],
        "inoponibilidad_velo": """
Se aplican, en lo pertinente, los mismos criterios que en la SA (por el
reenvío normativo del art. 316 LGS), aunque el escasísimo uso práctico actual
de este tipo hace que no existan precedentes judiciales recientes específicos
sobre la aplicación del art. 54, 3er párrafo, LGS a la comandita por
acciones en particular.
""",
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
        "debate_doctrinario": """
La SAS es, sin dudas, el tipo societario que más debate doctrinario genera en
la actualidad, con posiciones claramente enfrentadas:

- **Ricardo A. Nissen** es el crítico más constante y sistemático del
  régimen: en artículos como "Consideraciones sobre el nuevo tipo societario
  argentino. Necesidad de una reforma a la legislación societaria nacional..."
  (Revista de las Sociedades y Concursos, año 22, 2021-1), "Reflexiones en
  torno a las sociedades incluidas en la Sección IV de la ley 19.550; las
  sociedades por acciones simplificadas y el futuro del derecho societario
  argentino" (LA LEY, 24/10/2019) y "La naturalización de las anomalías
  societarias" (LA LEY, 1/10/2021), sostiene que la SAS -por su constitución
  simplificada, su escaso control estatal previo y su amplísima autonomía
  estatutaria- se ha convertido en un vehículo apto para el fraude, el lavado
  de activos y la elusión de obligaciones fiscales y laborales, y reclama una
  reforma legislativa que refuerce los controles.
- **Daniel R. Vítolo**, autor de "Ley 27.349 comentada" (Thomson Reuters - La
  Ley, 2017), sostiene una posición más favorable a la modernización que
  implica la SAS, poniendo el acento en su aporte a la agilización de
  trámites y al fomento del emprendedorismo, aunque reconoce la necesidad de
  mecanismos de control adecuados frente a usos abusivos.
- Un debate doctrinario específico y muy citado es el que enfrenta a
  **Sebastián Balbín**, quien sostiene que la autonomía estatutaria de la SAS
  permitiría a los socios apartarse incluso de la prohibición de cláusulas
  leoninas del art. 13 LGS (por ejemplo, pactos que aseguren a un socio la
  totalidad de las ganancias o lo excluyan de ellas), frente a la posición de
  **Nissen**, quien rechaza frontalmente esa lectura por considerar que
  equivaldría a convalidar, por vía estatutaria, el fraude que el art. 13 LGS
  busca precisamente evitar.
""",
        "jurisprudencia_clave": [
            {
                "caso": "Nota metodológica",
                "tribunal": "Fueros comercial y laboral (diversos)",
                "sintesis": (
                    "Al ser un tipo societario creado recién en 2017, la jurisprudencia sobre la "
                    "SAS es todavía escasa y está en formación. Los tribunales comerciales han "
                    "comenzado a aplicar supletoriamente el art. 54 LGS (por reenvío del art. 33, "
                    "Ley 27.349) en casos de uso fraudulento de la SAS, pero, por la novedad del "
                    "tipo, todavía no existe una línea jurisprudencial tan consolidada como la de "
                    "la SA. Se recomienda una búsqueda actualizada en bases de jurisprudencia "
                    "(SAIJ, CIJ, vLex, etc.) antes de citar un caso concreto en un trabajo "
                    "académico."
                ),
            }
        ],
        "conflictos_frecuentes": [
            "Interpretación de cláusulas estatutarias atípicas: la libertad para crear distintas clases de acciones con derechos políticos y económicos diferenciados (art. 46, Ley 27.349) genera disputas interpretativas cuando el instrumento constitutivo no es suficientemente preciso.",
            "Validez de cláusulas potencialmente leoninas a la luz del art. 13 LGS (ver el debate Balbín/Nissen en 'Debate doctrinario').",
            "Responsabilidad de administradores y representantes de hecho (art. 52, Ley 27.349): la ley reconoce expresamente esta figura -novedosa en el derecho societario argentino- y equipara su responsabilidad a la de los administradores de derecho, lo que genera litigios sobre quién debe considerarse administrador de hecho de una SAS.",
            "Transferencia y restricciones a la transferencia de acciones: el estatuto puede prohibir la transferencia de acciones, o de alguna de sus clases, por un plazo máximo (art. 48, Ley 27.349), lo que en la práctica genera conflictos con socios que buscan salir de la sociedad antes de ese plazo.",
        ],
        "inoponibilidad_velo": """
El art. 33 de la Ley 27.349 hace aplicables supletoriamente las disposiciones
de la LGS y del CCCN a la SAS, por lo que el art. 54, 3er párrafo, LGS es
plenamente aplicable a este tipo. La principal preocupación doctrinaria
-liderada por Nissen- es que, dada la simplicidad y rapidez de constitución
de la SAS y el bajo control estatal previo, el riesgo de que se utilice como
"sociedad pantalla" para actividades fraudulentas es más alto que en la SA
tradicional, lo que -sostiene ese sector de la doctrina- debería traducirse
en una aplicación más estricta y proactiva del art. 54 LGS por parte de los
jueces frente a la SAS, en lugar de esperar pasivamente a que se litigue caso
por caso.
""",
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
