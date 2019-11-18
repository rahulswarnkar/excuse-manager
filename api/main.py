from flask import Flask, request, jsonify

app = Flask(__name__)

excuse_list = []

def replace_list(new_list):
    global excuse_list
    excuse_list = new_list

@app.route("/")
def index():
    return "Excuse Manager"

@app.route("/excuses", methods=['GET'])
def list_excuses():
    app.logger.info("listing excuses")
    return jsonify(excuse_list)

@app.route("/excuses/<int:id>", methods=['GET'])
def get_excuse(id):
    app.logger.info("getting excuse by id")
    excuse = next((excuse for excuse in excuse_list if excuse['id'] == id), None)
    if(excuse is None):
        return 'excuse not found', 404
    return jsonify(excuse)

@app.route("/excuses", methods=['POST'])
def add_excuse():
    body = request.get_json()
    if('message' not in body):
        return 'message not found', 400
    excuse = {
        'id': len(excuse_list) + 1,
        'author': request.remote_addr,
        'message': body['message']
    }
    app.logger.info("adding an excuse")
    replace_list(excuse_list + [excuse])
    return '', 201

@app.route("/excuses/<int:id>", methods=['DELETE'])
def delete_excuse(id):
    app.logger.info("deleting an excuse by id")
    excuse = next((excuse for excuse in excuse_list if excuse['id'] == id), None)
    if(excuse is None):
        return 'excuse not found', 404
    replace_list([excuse for excuse in excuse_list if excuse['id'] != id])
    return '', 200

if __name__ == "__main__":
    app.run()