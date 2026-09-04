# Laboratorio 2: Filtros Digitales, Transformada Z y Señales Biomédicas

## Resumen General

En este laboratorio se estudiaron los fundamentos del procesamiento digital de señales, enfocándose principalmente en el análisis y diseño de filtros digitales. Los filtros permiten modificar selectivamente los componentes frecuenciales de una señal, por ejemplo, eliminando ruido o aislando determinadas frecuencias presentes en señales biomédicas como ECG, EEG y EMG.

Durante la clase se revisaron los principales tipos de filtros según su respuesta en frecuencia: pasa bajas (Low-pass), pasa altas (High-pass), pasa banda (Band-pass) y rechaza banda (Notch). También se analizaron conceptos como la función de transferencia, frecuencia de corte, magnitud y fase, utilizando Python y la librería SciPy para representar y analizar las respuestas en frecuencia.

Además, se compararon los sistemas analógicos y digitales, y se introdujeron conceptos fundamentales del filtrado digital como la convolución, respuesta al impulso, función de transferencia, polos y ceros y estabilidad. En el caso de sistemas digitales, se destacó que la estabilidad requiere que todos los polos se encuentren dentro del círculo unitario.

Una parte importante del laboratorio fue la comparación entre filtros FIR (Finite Impulse Response) e IIR (Infinite Impulse Response). Los filtros FIR son no recursivos, utilizan únicamente ceros, pueden presentar fase lineal y son siempre estables, aunque generalmente requieren un orden mayor. Los filtros IIR, en cambio, utilizan realimentación, presentan polos y ceros y permiten obtener filtros eficientes con un orden menor, aunque pueden presentar problemas de estabilidad y fase no lineal.
También se estudiaron diferentes ventanas para el diseño de filtros FIR, como rectangular, Hann, Hamming y Blackman, observando el compromiso entre el ripple y la atenuación de las bandas laterales.

Finalmente, se revisaron diferentes familias de filtros IIR, entre ellas Butterworth, Chebyshev tipo I, Chebyshev tipo II y Elíptico, comparando sus características de respuesta y ripple. También se introdujo el concepto de biquads o secciones de segundo orden, utilizadas para mejorar la estabilidad numérica y facilitar la implementación de filtros IIR en sistemas DSP y dispositivos embebidos.

En conjunto, el laboratorio permitió comprender cómo los filtros pueden utilizarse para analizar, modificar y mejorar señales biomédicas, así como implementar estos conceptos mediante herramientas computacionales en Python.

# Filtros Digitales, Transformada Z y Señales Biomédicas

## 1. Conceptos principales

### Extracción de características

La extracción de características permite obtener información relevante de una señal biomédica adquirida mediante sensores. Estas características pueden utilizarse para analizar procesos fisiológicos o como entrada para algoritmos de aprendizaje automático.

### Filtros digitales

Un **filtro digital** permite modificar una señal para conservar las componentes de interés y atenuar aquellas no deseadas, como ruido o interferencias.

El comportamiento de un filtro puede estudiarse mediante su **respuesta al impulso**, utilizando el delta de Kronecker. También puede analizarse mediante su respuesta en magnitud y fase.

### Transformada Z

La **Transformada Z** facilita el análisis de señales y sistemas discretos. En este dominio, operaciones como la convolución pueden representarse mediante multiplicaciones, simplificando el análisis.

La **transformada bilineal** permite convertir una función de transferencia continua en el dominio `s` a una función de transferencia discreta en el dominio `z`:

$$
s = \frac{2}{T}\frac{1-z^{-1}}{1+z^{-1}}
$$

### Polos y ceros

El diagrama de polos y ceros permite estudiar el comportamiento y la estabilidad de un filtro digital.

- Los **ceros** producen atenuación de determinadas frecuencias.
- Los **polos** pueden producir amplificación o resonancia.
- Un sistema discreto es estable si sus polos se encuentran dentro del círculo unitario.

### Teorema y frecuencia de Nyquist

El **teorema de Nyquist** establece que la frecuencia de muestreo debe ser al menos el doble de la frecuencia máxima presente en la señal:

$$
f_s \geq 2f_{max}
$$

La **frecuencia de Nyquist** corresponde a la mitad de la frecuencia de muestreo:

$$
f_N = \frac{f_s}{2}
$$

---

## 2. Filtros FIR e IIR

### Filtros FIR

Los filtros **FIR (Finite Impulse Response)** presentan una respuesta al impulso de duración finita y no utilizan realimentación de salidas anteriores.

Sus principales características son:

- Son inherentemente estables.
- Pueden presentar fase lineal.
- Generalmente requieren un orden mayor.
- Pueden diseñarse mediante el método de ventanas.

Al truncar una respuesta ideal pueden aparecer ondulaciones conocidas como **fenómeno de Gibbs**.

### Filtros IIR

Los filtros **IIR (Infinite Impulse Response)** utilizan muestras anteriores de la entrada y de la salida, por lo que presentan realimentación.

Sus principales características son:

- Requieren órdenes menores que los FIR para obtener respuestas similares.
- Presentan menor costo computacional.
- Pueden presentar fase no lineal.
- Pueden ser inestables, por lo que es necesario analizar la ubicación de sus polos.

En su ecuación, los coeficientes `b` se relacionan con las entradas y los coeficientes `a` con la realimentación de las salidas.

---

## 3. Análisis de señales en frecuencia

La **Transformada Discreta de Fourier (DFT)** permite conocer las frecuencias que componen una señal.

La **FFT (Fast Fourier Transform)** es un algoritmo eficiente utilizado para calcular computacionalmente la DFT.

Al observar el espectro de una señal, los picos permiten identificar sus principales componentes frecuenciales. Esto resulta útil para reconocer tanto información fisiológica como posibles interferencias antes de seleccionar un filtro.

---

## 4. Diseño y aplicación de filtros

Para eliminar componentes no deseadas de una señal pueden utilizarse herramientas como `scipy.signal`.

Por ejemplo, un filtro Butterworth pasa-bajos puede diseñarse mediante:

```python
from scipy import signal

sos = signal.butter(
    N=4,
    Wn=25,
    btype='lp',
    fs=250,
    output='sos'
)
```

## 5. PhysioNet

**PhysioNet** es una plataforma que permite acceder a bases de datos de señales fisiológicas reales, como ECG.

Mediante la librería `wfdb` se pueden cargar registros y obtener información como:

- Frecuencia de muestreo.
- Número de muestras.
- Canales disponibles.
- Unidades.
- Duración de la señal.

La duración de una señal puede calcularse mediante:

$$
t = \frac{N}{f_s}
$$

donde `N` representa el número de muestras y `f_s` la frecuencia de muestreo.

También puede eliminarse la **componente DC** restando la media de la señal antes de realizar determinados análisis frecuenciales.

---

# Laboratorios realizados

## Lab 1 — Introducción a PhysioNet

Se trabajó con un ECG real de la base de datos **MIT-BIH Arrhythmia Database**. Se aprendió a cargar registros mediante `wfdb`, seleccionar canales y obtener información como frecuencia de muestreo, duración y amplitud.

Además, se realizaron:

- Gráficas de la señal ECG.
- Representación de muestras discretas.
- Cálculo de estadísticas básicas.
- Normalización de la señal.
- Conversión del ECG a formato `.wav`.

---

## Lab 2 — Análisis temporal y frecuencial

Se analizaron señales de la **Normal Sinus Rhythm Database** tanto en el dominio temporal como en el dominio frecuencial.

Se utilizó la **FFT** para identificar las frecuencias dominantes y se compararon los espectros antes y después de eliminar la componente DC.

También se aplicó la **STFT (Short-Time Fourier Transform)** para observar cómo cambia el contenido frecuencial de la señal a lo largo del tiempo.

Esto permitió observar el compromiso entre **resolución temporal y resolución frecuencial** dependiendo del tamaño de la ventana utilizada.

---

## Lab 3 — Filtros FIR e IIR

Se trabajó con una señal ECG sintética para diseñar y comparar filtros digitales.

El procedimiento general fue:

> **Señal → análisis temporal → FFT → identificación del ruido → selección del filtro → filtrado → validación**

Se diseñaron y compararon:

- Un filtro **FIR pasa-bajos**.
- Un filtro **IIR Butterworth pasa-bajos**.

Posteriormente, se añadió una interferencia de **35 Hz** al ECG y se identificó mediante la FFT. Para reducirla se aplicó un filtro Butterworth pasa-bajos.

La calidad del filtrado se evaluó mediante:

- **MSE:** error cuadrático medio.
- **RMSE:** raíz del error cuadrático medio.
- **SNR:** relación señal-ruido.

Además, se verificó que el filtrado conservara características fisiológicas importantes del ECG, como la **morfología del complejo QRS** y la **frecuencia cardíaca**.

---

# Conclusión

Los laboratorios permitieron seguir el procesamiento de una señal biomédica desde su adquisición y representación hasta su análisis y filtrado.

Primero se exploraron señales reales mediante **PhysioNet**; posteriormente se utilizaron la **FFT** y la **STFT** para estudiar su contenido frecuencial; y finalmente se diseñaron filtros **FIR e IIR** para reducir componentes no deseadas.

En el procesamiento de señales biomédicas, el filtrado no consiste únicamente en eliminar ruido, sino también en **preservar la información fisiológica relevante de la señal**.
