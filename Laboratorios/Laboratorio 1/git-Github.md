 # Laboratorio 1: Organización de Repositorio en GitHub
Este repositorio fue creado como parte del primer laboratorio del curso Introducción a Señales Biomédicas, con el propósito de establecer un espacio de trabajo colaborativo para el desarrollo y documentación del proyecto del curso. Durante este laboratorio se realizó una introducción al uso de Git y GitHub como herramientas para el control de versiones y la colaboración en equipo, abordando la creación y gestión de un repositorio grupal y el uso de comandos básicos de Git.

## Objetivos específicos de la práctica
- Creación del repositorio grupal en GitHub.
- Manejo de comandos básicos de Git y GitHub.
- Agregar colaboradores al repositorio grupal.

---
## Git vs GitHub
Antes de comenzar a trabajar con un repositorio, es importante diferenciar Git de GitHub, ya que, aunque ambas herramientas están relacionadas, cumplen funciones distintas.

|**¿Qué es Git?**|**¿Qué es GitHub?**|
|---|---|
|Git es un **sistema de control de versiones** distribuido que permite registrar y administrar los cambios realizados sobre los archivos de un proyecto a lo largo del tiempo. Cada integrante puede trabajar con una copia local del proyecto y guardar diferentes versiones, lo que permite mantener un historial de modificaciones, identificar los cambios realizados y recuperar versiones anteriores cuando sea necesario.|GitHub es una **plataforma en línea** que permite alojar repositorios Git de manera remota y facilita el trabajo colaborativo entre diferentes usuarios. A través de GitHub, los integrantes de un equipo pueden compartir sus cambios, acceder a las actualizaciones realizadas por otros colaboradores y mantener una versión centralizada del proyecto disponible en línea.|

<img width="1814" height="1296" alt="Captura de pantalla 2026-08-21 154449" src="https://github.com/user-attachments/assets/58393175-de76-4d56-a286-6663ce4ea690" />

En resumen, la principal diferencia es que Git es la herramienta que gestiona el control de versiones, mientras que GitHub es una plataforma que permite almacenar y compartir repositorios Git en línea. Ambos se complementan, los cambios pueden realizarse y registrarse localmente mediante Git y posteriormente sincronizarse con el repositorio remoto alojado en GitHub.

## Flujo básico de trabajo con Git
El funcionamiento de Git puede entenderse a partir de cuatro áreas principales: el directorio de trabajo (Working Directory), donde se modifican los archivos del proyecto; el área de preparación (Staging Area), donde se seleccionan los cambios que serán registrados; el repositorio local (Local Repository), donde los cambios se almacenan en el historial mediante commits; y el repositorio remoto (Remote Repository), que permite compartir el proyecto y sus actualizaciones a través de plataformas como GitHub.

<img width="1336" height="1116" alt="Captura de pantalla 2026-08-21 155055" src="https://github.com/user-attachments/assets/310ea008-b46c-4f4b-94f4-0d359066fa2d" />

El flujo básico consiste en utilizar `git add` para preparar los cambios realizados, `git commit` para registrarlos en el repositorio local y `git push` para enviarlos al repositorio remoto. En sentido contrario, `git pull` permite obtener e integrar localmente los cambios realizados por otros colaboradores en el repositorio remoto.