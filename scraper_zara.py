import requests
import json
import sys
import time

import pymysql

HEADERS = {
    'accept': '*/*',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

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

def format_query_column(column_name):
    """
    Formats a column name for a SQL query.

    Args:
        column_name (str): The name of the column.

    Returns:
        str: The formatted column name.
    """
    return '`{}`'.format(column_name.replace('`', '``'))

def generate_insert_query(table_structure, table_name):
    """
    Generates an SQL insert query for a given table structure.

    Args:
        table_structure (dict): Dictionary representing the structure of the table.
        table_name (str): The name of the table.

    Returns:
        str: The SQL insert query.
    """
    names = list(table_structure)
    cols = ', '.join(map(format_query_column, names))
    placeholders = ', '.join(['%({})s'.format(name) for name in names])
    query = 'INSERT INTO {} ({}) VALUES ({})'.format(table_name, cols, placeholders)
    return query

def insert_into_database(products):
    """
    Inserts product data into a MySQL database.

    Args:
        products (list): List of dictionaries representing product data.
    """
    host = 'localhost'
    user = 'root'
    password = 'root'
    database = 'diaa'
    table_name = "products"

    connection = create_pymysql_connection(host=host, password=password, user=user, database=database)
    sql = generate_insert_query(product_struct(), table_name)
    print(sql)
    with connection.cursor() as cursor:
        cursor.execute('SET SESSION wait_timeout=8000;')
        l = cursor.executemany(sql, (products))
    connection.commit()
    connection.close()

def product_struct():
    """
    Defines the structure of product data.

    Returns:
        dict: Dictionary representing the structure of product data.
    """
    return {
        "product_id": "",
        "availability": "",
        "name": "",
        "price": "",
        "oldPrice" : "",
        "displayDiscountPercentage" : "",
        "familyName": "",
        "subfamilyName": "",
        "sectionName": "",
        "img": "",
        "link":"",
    }

def fetch_page_data(url, params):
    """
    Fetches data from a URL using GET requests and saves it to a JSON file.

    Args:
        url (str): The URL to fetch data from.
        params (dict): Parameters to include in the request.

    Returns:
        list: List of product data dictionaries.
    """
    product_list = []
    status_code = None

    while status_code != 200:
        response = requests.get(url, params=params, headers=HEADERS)
        status_code = response.status_code
        print("status_code: ", status_code)

    print("status_code: ", status_code)

    file_path = "page_zara.json"

    with open(file_path, 'w') as json_file:
        json.dump(response.json(), json_file, indent=4)

    data = response.json()

    results = data["results"]
    cpt = 0
    print("size : ", len(results))

    for row in results:
        if row["content"]["name"] == 'LOOK':
            continue  
        else:
            product = product_struct()
            product_availability = row["content"]["availability"]
            product_name = row["content"]["name"]
            product_price = row["content"]["price"]  
            product_familyName = row["content"]["familyName"]
            product_id = row["content"]["id"]
            product_subfamilyName = row["content"]["subfamilyName"]
            product_sectionName = row["content"]["sectionName"]
            if "oldPrice" in row["content"]:
                product_oldPrice = row["content"]["oldPrice"]
                product_displayDiscountPercentage = row["content"]["displayDiscountPercentage"]
            else:
                product_displayDiscountPercentage = None  
                product_oldPrice = None 
        
            img_path = row["content"]["xmedia"][0]["path"]
            img_name = row["content"]["xmedia"][0]["name"]
            img_timestamp = row["content"]["xmedia"][0]["timestamp"]
            img_based_link = "https://static.zara.net/photos//"
            product_img_link = ''.join([img_based_link, img_path, "/w/305/", img_name, ".jpg?ts=", img_timestamp])
            link_keyword = row["content"]["seo"]["keyword"]
            link_seo_product_id = row["content"]["seo"]["seoProductId"]
            link_discern_product_id = row["content"]["seo"]["discernProductId"]
            product_based_link = 'https://www.zara.com/dz/fr/' 
            product_link = ''.join([product_based_link , link_keyword , '-p' , link_seo_product_id , '.html?v1=',str(link_discern_product_id)] )
            
            
            ##https://www.zara.com/dz/fr/
            # debardeur-cotele-   == keyword
            # p00679402.html?    == seoProductId
            # v1=323216378  == discernProductId
       
         
        product["availability"] = product_availability
        product["name"] = product_name
        product["price"] = product_price
        product["oldPrice"] = product_oldPrice  
        product["displayDiscountPercentage"] = product_displayDiscountPercentage  
        product["familyName"] = product_familyName
        product["product_id"] = product_id
        product["subfamilyName"] = product_subfamilyName
        product["sectionName"] = product_sectionName
        product["img"] = product_img_link
        product["link"] = product_link
        
        product_list.append(product)
        cpt+=1
        print(cpt)
    return product_list

def main():
    """
    Main function to orchestrate the process of fetching and inserting data.
    to do : 
      - get the promotion     ====>  done
      - chose if i get the product classified as LOOk or not ;  ====> done
      - add the link of the product  ===> done 
      - variable man-woman is descreptif ?   ==> done 
      - create a scrapper who suggest to collect data for man or woman ;  
      - create a scrapper who suggest to collect data for the search input ;  
      
    """
    # product_limit = '100'
    # product_search = 't shirt'
    # sexe = 'MAN'

    if len(sys.argv) >= 4:
        
       product_limit = sys.argv[1]
       product_search = sys.argv[2]
       sexe = sys.argv[3]

       params = {
        'query': '{}'.format(product_search),
        'locale': 'fr_FR',
        'deviceType': 'desktop',
        'deviceOS': 'Linux',
        'catalogue': '45551',
        'warehouse': '47553',
        'section': '{}'.format(sexe),
        'offset': '0',
        'limit': '{}'.format(product_limit),
        'scope': 'default',
        'origin': 'default',
        'ajax': 'true',
    }

    url = 'https://www.zara.com/itxrest/1/search/store/16201/query'
    print('before fetching')
    products = fetch_page_data(url, params)
    print("product len : ", len(products))
    insert_into_database(products)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Exception:", e)
        sys.exit()
