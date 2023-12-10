import requests
import os


ids = {"2512.1":"349ee6f6-c295-4c38-9b98-48765b55280e",
       "2512.2":"04ba4d6c-957d-417f-bf63-5b9e015a9f86",
       "2512.3":"d0aa0792-4345-474b-9365-686cf4869d2e",
       "2512.4":"f2b15a0e-e65a-438a-affb-29b9d50b77d1",
       "2512.4.1":"24135b84-cbdd-4d42-9ed2-02fd982d15b2",
       "2512.5":"866c7813-2c03-47d7-9bdc-192cfbace57c"
       }

#print(f"DIR: {os.path.dirname(os.path.abspath(__file__))}")
      
with open(f"{os.path.dirname(os.path.abspath(__file__))}\\Resultado_competencias_ESCO.csv", "w") as f:
    f.write("ID;Competencia;Tipo de competencia\n")
    for key in ids:

        id = ids[key]

        url_root = 'https://ec.europa.eu/esco/api/resource/'
        target_uri = "http://data.europa.eu/esco/occupation/"+id
        language = 'es'
        acceptLanguage = 'es'

        header = {
            'content_type': 'application/json',
            'charset': 'UTF-8'
        }
        params = {
            'uri': target_uri,
            'language': language,
            'selectedVersion': "V1.1.1"
        }

        url = url_root + 'occupation'
        resp = requests.get(url, headers = header, params = params)
        essential_skills = resp.json()["_links"]["hasEssentialSkill"]
        optional_skills = resp.json()["_links"]["hasOptionalSkill"]
       
       #ESCRITURA A FICHERO
        for skill in essential_skills:
            f.write(f"{key};{skill["title"]};Esencial\n")
        for skill in optional_skills:
            f.write(f"{key};{skill["title"]};Opcional\n")         

    f.close()