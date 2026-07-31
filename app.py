from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def get_info():
    return jsonify({
        "Nombre": "Jancarlo Giovanni Schwarz Chen",        
        "Album": "From Zero"  
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)