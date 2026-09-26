from pathlib import Path
from html import escape
from shutil import copyfile

ROOT = Path(__file__).parent
OUT = ROOT / 'dist'
OUT.mkdir(exist_ok=True)
copyfile(ROOT / 'assets' / 'laura-mendez.webp', OUT / 'laura-mendez.webp')
copyfile(ROOT / 'assets' / 'unicaribe.png', OUT / 'unicaribe.png')

pages = [
 ('portada','Portada','Proyecto final'),
 ('inicio','Inicio','La candidatura'),
 ('diagnostico','Diagnóstico','El problema y la comunicación'),
 ('audiencias','Audiencias','A quiénes hablamos'),
 ('propuesta','Propuesta','Cómo funcionaría'),
 ('narrativa','Narrativa','Mensajes y tono'),
 ('discurso','Discurso','Guion completo'),
 ('oratoria','Oratoria','Video y pitch'),
 ('plan-digital','Plan digital','Canales y calendario'),
 ('riesgos','Riesgos','Prevención y respuesta'),
 ('evaluacion','Evaluación','Cómo medir resultados'),
]

def card(title, body, num=None):
    return f'<article class="card"><span class="eyebrow">{escape(str(num)) if num is not None else "ALCANZA RD"}</span><h3>{title}</h3>{body}</article>'

def grid(*items): return '<div class="grid">' + ''.join(items) + '</div>'

def table(headers, rows):
    h=''.join(f'<th scope="col">{x}</th>' for x in headers)
    b=''.join('<tr>'+''.join(f'<td>{v}</td>' for v in row)+'</tr>' for row in rows)
    return f'<div class="table-wrap"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

content = {}

content['portada'] = dict(kicker='UNICARIBE · CDI-223', title='Alcanza RD', lead='Plan de Comunicación Digital para una propuesta de discurso político sobre economía familiar, inflación, salarios y poder adquisitivo.', body='''
<div class="statement"><span>IDEA CENTRAL</span><p>«Que el ingreso alcance para la vida real».</p></div>
<section><img class="unicaribe-logo" src="unicaribe.png" alt="Logo de la Universidad del Caribe, UNICARIBE"><h2>Ficha del proyecto</h2>
<div class="fact-grid"><div><b>Universidad</b><span>Universidad del Caribe (UNICARIBE)</span></div><div><b>Carrera</b><span>Comunicación Digital</span></div><div><b>Asignatura</b><span>Metodología del Discurso Escrito y Oral · CDI-223</span></div><div><b>Tema de la ficha</b><span>Economía familiar y costo de vida</span></div><div><b>Enfoque</b><span>Inflación, salarios y poder adquisitivo de hogares trabajadores del Gran Santo Domingo</span></div><div><b>Sustentantes e ID</b><span>[Completar nombres y matrículas]</span></div><div><b>Docente</b><span>Sergio Elías Meregildo Rodríguez</span></div><div><b>Lugar y fecha</b><span>Santo Domingo, República Dominicana · septiembre de 2026</span></div></div></section>
<section><h2>El proyecto en un minuto</h2><p>Laura Méndez, candidata ficticia, propone <strong>Alcanza RD</strong>: un plan piloto para proteger el poder adquisitivo de hogares trabajadores de ingresos bajos y medios en el Gran Santo Domingo. La propuesta combina información verificable sobre gastos esenciales, apoyo temporal y focalizado durante aumentos extraordinarios en alimentos o transporte, y una mesa de diálogo sobre salarios e ingresos. Cada medida dependería de presupuesto, criterios públicos y evaluación. El plan de comunicación explica qué puede hacer una política pública, qué todavía requiere estudio y cómo escuchar a las familias.</p><p><a class="button" href="inicio.html">Explorar el proyecto <span aria-hidden="true">↗</span></a></p></section>
''')

content['inicio'] = dict(kicker='01 · CANDIDATURA FICTICIA', title='La economía se vive en casa', lead='Laura Méndez presenta Alcanza RD: una propuesta para que la discusión económica empiece por lo que una familia puede comprar con su ingreso.', body='''
<section><div class="candidate-layout"><div><h2>Laura Méndez</h2><p>Laura Méndez es una candidata ficticia creada para este ejercicio académico. Su plataforma, <strong>Economía para la Vida Real</strong>, propone tomar decisiones con datos públicos, escuchar a los hogares y explicar los costos de cada medida.</p><p><strong>Visión:</strong> que el crecimiento de los ingresos se traduzca en mayor capacidad para cubrir alimentación, transporte y otros gastos esenciales sin crear promesas que no puedan financiarse.</p><div class="quote">«Un dato puede decir que la inflación bajó. Una familia necesita saber cuánto le rinde el sueldo esta semana».</div></div><figure class="candidate-photo"><img src="laura-mendez.webp" alt="Retrato ilustrativo de Laura Méndez, candidata ficticia, con la bandera dominicana de fondo" width="1024" height="1536" loading="eager"><figcaption>Imagen ilustrativa de la candidata ficticia</figcaption></figure></div></section>
<section><h2>El problema</h2><p>Cuando suben los precios de bienes y servicios esenciales, un hogar puede sentir presión incluso si su salario nominal aumentó. La inflación mide el cambio de precios; una inflación menor indica que los precios crecen más lentamente, no que todos hayan vuelto al nivel anterior. Por eso el proyecto comunica <strong>poder adquisitivo</strong>: la relación entre ingreso y costo de vida.</p><p>Según el Banco Central de la República Dominicana, el índice de precios al consumidor aumentó 0.38 % en agosto de 2026 y la inflación interanual se situó en 5.13 %. El Ministerio de Trabajo informó que en febrero de 2026 entró en vigor otra fase de aumento del salario mínimo privado no sectorizado. Ambos datos son contexto; no muestran por sí solos el presupuesto de cada hogar. <a href="https://www.bancentral.gov.do/a/d/6653-bcrd-informa-que-la-variacion-del-ipc-en-agosto-2026-fue-de-038-" target="_blank" rel="noopener">Banco Central ↗</a> · <a href="https://www.presidencia.gob.do/noticias/ministerio-de-trabajo-llama-empresarios-cumplir-con-el-pago-del-aumento-del-8-del-salario" target="_blank" rel="noopener">Ministerio de Trabajo ↗</a></p></section>
''')

content['diagnostico'] = dict(kicker='02 · DIAGNÓSTICO COMUNICACIONAL', title='De los indicadores al presupuesto del hogar', lead='El reto es explicar inflación, ingresos y medidas propuestas con lenguaje claro, sin atribuirle a un solo actor el control de todos los precios.', body='''
<section><h2>Elementos de la comunicación</h2>'''+table(['Elemento','Definición en el proyecto'],[
('Emisor','Laura Méndez y el equipo de la plataforma ficticia Economía para la Vida Real.'),('Receptores','Hogares trabajadores, personas asalariadas, pequeños comercios y ciudadanía interesada.'),('Mensaje','Proteger el poder de compra requiere información, apoyo focalizado y diálogo sobre ingresos, con costos y límites transparentes.'),('Canales y medios','Sitio web, Instagram, Facebook, YouTube y encuentros comunitarios.'),('Código','Lenguaje escrito, ejemplos de presupuesto, voz, subtítulos, tablas sencillas e infografías.'),('Contexto','Variación de precios e ingresos en República Dominicana y diferencias entre hogares.'),('Interferencias','Confundir la baja de la tasa de inflación con una baja general de precios; esperar subsidios para todos; difundir cifras sin fecha.')]) + '''</section>
<section><h2>FODA comunicacional</h2>'''+grid(
card('Fortalezas','<p>Parte de gastos cotidianos; explica la relación entre salario y precios; puede mostrar fuentes y condiciones de cada medida.</p>','F'),
card('Oportunidades','<p>Interés de las familias en información útil y verificable; formatos visuales para explicar conceptos económicos con ejemplos.</p>','O'),
card('Debilidades','<p>No hay un presupuesto aprobado ni un mecanismo definitivo de selección; los indicadores nacionales no describen por igual a cada hogar.</p>','D'),
card('Amenazas','<p>Promesas de bajar precios de inmediato, desinformación con cifras viejas, expectativas de transferencias universales y debate partidista que oculte los detalles.</p>','A')) + '''</section>
<section class="secondary"><h2>Datos de contexto y límites</h2><p>La variación mensual del IPC de agosto de 2026 fue 0.38 % y la interanual 5.13 %, según el Banco Central. El Ministerio de Trabajo informó un aumento salarial nominal para categorías del sector privado no sectorizado en febrero de 2026. El diagnóstico no equipara un salario mínimo con el ingreso total de una familia ni afirma que todas las familias compren la misma canasta. Las piezas fecharán cada cifra y enlazarán la fuente oficial.</p></section>''')

content['audiencias'] = dict(kicker='03 · AUDIENCIAS', title='Una misma economía, distintas preocupaciones', lead='La campaña adapta la explicación sin convertir a las familias en categorías rígidas ni asumir que todas reciben el mismo ingreso.', body='''
<section><h2>Perfiles, plataformas y mensajes</h2>'''+table(['Audiencia','Qué necesita saber','Plataforma y formato','Mensaje adaptado'],[
('Hogares trabajadores de ingresos bajos','Si habría apoyo, bajo qué criterios y durante cuánto tiempo.','Facebook, WhatsApp compartido entre adultos y encuentros; video corto y preguntas frecuentes.','Los apoyos propuestos serían temporales y para hogares elegibles; publicaremos reglas y presupuesto antes de pedir confianza.'),
('Trabajadores asalariados de ingresos medios','Cómo se relacionan aumento nominal, inflación y gastos esenciales.','Instagram, YouTube y web; carrusel y ejemplo de presupuesto.','Un salario puede subir y rendir menos si algunos gastos crecen más; comparemos cifras con fecha y contexto.'),
('Pequeños empleadores y comercios','Cómo se plantearía el diálogo salarial y qué costos tendría cada medida.','Web, Facebook y conversatorio; ficha de propuesta.','El diálogo sobre ingresos debe escuchar a trabajadores y empleadores y evaluar la capacidad de implementación.'),
('Jóvenes que aportan al hogar','Cómo entender datos económicos sin tecnicismos ni promesas virales.','Instagram y YouTube; reel subtitulado.','Inflación más baja no significa precios más bajos: aprendamos a distinguir la tasa del gasto de la casa.')]) + '''</section><section class="secondary"><h2>Regla editorial compartida</h2><p>Ninguna pieza presentará un caso ficticio como testimonio real. No se pedirán datos personales por comentarios ni se publicará la situación económica identificable de una familia.</p></section>''')

content['propuesta'] = dict(kicker='04 · PROPUESTA', title='Así funcionaría Alcanza RD', lead='Un piloto para hogares trabajadores de ingresos bajos y medios del Gran Santo Domingo, sujeto a presupuesto, reglas públicas y evaluación.', body='''
<section><h2>Objetivo y alcance</h2><p>El objetivo es reducir la incertidumbre de los hogares sobre gastos esenciales y probar apoyos temporales cuando un aumento extraordinario en alimentos o transporte presione su presupuesto. La propuesta también abre un diálogo sobre ingresos laborales. El piloto tendría una duración inicial de doce meses. La cantidad de beneficiarios, los umbrales de elegibilidad y el costo se fijarían después de un estudio técnico y una asignación presupuestaria.</p></section>
<section><h2>Tres líneas de acción</h2>'''+grid(
card('Información clara','<p>Publicar cada mes un tablero sencillo con precios e indicadores oficiales, fecha de actualización y ejemplos ilustrativos de presupuesto. Explicar diferencias entre IPC, precio de un producto y gasto de un hogar.</p>','01'),
card('Alivio temporal','<p>Diseñar, con instituciones competentes, un apoyo focalizado para hogares elegibles ante aumentos extraordinarios de alimentos o transporte. Definir activadores, duración, costo, forma de entrega y revisión para evitar duplicidades.</p>','02'),
card('Diálogo sobre ingresos','<p>Convocar a trabajadores, empleadores y autoridades para revisar información sobre inflación, salarios, productividad y capacidad de las empresas. Presentar recomendaciones públicas; no prometer un aumento automático ni atribuirse decisiones de otros órganos.</p>','03')) + '''</section>
<section><h2>Del diseño a la evaluación</h2>'''+table(['Etapa','Qué ocurriría'],[
('1. Escuchar y medir','Levantar consultas a hogares del Gran Santo Domingo y revisar datos oficiales de precios e ingresos.'),
('2. Definir reglas','Publicar población elegible, condiciones de activación, duración, presupuesto estimado y entidad responsable.'),
('3. Ejecutar el piloto','Ofrecer información y, si se aprueba, apoyos focalizados mediante mecanismos auditables y accesibles.'),
('4. Rendir cuentas','Publicar alcance, gasto, errores de inclusión o exclusión y resultados agregados sin exponer datos personales.'),
('5. Decidir continuidad','Comparar indicadores y escuchar a beneficiarios y no beneficiarios antes de ampliar, ajustar o cerrar el programa.')]) + '''</section>
<div class="note"><strong>Lo que la propuesta no promete:</strong> congelar todos los precios, eliminar la inflación o depositar dinero a cada familia. Las medidas deben ser costeadas y aprobadas antes de aplicarse.</div>
''')

content['narrativa'] = dict(kicker='05 · NARRATIVA', title='Que el ingreso alcance', lead='La arquitectura del mensaje convierte una preocupación cotidiana en una propuesta con acciones, costos por definir y mecanismos de rendición de cuentas.', body='''
<section><h2>Arquitectura del mensaje</h2>'''+table(['Nivel','Texto de campaña'],[
('Idea central','Que el ingreso alcance para la vida real.'),
('Mensaje principal','Proponemos medir con claridad lo que cuesta vivir, apoyar temporalmente a hogares elegibles ante aumentos extraordinarios y dialogar sobre ingresos con reglas transparentes.'),
('Mensaje secundario 1','Una cifra de inflación necesita fecha, fuente y explicación: no representa igual el gasto de todos los hogares.'),
('Mensaje secundario 2','El alivio debe llegar a quien lo necesita, tener un plazo y contar con presupuesto publicado.'),
('Mensaje secundario 3','Hablar de salarios exige escuchar a trabajadores y empleadores y mirar el poder de compra, no solo el monto nominal.'),
('Llamado a la conversación','Revisemos la propuesta, preguntemos cuánto costaría y contemos qué gastos presionan más el hogar.')]) + '''</section>
<section><h2>Secuencia narrativa</h2>'''+grid(card('La escena','<p>Una familia organiza sus pagos al cobrar: comida, transporte, servicios y una pequeña reserva para imprevistos. El presupuesto exige decisiones difíciles.</p>','01'),card('La tensión','<p>Un titular económico puede hablar de una tasa menor, mientras la familia recuerda cuánto pagaba antes por sus compras.</p>','02'),card('La respuesta','<p>Explicar datos con claridad, proponer apoyos con reglas y dialogar sobre cómo sostener el poder adquisitivo.</p>','03')) + '''<p class="source">La escena es ilustrativa y no representa un testimonio de una familia real.</p></section>
<section class="secondary"><h2>Tono y reglas editoriales</h2><p>Cercano, preciso y respetuoso. No usar el miedo ni culpar a una persona o sector de todos los precios. Indicar siempre cuándo un dato corresponde a agosto de 2026 y cuándo se habla de un ejemplo. Nombrar a Laura Méndez como candidata ficticia y Alcanza RD como propuesta académica.</p></section>''')

content['discurso'] = dict(kicker='06 · DISCURSO POLÍTICO', title='Discurso de Laura Méndez', lead='Guion íntegro para exposición oral. Duración estimada: tres minutos a ritmo pausado.', body='''
<section class="speech"><p>Buenas tardes.</p>
<p>Hay un momento que se repite en muchos hogares: llega el ingreso y comienza la cuenta. Hay que separar dinero para comida, transporte, servicios y otros compromisos. Entonces aparece la pregunta que ninguna cifra nacional responde por sí sola: ¿alcanzará para llegar al próximo cobro?</p>
<p>El costo de vida no es solo un tema de economistas. Está en la compra de la semana, en el pasaje para ir al trabajo y en las decisiones que toma una familia cuando debe posponer algo importante.</p>
<p>Los datos importan. Nos ayudan a entender cómo cambian los precios y los salarios. Pero debemos explicarlos bien. Si la inflación se reduce, eso no significa necesariamente que los precios hayan regresado a los de antes. Y si un salario sube, necesitamos preguntar cuánto puede comprar con ese ingreso.</p>
<p>Por eso presento <strong>Alcanza RD</strong>, una propuesta piloto para hogares trabajadores de ingresos bajos y medios del Gran Santo Domingo. Tiene tres tareas. La primera es ofrecer información clara y actualizada sobre gastos esenciales, siempre con sus fuentes. La segunda es estudiar un apoyo temporal para hogares elegibles cuando aumentos extraordinarios en alimentos o transporte pongan más presión sobre su presupuesto. La tercera es abrir un diálogo responsable sobre salarios e ingresos, con trabajadores, empleadores y autoridades.</p>
<p>Quiero ser transparente: no estoy prometiendo bajar todos los precios por decreto ni un pago para cada familia. Un apoyo requiere reglas, presupuesto y seguimiento. Una decisión salarial exige escuchar a quienes trabajan y a quienes generan empleo. Sin esas condiciones, una promesa puede sonar bien y fallar en la vida real.</p>
<p>También debemos escuchar a quienes viven el problema. Antes de definir el piloto, preguntaremos qué gastos preocupan más, cómo se recibiría la información y qué obstáculos tendría una familia para solicitar apoyo. Después publicaremos cuánto se gastó, a quién llegó la medida en términos agregados y qué aprendimos.</p>
<p>Mi compromiso es hablar de economía con la misma claridad con que una familia lleva sus cuentas: ingresos, gastos y decisiones que se pueden sostener.</p>
<p>Porque la meta no es ganar un titular. La meta es que <strong>el ingreso alcance para la vida real</strong>. Muchas gracias.</p></section>
<section class="secondary"><h2>Recursos del discurso</h2><p><strong>Apertura:</strong> escena cotidiana y pregunta retórica. <strong>Desarrollo:</strong> diferencia entre precios e inflación, propuesta y límites. <strong>Cierre:</strong> regreso a la cuenta familiar y repetición de la idea central. Pausar después de la pregunta inicial y antes de la frase final.</p></section>''')

content['oratoria'] = dict(kicker='07 · ORATORIA', title='Video y defensa oral', lead='Guiones listos para grabar. El equipo debe insertar aquí su video antes de entregar el sitio.', body='''
<section><h2>Fragmento del discurso para video</h2><p class="meta">Duración estimada: 70 a 85 segundos. Ensayar para ajustar la velocidad real.</p><blockquote>«Hay un momento que se repite en muchos hogares: llega el ingreso y comienza la cuenta. Comida, transporte, servicios. Entonces surge una pregunta: ¿alcanzará para llegar al próximo cobro? [Pausa] Por eso proponemos Alcanza RD. Primero, información clara sobre los gastos esenciales, con datos y fechas. Segundo, estudiar apoyos temporales para hogares elegibles cuando aumentos extraordinarios presionen su presupuesto. Y tercero, dialogar sobre salarios e ingresos con trabajadores y empleadores. No prometemos bajar todos los precios por decreto. Cada medida necesita reglas, presupuesto y evaluación. Porque la meta es sencilla de entender, aunque exige trabajo serio: que el ingreso alcance para la vida real».</blockquote><div class="video-slot"><b>Video del equipo</b><span>Insertar aquí el video real del discurso antes de entregar el sitio.</span></div></section>
<section><h2>Indicaciones de oratoria</h2>'''+grid(card('Voz','<p>Enunciar los gastos con ritmo natural y dar énfasis a la pregunta. Diferenciar cada línea de acción con una pausa breve.</p>'),card('Cuerpo','<p>Mirar a cámara, mantener postura estable y gesticular con moderación al enumerar las tres medidas.</p>'),card('Tiempo','<p>Medir la duración de dos ensayos; evitar correr en los límites y cerrar con una pausa antes de la frase central.</p>')) + '''</section>
<section><h2>Pitch del proyecto paso a paso</h2><p class="meta">Guion orientativo de cuatro a cinco minutos para hasta tres integrantes. Redistribuir bloques si son menos.</p>'''+table(['Bloque','Guion sugerido'],[
('1. Presentación · integrante A · 45 s','«Somos [nombres] y presentamos Alcanza RD, una propuesta ficticia de Laura Méndez sobre economía familiar y costo de vida. Nos enfocamos en hogares trabajadores de ingresos bajos y medios del Gran Santo Domingo».'),
('2. Diagnóstico y audiencias · integrante A · 60 s','«El IPC y los salarios ofrecen contexto, pero una cifra no describe el presupuesto de todos. Distinguimos hogares de ingresos bajos, asalariados de ingresos medios, pequeños comercios y jóvenes que aportan en casa».'),
('3. Propuesta · integrante B · 75 s','«El piloto tiene tres líneas: información sobre gastos esenciales, apoyo temporal sujeto a criterios y presupuesto, y diálogo sobre ingresos. Planteamos escuchar, definir reglas, ejecutar, rendir cuentas y evaluar antes de ampliar».'),
('4. Narrativa y campaña · integrante C · 65 s','«Nuestra idea central es “Que el ingreso alcance para la vida real”. En cuatro semanas explicamos el problema, presentamos la propuesta, resolvemos dudas sobre costos y cerramos con una encuesta de comprensión».'),
('5. Riesgos y cierre · integrante C · 60 s','«Evitamos confundir menor inflación con precios más bajos, prometemos solo lo que puede diseñarse y publicamos correcciones. Medimos comprensión, preguntas y uso del sitio, no solo vistas. Gracias».' )]) + '''</section>''')

content['plan-digital'] = dict(kicker='08 · PLAN DE COMUNICACIÓN DIGITAL', title='Cuatro semanas para explicar y escuchar', lead='Secuencia editorial propuesta. Los días son relativos para ajustarlos después de acordar la fecha de campaña académica.', body='''
<section><h2>Canales y funciones</h2>'''+table(['Canal','Uso principal','Formato'],[
('Sitio web','Fuente completa de propuesta, límites, fuentes y preguntas frecuentes.','Páginas accesibles y enlaces oficiales.'),
('Instagram','Explicar conceptos y recoger dudas de trabajadores jóvenes.','Carruseles y reels subtitulados.'),
('Facebook','Conversación con familias y pequeños comercios.','Publicaciones, video y preguntas moderadas.'),
('YouTube','Alojar el discurso y explicaciones más largas.','Video horizontal con subtítulos.'),
('Encuentro comunitario','Escuchar experiencias fuera de las redes.','Conversatorio y resumen sin datos personales.')]) + '''</section>
<section><h2>Calendario de contenidos</h2>'''+table(['Semana','Objetivo','Piezas concretas','Llamado y señal a medir'],[
('1 · Entender el problema','Distinguir inflación, precios e ingreso real.','Lunes: carrusel «Inflación menor ≠ precios anteriores». Miércoles: video de presupuesto hipotético. Viernes: pregunta abierta sobre gastos esenciales.','«¿Qué gasto presiona más tu hogar?». Dudas recibidas y comprensión inicial.'),
('2 · Presentar la propuesta','Explicar las tres líneas de Alcanza RD.','Lunes: video de la candidata. Miércoles: infografía de tres acciones. Viernes: ficha de criterios todavía por definir.','«Lee el plan completo». Visitas al sitio y preguntas sobre elegibilidad.'),
('3 · Resolver objeciones','Explicar costos, límites y diálogo salarial.','Lunes: carrusel «Qué no prometemos». Miércoles: video de preguntas frecuentes. Viernes: conversatorio con trabajadores y comercios.','«Pregunta por el presupuesto». Calidad de respuestas y dudas recurrentes.'),
('4 · Cerrar y evaluar','Recoger opinión y verificar comprensión.','Lunes: resumen de hallazgos. Miércoles: fragmento del discurso. Viernes: encuesta y publicación de aclaraciones.','«Revisa la propuesta y responde». Comprensión y percepción de claridad.')]) + '''</section>
<section class="secondary"><h2>Copys listos para piezas</h2><p><strong>Carrusel, semana 1:</strong> «Si la inflación baja, los precios pueden seguir subiendo, solo que a menor ritmo. Por eso no basta con un titular: también hay que mirar cuánto alcanza el ingreso para los gastos del hogar. Conoce Alcanza RD, una propuesta académica ficticia».</p><p><strong>Video, semana 3:</strong> «¿Habrá un apoyo para todas las familias? No lo estamos prometiendo. La propuesta plantea estudiar un apoyo temporal para hogares elegibles, con presupuesto y criterios públicos. Lee los límites y haz tu pregunta».</p></section>''')

content['riesgos'] = dict(kicker='09 · GESTIÓN DE RIESGOS', title='Promesas claras, datos verificables', lead='La comunicación económica puede generar expectativas inmediatas. Cada afirmación necesita fecha, fuente y alcance.', body='''
<section><h2>Matriz de riesgos y respuesta</h2>'''+table(['Riesgo','Prevención','Respuesta si ocurre'],[
('«La inflación bajó, entonces todo cuesta menos»','Explicar que una tasa menor puede significar precios que aumentan más despacio; usar ejemplos sin cifras inventadas.','Corregir la pieza original y publicar una explicación con fuente y fecha.'),
('Promesa de subsidio universal','Repetir que cualquier apoyo sería temporal, focalizado y sujeto a presupuesto.','Retirar el texto ambiguo, aclarar criterios aún pendientes y actualizar sitio y redes.'),
('Cifras desactualizadas o fuera de contexto','Fecha visible en cada dato y enlace a BCRD o fuente competente.','Publicar corrección en el mismo canal y dejar registro de la cifra reemplazada.'),
('Expectativa de aumento salarial automático','Explicar que se propone diálogo con trabajadores, empleadores y autoridades.','Aclarar el alcance de la candidatura y los procesos institucionales.'),
('Exposición de finanzas personales','No pedir comprobantes ni ingresos en comentarios; ejemplos ficticios o autorizados.','Retirar datos identificables, registrar el incidente y orientar a canales apropiados.')]) + '''</section>
<section class="secondary"><h2>Protocolo de corrección</h2><p>La persona encargada registra la alerta, contrasta el dato con su fuente original, corrige en la misma plataforma y fecha la actualización. Si se expusieron datos personales, retira primero el contenido. La bitácora interna conserva pieza, problema, respuesta y aprendizaje.</p></section>''')

content['evaluacion'] = dict(kicker='10 · EVALUACIÓN', title='Medir si se entiende la propuesta', lead='Estos indicadores evalúan cuatro semanas de comunicación. El efecto económico de un programa real requeriría datos y seguimiento aparte.', body='''
<section><h2>Objetivos de comunicación</h2><ul><li>Al cerrar la semana 2, presentar las tres líneas de acción y enlazar a sus condiciones y límites.</li><li>Al cerrar la semana 3, clasificar y responder las dudas sobre inflación, elegibilidad, salarios y presupuesto.</li><li>En la semana 4, comprobar si las personas distinguen inflación de nivel de precios y propuesta ficticia de medida vigente.</li></ul></section>
<section><h2>Panel de indicadores</h2>'''+table(['Indicador','Cómo medirlo','Qué nos diría'],[
('Alcance y reproducciones','Estadísticas de cada plataforma por pieza.','Si llega el mensaje; no prueba comprensión.'),
('Visitas al sitio y clics','Analítica disponible y enlaces etiquetados.','Interés en revisar los detalles y fuentes.'),
('Preguntas recurrentes','Registro semanal por tema: precios, apoyo, salario y presupuesto.','Qué explicación necesita mejorar.'),
('Comprensión','Encuesta voluntaria de tres preguntas al final.','Si se entendieron los conceptos y límites básicos.'),
('Calidad de respuesta','Dudas respondidas con explicación o fuente verificable.','Si el equipo escucha y corrige con claridad.'),
('Participación comunitaria','Asistencia y resumen anónimo del conversatorio.','Si se escucharon voces fuera de redes sociales.')]) + '''</section>
<section><h2>Preguntas de la encuesta de cierre</h2><ol><li>Si la inflación baja de una tasa a otra, ¿significa necesariamente que los precios regresaron al nivel anterior?</li><li>¿Alcanza RD ya existe o es una propuesta ficticia de piloto sujeta a presupuesto y aprobación?</li><li>¿Qué parte requiere más explicación: información de precios, apoyo temporal, salarios o costos?</li></ol><p>El equipo compararía las respuestas con las dudas recogidas en la primera semana y corregiría las piezas menos comprendidas. Un alto número de vistas no bastaría para declarar exitosa la comunicación.</p></section>
<section class="secondary"><h2>Fuentes y alcance de la evidencia</h2><p><a href="https://www.bancentral.gov.do/a/d/6653-bcrd-informa-que-la-variacion-del-ipc-en-agosto-2026-fue-de-038-" target="_blank" rel="noopener">BCRD: IPC de agosto de 2026 ↗</a> · <a href="https://www.presidencia.gob.do/noticias/ministerio-de-trabajo-llama-empresarios-cumplir-con-el-pago-del-aumento-del-8-del-salario" target="_blank" rel="noopener">Ministerio de Trabajo: salario mínimo desde febrero de 2026 ↗</a> · Ficha de instrucciones del proyecto final CDI-223, UNICARIBE, septiembre de 2026.</p><p>Las fuentes sustentan el contexto. Alcanza RD, la candidata, las medidas y los casos narrativos son ficticios y no se presentan como políticas vigentes ni como efectos económicos demostrados.</p></section>''')

css = (ROOT / 'theme.css').read_text(encoding='utf-8')
(OUT / 'style.css').write_text(css, encoding='utf-8')
(OUT / 'menu.js').write_text((ROOT / 'menu.js').read_text(encoding='utf-8'), encoding='utf-8')

for i, (slug, label, desc) in enumerate(pages):
    d = content[slug]
    links = ''.join('<a href="{}.html" {}>{}</a>'.format(s, 'aria-current="page"' if s == slug else '', l) for s, l, _ in pages)
    prev = f'<a href="{pages[i-1][0]}.html">← {pages[i-1][1]}</a>' if i else '<span></span>'
    nxt = f'<a href="{pages[i+1][0]}.html">{pages[i+1][1]} →</a>' if i + 1 < len(pages) else '<span></span>'
    html = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#153a80">
<meta name="description" content="{escape(d['lead'], quote=True)}">
<title>{escape(label)} · Alcanza RD</title>
<link rel="stylesheet" href="style.css">
<script src="menu.js" defer></script>
</head>
<body>
<aside class="rail" aria-label="Acceso al menú principal">
  <a class="rail-brand" href="portada.html" aria-label="Alcanza RD, ir a portada">ARD</a>
  <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-drawer" aria-label="Abrir menú de navegación"><span></span><span></span><span></span></button>
  <span class="rail-label">CDI-223 · UNICARIBE</span>
</aside>
<div class="drawer-backdrop" id="drawer-backdrop" hidden></div>
<div class="drawer" id="site-drawer" aria-hidden="true">
  <div class="drawer-title">Explora el proyecto</div>
  <p class="drawer-sub">Alcanza RD · 11 secciones</p>
  <nav aria-label="Páginas del proyecto">{links}</nav>
  <small>Proyecto académico de candidatura ficticia</small>
</div>
<div class="site">
  <div class="topbar">
    <a class="wordmark" href="portada.html">Alcanza RD<span style="color:var(--orange)">.</span></a>
    <span class="topbar-note">Economía familiar y costo de vida</span>
  </div>
  <main>
    <div class="hero">
      <div class="hero-copy">
        <span class="eyebrow">{d['kicker']}</span>
        <h1>{d['title']}</h1>
        <p>{d['lead']}</p>
        <div class="hero-actions"><a class="button" href="propuesta.html">Conocer la propuesta <span aria-hidden="true">↗</span></a></div>
      </div>
      <div class="hero-visual" aria-hidden="true">
        <div class="visual-panel"><span>ALCANZA RD</span><strong>La economía<br>en casa.</strong><small>Ingresos · Gastos · Decisiones</small></div>
        <div class="visual-chip chip-a"><span>01 / HOGAR</span><b>Ingresos</b></div>
        <div class="visual-chip chip-b"><span>02 / VIDA REAL</span><b>Gastos</b></div>
      </div>
    </div>
    <div class="content-body">{d['body']}</div>
    <div class="pager">{prev}{nxt}</div>
  </main>
</div>
<footer><div>Alcanza RD · Propuesta ficticia con fines académicos · UNICARIBE CDI-223 · 2026.<br>El contenido no representa una política pública vigente ni una candidatura real.</div></footer>
</body>
</html>'''
    (OUT / f'{slug}.html').write_text(html, encoding='utf-8')
(OUT / 'index.html').write_text((OUT / 'portada.html').read_text(encoding='utf-8'), encoding='utf-8')
print('Built', len(pages), 'pages')
