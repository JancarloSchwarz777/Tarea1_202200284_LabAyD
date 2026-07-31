from flask import Flask, jsonify

app = Flask(__name__)

# Versión 1.0.0: nombre + canción favorita
@app.route('/info', methods=['GET'])
def get_info():
    return jsonify({
        "Nombre": "Jancarlo Giovanni Schwarz Chen",        
        "Cancion_favorita": "Heavy is the Crown"  
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)