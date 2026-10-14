## Descripción del Proyecto
Este proyecto es un prototipo de software de geolocalización desarrollado en Python para los visitantes de la Biblioteca Nacional

## Instrucciones de ejecución
Para ejecutar este script de Python correctamente en su entorno, siga estos pasos:

1. Asegúrese de tener instalada la librería `requests`. Si no la tiene, instálela ejecutando en su terminal:
   `pip install requests`
2. Abra el archivo `geolocalizacion.py` en su editor de código.
3. Localice la variable `api_key` en las primeras líneas del código y reemplace `"TU_TOKEN_AQUI"` por su Token de acceso personal de Graphhopper.
4. Abra una terminal en la ubicación del archivo y ejecute el script con el siguiente comando:
   `python3 geolocalizacion.py`
5. Siga las instrucciones en pantalla ingresando la ciudad de origen y destino. Para finalizar la ejecución en cualquier momento, escriba `s` o `salir`.
