from flask import Flask, jsonify, request
app = Flask(__name__)


todos =[{
    "label": "My first task", "done": False
}]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print('Incoming request with the folowwing body', request_body)
    todos.append(request_body)
    print('Updated todos', todos)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    for i in todos:
        if todos.index(i) == position:
            todos.remove(i)
            return jsonify(todos), 200

if __name__=='__main__':
    app.run(host='0.0.0.0', port=3245, debug= True)
