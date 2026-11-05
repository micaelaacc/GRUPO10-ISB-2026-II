# Laboratorio 11 – Extracción de características y clasificación de señales ECG

**Curso:** Introducción a las Señales Biomédicas  
**Universidad:** Universidad Peruana Cayetano Heredia  
**Grupo:** 10

## 1. Introducción

En este laboratorio trabajamos con registros electrocardiográficos (ECG) obtenidos con BITalino. El propósito fue identificar los latidos, extraer información de cada uno y comparar distintos algoritmos de aprendizaje automático para reconocer las condiciones en las que se registró la señal.

Se analizaron cuatro condiciones: basal, hiperventilación, hipoventilación y aeróbica. Para cada una se contó con registros de las derivaciones D1, D2 y D3, por lo que trabajamos con 12 archivos en total.

## 2. Objetivos

- Revisar la calidad de los registros y comparar la frecuencia cardíaca entre condiciones.
- Filtrar las señales ECG para reducir las interferencias presentes en la adquisición.
- Detectar los picos R y separar los latidos para su análisis.
- Calcular características de ritmo, morfología, estadística y frecuencia.
- Comparar cinco clasificadores y evaluar los resultados mediante F1-score macro.

## 3. Materiales y herramientas

- BITalino (r)evolution y sensor ECG.
- Registros ECG de las cuatro condiciones en las derivaciones D1, D2 y D3.
- Google Colab y Python.
- Bibliotecas NumPy, Pandas, SciPy, Matplotlib, PyWavelets y Scikit-learn.

Los registros fueron adquiridos a **1000 Hz** y con una resolución de **10 bits**.

## 4. Metodología

### 4.1. Revisión de los registros

Primero se identificaron los 12 archivos y se revisaron su duración, frecuencia de muestreo, paquetes perdidos y posibles muestras saturadas. También se comparó la frecuencia cardíaca entre condiciones y derivaciones.

### 4.2. Preprocesamiento

Se convirtieron las cuentas del ADC a milivoltios. Después se aplicó un filtro pasabanda Butterworth de **0.5 a 40 Hz** y un filtro notch de **60 Hz**, para reducir la deriva de línea base, el ruido de alta frecuencia y la interferencia eléctrica.

### 4.3. Detección de picos R y segmentación

Para localizar los latidos se utilizó una versión simplificada del algoritmo de Pan-Tompkins, basada en filtrado, derivada, elevación al cuadrado, integración y detección de picos. A partir de los picos R se calcularon los intervalos RR y la frecuencia cardíaca.

Cada latido se separó en una ventana de **600 ms**, con 200 ms antes y 400 ms después del pico R. Debido a la frecuencia de muestreo, cada ventana contiene 600 muestras.

### 4.4. Extracción de características

Se obtuvieron **24 características por latido**, organizadas de la siguiente manera:

| Grupo de características | Cantidad | Ejemplos |
|---|---:|---|
| Ritmo | 3 | RR anterior, RR siguiente y frecuencia cardíaca |
| Morfológicas | 7 | Amplitudes P, Q, R, S y T; duración Q-S y tiempo R-T |
| Estadísticas básicas | 5 | Media, mediana, desviación estándar y percentiles |
| Orden superior | 2 | Asimetría y curtosis |
| Frecuencia | 7 | FFT, potencia espectral y energías wavelet |
| **Total** | **24** | |

Para las características wavelet se empleó la transformada discreta **db4, nivel 6**, de la que se calcularon cuatro energías relativas.

### 4.5. Clasificación

Se compararon cinco algoritmos: árbol de decisión, regresión logística, Random Forest, KNN y SVM con kernel RBF. La evaluación principal se hizo mediante validación cruzada agrupando los latidos en bloques de 10 segundos, con el fin de reducir la similitud entre los datos de entrenamiento y prueba.

Se utilizó especialmente el **F1-score macro**, porque permite comparar el rendimiento en las cuatro clases sin dar mayor peso a la que tiene más latidos.

## 5. Resultados

En el análisis principal se utilizó la derivación **D1**, con **163 latidos válidos**: 35 de basal, 36 de hiperventilación, 33 de hipoventilación y 59 de aeróbica.

No se encontraron paquetes perdidos en los 12 registros. En `Hipoventilacion_D1.txt` se detectaron 70 muestras saturadas y un porcentaje elevado de intervalos RR anómalos, por lo que se tuvo en cuenta esa limitación al interpretar los resultados.

La condición aeróbica presentó la mayor frecuencia cardíaca media en D1, con aproximadamente **103 lpm**, frente a **70 lpm** en basal.

Al comparar los modelos y las derivaciones, se obtuvieron los siguientes resultados:

| Derivación | Modelo con mejor F1 macro | F1 macro (promedio ± DE) |
|---|---|---:|
| D1 | SVM (RBF) | 0.873 ± 0.099 |
| D2 | Regresión logística | 0.873 ± 0.085 |
| D3 | SVM (RBF) | 0.790 ± 0.156 |

En D1, Random Forest obtuvo la mayor exactitud global (**91.0 %**), pero SVM alcanzó un F1 macro mayor. La regresión logística en D2 obtuvo un F1 macro prácticamente igual al de SVM en D1 y mostró una menor variación entre los pliegues.

El cuaderno también incluye las pruebas del cuestionario final: comparación entre derivaciones, condiciones, número de características y umbral de detección de picos R.

## 6. Conclusiones

- El filtrado y la detección de picos R permitieron obtener ventanas de latidos para calcular sus características.
- Las 24 características ayudaron a resumir la información temporal y espectral del ECG antes de entrenar los clasificadores.
- **SVM en D1 y regresión logística en D2** obtuvieron el mejor F1 macro promedio (**0.873**). Por calidad de los registros, D2 resultó una alternativa conveniente para el análisis.
- La condición aeróbica fue la más fácil de diferenciar de la condición basal, principalmente por los cambios en la frecuencia cardíaca.
- Estos resultados corresponden a registros de un participante y no deben interpretarse como una validación clínica del modelo para otras personas.

## 7. Archivos del laboratorio

- [`LAB11_ECG_Extraccion_Caracteristicas_30102026.ipynb`](LAB11_ECG_Extraccion_Caracteristicas_30102026.ipynb): código, gráficas, respuestas y experimentos del laboratorio.
- [`Infografia.jpeg`](Infografia.jpeg): resumen visual del procedimiento y los resultados.

## 8. Ejecución

[**Abrir Laboratorio 11 en Google Colab**](https://colab.research.google.com/drive/13TMIRYXEkj27-PZRwOd4d_KdXciat2Iv)

Para repetir el análisis con los registros reales:

1. Abrir el notebook en Google Colab.
2. Cargar a la sesión los 12 archivos `.txt` del laboratorio, o subir el ZIP `señales-20261030T160256Z-1-001.zip` **antes de ejecutar la celda de carga de archivos**.
3. Elegir **Entorno de ejecución → Ejecutar todas** y verificar el mensaje **«datos reales del grupo»**.
4. Revisar las gráficas, los clasificadores y las respuestas del cuestionario.
5. Guardar el archivo `caracteristicas_ecg.csv` que se genera en la última celda.

**Nota:** Los archivos de adquisición originales no están incluidos en esta carpeta. Si no se cargan antes de ejecutar el notebook, este puede utilizar registros simulados para demostración.

## 9. Referencias

1. Subba T, Chingtham T. *Comparative Analysis of Machine Learning Algorithms With Advanced Feature Extraction for ECG Signal Classification*. IEEE Access, 2024. DOI: [10.1109/ACCESS.2024.3387041](https://doi.org/10.1109/ACCESS.2024.3387041).
2. Pan J, Tompkins WJ. *A Real-Time QRS Detection Algorithm*. IEEE Transactions on Biomedical Engineering, 1985.
