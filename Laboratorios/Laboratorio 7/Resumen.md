# Laboratorio 7: Filtros adaptativos y Transformada Wavelet
## Introducción
El presente laboratorio se enfocó en la aplicación y comparación de diferentes técnicas de filtrado digital de señales biomédicas, con el objetivo de evaluar su capacidad para reducir interferencias y ruido, preservando la información fisiológica relevante.

Para ello, se trabajó con una señal electrocardiográfica (ECG) adquirida en una sesión anterior mediante BITalino y OpenSignals, a la cual se añadieron artificialmente interferencias sinusoidales y ruido gaussiano. Posteriormente, se aplicaron diferentes técnicas de filtrado para evaluar su capacidad de recuperar la señal original.

Se compararon tres enfoques: 
- **Filtros convencionales:** Filtros pasa-banda Butterworth y notch.
- **Filtros adaptativos:** Algoritmo Least Mean Squares (LMS).
- **Transformada Wavelet:** Descomposición multirresolución y reducción de ruido (denoising).

El procesamiento se desarrolló en Google Colab, utilizando Python. A continuación, se resume el procedimiento realizado y los principales resultados obtenidos. El notebook original, que incluye el código, las gráficas y los resultados completos, se encuentra disponible aquí.

## Señal ECG original
Partimos utilizando el archivo *sampleECG.txt*, correspondiente a una señal electrocardiográfica adquirida en una sesión anterior mediante BITalino (r)evolution y OpenSignals. Se extrajeron los datos del canal analógico A2, convirtiendo los valores digitales a milivoltios (mV) mediante la función de transferencia del sensor.

<div align="center">

<img width="1860" height="580" alt="image" src="https://github.com/user-attachments/assets/e40e95c8-c635-404c-86e5-4a3ba9f63a02" />

**Figura 1.** Registro ECG original completo

<img width="1848" height="574" alt="image" src="https://github.com/user-attachments/assets/84527a83-3c9c-4181-990a-a16eb2c02b63" />

**Figura 2.** Ventana de cuatro segundos para visualizar la morfología de los complejos QRS.

</div>

En la Figura 1 se presenta el registro completo, de aproximadamente 22 segundos, donde se observa una sucesión de complejos QRS relativamente regulares. Para examinar mejor su morfología, en la Figura 2 se seleccionó una ventana de cuatro segundos, en la que se distinguen seis complejos QRS con deflexiones predominantemente negativas. A partir de estos, se estima por inspección una frecuencia cardíaca aproximada de 90 latidos por minuto, considerando un intervalo entre latidos cercano a 0.7 segundos.

## Contaminación artificial de la señal
Una vez obtenida la señal original, procedimos a contaminarla artificialmente mediante la incorporación de interferencias y ruido conocidos. El propósito de este procedimiento fue simular condiciones de adquisición menos favorables y, principalmente, contar con una señal de referencia que permitiera evaluar posteriormente qué tan eficazmente los diferentes métodos de filtrado recuperaban el ECG original.

Para ello, se añadieron tres componentes:

- **Interferencia sinusoidal de 60 Hz:** Simula la interferencia de la red eléctrica en Perú.
- **Interferencia sinusoidal de 120 Hz:** Representa el segundo armónico de la frecuencia de red.
- **Ruido gaussiano:** Simula perturbaciones aleatorias distribuidas en un amplio rango de frecuencias.

La señal contaminada se obtuvo sumando estas tres componentes al ECG original.

<div align="center">

<img width="2118" height="1192" alt="image" src="https://github.com/user-attachments/assets/ff6763ea-03f8-431a-b1c9-47ec6d425311" />

**Figura 3.** Componentes de ruido introducidos artificialmente: (a) interferencia sinusoidal de 60 Hz, (b) interferencia sinusoidal de 120 Hz y (c) ruido gaussiano.

</div>

Como se observa en la Figura 3, las dos interferencias sinusoidales presentan oscilaciones periódicas de amplitud constante. Sin embargo, la interferencia de 60 Hz (a) presenta menos oscilaciones por unidad de tiempo que la de 120 Hz (b), cuya frecuencia es el doble y corresponde al segundo armónico de la red eléctrica. Asimismo, se aprecia que la interferencia de 120 Hz tiene una amplitud menor que la de 60 Hz. En contraste, el ruido gaussiano (c) presenta fluctuaciones aleatorias alrededor de cero, sin una periodicidad definida y con amplitudes variables. A diferencia de las interferencias sinusoidales, que se concentran en frecuencias específicas, el ruido gaussiano simulado se distribuye en un amplio rango de frecuencias, lo que representa un desafío distinto para las técnicas de filtrado.

<div align="center">

<img width="1846" height="784" alt="image" src="https://github.com/user-attachments/assets/b5665bef-ecc9-48a8-a9d4-4fc0300446d1" />

**Figura 4.** Comparación entre la señal ECG original y la señal contaminada artificialmente

</div>

En la Figura 4 se compara la señal ECG original con la señal contaminada artificialmente durante una ventana de cuatro segundos. Se observa que la incorporación de las interferencias genera numerosas oscilaciones rápidas superpuestas a la señal, alterando considerablemente su morfología. Aunque los complejos QRS continúan siendo identificables debido a sus deflexiones pronunciadas, las perturbaciones dificultan la distinción de componentes de menor amplitud, como las ondas P y T.

Esta comparación evidencia la necesidad de aplicar técnicas de filtrado que permitan atenuar las interferencias introducidas y recuperar una señal lo más similar posible al ECG original, preservando sus características fisiológicas.

# Filtrado

<img width="1884" height="986" alt="image" src="https://github.com/user-attachments/assets/9070f6d8-554b-4358-b3c4-12afabe46bf1" />


<img width="2230" height="1610" alt="image" src="https://github.com/user-attachments/assets/55e96cd5-fe02-4673-9456-c45b3d92c1e7" />

<img width="1952" height="1020" alt="image" src="https://github.com/user-attachments/assets/7a8efffa-123f-4a9c-b33e-f195fc734a7d" />

<img width="1962" height="1428" alt="image" src="https://github.com/user-attachments/assets/87cddceb-8929-4a78-90c8-0e811ccb7561" />

<img width="1986" height="630" alt="image" src="https://github.com/user-attachments/assets/d7797af7-5144-4312-b119-3f05da15ea8e" />

