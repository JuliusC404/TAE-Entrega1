# Predicción de la satisfacción de niños y abuelos según la composición de su hogar y otros determinantes
Alejandro Betancur Quiroz 1007286609
Julian Esteban Carvajal Ramírez 1001774262
Wilfer Mauricio Chavarría Jaramillo 1035833003
Alejandro Bedoya Taborda 1152226157

link del aplicativo: http://tae-entrega1.herokuapp.com/index/inicio/-/

# Reporte técnico

# Introducción
El presente trabajo va referido al análisis de datos suministrados por el Departamento Administrativo Nacional de Estadística (DANE) específicamente tomando los datos de la **[Encuesta de Calidad de Vida 2020](https://www.dane.gov.co/index.php/estadisticas-por-tema/pobreza-y-condiciones-de-vida/calidad-de-vida-ecv)** el cual es un instrumento diseñado para realizar el seguimiento y la medición de las condiciones socioeconómicas de los habitantes de una región. Esta investigación cuantifica y caracteriza las condiciones de vida de los colombianos incluyendo variables relacionadas con la vivienda, las personas para los que se incluyen variables de: educación, salud, cuidado de los niños, fuerza de trabajo, gastos e ingresos, etc., y los hogares que involucra variables como: tenencia de bienes y percepción del jefe o del cónyuge sobre las condiciones de vida en el hogar.

# Objetivo
- Realizar un análisis descriptivo de los datos suministrados por el DANE.
- Desarrollar modelo predictivo para predecir el nivel de satisfacción de niños y abuelos de acuerdo con la composición del hogar y actividades realizadas diariamente.
- Entender como un abuelo y un niño o niña pueden estar satisfechos con su vida, a través de la construcción de variables predictivas.
- Crear aplicación web para la exploración de resultados.
- Crear un video para promocionar el estudio realizado y dar a conocer los resultados y conclusiones.

# Encuesta de Calidad de Vida 2020

La base de datos empleada corresponde a la **[Encuesta de Calidad de Vida 2020](https://www.dane.gov.co/index.php/estadisticas-por-tema/pobreza-y-condiciones-de-vida/calidad-de-vida-ecv)** (ECV-2020), realizada por el Departamento Administrativo Nacional de Estadísticas (DANE). La cual se ha realizado periódicamente desde aproximadamente 20 años y de forma anual desde el año 2010.  Así mismo, la aplicación de esta encuesta se ha realizado desde sus inicios en las principales regiones del país, sin embargo, desde el año 2017 se extendió su aplicación a todas las regiones del país.

La ECV es una operación estadística que tiene como objetivo caracterizar aspectos relacionados con el bienestar de los hogares de todo Colombia, tanto en área urbanas, cabeceras municipales y áreas rurales alejadas. El análisis posterior de esta encuesta ha permitido determinar y explicar los diferentes niveles de vida existentes en la sociedad colombiana. Además, es la fuente de información principal del cálculo del Índice de Pobreza Multidimensional (IPM).

La encuesta de 2020 incluye una lista de capítulos base que se ha venido manteniendo desde 2010, estos se describen brevemente a continuación:

1. [Datos de la vivienda](https://microdatos.dane.gov.co/index.php/catalog/718/datafile/F17): material de paredes y pisos.
2. [Servicios del hogar](https://microdatos.dane.gov.co/index.php/catalog/718/datafile/F2): conexión a servicios públicos, privados o comunales y calidad de los mismos y clasificación de basuras.
3. [Características y composición del hogar](https://microdatos.dane.gov.co/index.php/catalog/718/datafile/F3): sexo, edad, parentesco, estado civil, migración, estudios de padre y madre cuando estos no residen en el hogar.
4. [Salud](https://microdatos.dane.gov.co/index.php/catalog/718/datafile/F5): cobertura del sistema de seguridad social por regímenes, morbilidad, acciones tomadas para enfrentar enfermedades padecidas durante los últimos 30 días, tiempo para la atención en urgencias y para la consulta médica, fuentes para cubrir los gastos en salud y opinión sobre la calidad de los servicios.
5. [Atención integral de los niños y niñas menores de 5 años](https://microdatos.dane.gov.co/index.php/catalog/718/datafile/F4): sitio de permanencia de los niños menores de cinco años durante la mayor parte del tiempo entre semana, tipo de hogar comunitario, guardería, jardín o centro de desarrollo infantil al que asisten, persona que se encarga del cuidado de los niños menores de 5 años, niños que son llevados a control de crecimiento y desarrollo.
6. [Educación (personas de 5 años y más)](https://microdatos.dane.gov.co/index.php/catalog/718/datafile/F6): alfabetismo, asistencia escolar, máximo nivel educativo alcanzado y último año aprobado o que esté cursando, tasas brutas y netas de escolaridad, becas, subsidios y créditos.
7. [Fuerza de trabajo (personas de 12 años y más)](https://microdatos.dane.gov.co/index.php/catalog/718/datafile/F7): población económicamente activa (PEA), población económicamente inactiva (PEI), ocupados, rama de actividad, posición ocupacional, sitio de trabajo, tamaño de la empresa, tipo de transporte utilizado para desplazarse al trabajo e ingresos.
8. [Tecnologías de información y comunicación (TIC)](https://microdatos.dane.gov.co/index.php/catalog/718/data_dictionary#:~:text=126-,Tecnologias%20de%20informacion%20y%20comunicacion,-Esta%20tabla%20contiene): frecuencias de uso de computador y de internet, lugares de acceso a Internet y servicios o actividades para uso de internet y tenencia de celular.
9. [Trabajo infantil](https://microdatos.dane.gov.co/index.php/catalog/718/datafile/F9): actividad principal realizada por los menores de 5 a 11 años en la semana de referencia, ocupación, actividad donde realizan la labores, ingresos percibidos y sitios de trabajo y horas trabajadas.
10. [Tenencia y financiación de la vivienda que ocupa el hogar](https://microdatos.dane.gov.co/index.php/catalog/718/datafile/F11): tipo de tenencia de la vivienda; tenencia de escritura de propiedad; subsidios recibidos para la compra, construcción, mejora, titulación o escrituración de la vivienda.
11. [Condiciones de vida del hogar y tenencia de bienes](https://microdatos.dane.gov.co/index.php/catalog/718/datafile/F12): percepción del jefe o cónyuge sobre las condiciones de vida del hogar, hechos de los que han sido víctimas los miembros del hogar en los últimos 12 meses, ayudas o subsidios recibidos por miembros del hogar en los últimos 12 meses, tenencia de bienes en el hogar y conexión a internet.

Sumado a estas, en esta encuesta se realizó un capítulo especial llamado [Gastos de los hogares](https://microdatos.dane.gov.co/index.php/catalog/718/datafile/F15). Donde se pregunta sobre el nivel de gasto de los hogares en los distintos bienes y servicios de la canasta familiar de acuerdo con la clasificación del consumo individual por finalidad (COICOP).

# Base de datos

La base de datos de la [ECV-2020](https://microdatos.dane.gov.co/index.php/catalog/718/study-description) se encuentra en el Archivo Nacional de Datos (ANDA) del DANE. En el caso de esta encuesta en particular, los 12 diferentes capítulos se segregan en 16 tablas disponibles para su descarga en 3 formatos diferentes (CSV, DTA y SAV). Cabe resaltar que la asignación de la variables o indicativo en cada tabla para las diferentes preguntas, junto con las posibles respuestas de estas se describen en el [diccionario de datos](https://microdatos.dane.gov.co/index.php/catalog/718/data_dictionary) asociado a esta encuesta.

## Descripción técnica

Es necesario destacar que los diferentes capítulos (tablas) de la encuesta pueden ser divididos en tres grupos: viviendas, hogares y personas. Estos están relacionados con diferentes niveles estructurados en que es recolectada la información. En este caso, una misma vivienda puede agrupar diferentes hogares que se encuentran en la misma ubicación y, a su vez, un mismo hogar puede agrupar diferentes personas que residen en este. La pertenencia de las tablas a los grupos mencionados se presenta a continuación:

|      Viviendas       | Hogares                                                      | Personas                                                     |
| :------------------: | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Datos de la vivienda | Servicios del hogar<br />Tenencia y financiación de la vivienda<br />Condiciones de vida del hogar y tenencia de bienes<br />Gastos del hogar lugares de compra<br />Gastos del hogar gastos por ítem<br />Preguntas de tenencia y financiación de la vivienda<br />Preguntas condiciones de vida del hogar y tenencia de bienes | Características y composición del hogar<br />salud<br />atención integral de niños y niñas menores de 5 años<br />educación<br />fuerza de trabajo<br />tecnologías de información y comunicación<br />trabajo infantil |

Específicamente, la base de datos corresponde a una de tipo relacional, donde las relaciones entre tablas son de tipo *padre-hijo*. Además, las "llaves" empleadas para unir las diferentes tablas son llamadas en cada una de estas como: "DIRECTORIO", "SECUENCIA_ENCUESTA" y "SECUENCIA_P".

De acuerdo con esta relación tabla padre – tabla hijo, las llaves son:

* Llave entre tablas de vivienda y hogar: DIRECTORIO.
* Llave entre tablas de vivienda y personas: DIRECTORIO.
* Llave entre tablas de hogares: DIRECTORIO Y SECUENCIA_ENCUESTA.
* Llave entre tablas de hogar y de personas: DIRECTORIO y SECUENCIA_ENCUESTA de la tabla de hogares con DIRECTORIO y SECUENCIA_P de la tabla de personas.
* Llave entre tablas de personas: DIRECTORIO, SECUENCIA_P y SECUENCIA_ENCUESTA

La información presentada en este apartado es derivada del documento de estructuración de la base de datos realizado por el DANE. Para conocer más información de la base de datos original por favor remítase al [Link](https://microdatos.dane.gov.co/index.php/catalog/718/download/20590/Estructura%20de%20Base%20de%20Datos%20ECV%202020.pdf).

Colombia - Encuesta Nacional de Calidad de Vida - ECV 2020. Microdatos.dane.gov.co. (2021). Retrieved 2 May 2022, from https://microdatos.dane.gov.co/index.php/catalog/718/get_microdata.

# Ingeniería de características

El objetivo último de los modelos desarrollados es predecir la satisfacción de dos grupos poblacionales: niños y abuelos. Por lo que es necesario, determinar edades que segregan ambos grupos poblacionales.

En el caso de los abuelos, se toma los 60 años como edad para limitar este grupo poblacional. Cabe resaltar, que no se toma el término abuelo como referencia a las personas que tienen nietos sino que se toma como referencia a aquellas personas que son adultos mayores o que ya han entrado en una etapa final de envejecimiento humano tal como lo expresa el Ministerio de Salud de Colombia en la definición de ["Envejecimiento y Vejez"](https://www.minsalud.gov.co/proteccionsocial/promocion-social/Paginas/envejecimiento-vejez.aspx).

Colombia, M. (2022). Envejecimiento y Vejez. Minsalud.gov.co. Retrieved 2 May 2022, from https://www.minsalud.gov.co/proteccionsocial/promocion-social/Paginas/envejecimiento-vejez.aspx.

En el caso de los niños, se toma los 5 años como edad para limitar este grupo poblacional. 

# Resultados

En los adultos mayores se tuvieron en cuenta las preguntas sobre la satisfacción en diferentes aspectos de su vida, tal como el salario, la salud, la seguridad, su trabajo, etc.
