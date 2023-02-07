from flask import Flask, jsonify, request

app = Flask(__name__)


# my custom data storage
class mydb():
    store = [{
        'id': 1,
        'name': 'atif',
        'age': 30
    },
        {
        'id': 2,
        'name': 'faisal',
        'age': 25
    }]
    lastRow = ''

    def __init__(self):
        pass
        # print('db initialized')

    def add(self, row):
        row['id'] = len(self.store) + 1
        self.lastRow = row
        self.store.append(row)
        return self.store

    def get(self):
        return self.store

    def getSingle(self, id):

        # first approch
        singleList = list(filter(lambda row: row['id'] == int(id), self.store))

        # 2nd approch
        # for row in db.store:
        #     if(row['name'] == name):
        #         return row

        return singleList

    def delete(self, id):
        newStore = list(filter(lambda row: row['id'] != id, self.store))
        self.store = newStore
        return newStore

    def update(self, id, set):
        for i in range(len(self.store)):
            if(self.store[i]['id'] == int(id)):
                self.store[i]['name'] = set['name']
                self.store[i]['age'] = int(set['age'])

        return self.store

    # db object
db = mydb()


@app.route('/', methods=['GET'])
def get():
    result = db.get()
    return jsonify(result)


@app.route('/<id>', methods=['GET'])
def getSingle(id):
    result = db.getSingle(id)
    return jsonify(result)


@app.route('/add', methods=['POST'])
def add():
    name = request.json['name']
    age = request.json['age']

    result = db.add({'name': name, 'age': age})
    return jsonify(result)


@app.route('/update/<id>', methods=['PUT'])
def update(id):
    name = request.json['name']
    age = request.json['age']
    result = db.update(id, {'name': name, 'age': age})
    return jsonify(result)


@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    result = db.delete(int(id))
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
