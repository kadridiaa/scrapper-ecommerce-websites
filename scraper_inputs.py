
from flask import Flask, request, jsonify
import json
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/store_data_zara', methods=['POST'])
def store_data_zara():
    data = request.json
    print(data)
    numberOfProducts = str(data['numberOfProducts'])
    nameOfProduct = data['nameOfProduct']
    sexe = data['sexe'].upper()
    subprocess.run(['python', r'D:\Projects\Scrapping_pfe\scrapper-ecommerce-websites\scraper_zara.py', numberOfProducts, nameOfProduct, sexe])
    
    return jsonify({'message': 'Data stored successfully'})

@app.route('/store_data_pmg', methods=['POST'])
def store_data_pmg():
    data = request.json
    print(data)
    product_searched = data['product_searched']
    sexe = data['sexe'].upper()
    brand = data['brand'].upper()
    
    subprocess.run(['python', r'D:\Projects\Scrapping_pfe\scrapper-ecommerce-websites\scraper_pmg.py', product_searched, brand, sexe])
    
    response = jsonify({'message': 'Data stored successfully'})
    return response

if __name__ == '__main__':
    app.run(debug=True)
