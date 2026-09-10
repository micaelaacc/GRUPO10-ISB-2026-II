# Laboratorio 3: Uso de BiTalino para EMG y ECG
Durante el laboratorio se realizó la adquisición de señales biomédicas utilizando el kit **BITalino (r)evolution** y el software **OpenSignals (r)evolution**. La sesión permitió familiarizarnos con la configuración del dispositivo, la conexión de los sensores y electrodos, la adquisición de señales y la posterior extracción de los datos registrados.

En particular, se trabajó con la adquisición de **electromiografía (EMG)**, registrando la actividad eléctrica muscular mediante electrodos superficiales. Se observaron las diferencias entre los periodos de reposo y de activación muscular, identificando un incremento de la amplitud de la señal durante la contracción.

Finalmente, las adquisiciones realizadas en OpenSignals fueron almacenadas y posteriormente importadas a **Python**, permitiendo acceder a los datos crudos y representar nuevamente la señal fuera del software de adquisición.

## Objetivos específicos de la práctica
- Adquirir señales biomédicas de EMG y ECG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales EMG y ECG del software OpenSignals (r)evolution
---

A continuación se detalla el paso a paso seguido durante la sesión del laboratorio.
## Configuración de BITalino y OpenSignals
Antes de iniciar la adquisición, se verificó que el kit BITalino (r)evolution contara con los componentes necesarios para la práctica. Se conectó la batería a la placa y posteriormente se encendió el dispositivo, dejándolo disponible para establecer la comunicación inalámbrica con la computadora.

Con el BITalino encendido, se activó el Bluetooth de la computadora y se buscó el dispositivo BITalino disponible como se muestra en la Figura 1. Una vez identificado, se realizó el emparejamiento desde la configuración de Windows para permitir posteriormente la comunicación con OpenSignals (r)evolution.

<div align="center">
<img width="2046" height="824" alt="image" src="https://github.com/user-attachments/assets/2cf34765-1510-42e5-9c46-224908df8c10" />

  **Figura 1.** Dispositivo BITalino emparejado mediante Bluetooth en Windows.
</div>

Luego se abrió el software **OpenSignals (r)evolution)** y se realizó la búsqueda de dispositivos disponibles. El programa detectó correctamente la tarjeta BITalino previamente emparejada tal como se muestra en la Figura 2.

<div align="center">
<img width="3000" height="1900" alt="bitalino found" src="https://github.com/user-attachments/assets/3676b60c-b22c-4fdb-ab3f-06c856c025cd" />

  **Figura 2.** Detección del dispositivo BITalino en OpenSignals.
</div>

Una vez habilitado el dispositivo, se configuró el canal analógico correspondiente al sensor de electromiografía. Se seleccionó el canal **A1** como señal **EMG** y se estableció una frecuencia de muestreo de **1000 Hz**, mientras que los demás canales analógicos permanecieron deshabilitados como se muestra en la Figura 3.

<div align="center">
<img width="1624" height="1360" alt="seleccionar canal" src="https://github.com/user-attachments/assets/299db446-e5cc-4d86-a1a9-66f04950727d" />

  **Figura 3.** Configuración del BITalino en OpenSignals.
</div>

## Conexión del sensor EMG y colocación de electrodos
Una vez configurado el dispositivo en OpenSignals (r)evolution, se realizó la conexión del sensor de **electromiografía (EMG)** al BITalino. Se utilizó el cable correspondiente al sensor y se conectó al canal analógico **A1**, previamente habilitado en el software para la adquisición de la señal.

<div align="center">
 <img width="996" height="848" alt="image" src="https://github.com/user-attachments/assets/b7ace4ea-cebf-4dd2-b2dc-64fc3ef2833f" />

 **Figura 4.** Conexión del sensor EMG al canal analógico A1 del BITalino (r)evolution para la adquisición de la actividad eléctrica muscular.
</div>

Durante la práctica se registró la actividad electromiográfica de dos músculos: **bíceps y tríceps**. Para cada adquisición se colocaron electrodos superficiales en la región correspondiente al músculo de interés y se utilizó adicionalmente un **electrodo de referencia** colocado en el codo.

<div align="center">
 <img width="600" height="800" alt="image" src="https://github.com/user-attachments/assets/2e147336-04e9-4b63-96dd-3f05dde2da46" />

 **Figura 5.** Colocación de los electrodos superficiales para la adquisición de la señal EMG del bíceps

 <img width="600" height="800" alt="image" src="https://github.com/user-attachments/assets/73bc4d06-18be-4156-bfec-7103bef622fb" />

 **Figura 6.** Colocación de los electrodos superficiales para la adquisición de la señal EMG del tríceps

</div>
