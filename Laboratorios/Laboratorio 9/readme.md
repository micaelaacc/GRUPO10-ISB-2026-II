# Laboratorio 10 – Procesamiento y análisis de señales EMG

**Curso:** Introducción a las Señales Biomédicas  
**Universidad:** Universidad Peruana Cayetano Heredia  
**Grupo:** 10

## 1. Introducción

En este laboratorio se realizó el procesamiento y análisis de señales electromiográficas (EMG) registradas mediante el sistema BITalino. Estas señales permiten estudiar la actividad eléctrica de los músculos durante diferentes condiciones, como el reposo y la contracción muscular.

A partir de los registros obtenidos, se aplicaron técnicas de filtrado, segmentación y extracción de características para identificar patrones de actividad muscular. Asimismo, se evaluaron métodos de clasificación basados en aprendizaje automático y redes neuronales convolucionales (CNN).

## 2. Objetivos

- Procesar señales EMG para reducir el ruido y facilitar su análisis.
- Identificar los periodos de actividad muscular mediante técnicas de segmentación.
- Extraer características temporales y frecuenciales de las señales.
- Aplicar algoritmos de clasificación LDA, SVM y CNN.
- Analizar posibles cambios en las características de la señal asociados con la fatiga muscular.
- Comparar el comportamiento de una CNN utilizando ventanas de diferentes duraciones.

## 3. Materiales y herramientas

Para el desarrollo del laboratorio se utilizaron:

- Sistema de adquisición BITalino.
- Electrodos superficiales para el registro EMG.
- Registros experimentales `BASELINEBRAZO.txt` y `PRUEBABRAZO1.txt`.
- Google Colab y Python.
- Bibliotecas NumPy, Pandas, SciPy, Matplotlib, Scikit-learn y TensorFlow/Keras.

## 4. Metodología

### 4.1. Adquisición de señales

Se trabajó con dos registros de actividad muscular obtenidos mediante BITalino, utilizando una frecuencia de muestreo de 1000 Hz.

Los registros contienen información de la actividad eléctrica del músculo, lo que permitió comparar el comportamiento de la señal durante periodos de reposo y contracción.

### 4.2. Preprocesamiento

Se aplicaron técnicas de filtrado para disminuir las interferencias presentes en los registros y conservar las componentes relevantes de la señal EMG.

Posteriormente, se analizaron las señales mediante representaciones temporales y frecuenciales para observar sus principales características.

### 4.3. Segmentación y extracción de características

Se utilizó el valor RMS como indicador de la actividad muscular, permitiendo identificar periodos de contracción.

En el análisis se detectaron 21 episodios de contracción y se obtuvieron 504 ventanas de 250 ms.

También se calcularon características temporales y frecuenciales para describir el comportamiento de la señal y utilizarlas en los modelos de clasificación.

### 4.4. Clasificación de señales

Se evaluaron diferentes métodos de clasificación:

- **LDA:** para analizar la separación de clases mediante combinaciones lineales de las características.
- **SVM:** para establecer fronteras de decisión entre las clases.
- **CNN:** para reconocer patrones a partir de representaciones de las señales EMG.

Adicionalmente, se compararon redes CNN utilizando ventanas de 250 ms y 500 ms.

### 4.5. Análisis de fatiga muscular

Se estudiaron cambios en las características de la señal EMG que podrían estar relacionados con la fatiga muscular, considerando parámetros de amplitud y contenido frecuencial.

Este análisis permitió observar tendencias en los registros, aunque estas no representan por sí solas una confirmación clínica de fatiga.

## 5. Resultados

El procesamiento permitió identificar los periodos de actividad muscular y extraer características relevantes para su posterior clasificación.

| Parámetro | Resultado |
|---|---|
| Frecuencia de muestreo | 1000 Hz |
| Contracciones detectadas | 21 |
| Ventanas de 250 ms | 504 |
| Exactitud balanceada CNN (250 ms) | 96.8 % |
| Exactitud balanceada CNN (500 ms) | 97.6 % |

En la comparación realizada, la CNN con ventanas de 500 ms presentó una exactitud balanceada ligeramente superior a la obtenida con ventanas de 250 ms.

Sin embargo, estos resultados corresponden a etiquetas generadas automáticamente a partir de los registros. Por ello, no deben interpretarse como una validación del modelo en nuevos sujetos ni como evidencia de desempeño clínico.

## 6. Conclusiones

- El procesamiento permitió identificar los periodos de contracción muscular y obtener características representativas de la señal EMG.
- La extracción de características temporales y frecuenciales facilitó el análisis de la actividad muscular y su utilización en diferentes métodos de clasificación.
- Las redes CNN permitieron reconocer patrones dentro de los registros analizados. En esta evaluación, las ventanas de 500 ms obtuvieron resultados ligeramente superiores a las de 250 ms.
- El análisis de fatiga permitió explorar posibles variaciones en la actividad muscular; sin embargo, sería necesario contar con más registros y un protocolo específico para establecer conclusiones más sólidas.
- En general, el laboratorio permitió aplicar técnicas de procesamiento digital de señales y aprendizaje automático al estudio de señales biomédicas reales.

## 7. Archivos del laboratorio

- **`Laboratorio_10_EMG_COMPLETO.ipynb`:** cuaderno con el desarrollo del laboratorio, código, gráficas, ejercicios y resultados.
- **`BASELINEBRAZO.txt`:** registro EMG utilizado en el análisis.
- **`PRUEBABRAZO1.txt`:** registro experimental de actividad muscular.
- **`electrodos_brazo.PNG`:** fotografía de la colocación de los electrodos.
- **`ploteo_brazo.PNG`:** fotografía del registro experimental.

## 8. Ejecución

El laboratorio se encuentra desarrollado en Google Colab:

[**Abrir Laboratorio 10 en Google Colab**](https://colab.research.google.com/drive/1_4b6LCzWWPBAypdKJrUT7dnn10iuaHbP)

Para revisar los resultados:

1. Abrir el cuaderno mediante el enlace.
2. Seleccionar **Entorno de ejecución → Ejecutar todas**.
3. Revisar las gráficas, características extraídas y resultados de clasificación.

El cuaderno incluye los datos necesarios para reproducir el análisis sin tener que cargar manualmente los registros originales.

## 9. Observaciones

Los resultados fueron obtenidos a partir de los registros experimentales utilizados durante el laboratorio. Debido a que las etiquetas de contracción se estimaron automáticamente, las métricas de clasificación deben interpretarse considerando las limitaciones de este procedimiento.

Para evaluar la capacidad de generalización de los modelos sería necesario incorporar registros adicionales y etiquetas de referencia independientes.
