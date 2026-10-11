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
Partimos utilizando el archivo *sampleECG.txt*, correspondiente a una señal electrocardiográfica adquirida en una sesión anterior mediante BITalino (r)evolution y OpenSignals. Se extrajeron los datos del canal analógico A2, convirtiendo los valores digitales a milivoltios (mV) mediante la función de transferencia del sensor.

<div align="center">

<img width="1848" height="630" alt="fig1" src="https://github.com/user-attachments/assets/d08d94d1-8cfa-4657-a4b4-c9b9dd822c45" />

**Figura 1.** Registro ECG original completo

<img width="1862" height="634" alt="image" src="https://github.com/user-attachments/assets/0c1c8ff0-54a0-4844-a695-9a719948945b" />

**Figura 2.** ventana de cuatro segundos para visualizar la morfología de los complejos QRS.

</div>

En la Figura 1 se presenta el registro completo, de aproximadamente 22 segundos, donde se observa una sucesión de complejos QRS relativamente regulares. Para examinar mejor su morfología, en la Figura 2 se seleccionó una ventana de cuatro segundos, en la que se distinguen seis complejos QRS con deflexiones predominantemente negativas. A partir de estos, se estima por inspección una frecuencia cardíaca aproximada de 90 latidos por minuto, considerando un intervalo entre latidos cercano a 0.7 segundos.
