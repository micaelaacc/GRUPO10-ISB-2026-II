# Laboratorio 2
# 🫀 Laboratorio 2 — Señales Biomédicas
**Curso:** Introducción a las Señales Biomédicas (ISB)  
**Universidad:** Universidad Peruana Cayetano Heredia (UPCH)  
**Grupo:** Grupo 10  
**Docente:** Ing. Alexander Valdez Portocarrero  
**Entorno:** Python 3.x | Jupyter Notebook / Google Colab

---

## 🎯 Resumen General

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
