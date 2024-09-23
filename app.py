from flask import Flask, jsonify, request, send_from_directory
import json
import os

app = Flask(__name__)

# Загружаем данные из файла food.json
with open('food.json', 'r', encoding='utf-8') as f:
    food_data = json.load(f)

# Роут для получения всех продуктов
@app.route('/api/foods', methods=['GET'])
def get_foods():
    return jsonify(food_data)

# Роут для получения продукта по его ID
@app.route('/api/foods/<int:product_id>', methods=['GET'])
def get_food(product_id):
    product = next((item for item in food_data if item['product_id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

# Роут для получения продуктов по категории
@app.route('/api/foods/category/<int:category_id>', methods=['GET'])
def get_foods_by_category(category_id):
    products = [item for item in food_data if item['category_id'] == category_id]
    if products:
        return jsonify(products)
    else:
        return jsonify({'error': 'No products found in this category'}), 404

# Роут для получения изображения продукта
@app.route('/api/img/<filename>', methods=['GET'])
def get_image(filename):
    img_folder = os.path.join(os.getcwd(), 'img')
    return send_from_directory(img_folder, filename)

# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True)
