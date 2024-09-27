# Sistema de Gestión de Tareas basado-cliente — Ibero, Arquitectura de Software

Este proyecto implementa un sistema de gestión de tareas utilizando hecho únicamente del lado del cliente en Python, sin necesidad de conectarse a un servidor. El sistema permite agregar, listar, eliminar y actualizar tareas, almacenando los datos en una base de datos SQLite similar al ejemplo que se colocó en clase sobre los usuarios y en la aplicación que se creó para cliente/servidor.

## Características

- **Agregar Tareas**: Los usuarios pueden agregar tareas proporcionando una descripción.
- **Listar Tareas**: Se listan todas las tareas (su descripción).
- **Eliminar Tareas**: Los usuarios pueden eliminar una tarea existente con el botón correspondiente.
- **Actualizar Tareas**: Los usuarios pueden modificar la descripción de una tarea con el botón correspondiente.

## Requisitos

- **Python 3.x**
- **Flask**
- **SQLite** (viene integrado ya con Python)

## Uso

### 1. Ejecutar el app.py

El app.py se encarga de hacer todas las operaciones sobre la base de datos y tiene todas las rutas o endpoints sobre los que se hace cada acción.

```bash
python app.py
```

### 2. Abrir el enlace en localhost

Para poder ver la web, se debe primero haber ejecutado el app.py y luego poner esta URL en nuestro navegador preferido:

```bash
http://127.0.0.1:5000
```

### Estructura del Proyecto

- **static**: Directorio con los archivos estáticos del sistema, aquí está el CSS y JS.
- **templates**: Directorio con los archivos HTML.
- **app.py**: Lógica que maneja el enrutador y las transacciones con la base de datos.
- **tareas.db**: Base de datos SQLite (se genera automáticamente)
- **README.md**: Documentación del proyecto