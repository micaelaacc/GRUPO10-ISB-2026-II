# Laboratorio 7: Filtros adaptativos y Transformada Wavelet
## Introducción
El presente laboratorio se enfocó en la aplicación y comparación de diferentes técnicas de filtrado digital de señales biomédicas, con el objetivo de evaluar su capacidad para reducir interferencias y ruido, preservando la información fisiológica relevante.

Para ello, se trabajó con una señal electrocardiográfica (ECG) adquirida en una sesión anterior mediante BITalino y OpenSignals, a la cual se añadieron artificialmente interferencias sinusoidales y ruido gaussiano. Posteriormente, se aplicaron diferentes técnicas de filtrado para evaluar su capacidad de recuperar la señal original.

Se compararon tres enfoques: 
- **Filtros convencionales:** filtros pasa-banda Butterworth y notch.
- **Filtros adaptativos:** algoritmo Least Mean Squares (LMS).
- **Transformada Wavelet:** descomposición multirresolución y reducción de ruido (denoising).

El procesamiento se desarrolló en Google Colab, utilizando Python. A continuación, se resume el procedimiento realizado y los principales resultados obtenidos. El notebook original, que incluye el código, las gráficas y los resultados completos, se encuentra disponible aquí.

## Señal ECG original
![alt text](image.png)