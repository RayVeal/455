curl -X GET http://127.0.0.1:5000/products
curl -X GET http://127.0.0.1:5000/products/2
#curl -X POST -H "Content-Type: application/json" -d '{"title": "New Product"}' http://127.0.0.1:5000/products
cURL -X POST -H "Content-Type: application/json" -d '{"name": "Aioli", "price": "$27.50", "quantity": "367"}' http://127.0.0.1:5000/products
curl -X POST -H "Content-Type: application/json" -d '{"quantity": 2}' http://your-cart-service-url/cart/user_id/add/product_id

