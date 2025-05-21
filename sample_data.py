# Datos de ejemplo para lista de especialidades médicas
# Los datos de ejemplo no incluyen caracteres especiales como acentos para no complicar el codigo posterior de visualización
especialidades = [
    "cardiologia",
    "dermatologia",
    "neurologia",
    "pediatria",
    "psiquiatria",
    "traumatologia"
]

# Datos de ejemplo para lista de pacientes DNI, nombre, apellidos, fecha de nacimiento, email, telefono y direccion
# Los datos de ejemplo no incluyen caracteres especiales como acentos para no complicar el codigo posterior de visualización
pacientes = [
    ('12345678A', 'Juan', 'Perez', '1980-05-15', 'juan.perez@example.com', '123456789', 'Calle Falsa 123'),
    ('23456789B', 'Maria', 'Gomez', '1990-07-20', 'maria.gomez@example.com', '987654321', 'Avenida Siempre Viva 456'),
    ('34567890C', 'Carlos', 'Lopez', '1975-03-10', 'carlos.lopez@example.com', '456789123', 'Calle del Sol 789'),
    ('45678901D', 'Ana', 'Martinez', '1985-11-25', None, '789123456', 'Plaza Mayor 101'),
    ('56789012E', 'Luis', 'Fernandez', '1995-09-30', 'luis.fernandez@example.com', '321654987', 'Calle Luna 202'),
    ('67890123F', 'Laura', 'Sanchez', '1988-02-14', None, '654987321', 'Avenida del Mar 303'),
    ('78901234G', 'Pedro', 'Garcia', '1978-06-05', 'pedro.garcia@example.com', '987321654', 'Calle Rio 404'),
    ('89012345H', 'Elena', 'Torres', '1992-08-18', None, '321987654', 'Calle Montaña 505'),
    ('90123456I', 'Jorge', 'Ramirez', '1983-12-22', 'jorge.ramirez@example.com', '654321987', 'Avenida Bosque 606'),
    ('01234567J', 'Sofia', 'Ruiz', '1998-04-09', None, '789654123', 'Calle Jardín 707')
]
    
# Diccionario para almacenar las historias médicas
historias_medicas = {
    "cardiologia": [],
    "dermatologia": [],
    "neurologia": [],
    "pediatria": [],
    "psiquiatria": [],
    "traumatologia": []
}

# Historias médicas de ejemplo
historias_medicas["cardiologia"] = [
    "Antecedentes de hipertensión arterial y diabetes mellitus tipo 2. Acude a consulta por dolor torácico opresivo de 30 minutos de duración, irradiado a brazo izquierdo. Se realiza electrocardiograma que muestra elevación del segmento ST en derivaciones V2-V4. Se diagnostica infarto agudo de miocardio y se inicia tratamiento con trombolíticos y anticoagulantes. Paciente ingresa a unidad de cuidados intensivos para monitorización y manejo.",
    "Antecedentes de insuficiencia cardíaca congestiva. Consulta por disnea progresiva y edema en miembros inferiores. Se realiza ecocardiograma que muestra fracción de eyección del ventrículo izquierdo del 35%. Se ajusta tratamiento con diuréticos, inhibidores de la ECA y betabloqueantes. Paciente es educada sobre la importancia de la adherencia al tratamiento y el control de factores de riesgo.",
    "Antecedentes familiares de enfermedad coronaria. Consulta por palpitaciones y mareos. Se realiza prueba de esfuerzo que muestra signos de isquemia miocárdica. Se prescribe tratamiento con antianginosos y se programa angiografía coronaria para evaluación adicional.",
    "Antecedentes de hipercolesterolemia. Consulta por dolor torácico intermitente. Se realiza ecocardiograma que muestra hipertrofia ventricular izquierda. Se ajusta tratamiento con estatinas y se recomienda dieta baja en grasas saturadas.",
    "Antecedentes de tabaquismo. Consulta por disnea al esfuerzo. Se realiza espirometría que muestra patrón obstructivo moderado. Se prescribe tratamiento con broncodilatadores y se recomienda cese del hábito tabáquico.",
    "Antecedentes de obesidad mórbida. Consulta por edema en miembros inferiores y disnea paroxística nocturna. Se realiza ecocardiograma que muestra insuficiencia cardíaca derecha. Se ajusta tratamiento con diuréticos y se recomienda pérdida de peso.",
    "Antecedentes de fibrilación auricular. Consulta por episodios recurrentes de palpitaciones y fatiga. Se realiza electrocardiograma que confirma fibrilación auricular paroxística. Se inicia tratamiento con anticoagulantes y antiarrítmicos.",
    "Antecedentes de enfermedad valvular cardíaca. Consulta por síncope y mareos. Se realiza ecocardiograma que muestra estenosis aórtica severa. Paciente ingresa a cirugía cardíaca para reemplazo valvular.",
    "Antecedentes relevantes. Consulta por dolor torácico agudo tras esfuerzo físico intenso. Se realiza electrocardiograma que muestra taquicardia ventricular no sostenida. Se prescribe reposo absoluto y se programa estudio electrofisiológico.",
    "Antecedentes de insuficiencia renal crónica. Consulta por disnea progresiva y edema generalizado. Se realiza ecocardiograma que muestra insuficiencia cardíaca avanzada. Paciente ingresa a unidad de cuidados paliativos para manejo sintomático.",
]

historias_medicas["dermatologia"] = [
    "Consulta por lesiones eritematosas y pruriginosas en cara y cuello. Antecedentes de dermatitis atópica desde la infancia. Se realiza examen físico que muestra placas eccematosas con exudado seroso. Se prescribe tratamiento tópico con corticosteroides y antihistamínicos orales. Paciente es educado sobre medidas de cuidado de la piel y evitar factores desencadenantes.",
    "Consulta por aparición de múltiples nevos pigmentados en tronco y extremidades. Antecedentes familiares de melanoma. Se realiza dermatoscopia que muestra características benignas en la mayoría de los nevos, excepto uno con bordes irregulares y variación en el color. Se realiza biopsia excisional del nevo sospechoso para estudio histopatológico.",
    "Consulta por acné severo en cara, pecho y espalda. Antecedentes personales sin relevancia dermatológica previa. Se prescribe tratamiento tópico con retinoides y antibióticos orales para control del acné inflamatorio.",
    "Consulta por aparición súbita de urticaria generalizada tras ingesta alimentaria sospechosa. Antecedentes personales sin alergias conocidas previas. Se prescribe antihistamínicos orales y se recomienda evitar el alimento desencadenante.",
    "Consulta por lesiones descamativas en cuero cabelludo, codos y rodillas. Antecedentes familiares de psoriasis vulgaris. Se prescribe tratamiento tópico con corticosteroides y queratolíticos para control del brote psoriásico.",
    "Consulta por manchas hiperpigmentadas en rostro tras exposición solar prolongada sin protección adecuada. Antecedentes personales sin relevancia dermatológica previa. Se prescribe despigmentantes tópicos y se recomienda uso diario de protector solar.",
    "Consulta por prurito intenso en región genital acompañado de lesiones vesiculosas dolorosas. Antecedentes personales sin relevancia dermatológica previa. Se prescribe antivirales orales para control del brote herpético genital.",
    "Consulta por aparición de lesiones verrugosas en manos y pies. Antecedentes personales sin relevancia dermatológica previa. Se realiza crioterapia para eliminación de verrugas y se recomienda evitar contacto con superficies contaminadas.",
    "Consulta por aparición de lesiones hipopigmentadas en tronco y extremidades. Antecedentes familiares de vitiligo. Se prescribe tratamiento tópico con corticosteroides y fototerapia para control de la despigmentación.",
    "Consulta por aparición de lesiones ampollosas en mucosa oral y genital. Antecedentes personales sin relevancia dermatológica previa. Se realiza biopsia de piel que confirma diagnóstico de pénfigo vulgar. Se inicia tratamiento con corticosteroides sistémicos.",
]

historias_medicas["neurologia"] = [
    "Consulta por insomnio, ansiedad y pensamientos recurrentes sobre muerte. Antecedentes familiares de trastorno depresivo mayor. Se realiza evaluación psiquiátrica que confirma diagnóstico de depresión mayor moderada. Se inicia tratamiento con antidepresivos y terapia cognitivo-conductual.",
    "Consulta por episodios recurrentes de pérdida de conciencia y movimientos involuntarios en extremidades. Antecedentes familiares de epilepsia. Se realiza electroencefalograma que muestra actividad epileptiforme en región temporal izquierda. Se inicia tratamiento con anticonvulsivantes y se programa resonancia magnética cerebral para evaluación adicional.",
    "Consulta por debilidad progresiva en extremidades inferiores y dificultad para caminar. Antecedentes personales sin relevancia neurológica previa. Se realiza resonancia magnética que muestra lesiones desmielinizantes en médula espinal. Se inicia tratamiento con corticosteroides y se programa estudio de potenciales evocados.",
    "Consulta por dolor facial intenso y paroxístico. Antecedentes personales sin relevancia neurológica previa. Se realiza resonancia magnética que muestra compresión del nervio trigémino por un vaso sanguíneo. Se inicia tratamiento con anticonvulsivantes y se programa cirugía de descompresión microvascular.",
    "Consulta por temblor en manos y rigidez muscular. Antecedentes familiares de enfermedad de Parkinson. Se realiza examen neurológico que confirma diagnóstico de enfermedad de Parkinson. Se inicia tratamiento con levodopa y se recomienda terapia física.",
    "Consulta por pérdida progresiva de memoria y desorientación. Antecedentes familiares de enfermedad de Alzheimer. Se realiza evaluación neuropsicológica que confirma diagnóstico de enfermedad de Alzheimer en etapa temprana. Se inicia tratamiento con inhibidores de la colinesterasa y se recomienda apoyo familiar.",
    "Consulta por dolor lumbar irradiado a miembro inferior derecho. Antecedentes personales de hernia discal lumbar. Se realiza resonancia magnética que muestra recurrencia de hernia discal con compresión radicular. Se inicia tratamiento con analgésicos y se programa cirugía de discectomía.",
    "Consulta por visión borrosa y dolor ocular. Antecedentes personales sin relevancia neurológica previa. Se realiza resonancia magnética que muestra lesiones desmielinizantes en nervio óptico. Se inicia tratamiento con corticosteroides y se programa estudio de potenciales evocados visuales.",
    "Consulta por debilidad progresiva en extremidades superiores y dificultad para realizar actividades diarias. Antecedentes personales sin relevancia neurológica previa. Se realiza electromiografía que muestra signos de neuropatía periférica. Se inicia tratamiento con inmunoglobulinas intravenosas y se programa estudio de conducción nerviosa.",
    "Consulta por pérdida progresiva de memoria y desorientación. Antecedentes familiares de demencia frontotemporal. Se realiza evaluación neuropsicológica que confirma diagnóstico de demencia frontotemporal. Se inicia tratamiento con inhibidores de la colinesterasa y se recomienda apoyo familiar."
]

historias_medicas["pediatria"] = [
    "Consulta por fiebre alta, tos y dificultad respiratoria. Antecedentes de bronquiolitis recurrente. Se realiza radiografía de tórax que muestra infiltrados intersticiales bilaterales. Se inicia tratamiento con broncodilatadores, corticosteroides inhalados y antibióticos. Paciente es monitorizado en sala pediátrica para evaluación continua.",
    "Consulta por irritabilidad, llanto inconsolable y rechazo al alimento. Antecedentes de reflujo gastroesofágico. Se realiza ecografía abdominal que muestra engrosamiento del músculo pilórico, compatible con estenosis pilórica. Paciente ingresa a cirugía pediátrica para corrección quirúrgica.",
    "Consulta por dolor abdominal, vómitos y diarrea. Antecedentes personales sin relevancia pediátrica previa. Se realiza examen físico que muestra signos de deshidratación moderada. Se inicia tratamiento con rehidratación oral y se recomienda dieta blanda.",
    "Consulta por erupción cutánea generalizada y fiebre. Antecedentes personales sin relevancia pediátrica previa. Se realiza examen físico que muestra exantema maculopapular. Se diagnostica exantema súbito y se recomienda tratamiento sintomático.",
    "Consulta por otalgia y fiebre. Antecedentes de otitis media recurrente. Se realiza otoscopia que muestra membrana timpánica eritematosa y abombada. Se inicia tratamiento con antibióticos y se recomienda seguimiento otorrinolaringológico.",
    "Consulta por tos persistente y dificultad respiratoria. Antecedentes de asma infantil. Se realiza espirometría que muestra patrón obstructivo. Se ajusta tratamiento con broncodilatadores y corticosteroides inhalados.",
    "Consulta por dolor en extremidades inferiores y cojera. Antecedentes personales sin relevancia pediátrica previa. Se realiza radiografía que muestra signos de enfermedad de Legg-Calvé-Perthes. Se recomienda reposo y seguimiento ortopédico.",
    "Consulta por fiebre alta, irritabilidad y rechazo al alimento. Antecedentes personales sin relevancia pediátrica previa. Se realiza punción lumbar que muestra pleocitosis y aumento de proteínas. Se diagnostica meningitis bacteriana y se inicia tratamiento con antibióticos intravenosos.",
    "Consulta por dolor abdominal recurrente y pérdida de peso. Antecedentes familiares de enfermedad celíaca. Se realiza serología que muestra anticuerpos anti-transglutaminasa positivos. Se recomienda dieta sin gluten y seguimiento gastroenterológico.",
    "Consulta por dolor torácico y disnea. Antecedentes personales sin relevancia pediátrica previa. Se realiza radiografía de tórax que muestra cardiomegalia. Se realiza ecocardiograma que muestra miocardiopatía dilatada. Paciente ingresa a unidad de cuidados intensivos para manejo y monitorización."
]


historias_medicas["psiquiatria"] = [
    "Consulta por insomnio, ansiedad y pensamientos recurrentes sobre muerte. Antecedentes familiares de trastorno depresivo mayor. Se realiza evaluación psiquiátrica que confirma diagnóstico de depresión mayor moderada. Se inicia tratamiento con antidepresivos y terapia cognitivo-conductual.",
    "Consulta por episodios recurrentes de pánico, palpitaciones y sensación de ahogo. Antecedentes personales de trastorno de ansiedad generalizada. Se realiza evaluación psiquiátrica que confirma diagnóstico de trastorno de pánico. Se inicia tratamiento con ansiolíticos y terapia cognitivo-conductual.",
    "Consulta por alucinaciones auditivas y delirios persecutorios. Antecedentes familiares de esquizofrenia. Se realiza evaluación psiquiátrica que confirma diagnóstico de esquizofrenia paranoide. Se inicia tratamiento con antipsicóticos y se recomienda seguimiento psiquiátrico regular.",
    "Consulta por episodios recurrentes de tristeza profunda, pérdida de interés en actividades y cambios en el apetito. Antecedentes personales sin relevancia psiquiátrica previa. Se realiza evaluación psiquiátrica que confirma diagnóstico de trastorno depresivo mayor. Se inicia tratamiento con antidepresivos y terapia cognitivo-conductual.",
    "Consulta por episodios recurrentes de ira, irritabilidad y dificultad para controlar impulsos. Antecedentes personales sin relevancia psiquiátrica previa. Se realiza evaluación psiquiátrica que confirma diagnóstico de trastorno explosivo intermitente. Se inicia tratamiento con estabilizadores del ánimo y terapia cognitivo-conductual.",
    "Consulta por miedo irracional a situaciones sociales, evitación de eventos sociales y ansiedad intensa en situaciones sociales. Antecedentes personales sin relevancia psiquiátrica previa. Se realiza evaluación psiquiátrica que confirma diagnóstico de fobia social. Se inicia tratamiento con ansiolíticos y terapia cognitivo-conductual.",
    "Consulta por pérdida progresiva de memoria, desorientación y cambios en el comportamiento. Antecedentes familiares de enfermedad de Alzheimer. Se realiza evaluación neuropsicológica que confirma diagnóstico de enfermedad de Alzheimer en etapa temprana. Se inicia tratamiento con inhibidores de la colinesterasa y se recomienda apoyo familiar.",
    "Consulta por episodios recurrentes de atracones seguidos de conductas compensatorias como vómitos autoinducidos y uso excesivo de laxantes. Antecedentes personales sin relevancia psiquiátrica previa. Se realiza evaluación psiquiátrica que confirma diagnóstico de bulimia nerviosa. Se inicia tratamiento con antidepresivos y terapia cognitivo-conductual.",
    "Consulta por insomnio crónico, irritabilidad y dificultad para concentrarse. Antecedentes personales sin relevancia psiquiátrica previa. Se realiza evaluación psiquiátrica que confirma diagnóstico de trastorno del sueño-vigilia. Se inicia tratamiento con hipnóticos y terapia cognitivo-conductual.",
    "Consulta por episodios recurrentes de ansiedad intensa, miedo a perder el control y evitación de situaciones que puedan desencadenar ataques de pánico. Antecedentes personales sin relevancia psiquiátrica previa. Se realiza evaluación psiquiátrica que confirma diagnóstico de trastorno de pánico con agorafobia. Se inicia tratamiento con ansiolíticos y terapia cognitivo-conductual."
]

historias_medicas["traumatologia"] = [
    "Consulta por dolor intenso en rodilla derecha tras accidente deportivo. Antecedentes personales sin relevancia traumatológica previa. Se realiza resonancia magnética que muestra ruptura del ligamento cruzado anterior. Paciente ingresa a cirugía ortopédica para reconstrucción ligamentaria.",
    "Consulta por dolor lumbar crónico irradiado a miembro inferior derecho. Antecedentes personales de hernia discal lumbar L4-L5 tratada conservadoramente hace 5 años. Se realiza tomografía computarizada que muestra recurrencia de hernia discal con compresión radicular. Paciente ingresa a cirugía ortopédica para discectomía.",
    "Consulta por dolor en hombro izquierdo tras caída en bicicleta. Antecedentes personales sin relevancia traumatológica previa. Se realiza radiografía que muestra luxación acromioclavicular grado III. Paciente ingresa a cirugía ortopédica para reducción y fijación interna.",
    "Consulta por dolor en cadera derecha tras caída en su domicilio. Antecedentes personales sin relevancia traumatológica previa. Se realiza radiografía que muestra fractura intertrocantérica del fémur derecho. Paciente ingresa a cirugía ortopédica para osteosíntesis.",
    "Consulta por dolor en muñeca derecha tras accidente laboral. Antecedentes personales sin relevancia traumatológica previa. Se realiza radiografía que muestra fractura distal del radio con desplazamiento dorsal. Paciente ingresa a cirugía ortopédica para reducción abierta y fijación interna.",
    "Consulta por dolor en rodilla izquierda y dificultad para caminar tras caída en la calle. Antecedentes personales sin relevancia traumatológica previa. Se realiza radiografía que muestra fractura supracondílea del fémur izquierdo. Paciente ingresa a cirugía ortopédica para reducción abierta y fijación interna.",
    "Consulta por dolor en tobillo derecho tras torcedura durante actividad deportiva. Antecedentes personales sin relevancia traumatológica previa. Se realiza radiografía que muestra fractura bimaleolar del tobillo derecho. Paciente ingresa a cirugía ortopédica para reducción abierta y fijación interna.",
    "Consulta por dolor en hombro derecho tras caída en su domicilio. Antecedentes personales sin relevancia traumatológica previa. Se realiza resonancia magnética que muestra desgarro del manguito rotador. Paciente ingresa a cirugía ortopédica para reparación del manguito rotador.",
    "Consulta por dolor en codo izquierdo tras accidente automovilístico. Antecedentes personales sin relevancia traumatológica previa. Se realiza radiografía que muestra fractura conminuta del olécranon izquierdo. Paciente ingresa a cirugía ortopédica para reducción abierta y fijación interna.",
    "Consulta por dolor en pie derecho tras caída desde altura considerable. Antecedentes personales sin relevancia traumatológica previa. Se realiza radiografía que muestra fractura del calcáneo derecho con desplazamiento significativo. Paciente ingresa a cirugía ortopédica para reducción abierta y fijación interna."
]
