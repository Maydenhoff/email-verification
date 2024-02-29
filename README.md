# email-verification

1. Luego de clonar el repositorio, debes crear un entorno de desarrollo y activarlo: 
``` bash
python3 -m venv <ENV> 
source <ENV>/bin/activate
```
2. Debes instalar las dependencias con el siguiente comando:
```bash
pip install -r requirements.txt
```
3. Levantar la base de datos con el siguente comando:
```bash 
docker-compose up -d
```
4. Levantar el servidor con el siguiente comando:
``` bash
uvicorn main:app --reload
```

Documentacion:
    ``:PORT/docs``
