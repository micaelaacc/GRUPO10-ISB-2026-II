# Laboratorio 6: Electroencefalografía (EEG)

**Curso:** Introducción a Señales Biomédicas

**Grupo:** 10 | **Ciclo:** 2026-II

## 1. Introducción y objetivos

En esta sesión relacionamos los fundamentos de la electroencefalografía con la adquisición de una señal mediante BITalino y su visualización en OpenSignals. El EEG registra diferencias de potencial en la superficie de la cabeza, asociadas principalmente con la actividad postsináptica conjunta de poblaciones de neuronas corticales.

Los objetivos fueron comprender el origen de la señal EEG, reconocer sus principales bandas de frecuencia y familiarizarnos con el montaje de adquisición. La práctica también permitió observar la importancia de la colocación de electrodos y del control de movimientos para obtener un registro interpretable.

## 2. Resumen de la clase

### Bases fisiológicas

El sistema nervioso central comprende el encéfalo y la médula espinal; el periférico incluye nervios y ganglios. Las neuronas se comunican mediante sinapsis que producen respuestas excitadoras o inhibidoras. En el EEG de superficie destaca la contribución de las neuronas piramidales, cuya orientación favorece la suma de sus campos eléctricos. El registro refleja actividad colectiva, no el potencial de acción de una neurona aislada.

Los tejidos entre la corteza y los electrodos atenúan y distribuyen espacialmente la señal, que se expresa habitualmente en microvoltios (µV). Los circuitos entre el tálamo y la corteza participan en la generación de ritmos durante la vigilia y el sueño. [1, diap. 7–14; 2, p. 8]

| Región cerebral | Funciones relacionadas revisadas en clase |
|---|---|
| Frontal | Planificación, atención, razonamiento y control motor voluntario. |
| Parietal | Integración sensorial y orientación espacial. |
| Temporal | Audición, memoria y procesamiento del lenguaje. |
| Occipital | Procesamiento de información visual. |

### Electrodos, canales y sistema 10-20

Un canal de EEG representa una **diferencia de potencial entre dos puntos**. El sistema internacional 10-20 permite ubicar electrodos según proporciones de las dimensiones de la cabeza, utilizando referencias anatómicas como el nasion y el inion.

- Las letras indican la región: Fp (frontopolar), F (frontal), C (central), P (parietal), T (temporal) y O (occipital).
- Los números impares corresponden al hemisferio izquierdo y los pares al derecho.
- La letra **z** identifica la línea media.

El montaje bipolar de BITalino utiliza dos entradas de medición, **IN+ e IN−**, y una conexión adicional de referencia. La guía propone colocar esta referencia en una zona ósea detrás de la oreja. La práctica documentada muestra un montaje frontal; las fotografías no permiten confirmar su correspondencia exacta con Fp1 o Fp2. [1, diap. 31–32; 2, pp. 10–12]

### Ritmos del EEG

Las bandas permiten describir el contenido de frecuencia de una señal. Sus límites varían ligeramente entre las fuentes; la tabla utiliza los rangos de la clase.

| Banda | Frecuencia en la clase | Asociación general |
|---|---|---|
| Delta | 0,5–4 Hz | Sueño profundo. |
| Theta | 4–8 Hz | Somnolencia y etapas iniciales del sueño. |
| Alfa | 8–13 Hz | Vigilia relajada; puede aumentar al cerrar los ojos. |
| Beta | 13–30 Hz | Vigilia activa y actividad mental. |
| Gamma | 30–100 Hz | Procesos de atención e integración de información. |

La guía de BITalino emplea alfa de 8–12 Hz, beta de 12–25 Hz y gamma por encima de 25 Hz. Por ello, en un análisis cuantitativo habría que declarar los intervalos elegidos. Además, el ancho de banda del sensor descrito en la guía, **0,8–48 Hz**, no permite estudiar íntegramente todos los rangos de la tabla. [1, diap. 33–34; 2, pp. 9–12]

### Sueño y aplicaciones

La clase distingue sueño **no REM** (N1, N2 y N3) y **REM**. N1 corresponde a la transición desde la vigilia; N2 presenta husos del sueño y complejos K; N3 se caracteriza por actividad delta de gran amplitud. REM presenta actividad de baja amplitud y frecuencias mixtas. Aquí se sigue la clasificación N1–N3 de las diapositivas 35–36, ya que las diapositivas previas de ritmos emplean otra numeración de etapas.

También se revisaron Alzheimer, accidente cerebrovascular, meningitis y epilepsia como contexto de las alteraciones neurológicas. Se presentaron modalidades de EEG de rutina, prolongado, ambulatorio y video-EEG. En el estudio del sueño, la polisomnografía combina EEG con señales oculares, musculares, respiratorias y de oxigenación. Como aplicaciones adicionales se discutieron las interfaces cerebro-computadora y la combinación de EEG con estimulación magnética transcraneal. [1, diap. 17–40; 2, p. 13]

## 3. Materiales y montaje

En las evidencias se observan:

- Placa BITalino y batería.
- Sensor de EEG con electrodos adhesivos en la frente y cables de conexión.
- Computadora con OpenSignals para visualizar la señal.
- Audífonos utilizados por los participantes.

La guía especifica electrodos pregelificados de Ag/AgCl, dos contactos de medición y una referencia adicional. Los audífonos son visibles, pero las imágenes no permiten determinar qué audio se reprodujo ni establecer su efecto sobre el registro. [2, pp. 6 y 11–12]

## 4. Desarrollo de la práctica

### Registro documentado

Se colocó el sensor en la zona frontal y se conectó el sistema a BITalino. Los participantes permanecieron sentados mientras la señal se mostraba en OpenSignals. Las fotografías documentan el montaje en dos participantes; los videos muestran la evolución del trazado durante la adquisición.

En la interfaz fotografiada se distingue una frecuencia de muestreo de **1000 Hz** y un canal identificado como **4 / EEG / A4**. La frecuencia de muestreo indica cuántas muestras se adquieren por segundo y no debe confundirse con la frecuencia de las ondas cerebrales.

En los videos aparecen segmentos de distinta amplitud y cambios transitorios del trazado. También se observa manipulación de los audífonos en uno de los registros, lo que subraya la necesidad de anotar los movimientos durante la adquisición.

### Protocolo de referencia de la guía

La guía plantea la siguiente secuencia para comparar condiciones: [2, pp. 14–15]

1. Preparar el montaje frontal y colocar la referencia detrás de la oreja.
2. Configurar OpenSignals y seleccionar una frecuencia de muestreo apropiada para el ancho de banda.
3. Registrar una línea base de 30 segundos, procurando evitar movimientos.
4. Alternar ojos abiertos y cerrados cinco veces, manteniendo cada condición durante cinco segundos.
5. Registrar otra línea base de 30 segundos.
6. Realizar cálculos mentales y guardar la adquisición.
7. Repetir la experiencia en Fp2, Fp1 y O2 para comparar ubicaciones.

Esta secuencia describe la propuesta de la guía. Las evidencias aportadas no documentan por completo sus tiempos, repeticiones, cálculos mentales o cambios de ubicación, por lo que no se presentan como etapas verificadas de nuestra sesión.

## 5. Observaciones y discusión

| Observación en las evidencias | Interpretación y alcance |
|---|---|
| OpenSignals muestra un trazado variable durante el registro. | Se documenta la adquisición y visualización de la señal del canal EEG. |
| Hay oscilaciones de menor amplitud y deflexiones más pronunciadas. | La amplitud cambia en el tiempo; una deflexión grande, por sí sola, no demuestra mayor actividad cerebral ni concentración. |
| El montaje se encuentra cerca de los ojos y músculos faciales. | Los parpadeos, movimientos oculares y contracciones pueden contaminar el registro. |
| Se observan ajustes de los audífonos durante un video. | Son eventos relevantes para revisar posibles artefactos; no se puede atribuir cada pico a una causa sin sincronización precisa. |
| Se registró a dos participantes. | Las imágenes no bastan para comparar su potencia por bandas ni su estado de atención. |

La guía describe una ganancia de **40 000** y un filtrado pasabanda de **0,8–48 Hz** para el sensor. La elevada sensibilidad hace importante mantener un buen contacto electrodo-piel y reducir movimientos e interferencia eléctrica. El filtrado limita frecuencias no deseadas, pero no elimina necesariamente artefactos que comparten el rango del EEG. [2, p. 12]

Según la guía, cerrar los ojos durante la vigilia relajada puede favorecer la actividad alfa. Sin embargo, para comprobarlo en esta práctica se necesitarían los datos originales, segmentos identificados por condición y un análisis espectral. **Las fotos y los videos del trazado no permiten afirmar que predominó una banda específica ni cuantificar cambios de potencia.**

El material recibido contiene evidencia visual, pero no archivos de señal exportados de OpenSignals. Por ello, este resumen presenta observaciones cualitativas: no se calcularon espectros, amplitudes exactas, diferencias entre Fp1 y Fp2 ni indicadores de concentración.

## 6. Evidencias de la sesión

### Fotografías

<img src="evidencias/registro-eeg-01.jpeg" alt="Primer participante con montaje frontal y señal EEG visualizada en OpenSignals" width="520">

*Figura 1. Montaje frontal, BITalino y visualización de la señal en el primer participante.*

<img src="evidencias/registro-eeg-02.jpeg" alt="Segunda participante con electrodos frontales, audífonos y registro en OpenSignals" width="520">

*Figura 2. Registro en una segunda participante; el trazado presenta variaciones y deflexiones de distinta amplitud.*

### Videos

Los archivos conservan el contenido original. Las horas de esta tabla proceden de los nombres de los archivos de WhatsApp.

| Archivo original del 25/09/2026 | Evidencia visual | Enlace |
|---|---|---|
| 3.23.11 PM | Primer participante y trazado en OpenSignals. | [Ver video 1](evidencias/video-eeg-01.mp4) |
| 3.23.31 PM | Continuación del registro y variaciones del trazado. | [Ver video 2](evidencias/video-eeg-02.mp4) |
| 3.25.43 PM | Adquisición con ajustes de los audífonos durante el registro. | [Ver video 3](evidencias/video-eeg-03.mp4) |
| 3.26.09 PM | Registro en la segunda participante. | [Ver video 4](evidencias/video-eeg-04.mp4) |

## 7. Conclusiones

La sesión permitió relacionar la actividad eléctrica colectiva de las neuronas con un registro de superficie y reconocer los elementos de un sistema de adquisición EEG. BITalino y OpenSignals facilitaron observar la señal durante la práctica.

La calidad del registro depende del montaje, del contacto de los electrodos y del control de artefactos. Los cambios de amplitud observados no equivalen directamente a cambios en la concentración: deben interpretarse considerando movimientos, interferencias y condiciones experimentales.

Para comparar ojos abiertos y cerrados, tareas mentales o regiones cerebrales, se requiere conservar la señal digital y marcar cada condición. El análisis por bandas permitiría contrastar las observaciones con los ritmos estudiados en clase.

## 8. Fuentes

1. De La Cruz, L.; Meza, M.; Cáceres, J. A. **Electroencefalograma: Ritmos, medición, adquisición y canales.** Material de clase proporcionado: `Clase EEG_2026_02.pptx`, 44 diapositivas.
2. PLUX – Wireless Biosignals. **BITalino Home-Guide #3: Electroencephalography (EEG), Exploring Brain Signals.** Material proporcionado: `HomeGuide3_EEG.pdf`, versión fechada el 15/02/2021. Se consultaron especialmente las páginas 8–15.
3. **Evidencias del grupo:** dos fotografías y cuatro videos proporcionados, identificados en sus nombres como archivos del 25/09/2026 e incluidos en la carpeta `evidencias/`.
