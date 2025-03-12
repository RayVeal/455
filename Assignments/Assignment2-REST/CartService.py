import os
from flask import Flask, jsonify, request
""" from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__)) """

from ProductService import *

""" app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'carts.sqlite')
db = SQLAlchemy(app) """

""" # User Model
class User(db.Model):  
    user_id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Integer)
 
    #individual cart items
    class Item(db.Model): 
        item_id = db.Column(db.Integer, primary_key=True) 
        product = db.Column(db.String(100), nullable=False)
        price = db.Column(db.Integer)
        cart_quantity = db.Column(db.Integer) """
        
        
#User data
users = [
    {"id": 1,"cart": 
        [
            {"product": "", "price": "", "cart_quantity": ""}
        ]
    },
    {"id": 2,"cart": 
        [
            {"product": "", "price": "", "cart_quantity": ""}
        ]
    }
]


# Endpoint 1: Retrieve the current contents of a user’s shopping car
""" @app.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    #user = User.query.filter(user_id == User.id)
    user = User.query.get(user_id)
    cart = [{"id": item.user_id, "total": item.total_price, "item_id": item.Item.item_id, "name" : item.Item.product, "price" : item.Item.price, "quantity": item.Item.cart_quantity} for item in user]
    return jsonify({"cart": cart}) """
    
@app.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    user = users[user_id-1]
    if user:
        return jsonify({"user": user})
    else:
        return jsonify({"error": "user not found"}), 404
    

# Endpoint 2: Add a specified quantity of a product to the user’s cart
""" @app.route('/cart/<int:user_id>/add/<int:product_id>', methods=['POST'])
def add_to_cart(user_id, product_id, quantity):
    user = User.query.get(user_id)
    #product = get_product(product_id=product_id)
    product = Product.query.get(product_id)
    
    data = request.json
    if "quantity" not in data:
        return jsonify({"error": "quantity is required"}), 400
    
    user.total_price += data['quantity'] * product.price

    new_product = User.Item(item_id=product.id, product=product.name, price=product.price, cart_quantity=quantity)
    #cart = [{"id": item.user_id, "total": item.total_price, "item_id": item.Item.item_id, "name" : item.Item.product, "price" : item.Item.price, "quantity": item.Item.cart_quantity} for item in user]
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "product added to cart", "product": {"id": new_product.id, "name": new_product.name, "price" : new_product.price, "quantity" : new_product.quantity}}), 201 """

@app.route('/cart/<int:user_id>/add/<int:product_id>', methods=['POST'])
def add_to_cart(user_id, product_id, quantity):
    #product = request.json.get(Product(product_id==id))
    #product = Product.query.get(product_id)
    #quantity = request.json.get("quantity", 1)
    product = request.get(f'http://ProductService:5000/products/{product_id}').json()
    #product = request.get(f'http://127.0.0.1:5000/products/{product_id}').json()

    cart = users.setdefault(user_id, {})
    if product in cart:
        cart[product_id-1]["quantity"] += quantity
    else:
        cart[product_id-1] = {
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        }
    
    #users[user_id].append(new_item)
    return jsonify({"message": "Item added", "cart": cart}), 201

# Endpoint 3: Remove a specified quantity of a product from the user’s cart
def remove_from_cart(user_id, product_id):
    quantity = request.json.get("quantity", 1)
    product = request.get(f'http://ProductService:5000/products/{product_id}').json()


    cart = users.get(user_id, {})
    if product in cart:
        if cart[product_id]["quantity"] <= quantity:
            del cart[product_id]
        else:
            cart[product_id]["quantity"] -= quantity

    return jsonify(cart)


if __name__ == '__main__':
    """ with app.app_context():
        db.create_all() """
    app.run(debug=True)
