import requests

def obtener_info_pokemon(nombre_o_id):
    """Obtiene y muestra informacion de un Pokemon dado su nombre o ID."""
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_o_id}" # URL de la API de Pokemon

    try: 
        respuesta = requests.get(url) # Realiza la solicitud GET a la API
        respuesta.raise_for_status()  # Lanza un error si la solicitud falla

        data = respuesta.json() # Convierte la respuesta a formato JSON

        nombre = data["name"] # Nombre del Pokemon
        peso = data["weight"] # Peso del Pokemon
        habilidades = [h["ability"]["name"] for h in data ["abilities"]] # Lista de habilidades del Pokemon 

        print("=" * 50)
        print("Informacion del Pokemon") 
        print("=" * 50)
        print(f"Nombre: {nombre}") #Imprime el nombre del Pokemon
        print(f"Peso: {peso}") #Imprime el peso del Pokemon
        print("Habilidades:", ", ".join(habilidades)) # Imprime las habilidades del Pokemon
        print("=" * 50)

    except requests.exceptions.HTTPError: # Maneja errores HTTP (Ej. 404, si no se encuentra el Pokemon)
        print(f"Error, Pokemon no encontrado:") # Imprime mensaje de error si el Pokemon no se encuentra
    
    except Exception as err: # Maneja otros errores
        print(f"Error de solicitud: {err}") # Imprime mensaje de error general

nombre_pikachu = input("Ingresar nombre del Pokemon:") # Solicita al usuario el nombre del Pokemon
obtener_info_pokemon(nombre_pikachu) # Llamma a la funcion con el nombre del Pokemon


