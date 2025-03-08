# Proyecto de Automatización de Pruebas de API REST

Este proyecto implementa un framework de automatización de pruebas para la API REST [ReqRes](https://reqres.in/) utilizando Python, Requests y Pytest.

## Estructura del Proyecto

```
Test-Backend-Cod/
├── config.py           # Configuración y constantes del proyecto
├── pages/              # Clases para interactuar con la API
│   └── user_api.py     # Clase para interactuar con el endpoint de usuarios
└── tests/              # Casos de prueba
    └── test_user_api.py  # Pruebas para el endpoint de usuarios
```

## Requisitos

- Python 3.7+
- Requests
- Pytest

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/dux14/Test-Backend-Cod
cd Test-Backend-Cod
```

2. Crear un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate
```

3. Instalar las dependencias:
```bash
pip install pytest requests pytest-html
```

## Configuración

El archivo `config.py` contiene todas las constantes y configuraciones necesarias para las pruebas:

- URL base de la API
- Endpoints específicos
- Headers por defecto
- Códigos de estado HTTP esperados

## Casos de Prueba

El proyecto incluye los siguientes casos de prueba:

1. **test_create_user_positive**: Verifica la creación exitosa de usuarios con diferentes conjuntos de datos.
   - Caso 1: Creación de usuario con datos básicos (nombre y trabajo)
   - Caso 2: Creación de usuario con datos adicionales (género y edad)

2. **test_create_user_negative**: Verifica el manejo de errores al enviar datos malformados.

## Ejecución de Pruebas

Para ejecutar todas las pruebas:

```bash
python -m pytest tests/test_user_api.py -v
```

Para generar un reporte HTML:

```bash
python -m pytest tests/test_user_api.py -v --html=report.html
```

## Parametrización de Pruebas

Este proyecto utiliza la funcionalidad de parametrización de Pytest para ejecutar el mismo caso de prueba con diferentes conjuntos de datos:

```python
@pytest.mark.parametrize("payload, expected_status, expected_data", [
    (
        {"name": "John Arias", "job": "Software Engineer"}, 
        STATUS_CREATED, 
        {"name": "John Arias", "job": "Software Engineer"}
    ),
    (
        {"name": "John Arias", "job": "Software Engineer", "gender": "Male", "age": 33}, 
        STATUS_CREATED, 
        {"name": "John Arias", "job": "Software Engineer", "gender": "Male", "age": 33}
    ),
])
```

## Arquitectura del Proyecto

El proyecto sigue una arquitectura simple pero efectiva:

- **Capa de Configuración**: Contiene todas las constantes y configuraciones.
- **Capa de Servicio**: Clases en el directorio `pages/` que encapsulan las llamadas a la API.
- **Capa de Pruebas**: Casos de prueba que utilizan las clases de servicio.

## Autor

Samuel Duque Porras
