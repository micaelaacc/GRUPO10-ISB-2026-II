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

## Aplicación de filtros digitales

### Filtro pasa-banda Butterworth
En primer lugar, aplicamos un filtro pasa-banda Butterworth de cuarto orden, con frecuencias de corte de 0.5 Hz y 40 Hz. Este filtro permite conservar las componentes de la señal comprendidas dentro de dicho intervalo, mientras atenúa las frecuencias inferiores y superiores. De esta manera, buscamos reducir las interferencias sinusoidales de 60 Hz y 120 Hz, así como parte del ruido gaussiano.

<div align="center">

<img width="1884" height="986" alt="image" src="https://github.com/user-attachments/assets/9070f6d8-554b-4358-b3c4-12afabe46bf1" />

**Figura 5.** Comparación entre el ECG original, el ECG contaminado y el ECG filtrado mediante Butterworth pasa-banda de 0.5–40 Hz

</div>

Como se observa en la Figura 5, el filtrado reduce considerablemente las oscilaciones rápidas presentes en la señal contaminada, recuperando una morfología similar a la del ECG original. Los complejos QRS permanecen claramente identificables y se conserva su ubicación temporal. Sin embargo, también se aprecia un ligero suavizado de la señal, debido a la atenuación de componentes de alta frecuencia que pueden formar parte de la morfología original del ECG.

### Filtro notch
Posteriormente, aplicamos filtros notch, diseñados para atenuar componentes de frecuencia específicas sin eliminar una banda tan amplia como el filtro pasa-banda. Se realizaron dos pruebas: B1, utilizando un notch de 60 Hz, y B2, aplicando dos filtros notch en cascada, a 60 Hz y 120 Hz.

<div align="center">

<img width="2230" height="1610" alt="image" src="https://github.com/user-attachments/assets/55e96cd5-fe02-4673-9456-c45b3d92c1e7" />

**Figura 6.** Comparación de los resultados del filtrado notch: (B1) eliminación de la interferencia de 60 Hz y (B2) eliminación de las interferencias de 60 Hz y 120 Hz.

</div>

En la Figura 6, observamos que el filtro B1 reduce parte de las oscilaciones periódicas, aunque todavía permanece una interferencia considerable asociada a los 120 Hz. En cambio, el filtro B2 consigue una señal visualmente más limpia al atenuar ambas frecuencias. No obstante, persisten fluctuaciones irregulares debido al ruido gaussiano, ya que este se distribuye en un rango amplio de frecuencias y no puede eliminarse completamente mediante filtros notch.


### Filtro adaptativo LMS
A continuación, implementamos un filtro adaptativo mediante el algoritmo Least Mean Squares (LMS), utilizando un paso de adaptación $\mu=0.005$. A diferencia de los filtros anteriores, el LMS ajusta progresivamente sus coeficientes para estimar las interferencias a partir de señales de referencia y sustraerlas del ECG contaminado.


<div align="center">

<img width="1952" height="1020" alt="image" src="https://github.com/user-attachments/assets/7a8efffa-123f-4a9c-b33e-f195fc734a7d" />

**Figura 7.** Comparación entre el ECG original, el ECG contaminado y el ECG recuperado mediante el filtro adaptativo LMS

</div>

Como se observa en la Figura 7, el filtro adaptativo logra reducir gran parte de las oscilaciones sinusoidales, recuperando la estructura general del ECG y conservando los complejos QRS. Sin embargo, todavía se identifican fluctuaciones de pequeña amplitud, principalmente asociadas al ruido gaussiano. Esto evidencia que el LMS resulta útil para cancelar interferencias relacionadas con las referencias utilizadas, pero presenta limitaciones frente a perturbaciones aleatorias no correlacionadas con ellas.

### Filtrado mediante Transformada Wavelet
Finalmente, aplicamos un procedimiento de reducción de ruido (denoising) mediante la Transformada Wavelet Discreta (DWT), utilizando la familia Daubechies 4 (db4) y umbralización suave (soft thresholding). Este método permite descomponer la señal en diferentes escalas y reducir los coeficientes asociados al ruido antes de reconstruirla.

Adicionalmente, evaluamos un método híbrido, que combina los filtros notch de 60 Hz y 120 Hz con el denoising Wavelet, buscando aprovechar la capacidad de ambas técnicas para atenuar diferentes tipos de interferencias.

<div align="center">

<img width="1962" height="1428" alt="image" src="https://github.com/user-attachments/assets/87cddceb-8929-4a78-90c8-0e811ccb7561" />

**Figura 8.** Comparación entre el ECG original, el ECG contaminado, el ECG filtrado mediante Wavelet y el resultado del método híbrido notch + Wavelet.

</div>

En la Figura 8, observamos que el filtrado Wavelet por sí solo reduce parte del ruido, pero mantiene oscilaciones periódicas que dificultan recuperar completamente la morfología original. Por el contrario, el método híbrido produce una señal considerablemente más suave y cercana al ECG de referencia, conservando la ubicación de los complejos QRS. Esto demuestra la utilidad de combinar técnicas complementarias para tratar interferencias de distinta naturaleza.

## Comparación de métodos de filtrado e interpretación

Para evaluar cuantitativamente el desempeño de las técnicas implementadas, se calculó la relación señal-ruido (SNR) de cada señal filtrada respecto al ECG original. Esta métrica, expresada en decibelios (dB), permite comparar la potencia de la señal de referencia con la potencia del error residual, de modo que un valor mayor indica una recuperación más precisa.

<div align="center">

<img width="1986" height="630" alt="image" src="https://github.com/user-attachments/assets/d7797af7-5144-4312-b119-3f05da15ea8e" />

**Figura 9.** Comparación de la relación señal-ruido (SNR) obtenida mediante los diferentes métodos de filtrado respecto al ECG original.

</div>

Como se observa en la Figura 9, el filtro pasa-banda Butterworth obtuvo el mejor resultado, con una SNR aproximada de 14.7 dB, seguido del método híbrido notch + Wavelet, con 11.7 dB. Los filtros notch de 60 y 120 Hz y el LMS alcanzaron valores cercanos a 10 dB, mientras que el denoising Wavelet individual y el notch de 60 Hz presentaron resultados inferiores.

Estos resultados indican que, para las interferencias simuladas en este laboratorio, el filtro pasa-banda fue el más eficaz en términos de SNR. 

## Conclusiones
El laboratorio permitió comprender que la elección de una técnica de filtrado depende principalmente de las características del ruido presente y de la información que se desea preservar. Los filtros convencionales resultaron eficaces frente a interferencias conocidas: el pasa-banda Butterworth permitió atenuar componentes fuera del rango de interés, mientras que los filtros notch ofrecieron una alternativa más selectiva para eliminar frecuencias específicas sin afectar ampliamente el espectro de la señal.

Por otro lado, el filtrado adaptativo LMS demostró su utilidad para cancelar interferencias mediante señales de referencia, mientras que la Transformada Wavelet permitió abordar el ruido desde una representación multirresolución. Asimismo, el método híbrido notch + Wavelet evidenció las ventajas de combinar técnicas para tratar diferentes tipos de perturbaciones.

Finalmente, aunque el filtro Butterworth obtuvo la mayor SNR (≈14.7 dB) en este experimento, esto no significa que sea siempre la mejor alternativa. La selección del método debe considerar tanto la reducción del ruido como la conservación de la morfología del ECG, ya que el objetivo del filtrado biomédico no es únicamente obtener una señal más limpia, sino preservar la información fisiológica necesaria para su interpretación.




