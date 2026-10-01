# Quiz: Exploración de señales EEG con BITalino

**Curso:** Introducción a Señales Biomédicas  
**Grupo:** 10 | **Ciclo:** 2026-II  
**Laboratorio:** 6 | **Guía:** Home-Guide #3, sección 7, preguntas Q1-Q7.

[Volver al informe del Laboratorio 6](README.md)

Las respuestas distinguen el fundamento teórico y el protocolo de la guía de lo que muestran las evidencias de nuestra práctica. Se dispone de dos fotografías y cuatro videos, pero no de archivos digitales de señal EEG exportados de OpenSignals ni de registros etiquetados por condición o posición del sensor. Por ello, las preguntas experimentales se responden con observaciones cualitativas y sus límites, sin inventar mediciones o resultados.

---

## 1. Frecuencias relevantes y diferencias entre áreas cerebrales

**Pregunta:** ¿Cuáles son las frecuencias significativas para adquirir EEG? ¿Son las mismas en todas las áreas del cerebro?

Las principales bandas de interés son delta, theta, alfa, beta y gamma. Para responder este quiz se utilizan los límites de la **Tabla 1 de la guía**, que difieren ligeramente de los empleados en las diapositivas de clase:

| Banda | Intervalo según la guía | Asociación general descrita en la guía |
|---|---|---|
| Delta | 0-4 Hz | Sueño y etapas de sueño profundo. |
| Theta | 4-8 Hz | Somnolencia y actividad relacionada con tareas cognitivas. |
| Alfa | 8-12 Hz | Vigilia relajada, especialmente con ojos cerrados. |
| Beta | 12-25 Hz | Pensamiento activo y actividad mental. |
| Gamma | Mayor de 25 Hz | Procesamiento rápido; su interpretación requiere especial atención a los artefactos. |

Las bandas se definen con los mismos intervalos al comparar las distintas áreas; **lo que cambia es su potencia relativa, distribución espacial y respuesta a la tarea**, no la definición de la banda. La guía relaciona las regiones frontal, temporal, parietal y occipital con funciones diferentes. Por ejemplo, la posición occipital O2 permite explorar la respuesta vinculada a la condición visual, mientras Fp1 y Fp2 permiten estudiar registros frontales. Esto no significa que cada región produzca exclusivamente una sola banda.

El sensor descrito tiene un pasabanda de **0,8-48 Hz**: atenúa la parte más lenta de delta y no permite estudiar toda la actividad gamma. El extremo de 0 Hz de la clasificación de la guía no representa una oscilación adquirida por este sensor. Los **1000 Hz de muestreo** visibles en OpenSignals indican muestras por segundo y deben distinguirse de las frecuencias de las ondas EEG.

**Fuente:** guía, pp. 8-12 y 15; informe y fotografías del laboratorio.

---

## 2. Filtro esencial para trabajar con EEG

**Pregunta:** ¿Qué tipo de filtro es esencial al trabajar con EEG y por qué debemos aplicarlo?

Es esencial un **filtro pasabanda** que conserve el intervalo de interés y atenúe las componentes fuera de él. Según la guía, el sensor BITalino ya filtra la diferencia de potencial entre sus entradas con un pasabanda de **0,8-48 Hz**. Su límite inferior reduce componentes muy lentas y deriva de la línea base, y su límite superior atenúa componentes de alta frecuencia ajenas al intervalo de adquisición.

La señal EEG es pequeña y el sensor utiliza una ganancia elevada, por lo que el registro es sensible a interferencias eléctricas y movimientos. Si persiste contaminación de la red de **50/60 Hz**, puede ser útil un filtro de rechazo de banda estrecha (*notch*) en la frecuencia correspondiente, previa evaluación del registro; este es complementario al pasabanda y **no se afirma que se haya aplicado durante nuestra sesión**.

El filtrado no elimina todos los artefactos: parpadeos, movimientos oculares y contracciones musculares pueden tener componentes dentro del pasabanda. También se necesita buen contacto de los electrodos y controlar los movimientos. Además, el registro mostrado por el equipo ya tiene el acondicionamiento del sensor; no es una señal completamente sin filtrar.

**Fuente:** guía, p. 12.

---

## 3. Influencia de los pensamientos y activación de una banda

**Pregunta:** ¿Podemos influir en el EEG con nuestros pensamientos? ¿Qué acción puede favorecer una banda elegida? ¿Pudimos visualizar ese cambio?

Sí: cambiar la actividad mental o la condición sensorial puede modificar la actividad neuronal y la potencia de algunas bandas. Sin embargo, no se controla voluntariamente una frecuencia exacta ni se obtiene siempre la misma respuesta.

Una acción concreta para explorar la **banda alfa de 8-12 Hz** es permanecer despierto y relajado, cerrar los ojos y comparar el registro con la condición de ojos abiertos. La guía describe un aumento de alfa con los ojos cerrados y una reducción al abrirlos o durante actividad mental. Su Figura 8 muestra un ejemplo de esa respuesta; **ese registro pertenece a la guía, no a nuestro grupo**.

En nuestra práctica se observan variaciones del trazado en OpenSignals, pero las evidencias no identifican con precisión segmentos de ojos abiertos y cerrados. Por eso, **no podemos confirmar que el cambio observado sea un aumento de alfa**. Harían falta segmentos de señal digital etiquetados por condición y una comparación de potencia en la banda, además de revisar posibles artefactos.

**Fuente:** guía, pp. 9, 13 y 15; evidencias audiovisuales del laboratorio.

---

## 4. Evidencia de un segmento del registro y relación con lo esperado

**Pregunta:** Muestra una captura de una porción relevante de EEG del experimento propuesto. ¿Corresponde a lo esperado y por qué?

La siguiente evidencia muestra un segmento del trazado de OpenSignals durante la adquisición. **Es una fotografía de la pantalla tomada en la práctica, no una captura digital exportada del programa.** Se conserva la imagen original para mostrar el contexto del registro y evitar presentar una señal reconstruida como si fuera un dato experimental.

<div align="center">

<img src="evidencias/registro-eeg-02.jpeg" alt="Fotografía de la segunda participante y pantalla de OpenSignals con un segmento del trazado EEG" width="600" />

**Figura 1.** Evidencia original de la segunda participante. En la pantalla inferior se observan oscilaciones y deflexiones de distinta amplitud durante la adquisición.

</div>

[Abrir la fotografía en tamaño completo](evidencias/registro-eeg-02.jpeg)

Se aprecia un trazado irregular, con oscilaciones pequeñas y deflexiones más pronunciadas, incluida una deflexión negativa destacada. Esto es compatible con la visualización de un registro adquirido por el canal EEG y con la posible presencia de artefactos. **No permite confirmar la respuesta específica esperada para ojos cerrados o cálculos mentales**, porque no se conoce qué condición corresponde a ese segmento ni se dispone de datos para analizar sus frecuencias.

Una señal variable es esperable durante la adquisición, pero las deflexiones grandes no prueban mayor actividad cerebral o concentración. En un montaje frontal también pueden influir los ojos, los músculos y el contacto de los electrodos. No se atribuye una causa concreta a cada deflexión ni se extraen amplitudes exactas de esta fotografía.

**Alcance de la evidencia:** no se proporcionó una captura digital con un intervalo de tarea identificado; la fotografía es la evidencia disponible y no sustituye esa comprobación experimental.

**Fuente:** `evidencias/registro-eeg-02.jpeg`; guía, pp. 12-15.

---

## 5. Comparación entre Fp1 y Fp2

**Pregunta:** ¿Existe alguna diferencia en la señal entre las posiciones Fp1 y Fp2?

**Fp1 está en la región frontopolar izquierda y Fp2 en la derecha**, según el sistema internacional 10-20. Los registros pueden diferir por la distribución espacial de la actividad neuronal, la tarea y las condiciones de adquisición. También pueden aparecer diferencias por contacto de los electrodos, posición de la referencia, orientación del montaje bipolar o artefactos. No existe una regla que permita afirmar que una de estas posiciones siempre tendrá mayor amplitud o concentración.

La guía propone repetir las actividades en Fp2, Fp1 y O2. En las evidencias del grupo se observa un montaje frontal en dos participantes, pero no se confirma su ubicación exacta ni se presentan registros separados e identificados como Fp1 y Fp2. **Por ello, no es posible establecer una diferencia experimental entre ambas posiciones con el material disponible.**

Las diferencias entre fotografías de participantes distintos tampoco equivalen a una comparación Fp1-Fp2. Para comprobarla habría que mantener condiciones comparables, identificar cada montaje y tarea, revisar artefactos y comparar los segmentos digitales mediante medidas definidas, como potencia por bandas.

**Fuente:** guía, pp. 10-12 y 14-15; fotografías del laboratorio.

---

## 6. Frecuencias esperadas en las tareas y observación del registro RAW

**Pregunta:** ¿Qué frecuencias deberían cambiar en las tareas propuestas? ¿Se pueden ver esos cambios específicos en la señal RAW? Describe lo observado.

| Condición del protocolo | Cambio teórico que se busca explorar | Alcance en nuestra práctica |
|---|---|---|
| Línea base despierto, relajado y con ojos cerrados | Mayor presencia relativa de alfa, 8-12 Hz, respecto a ojos abiertos. | No hay un segmento digital identificado que permita comprobarla. |
| Alternancia de ojos abiertos y cerrados | Aumento de alfa al cerrar los ojos y reducción al abrirlos; la respuesta puede variar con la posición del sensor. | Las imágenes no identifican los tiempos ni cada condición. |
| Cálculos mentales | Modulación de beta, 12-25 Hz, asociada al pensamiento activo; la guía también relaciona theta, 4-8 Hz, con tareas cognitivas. No se espera un cambio idéntico en todos los sujetos. | No se proporcionaron segmentos etiquetados como cálculos mentales ni potencia por bandas. |

Estos cambios describen **expectativas del protocolo**, no resultados medidos por nuestro grupo. No se espera comprobar sueño profundo ni un aumento de delta únicamente por cerrar los ojos estando despierto.

En un trazado temporal pueden apreciarse cambios de amplitud, regularidad y rapidez de las oscilaciones. Sin embargo, la mezcla de frecuencias y los artefactos impiden identificar de forma fiable una banda solo mirando fotos o videos. Para confirmar cambios específicos se necesitan los datos digitales y un análisis espectral por segmentos o una estimación de potencia por bandas.

En el material disponible se ve un trazado que cambia en el tiempo, con oscilaciones pequeñas y deflexiones más grandes. Uno de los videos muestra ajustes de los audífonos, evento relevante al revisar artefactos; no se puede relacionar cada pico con ese movimiento sin una sincronización precisa. **No podemos afirmar que se haya visto un aumento de alfa, beta o theta en la señal RAW.** Además, incluso el registro denominado RAW en el contexto del equipo ya pasó por la amplificación y el pasabanda del sensor de 0,8-48 Hz.

**Fuente:** guía, pp. 9, 12-15; fotografías y videos del laboratorio.

---

## 7. Amplitud del EEG y nivel de concentración

**Pregunta:** ¿La amplitud del EEG equivale al nivel de concentración aplicado?

**No. La amplitud global del EEG no es una medida directa ni proporcional de concentración.** Depende de la actividad neuronal conjunta, la ubicación y referencia de los electrodos, el contacto con la piel, la ganancia del equipo y los artefactos. Una deflexión grande puede deberse a un parpadeo, actividad muscular o un cambio de contacto, sin representar mayor concentración.

La relación entre una tarea y el EEG se estudia con características específicas, como la potencia de determinadas bandas, bajo condiciones controladas. Por ejemplo, la guía asocia alfa con relajación y beta con pensamiento activo, pero esas asociaciones no permiten convertir la altura del trazado en un porcentaje de atención.

Con nuestras fotos y videos **no se puede cuantificar el nivel de concentración ni ordenar a los participantes según su amplitud EEG**.

**Fuente:** guía, pp. 9 y 12; limitaciones de las evidencias del laboratorio.

---

## Referencias y evidencias

1. PLUX - Wireless Biosignals. **BITalino Home-Guide #3: Electroencephalography (EEG), Exploring Brain Signals.** Versión del 15/02/2021. Secciones 5-7, pp. 8-16 del archivo PDF. La página del quiz es la 16 del PDF, aunque su pie dice “16 of 15”.
2. Grupo 10. [Informe del Laboratorio 6: Adquisición de EEG con BITalino y OpenSignals](README.md). Curso Introducción a Señales Biomédicas, ciclo 2026-II.
3. Grupo 10. [Evidencias de la práctica](evidencias/): dos fotografías, cuatro videos y cuatro miniaturas. En este quiz se reutiliza la fotografía original `registro-eeg-02.jpeg`.

**Comprobación de cobertura:** se responden las siete preguntas y sus subpreguntas; la Q4 incluye una evidencia visual. La confirmación de bandas, condiciones de tarea y diferencias Fp1-Fp2 queda limitada por la ausencia de registros EEG digitales y etiquetas experimentales.
