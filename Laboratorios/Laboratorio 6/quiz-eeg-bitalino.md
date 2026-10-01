# Quiz: Exploración de señales EEG con BITalino

**Curso:** Introducción a Señales Biomédicas  
**Grupo:** 10 | **Ciclo:** 2026-II  
**Laboratorio:** 6 | **Guía:** Home-Guide #3, sección 7, preguntas Q1-Q7.

[Volver al informe del Laboratorio 6](README.md)

Durante la práctica realizamos preguntas para estimular el pensamiento, utilizamos música relajante y música estruendosa, y alternamos ojos abiertos y cerrados mientras observábamos el trazado en OpenSignals. Las respuestas combinan estas actividades, recordadas por el grupo, con las fotografías, los videos y el fundamento de la guía. No se dispone de archivos digitales de EEG para medir potencia por bandas.

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

---

## 2. Filtro esencial para trabajar con EEG

**Pregunta:** ¿Qué tipo de filtro es esencial al trabajar con EEG y por qué debemos aplicarlo?

Es esencial un **filtro pasabanda** que conserve el intervalo de interés y atenúe las componentes fuera de él. Según la guía, el sensor BITalino ya filtra la diferencia de potencial entre sus entradas con un pasabanda de **0,8-48 Hz**. Su límite inferior reduce componentes muy lentas y deriva de la línea base, y su límite superior atenúa componentes de alta frecuencia ajenas al intervalo de adquisición.

La señal EEG es pequeña y el sensor utiliza una ganancia elevada, por lo que el registro es sensible a interferencias eléctricas y movimientos. Si persiste contaminación de la red de **50/60 Hz**, puede ser útil un filtro de rechazo de banda estrecha (*notch*) en la frecuencia correspondiente, previa evaluación del registro; este es complementario al pasabanda y **no se afirma que se haya aplicado durante nuestra sesión**.

El filtrado no elimina todos los artefactos: parpadeos, movimientos oculares y contracciones musculares pueden tener componentes dentro del pasabanda. También se necesita buen contacto de los electrodos y controlar los movimientos. Además, el registro mostrado por el equipo ya tiene el acondicionamiento del sensor; no es una señal completamente sin filtrar.

---

## 3. Influencia de los pensamientos y activación de una banda

**Pregunta:** ¿Podemos influir en el EEG con nuestros pensamientos? ¿Qué acción puede favorecer una banda elegida? ¿Pudimos visualizar ese cambio?

Sí. La actividad mental y los estímulos sensoriales pueden modificar la actividad neuronal y la potencia relativa de algunas bandas. Esto no significa controlar una frecuencia exacta ni obtener la misma respuesta en todas las personas.

En nuestra experiencia hicimos preguntas para que la persona pensara mientras llevaba audífonos y tenía los ojos cubiertos. También utilizamos música relajante y después música estruendosa para explorar posibles cambios del registro. En otra parte, tras permanecer un rato con los ojos cubiertos y los audífonos, se descubrieron los ojos y se indicó mirar la pared; luego se alternó cerrar y abrir los ojos varias veces. El tiempo recordado antes de volver a abrirlos es de aproximadamente **cinco a siete segundos**, sin un conteo exacto de las repeticiones ni una secuencia completa confirmada.

Una acción concreta para explorar la **banda alfa de 8-12 Hz** es comparar ojos cerrados, estando despierto y relajado, con ojos abiertos. Según la guía, alfa puede aumentar con los ojos cerrados y disminuir al abrirlos. Las preguntas que requieren pensar también permiten explorar cambios asociados a la actividad cognitiva.

**Sí observamos variaciones del trazado en OpenSignals durante la sesión.** Esa observación visual no identifica por sí sola la banda que cambió. Para afirmar que aumentó alfa o beta habría que comparar segmentos digitales correspondientes a cada condición. La música tampoco permite asignar automáticamente una banda a cada tipo de sonido.

---

## 4. Muestra del registro y relación con lo esperado

**Pregunta:** Muestra una captura de una porción relevante de EEG del experimento propuesto. ¿Corresponde a lo esperado y por qué?

La siguiente fotografía muestra una porción del registro que visualizamos en OpenSignals durante la práctica. Sirve como muestra del trazado observado al trabajar con estímulos auditivos, preguntas y cambios entre ojos abiertos y cerrados, aunque no recordamos a cuál de esas etapas corresponde exactamente esta imagen.

<div align="center">

<img src="evidencias/registro-eeg-02.jpeg" alt="Fotografía de la segunda participante y pantalla de OpenSignals con un segmento del trazado EEG" width="600" />

**Figura 1.** Registro de la segunda participante en OpenSignals. La pantalla muestra oscilaciones y deflexiones de distinta amplitud.

</div>

La imagen muestra el tipo de señal variable que observamos durante la sesión. **Corresponde a lo esperado en cuanto a visualizar un trazado que varía en el tiempo**, pero la fotografía aislada no demuestra que esas variaciones fueran causadas por la música, las preguntas o la apertura de los ojos.

Para la alternancia de ojos abiertos y cerrados, el cambio teórico esperado era una modificación de la actividad alfa; para las preguntas, una modificación de la actividad relacionada con el pensamiento. En la foto se distinguen oscilaciones pequeñas y deflexiones más marcadas, pero no podemos identificar una banda específica solo por su apariencia. También pueden intervenir parpadeos, movimientos y cambios de contacto de los electrodos.

---

## 5. Comparación entre Fp1 y Fp2

**Pregunta:** ¿Existe alguna diferencia en la señal entre las posiciones Fp1 y Fp2?

**Fp1 está en la región frontopolar izquierda y Fp2 en la derecha**, según el sistema internacional 10-20. Los registros pueden diferir por la distribución espacial de la actividad neuronal, la tarea y las condiciones de adquisición. También pueden aparecer diferencias por contacto de los electrodos, posición de la referencia, orientación del montaje bipolar o artefactos. No existe una regla que permita afirmar que una de estas posiciones siempre tendrá mayor amplitud o concentración.

La guía propone repetir las actividades en Fp2, Fp1 y O2. En las evidencias del grupo se observa un montaje frontal en dos participantes, pero no se confirma su ubicación exacta ni se presentan registros separados e identificados como Fp1 y Fp2. **Por ello, no es posible establecer una diferencia experimental entre ambas posiciones con el material disponible.**

Las diferencias entre fotografías de participantes distintos tampoco equivalen a una comparación Fp1-Fp2. Para comprobarla habría que mantener condiciones comparables, identificar cada montaje y tarea, revisar artefactos y comparar los segmentos digitales mediante medidas definidas, como potencia por bandas.

---

## 6. Frecuencias esperadas en las tareas y observación del registro RAW

**Pregunta:** ¿Qué frecuencias deberían cambiar en las tareas propuestas? ¿Se pueden ver esos cambios específicos en la señal RAW? Describe lo observado.

| Actividad | Cambio que se busca explorar |
|---|---|
| Alternar ojos abiertos y cerrados | Modulación de alfa, **8-12 Hz**: puede aumentar al cerrar los ojos durante la vigilia relajada y disminuir al abrirlos. |
| Responder preguntas que requieren pensar | Cambios de beta, **12-25 Hz**, asociada en la guía al pensamiento activo. Theta, **4-8 Hz**, también puede variar según el tipo y dificultad de la tarea. |
| Escuchar música relajante y después música estruendosa | Posibles cambios de la actividad asociada a relajación, atención o alerta. El tipo de música por sí solo no define una banda ni garantiza un aumento de alfa o beta. |

Estas son expectativas teóricas para interpretar las actividades que realizamos, no cambios de potencia ya medidos. La guía propone cálculos mentales; nuestro recuerdo de la experiencia confirma preguntas para pensar, sin precisar que todas fueran operaciones de cálculo. Cubrir los ojos o escuchar música relajante tampoco demuestra que la persona estuviera dormida.

**Durante la práctica observamos variaciones del trazado en OpenSignals.** En las fotografías y los videos se aprecian oscilaciones de menor amplitud y deflexiones más pronunciadas. No recordamos con certeza qué etapa corresponde a cada fragmento, por lo que no asignamos esos cambios a una música o a una respuesta concreta.

La señal temporal RAW contiene una mezcla de componentes y posibles artefactos. La amplitud o la forma de un pico no basta para identificar alfa, beta o theta. Para comprobar sus cambios específicos se necesitan segmentos digitales identificados por tarea y un análisis de potencia por bandas. Además, el registro del equipo ya pasó por la amplificación y el pasabanda del sensor de **0,8-48 Hz**.

---

## 7. Amplitud del EEG y nivel de concentración

**Pregunta:** ¿La amplitud del EEG equivale al nivel de concentración aplicado?

**No. La amplitud global del EEG no es una medida directa ni proporcional de concentración.** Depende de la actividad neuronal conjunta, la ubicación y referencia de los electrodos, el contacto con la piel, la ganancia del equipo y los artefactos. Una deflexión grande puede deberse a un parpadeo, actividad muscular o un cambio de contacto, sin representar mayor concentración.

La relación entre una tarea y el EEG se estudia con características específicas, como la potencia de determinadas bandas, bajo condiciones controladas. Por ejemplo, la guía asocia alfa con relajación y beta con pensamiento activo, pero esas asociaciones no permiten convertir la altura del trazado en un porcentaje de atención.

Con nuestras fotos y videos **no se puede cuantificar el nivel de concentración ni ordenar a los participantes según su amplitud EEG**.

---

## Referencias y evidencias

1. PLUX - Wireless Biosignals. **BITalino Home-Guide #3: Electroencephalography (EEG), Exploring Brain Signals.** Versión del 15/02/2021. Secciones 5-7, pp. 8-16 del archivo PDF.
2. Grupo 10. [Informe del Laboratorio 6: Adquisición de EEG con BITalino y OpenSignals](README.md). Curso Introducción a Señales Biomédicas, ciclo 2026-II.
3. Grupo 10. [Evidencias de la práctica](evidencias/): dos fotografías, cuatro videos y cuatro miniaturas. En este quiz se reutiliza la fotografía original `registro-eeg-02.jpeg`.
4. Grupo 10. Descripción recordada de las actividades de la sesión: preguntas para pensar, música relajante y estruendosa, y alternancia de ojos abiertos y cerrados. Los tiempos se recuerdan de manera aproximada.
