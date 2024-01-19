Pasos para correr la aplicación (Se debe tener instalado python como minimo)

1. Hacer un git clone del repositorio
2. Crear un entorno virtual dentro de la carpeta raiz con el comando "python -m venv venv"
3. Activar el entorno virtual con el comando ".\venv\scripts\activate"
4. Instalar los requerimientos del proyecto con el comando "pip install -r requirements.txt"
5. Realizar las migraciones con el comando "python manage.py migrate"
6. Llenar la base de datos con los fixtures con el siguiente comando "python manage.py loaddata seat_fixture(nombre del fixture)"
7. Correr el servidor con el comando "python manage.py runserver"
