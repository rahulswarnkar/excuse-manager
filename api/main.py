from flask import Flask, request, jsonify
import service

app = Flask(__name__)

@app.route("/")
def index():
    return "Excuse Manager"

@app.route("/excuses", methods=['GET'])
def list_excuses():
    app.logger.info("listing excuses")
    return jsonify(service.get_all())

@app.route("/excuses/<int:id>", methods=['GET'])
def get_excuse(id):
    app.logger.info("getting excuse by id")
    excuse = service.get_by_id(id)
    if(excuse is None):
        return 'excuse not found', 404
    return jsonify(excuse)

@app.route("/excuses", methods=['POST'])
def add_excuse():
    body = request.get_json()
    if('message' not in body):
        return 'message not found', 400
    app.logger.info("adding an excuse")
    service.add(body)
    return '', 201

@app.route("/excuses/<int:id>", methods=['DELETE'])
def delete_excuse(id):
    app.logger.info("deleting an excuse by id")
    if(service.delete_by_id(id)):
        return '', 200
    return 'excuse not found', 404

if __name__ == "__main__":
    app.run()