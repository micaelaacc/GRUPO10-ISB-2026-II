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
Inicialmente se verificaron los componentes del kit BITalino y se realizaron las conexiones necesarias para la adquisición de la señal EMG. Los electrodos fueron conectados al sensor y colocados sobre la región muscular seleccionada.

Posteriormente, se encendió la tarjeta BITalino y se estableció la comunicación con la computadora mediante **Bluetooth**. Una vez reconocido el dispositivo, se configuró en **OpenSignals (r)evolution)** el canal correspondiente al sensor utilizado y se inició la adquisición.