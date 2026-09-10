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
 <img width="996" height="700" alt="image" src="https://github.com/user-attachments/assets/b7ace4ea-cebf-4dd2-b2dc-64fc3ef2833f" />

 **Figura 4.** Conexión del sensor EMG al canal analógico A1 del BITalino (r)evolution para la adquisición de la actividad eléctrica muscular.
</div>

Durante la práctica se registró la actividad electromiográfica de dos músculos: **bíceps y tríceps**. Para cada adquisición se colocaron electrodos superficiales en la región correspondiente al músculo de interés y se utilizó adicionalmente un **electrodo de referencia** colocado en el codo.

<div align="center">
 <img width="400" height="600" alt="image" src="https://github.com/user-attachments/assets/2e147336-04e9-4b63-96dd-3f05dde2da46" />

 **Figura 5.** Colocación de los electrodos superficiales para la adquisición de la señal EMG del bíceps

 <img width="400" height="600" alt="image" src="https://github.com/user-attachments/assets/73bc4d06-18be-4156-bfec-7103bef622fb" />

 **Figura 6.** Colocación de los electrodos superficiales para la adquisición de la señal EMG del tríceps

</div>

## Adquisición de las señales EMG
Una vez realizada la conexión del sensor y la colocación de los electrodos, se inició la adquisición de las señales EMG mediante **OpenSignals (r)evolution**. El protocolo se aplicó tanto para el **bíceps** como para el **tríceps**, con el objetivo de observar los cambios en la actividad electromiográfica bajo diferentes niveles de activación muscular.

Para cada músculo se evaluaron tres condiciones:

1. **Reposo:** el participante mantuvo el músculo relajado, evitando realizar movimientos voluntarios durante el registro.
2. **Movimiento leve:** se realizó el movimiento correspondiente a la activación del músculo sin aplicar una resistencia externa adicional.
3. **Movimiento con fuerza en dirección contraria:** se realizó el movimiento mientras se aplicaba una fuerza externa en sentido contrario, generando una mayor resistencia al movimiento y, por tanto, una mayor demanda de activación muscular.

Para cada una de las condiciones se realizaron **tres adquisiciones independientes**. Entre adquisiciones se mantuvo un periodo de descanso de aproximadamente **30 segundos a 1 minuto**, con la finalidad de permitir la recuperación antes de realizar la siguiente toma.


<div align="center">
 
https://github.com/user-attachments/assets/7c319073-d8d7-4ad9-9d49-2b0679783f39
 
**Video 1.** Ejecución del movimiento leve durante la adquisición de la señal EMG del bíceps.

Durante cada adquisición, la señal EMG fue visualizada en tiempo real mediante OpenSignals. Esto permitió observar las variaciones de amplitud de la señal entre los periodos de reposo y las condiciones de activación muscular.


https://github.com/user-attachments/assets/bdf2c63a-f7f7-4205-9f6c-91244807fbeb
 
**Video 2.** Visualización en OpenSignals (r)evolution de la señal EMG durante la adquisición correspondiente al movimiento leve del bíceps.
</div>


