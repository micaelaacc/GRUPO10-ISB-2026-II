# Laboratorio 05 — Planteamiento del proyecto

# EyeTalk: Sistema de comunicación asistida mediante señales EOG


## Video de presentación

[Ver presentación de EyeTalk](https://drive.google.com/drive/folders/1I8qH7lWKL6E-CYdp41NjwEv9tynHp5Rc?usp=sharing)

## 1. Planteamiento del problema

Las personas con esclerosis lateral amiotrófica (ELA) pueden perder la capacidad de hablar y presentar dificultades para utilizar las manos, lo que limita el acceso a herramientas convencionales de comunicación.

Cuando conservan movimientos oculares voluntarios, pueden comunicarse mediante miradas o parpadeos interpretados por un cuidador. Sin embargo, esta dependencia dificulta expresar necesidades y decisiones de manera autónoma.

EyeTalk surge como una propuesta para aprovechar los movimientos oculares como medio de selección de mensajes con salida de voz.

## 2. Usuario objetivo

Personas adultas con ELA que presentan limitaciones graves del habla y del uso de las manos, pero conservan:

- Movimientos oculares voluntarios.
- Capacidad para comprender instrucciones.
- Visión suficiente para observar un tablero de comunicación.

La propuesta dependerá de las capacidades conservadas de cada persona y no estará dirigida a todos los pacientes con ELA.

## 3. Objetivo del proyecto

Desarrollar una prueba de concepto que permita convertir movimientos oculares y patrones de parpadeo, registrados mediante electrooculografía, en comandos para seleccionar y reproducir mensajes.

## 4. Propuesta de solución

EyeTalk integrará la adquisición de señales EOG, su procesamiento digital y un tablero de comunicación.

Se plantea utilizar dos canales: uno horizontal para identificar movimientos hacia izquierda y derecha, y uno vertical para registrar eventos asociados al parpadeo. La configuración de adquisición y los sensores compatibles con BITalino deberán verificarse durante las pruebas iniciales.

| Acción del usuario | Función propuesta |
|---|---|
| Mirar hacia la izquierda | Desplazarse a la opción anterior. |
| Mirar hacia la derecha | Desplazarse a la siguiente opción. |
| Realizar un doble parpadeo | Seleccionar el mensaje resaltado. |
| Permanecer en reposo | Mantener la selección sin ejecutar comandos. |

El doble parpadeo se evaluará como estrategia para reducir selecciones accidentales. Su uso no garantiza por sí solo la eliminación de falsos positivos.

## 5. Procesamiento de la señal

El procesamiento previsto comprende las siguientes etapas:

1. **Adquisición:** registro de EOG horizontal y vertical mediante BITalino y sensores compatibles.
2. **Filtrado digital:** reducción de ruido y tratamiento de la deriva.
3. **Acondicionamiento:** ajuste de línea base y normalización.
4. **Extracción de características:** amplitud, pendiente y duración de los eventos.
5. **Clasificación:** identificación de izquierda, derecha, parpadeo y reposo.
6. **Interpretación de comandos:** reconocimiento de la secuencia de doble parpadeo y actualización del tablero.

Se iniciará con detección mediante umbrales y posteriormente se evaluará un clasificador de machine learning, como una máquina de vectores de soporte (SVM).

Los parámetros de procesamiento se ajustarán según las características de las señales adquiridas.

## 6. Frontend: tablero de comunicación

La interfaz mostrará mensajes predefinidos y resaltará la opción seleccionada. Una vez confirmado el comando, el mensaje aparecerá en pantalla y se reproducirá mediante voz.

| Mensajes iniciales |
|---|
| Tengo sed |
| Tengo dolor |
| Llamar a la enfermera |
| Sí |
| No |

Los mensajes podrán adaptarse al entorno de uso y a las necesidades del usuario. Se contempla incorporar opciones de cancelación y pausa.

## 7. Adquisición de datos

Se propone construir una base de datos propia con registros de:

- Movimientos oculares hacia la izquierda.
- Movimientos oculares hacia la derecha.
- Parpadeos simples y dobles.
- Periodos de reposo.
- Movimientos espontáneos para evaluar activaciones accidentales.

Las pruebas iniciales se realizarán con participantes sanos, con consentimiento y siguiendo las indicaciones del laboratorio. Se utilizarán sesiones separadas para entrenamiento y evaluación.



## 8. Plan de trabajo y evaluación

| Etapa | Actividad |
|---|---|
| 1 | Verificar el equipo, adquirir señales y realizar filtrado preliminar. |
| 2 | Extraer características y desarrollar la detección por umbrales. |
| 3 | Entrenar y evaluar el clasificador. |
| 4 | Integrar el procesamiento con el tablero y la salida de voz. |
| 5 | Realizar pruebas de funcionamiento y documentar resultados. |

Se plantea como meta inicial superar el **90 % de exactitud en la clasificación de los cuatro eventos**, sujeto a evaluación experimental.

También se medirán las selecciones correctas, las activaciones accidentales y el tiempo necesario para transmitir un mensaje. La exactitud del clasificador se evaluará por separado del funcionamiento completo del comunicador.

## 9. Alcance

El resultado esperado es un prototipo funcional de laboratorio que permita seleccionar mensajes mediante EOG.

Las pruebas iniciales permitirán evaluar su viabilidad técnica. La utilidad clínica en personas con ELA requerirá una evaluación posterior con la población objetivo.

## 10. Referencias

1. Chang WD, et al. Development of an electrooculogram-based eye-computer interface for communication of individuals with amyotrophic lateral sclerosis. *Journal of NeuroEngineering and Rehabilitation*. 2017;14:89.  
   https://doi.org/10.1186/s12984-017-0303-5

2. Tonin A, et al. Auditory Electrooculogram-based Communication System for ALS Patients in Transition from Locked-in to Complete Locked-in State. *Scientific Reports*. 2020;10:8452.  
   https://doi.org/10.1038/s41598-020-65333-1