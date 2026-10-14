import requests
import urllib.parse

api_key = "d4293b59-4cb6-4e37-b3da-e515251d703d" 
route_url = "https://graphhopper.com/api/1/route?"
geocode_url = "https://graphhopper.com/api/1/geocode?"

while True:
    print("\n--- Planificador de Rutas de la Biblioteca Nacional ---")
    origen = input("Ingrese la ciudad de origen (o escriba 's' o 'salir' para terminar): ")
    if origen.lower() in ['s', 'salir']:
        print("Saliendo del programa. ¡Que tenga un excelente viaje!")
        break
        
    destino = input("Ingrese la ciudad de destino (o escriba 's' o 'salir' para terminar): ")
    if destino.lower() in ['s', 'salir']:
        print("Saliendo del programa. ¡Que tenga un excelente viaje!")
        break

    url_origen = geocode_url + urllib.parse.urlencode({"q": origen, "limit": "1", "key": api_key})
    res_origen = requests.get(url_origen).json()
    
    url_destino = geocode_url + urllib.parse.urlencode({"q": destino, "limit": "1", "key": api_key})
    res_destino = requests.get(url_destino).json()

    if "hits" in res_origen and len(res_origen["hits"]) > 0 and "hits" in res_destino and len(res_destino["hits"]) > 0:
        lat_origen = res_origen["hits"][0]["point"]["lat"]
        lng_origen = res_origen["hits"][0]["point"]["lng"]
        lat_destino = res_destino["hits"][0]["point"]["lat"]
        lng_destino = res_destino["hits"][0]["point"]["lng"]

        opciones_ruta = {
            "point": [f"{lat_origen},{lng_origen}", f"{lat_destino},{lng_destino}"],
            "vehicle": "car",
            "locale": "es",  # Asegura que las instrucciones vengan en español
            "instructions": "true",
            "key": api_key
        }
        
        url_final = route_url + urllib.parse.urlencode(opciones_ruta, doseq=True)
        res_ruta = requests.get(url_final).json()

        if "paths" in res_ruta:
            distancia_km = res_ruta["paths"][0]["distance"] / 1000.0
            tiempo_minutos = (res_ruta["paths"][0]["time"] / 1000.0) / 60.0

            # Valores numéricos formateados a 2 decimales (.2f)
            print(f"\n=================================================")
            print(f"Resumen del viaje de {origen} a {destino}:")
            print(f"Distancia total: {distancia_km:.2f} km.")
            print(f"Tiempo estimado: {tiempo_minutos:.2f} minutos.")
            print(f"=================================================\n")
            
            print("Instrucciones paso a paso:")
            for paso in res_ruta["paths"][0]["instructions"]:
                dist_paso = paso["distance"] / 1000.0
                print(f"- {paso['text']} ({dist_paso:.2f} km)")
        else:
            print("No se pudo encontrar una ruta válida.")
    else:
        print("Error: No se pudieron encontrar las coordenadas.")
