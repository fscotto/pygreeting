from flask import Flask, jsonify, request, Blueprint
from flasgger import Swagger
import logging

app = Flask(__name__)
swagger = Swagger(app)

# Configura il logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Crea un blueprint per l'API v1
api_v1 = Blueprint('api_v1', __name__)

@api_v1.route('/greet', methods=['GET'])
def greet():
    """
    Greet a user by name.
    ---
    tags:
      - Greeting
    parameters:
      - name: name
        in: query
        type: string
        required: false
        default: World
        description: The name to greet.
    responses:
      200:
        description: A greeting message
        schema:
          type: object
          properties:
            message:
              type: string
              example: Hello, World!
    """
    name = request.args.get('name', 'World')
    message = f'Hello, {name}!'
    logger.info(f"[v1] Greeting requested for name: {name}")
    return jsonify({'message': message})

# Aggiungi endpoint di health check
@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    ---
    tags:
      - Health
    responses:
      200:
        description: Service is healthy
        schema:
          type: object
          properties:
            status:
              type: string
              example: OK
    """
    return jsonify({'status': 'OK'}), 200

# Registra il blueprint sotto /api/v1
app.register_blueprint(api_v1, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
