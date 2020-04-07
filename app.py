from flask import Flask, jsonify, request

app = Flask(__name__)
# @app.route('/')
# def home():
#     return "Hello Flask"

stores = [
            {
            'name':'Store1',
            'item':[
                        {
                        'name':'My Item1',
                        'price': 15.99
                        }                   
                    ]
            },
            {
            'name':'Store2',
            'item':[
                        {
                        'name':'My Item2',
                        'price': 10.99
                        }                   
                    ]
            },
         ]

# POST /store
# Create new store  
@app.route('/store', methods = ['POST']) 
def create_store():
    requested_data = request.get_json()
    for store in stores:
        if store['name'] == requested_data['name']:
            return jsonify({'Message':'Store already exists'})
    new_store = {'name':requested_data['name'], 'item':[]}
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name> 
# Get store
@app.route('/store/<string:name>')
def get_store(name):
    #Iterate over store 
    #if the store matches, return it otherwise error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'Message':'Store not found'})
 
# GET /store 
# Get list of all stores   
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})  

# POST /store/<string:name>/item {name:price}
# Create new item in store
@app.route('/store/<string:name>/item', methods = ['POST']) 
def create_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            for i in store['item']:
                requested_data = request.get_json()
                if i['name'] == requested_data['name']:
                    return jsonify({'Message':'Item already in list'})
            new_item = {'name':requested_data['name'], 'price':requested_data['price']}
            store['item'].append(new_item)
            return jsonify({'items':store['item']})
    return jsonify({'Message':'Store not found'})

# GET /store/<string:name>/item 
# Get list of all items in store
@app.route('/store/<string:name>/item') 
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['item']})
    return jsonify({'Message':'Store not found'}) 

app.run(port=5000)
