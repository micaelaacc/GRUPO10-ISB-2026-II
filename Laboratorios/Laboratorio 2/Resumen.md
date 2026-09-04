# Laboratorio 2
# 🫀 Laboratorio 2 — Señales Biomédicas
**Curso:** Introducción a las Señales Biomédicas (ISB)  
**Universidad:** Universidad Peruana Cayetano Heredia (UPCH)  
**Grupo:** Grupo 10  
**Docente:** Ing. Alexander Valdez Portocarrero  
**Entorno:** Python 3.x | Jupyter Notebook / Google Colab

---

## 📋 Tabla de Contenidos
1. [Resumen General](#-resumen-general)
2. [Lab 001 — Introducción con PhysioNet](#-lab-001--introducción-con-physionet)
3. [Lab 002 — Análisis Temporal, FFT y STFT](#-lab-002--análisis-temporal-fft-y-stft)
4. [Lab 003 — Filtros FIR, IIR y Transformada Z](#-lab-003--filtros-fir-iir-y-transformada-z)
5. [Infografía Integradora](#-infografía-integradora)
6. [Fórmulas Clave](#-fórmulas-clave)
7. [Estructura del Repositorio](#-estructura-del-repositorio)
8. [Requisitos y Ejecución](#-requisitos-y-ejecución)
9. [Conclusiones](#-conclusiones)
10. [Referencias](#-referencias)

---

## 🎯 Resumen General

En este laboratorio se estudiaron los fundamentos del procesamiento digital de señales, enfocándose principalmente en el análisis y diseño de filtros digitales. Los filtros permiten modificar selectivamente los componentes frecuenciales de una señal, por ejemplo, eliminando ruido o aislando determinadas frecuencias presentes en señales biomédicas como ECG, EEG y EMG.

Durante la clase se revisaron los principales tipos de filtros según su respuesta en frecuencia: pasa bajas (Low-pass), pasa altas (High-pass), pasa banda (Band-pass) y rechaza banda (Notch). También se analizaron conceptos como la función de transferencia, frecuencia de corte, magnitud y fase, utilizando Python y la librería SciPy para representar y analizar las respuestas en frecuencia.

Además, se compararon los sistemas analógicos y digitales, y se introdujeron conceptos fundamentales del filtrado digital como la convolución, respuesta al impulso, función de transferencia, polos y ceros y estabilidad. En el caso de sistemas digitales, se destacó que la estabilidad requiere que todos los polos se encuentren dentro del círculo unitario.

Una parte importante del laboratorio fue la comparación entre filtros FIR (Finite Impulse Response) e IIR (Infinite Impulse Response). Los filtros FIR son no recursivos, utilizan únicamente ceros, pueden presentar fase lineal y son siempre estables, aunque generalmente requieren un orden mayor. Los filtros IIR, en cambio, utilizan realimentación, presentan polos y ceros y permiten obtener filtros eficientes con un orden menor, aunque pueden presentar problemas de estabilidad y fase no lineal.
También se estudiaron diferentes ventanas para el diseño de filtros FIR, como rectangular, Hann, Hamming y Blackman, observando el compromiso entre el ripple y la atenuación de las bandas laterales.

Finalmente, se revisaron diferentes familias de filtros IIR, entre ellas Butterworth, Chebyshev tipo I, Chebyshev tipo II y Elíptico, comparando sus características de respuesta y ripple. También se introdujo el concepto de biquads o secciones de segundo orden, utilizadas para mejorar la estabilidad numérica y facilitar la implementación de filtros IIR en sistemas DSP y dispositivos embebidos.

En conjunto, el laboratorio permitió comprender cómo los filtros pueden utilizarse para analizar, modificar y mejorar señales biomédicas, así como implementar estos conceptos mediante herramientas computacionales en Python.
