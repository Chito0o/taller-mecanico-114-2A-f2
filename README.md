# Bitácora de Módulo

Repositorio destinado al registro, seguimiento y documentación de actividades, aprendizajes y avances del módulo.

---

## 📌 Información General

- **Estudiante / Autor:** Chito0o
- **Módulo / Materia:** [Nombre del Módulo]
- **Periodo:** 2026
- **Estado:** En progreso

---

## 📖 Entradas de la Bitácora

### Sesión 1: 07/09/2026
- **Objetivo:** Implementar la clase base `Vehiculo` con sus atributos, constructor y métodos de gestión de estado en Python, documentando el código y sincronizando los avances en GitHub.
- **Actividades realizadas:**
  - [x] Creación del repositorio y configuración inicial.
  - [x] Clonación local y configuración de credenciales de Git (`user.name`, `user.email`).
  - [x] Creación del archivo `vehiculo.py` con la clase `Vehiculo`.
  - [x] Declaración de atributos con tipos indicados (`patente: str`, `anio: int`, `_en_taller: bool`).
  - [x] Implementación del método constructor `__init__` con asignación directa e inicialización de `_en_taller = False`.
  - [x] Implementación de los métodos de instancia `ingresar()` y `entregar()`.
  - [x] Publicación y sincronización de cambios en el repositorio remoto GitHub (`master`).
- **Conceptos aprendidos:**
  - Fundamentos de Programación Orientada a Objetos (POO) en Python: clases, instancias, constructor `__init__` y uso del parámetro `self`.
  - Tipado de atributos (`str`, `int`, `bool`) y convención de nombres para atributos protegidos (`_en_taller`).
  - Métodos de instancia para modificar el estado interno de un objeto.
  - Flujo de trabajo con Git y GitHub (`clone`, `add`, `commit`, `push`).
- **Dificultades / Retos:**
  - Configuración inicial de usuario y correo en Git local para permitir la creación de commits.
  - Definición y consenso de la estructura y alcance del constructor.
- **Próximos pasos:**
  - Realizar pruebas de instanciación y verificar el funcionamiento de los métodos en consola.
  - Agregar nuevas clases derivadas o relaciones de herencia según el avance del módulo.

### Sesión 2: 09/09/2026
- **Objetivo:** Implementar herencia en POO con la creación de clases derivadas (`AUTO`, `camion`, `moto`), incorporar nuevos atributos, documentar línea por línea el código de los módulos Python y publicar los avances en la rama `feature/desarrollo`.
- **Actividades realizadas:**
  - [x] Refactorización del tipado de atributos a nivel de instanciación en el constructor `__init__` (`self.atributo: tipo = valor`).
  - [x] Incorporación de los métodos `tarifa_hora()`, `get_patente()` y `get_anio()` en la clase base `VEHICULO`.
  - [x] Creación de clases derivadas en archivos independientes: `AUTO` (`auto.py`), `camion` (`camion.py`) y `moto` (`moto.py`) heredando de `VEHICULO`.
  - [x] Incorporación de atributos específicos `marca` y `modelo` con tipado de datos en el constructor de la clase `moto`.
  - [x] Documentación exhaustiva con comentarios explicativos línea por línea en todos los archivos `.py` del proyecto.
  - [x] Pruebas de ejecución e integración en `main.py`.
  - [x] Configuración de archivo `.gitignore` para ignorar archivos temporales y bytecode (`__pycache__/`, `*.pyc`).
  - [x] Publicación y sincronización de cambios en la rama `feature/desarrollo` en GitHub.
- **Conceptos aprendidos:**
  - Herencia en Python usando la sintaxis `class SubClase(ClasePadre)`.
  - Uso de `super().__init__()` para invocar el constructor de la clase base desde una subclase.
  - Firma de constructores extendidos con parámetros adicionales y tipado explícito.
  - Documentación de código y buenas prácticas para control de versiones ignorando archivos `.pyc` / `__pycache__`.
- **Próximos pasos:**
  - Definir métodos y atributos específicos para `AUTO` y `camion`.
  - Implementar polimorfismo sobreescribiendo el método `tarifa_hora()` en cada clase derivada.

---

## 📂 Recursos y Enlaces
- [Documentación oficial](https://docs.github.com)
