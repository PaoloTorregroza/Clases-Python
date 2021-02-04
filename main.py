from ClasesImportantes import Estudiante
import requests  # pip install requests

# https://docs.python.org/3/library/math.html
luke = requests.get("https://swapi.dev/api/people/1/")
print(luke.content)
