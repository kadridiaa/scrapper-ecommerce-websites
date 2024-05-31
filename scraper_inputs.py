from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import pymysql


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
def create_pymysql_connection(host, database, password, user):
    """
    Establishes a connection to a MySQL database using pymysql.

    Args:
        host (str): The host address of the MySQL database.
        database (str): The name of the MySQL database.
        password (str): The password for the MySQL user.
        user (str): The username for the MySQL database.

    Returns:
        pymysql.connections.Connection: A connection object to the MySQL database.
    """
    try:
        db = pymysql.connect(host=host, database=database, password=password, user=user, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        return db
    except Exception as e:
        print(str(e))

def generate_insert_website_query(table_name):
    query = "REPLACE INTO {} (NombreS) VALUES (%s)".format(table_name)
    return query

def increment_website_count(connection, table_name, website_id):
    current_count = 0
    if website_id == 1 or website_id == 2:
        with connection.cursor() as cursor:
            cursor.execute("SELECT NombreS FROM {} WHERE website_id = %s".format(table_name), (website_id,))
            result = cursor.fetchone()
            if result:
                current_count = result["NombreS"]
                current_count += 1
                cursor.execute("UPDATE {} SET NombreS = %s WHERE website_id = %s".format(table_name), (current_count, website_id))
            else:
                cursor.execute("INSERT INTO {} (NombreS, websiteId) VALUES (%s, %s)".format(table_name), (1, website_id))
        connection.commit()
    return current_count

def insert_into_website_table(connection, current_count):
    table_name = "website"
    sql = generate_insert_website_query(table_name)
    with connection.cursor() as cursor:
        cursor.execute(sql, (current_count,))
    connection.commit()

@app.route('/store_data_zara', methods=['POST'])
def store_data_zara():
    data = request.json
    print(data)
    numberOfProducts = str(data['numberOfProducts'])
    nameOfProduct = data['nameOfProduct']
    sexe = data['sexe'].upper()
    subprocess.run(['python', r'D:\Projects\Scrapping_pfe\scrapper-ecommerce-websites\scraper_zara.py', numberOfProducts, nameOfProduct, sexe])

    # Increment Zara website count
    connection = create_pymysql_connection(host='localhost', password='root', database='diaa', user='root')
    current_count = increment_website_count(connection, "website", 1)
    print(current_count)
    insert_into_website_table(connection, current_count)

    return jsonify({'message': 'Data stored successfully'})

@app.route('/store_data_pmg', methods=['POST'])
def store_data_pmg():
    data = request.json
    print(data)
    product_searched = data['product_searched']
    sexe = data['sexe'].upper()
    brand = data['brand'].upper()
    subprocess.run(['python', r'D:\Projects\Scrapping_pfe\scrapper-ecommerce-websites\scraper_pmg.py', product_searched, brand, sexe])

    # Increment PMG website count
    connection = create_pymysql_connection(host='localhost', password='root', database='diaa', user='root')
    current_count = increment_website_count(connection, "website", 2)
    print(current_count)
    insert_into_website_table(connection, current_count)

    response = jsonify({'message': 'Data stored successfully'})
    return response

if __name__ == '__main__':
    app.run(debug=True)
