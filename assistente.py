import requests
import os
from dotenv import load_dotenv

load_dotenv()

class AssitenteMaratona():
    def buscar_serie(self, titulo):
        chave = os.getenv("API_KEY") 
        
        if not chave:
            print("Chave de acesso da API não encontrada/errada")
            return {"Erro": "Chave da API não encontrada"}

        url = f"http://www.omdbapi.com/?t={titulo}&apikey={chave}"
        
        try:
            r = requests.get(url, timeout = 10)
            r.raise_for_status() 
            dados = r.json() 

            if dados.get("Response") == "True":
  
                return {
                    "titulo": dados.get('Title'),
                    "ano": dados.get('Year'),
                    "nota": dados.get('imdbRating')
                }
            else:
                return {"Erro": f"Não foi possível encontrar a série: '{titulo}'."}
                

        except Exception as e:
            return {"Erro": f"Falha na conexão: {e}"}
        
assistente = AssitenteMaratona()


minha_lista = ["Breaking Bad", "Round 6", "SerieQueNaoExiste"]

for serie in minha_lista:
    assistente.buscar_serie(serie)