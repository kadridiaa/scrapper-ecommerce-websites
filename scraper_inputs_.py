# from flask import Flask, request, jsonify
# import json
# from flask_cors import CORS
# import subprocess

# app = Flask(__name__)
# CORS(app)
# @app.route('/store_data_zara', methods=['POST'])
# def store_data():
#     data = request.json
#     numberOfProducts = str(data['numberOfProducts'])
#     nameOfProduct = data['nameOfProduct']
#     sexe = data['sexe'].upper()
#     # with open('scraped_data.json', 'w') as json_file:
#     #     json.dump(data, json_file, indent=4)

#     subprocess.run(['python', r'D:\Projects\Scrapping_pfe\Scrapperrebots\scraper_zara.py', numberOfProducts,nameOfProduct , sexe])
#     return jsonify({'message': 'Data stored successfully'})


# @app.route('/store_data_pmg', methods=['POST'])
# def store_data_pmg():
#     data = request.json
#     product_searched= data['product_searched']
#     sexe = data['sexe'].upper()
#     brand = data.get('brand', '') 
#     subprocess.run(['python', r'D:\Projects\Scrapping_pfe\Scrapperrebots\scraper_pmg.py', product_searched,brand , sexe])
#     return jsonify({'message': 'Data stored successfully'})




# if __name__ == '__main__':
#     app.run(debug=True)


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
    subprocess.run(['python', r'D:\Projects\Scrapping_pfe\Scrapperrebots\scraper_zara.py', numberOfProducts, nameOfProduct, sexe])
    
    return jsonify({'message': 'Data stored successfully'})

@app.route('/store_data_pmg', methods=['POST'])
def store_data_pmg():
    data = request.json
    print(data)
    product_searched = data['product_searched']
    sexe = data['sexe'].upper()
    brand = data['brand'].upper()
    
    subprocess.run(['python', r'D:\Projects\Scrapping_pfe\Scrapperrebots\scraper_pmg.py', product_searched, brand, sexe])
    
    response = jsonify({'message': 'Data stored successfully'})
    return response

if __name__ == '__main__':
    app.run(debug=True)
