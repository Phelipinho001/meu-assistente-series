from flask import Flask, jsonify

from assistente import AssitenteMaratona

app = Flask(__name__)

@app.route('/api/dados-maratona', methods=['GET'])
def executar_loop_maratona():
    """
    Rota web que inicializa o assistente, executa um loop 
    e retorna os dados processados em formato JSON.
    """
    try:
        assistente = assistente.AssistenteMaratona()

        resultados = []
        
        for i in range(1, 6):
            dado_processado = assistente.coletar_dados_etapa(i) 
            
            resultados.append({
                "etapa": i,
                "info": dado_processado
            })
            
        return jsonify({
            "status": "sucesso",
            "quantidade": len(resultados),
            "dados": resultados
        }), 200

    except Exception as e:
        return jsonify({
            "status": "erro",
            "mensagem": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)