# 4. Extensiones y personalización en Markdown.

Markdown ofrece la posibilidad de utilizar extensiones y personalizar su sintaxis para adaptarse a las necesidades específicas de cada usuario. Algunas de las extensiones comunes en Markdown incluyen:

- **Tablas avanzadas:** Permiten agregar funcionalidades adicionales a las tablas, como la combinación de celdas, el ajuste automático de ancho, la alineación del contenido, entre otros.

- **Listas de tareas:** Permite crear listas con casillas de verificación, útiles para hacer listas de tareas o checklists.

- **Diagramas y gráficos:** Algunas extensiones de Markdown permiten crear diagramas, gráficos y visualizaciones más complejas dentro del texto.

La personalización en Markdown puede realizarse a través de estilos CSS para cambiar la apariencia del texto formateado, o utilizando preprocesadores Markdown que amplían la sintaxis básica con características adicionales.


----
Aquí tienes algunos ejemplos de extensiones y personalización en Markdown:

1. **Tablas avanzadas:**

   ```Markdown
   | Nombre   | Edad | País     |
   | -------- | ---- | -------- |
   | Juan     | 25   | México   |
   | María    | 30   | España   |
   | Carlos   | 28   | Argentina|
   ```

   Esta tabla básica se puede mejorar utilizando una extensión de tablas avanzadas que permite combinar celdas, ajustar automáticamente el ancho de las columnas y alinear el contenido, como se muestra a continuación:

   ```Markdown
   | Nombre   | Edad | País     |
   |:--------:| ----:|:-------: |
   | Juan     | 25   | México   |
   | María    | 30   | España   |
   | Carlos   | 28   | Argentina|
   ```

2. **Listas de tareas:**

   ```Markdown
   - [x] Tarea 1
   - [ ] Tarea 2
   - [ ] Tarea 3
   ```

   Las listas de tareas se pueden utilizar para crear listas de tareas pendientes, donde se puede marcar o desmarcar cada tarea según sea necesario.

3. **Diagramas y gráficos:**

   Algunas extensiones de Markdown, como Mermaid, permiten crear diagramas y gráficos directamente en el texto. Por ejemplo:

   ```Markdown
   ```mermaid
   graph LR
       A-->B
       B-->C
       C-->D
   ```

   Este ejemplo crea un diagrama de flujo simple con flechas que conectan nodos.

Recuerda que la disponibilidad de estas extensiones y personalizaciones puede variar según la implementación de Markdown que utilices. Durante el curso, se explorarán más opciones y ejemplos para extender y personalizar Markdown según tus necesidades.

---
- **Ejemplo**
```sequenceDiagram
    participant User
    participant System
    participant Database

    User->>System: Envía solicitud de inicio de sesión
    alt Verificación exitosa
        System->>Database: Consulta información del usuario
        Database-->>System: Retorna datos del usuario
        System-->>User: Envía confirmación de inicio de sesión exitoso
    else Verificación fallida
        System-->>User: Envía mensaje de error
    end
 ```
Este **ejemplo** representa un diagrama de secuencia que ilustra el proceso de inicio de sesión en un sistema. Aquí hay una descripción paso a paso de lo que sucede:

- El usuario envía una solicitud de inicio de sesión al sistema.
- El sistema consulta la información del usuario en la base de datos.
La base de datos devuelve los datos del usuario al sistema.
- El sistema envía una confirmación de inicio de sesión exitoso al usuario si la verificación es exitosa.
- Si la verificación falla, el sistema envía un mensaje de error al usuario.
- Este diagrama de secuencia ayuda a visualizar y comprender mejor el flujo y la interacción entre los participantes (usuario, sistema y base de datos) durante el proceso de inicio de sesión.

Recuerda que este es solo un ejemplo y existen muchas otras posibilidades y tipos de diagramas y gráficos que se pueden crear utilizando diferentes extensiones de Markdown.

Es importante destacar que las extensiones y personalizaciones pueden variar dependiendo de la implementación de Markdown utilizada. Durante el curso, se explorarán diferentes extensiones y opciones de personalización, así como las mejores prácticas para su uso.
