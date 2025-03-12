import requests

def get_all_products():
    response = requests.get('http://127.0.0.1:5000/products')
    data = response.json()
    return data

def get_product(product_id):
    response = requests.get(f'http://127.0.0.1:5000/products/{product_id}')
    data = response.json()
    return data

    """ try:
        response = requests.get('http://127.0.0.1:5000/products/{product_id}')
        data = response.json()
        return data
    except json.decoder.JSONDecodeError:
        print('The string does NOT contain valid JSON')
 """
 
def create_product(name, price, quantity):
    new_product = {"name": name, "price" : price, "quantity" : quantity}
    response = requests.post('http://127.0.0.1:5000/products', json=new_product)
    data = response.json()
    return data

def add_to_cart(user_id, product_id, quantity):
    user = requests.get(f'http://127.0.0.1:5000/cart/{user_id}')
    item = requests.get(f'http://127.0.0.1:5000/products/{product_id}')
    response = requests.post('/cart/{user_id}/add/{product_id}', json=item)
    data = response.json()
    return data
    

""" def remove_product(product_id):
    response = requests.delete(f'http://127.0.0.1:5000/products/{product_id}')
    data = response.json()
    return data """
    
def remove_from_cart(user_id, product_id, quantity):
    user = requests.get(f'http://127.0.0.1:5000/cart/{user_id}')
    item = requests.get(f'http://127.0.0.1:5000/products/{product_id}')
    response = requests.delete('/cart/{user_id}/add/{product_id}', json=item)
    data = response.json()
    return data    

if __name__ == '__main__':
    all_products = get_all_products()
    print("All products:")
    print(all_products)

    product_id = 1
    specific_product = get_product(product_id)
    print(f"\nproduct {product_id}:")
    print(specific_product)
    
    add_to_cart(1,1,2)


"""     new_product_name = "new product"
    new_product_price = "$27.50"
    new_product_quantity = "400"
    created_product = create_product(new_product_name, new_product_price, new_product_quantity)
    print(f"\nCreated product:")
    print(created_product) """
    
    
"""     deleted_product = remove_product(product_id)
    print(f"\nDeleted product {product_id}:")
    print(deleted_product) """
