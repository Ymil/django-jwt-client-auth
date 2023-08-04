# Aplicación Cliente para Autenticaciones de Django contra Servicios Externos

Esta es una aplicación cliente para Django que permite autenticar usuarios mediante JSON Web Tokens (JWT) con servicios externos. La aplicación es capaz de crear un usuario en la base de datos de Django y realizar la autenticación estándar de Django para proporcionar acceso a toda la funcionalidad de gestión de usuarios de Django.

## Características principales

- **Autenticación por JWT:** La aplicación cliente puede autenticarse con servicios externos utilizando tokens JWT.
- **Creación de usuarios:** Una vez autenticado correctamente con JWT, la aplicación crea un usuario en la base de datos de Django, lo que permite gestionar los usuarios desde el propio Django.
- **Autenticación de Django:** Tras la creación del usuario, la aplicación realiza la autenticación estándar de Django, permitiendo al usuario acceder a todas las funcionalidades de gestión de usuarios que Django ofrece por defecto.

## Configuración

1. **Instalación:** Para utilizar esta aplicación, asegúrate de tener Django instalado en tu entorno virtual. Luego, puedes instalar la aplicación cliente mediante el siguiente comando:

    ```bash
    pip install -e git+https://github.com/Ymil/django-jwt-client-auth.git
    ```

2. **Configuración de la aplicación:** Añade `external_auth_client` a la lista `INSTALLED_APPS` en el archivo `settings.py` de tu proyecto Django:

    ```python
    INSTALLED_APPS = [
        # Otras aplicaciones instaladas...
        'jwt_client_auth',
    ]
    ```

3. **Configuración de la URL:** Añade la URL para iniciar la autenticación JWT en tu archivo `urls.py`:

    ```python
    from django.urls import include

    urlpatterns = [
        # Otras URLs...
        path('', include("jwt_client_auth.urls")),
    ]
    ```

## Uso

1. Cuando un usuario acceda a la URL `login/`, la aplicación cliente iniciará el proceso de autenticación con el servicio externo mediante JWT.

2. Si la autenticación con JWT es exitosa, la aplicación creará automáticamente un usuario en la base de datos de Django con los datos proporcionados por el servicio externo.

3. El usuario recién creado será autenticado automáticamente mediante el sistema de autenticación estándar de Django, lo que permitirá al usuario acceder a todas las funcionalidades de gestión de usuarios proporcionadas por Django.

## Configuración

### Variables

Las siguientes variables se deben/pueden configurar en el settings.py del proyecto.

```python
JWT_ENDPOINT # URL de autenticación [Obligatoria]
JWT_REDIRECT_URL # Name redirection
JWT_ENDPOINT_SSL_VERIFY # Activa o desactiva la verificación SSL
JWT_ENDPOINT_ERROR_MESSAGE_FIELD # Indica el campo donde se devuelve la respuesta del error
```

### Template

Podes agregar en tu proyecto el template login.html para customizar el login

### Acceso al JWT

Se puede acceder al JWT mediante la variable `request.session["JWT"]`

## Consideraciones finales

Esta aplicación cliente para autenticaciones de Django contra servicios externos proporciona una forma sencilla de integrar la autenticación mediante JWT en tu proyecto Django. Al permitir la creación de usuarios en la base de datos y utilizar la autenticación estándar de Django, tu aplicación podrá ofrecer una experiencia de usuario coherente y segura, aprovechando todas las funcionalidades de gestión de usuarios que Django proporciona de forma nativa.

Es importante asegurarse de que el servicio externo proporcione tokens JWT válidos y que la aplicación cliente esté correctamente configurada para comunicarse con dicho servicio. Además, ten en cuenta las medidas de seguridad adecuadas para proteger la autenticación y asegurar que solo usuarios autorizados tengan acceso a tu aplicación Django.