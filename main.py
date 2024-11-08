from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/hello_world', methods = ['GET'])
def sayHello():
    data = {
        1:"Hello world"
    }
    return jsonify(data)

@app.route('/users', methods = ["GET"])
def returnUserInfo():
    id = request.args.get("id")
    return jsonify(users[int(id)])

users = {
    1:{
        "name": "Alex",
        "age": "25"
    },

    2:{
        "name": "Sanya",
        "age": "19"
    },

    3:{
        "name": "Ivan",
        "age": "18"
    }
}




if __name__ == "__main__":
    app.run(debug = True)
