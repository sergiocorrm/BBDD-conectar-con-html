# Registro de usuarios con Flask y MySQL

Aplicación web sencilla que permite añadir un **nombre** y un **usuario** desde un formulario HTML y guardarlos en una tabla de una base de datos MySQL. Los usuarios guardados se muestran en una tabla en la propia página.

**Autor:** Sergio Corrales 1ºDAM

## Cómo funciona

```
Formulario HTML  →  Servidor Python (Flask)  →  Base de datos MySQL
```

1. El usuario rellena el formulario y pulsa "Añadir".
2. Flask recibe los datos con una petición POST.
3. Se insertan en la tabla `usuarios` con una consulta preparada (evita la inyección SQL).
4. La página se recarga mostrando la tabla actualizada.

## Tecnologías

- Python 3
- Flask
- MySQL (gestionado con MySQL Workbench)
- mysql-connector-python
- python-dotenv

## Estructura del proyecto

```
.
├── app.py
├── database.sql
├── templates/
│   └── index.html
├── .env.example
├── .gitignore
└── README.md
```

## Instalación

1. **Clonar el repositorio**

   ```
   git clone URL_DEL_REPOSITORIO
   cd NOMBRE_DEL_REPOSITORIO
   ```

2. **Instalar las dependencias**

   ```
   pip install flask mysql-connector-python python-dotenv
   ```

3. **Crear la base de datos**

   Abre MySQL Workbench, conecta con tu servidor y ejecuta el contenido del archivo `database.sql`.

4. **Configurar las credenciales**

   Copia `.env.example` y renómbralo como `.env`. Después, escribe tu contraseña de MySQL:

   ```
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=tu_contraseña
   DB_NAME=mibd
   ```

5. **Ejecutar la aplicación**

   ```
   python app.py
   ```

6. Abre `http://localhost:5000` en el navegador.

## Base de datos

Tabla `usuarios`:

| Campo   | Tipo         | Descripción                           |
|---------|--------------|---------------------------------------|
| id      | INT          | Clave primaria, autoincremental       |
| nombre  | VARCHAR(100) | Nombre de la persona                  |
| usuario | VARCHAR(50)  | Nombre de usuario, único (`UNIQUE`)   |

## Seguridad

- Las credenciales de la base de datos están en el archivo `.env`, que **no se sube** a GitHub gracias al `.gitignore`.
- Las consultas usan parámetros (`%s`), por lo que los datos nunca se mezclan con el SQL.
- Flask escapa automáticamente el texto mostrado en la página.
