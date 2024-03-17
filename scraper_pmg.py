import requests
from bs4 import BeautifulSoup
import sys
import pymysql

cookies = {
    "_gid": "GA1.2.2040364351.1709239339",
    "tk_or": "%22https%3A%2F%2Fl.facebook.com%2F%22",
    "tk_r3d": "%22https%3A%2F%2Fl.facebook.com%2F%22",
    "tk_lr": "%22%22",
    "tk_ai": "SkrUn7rdhiQdtBDWfjooFd9p",
    "tk_qs": "",
    "_gat": "1",
    "_gat_gtag_UA_63486687_1": "1",
    "_ga": "GA1.1.1205079837.1709239339",
    "_ga_00T8MSY9YE": "GS1.1.1709239339.1.1.1709241358.0.0.0",
    "_ga_DJKTT1XZTQ": "GS1.2.1709239408.1.1.1709241359.0.0.0",
}

headers = {
    "authority": "pmg.dz",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    # 'cookie': '_gid=GA1.2.2040364351.1709239339; tk_or=%22https%3A%2F%2Fl.facebook.com%2F%22; tk_r3d=%22https%3A%2F%2Fl.facebook.com%2F%22; tk_lr=%22%22; tk_ai=SkrUn7rdhiQdtBDWfjooFd9p; _ga_DJKTT1XZTQ=GS1.2.1709253389.2.1.1709255173.0.0.0; _ga=GA1.2.1205079837.1709239339; _ga_00T8MSY9YE=GS1.1.1709253388.3.1.1709255211.0.0.0',
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
}

product_searched = sys.argv[1]

if len(sys.argv) >= 4:
    brand = sys.argv[2]
    sexe = sys.argv[3]
else:
    brand = None
    sexe = None

if brand:
    params = {
        "s": product_searched,
        "post_type": "product",
        "dgwt_wcas": "1",
        "brand": brand,
    }
    if sexe:
        params = {
            "s": product_searched,
            "post_type": "product",
            "dgwt_wcas": "1",
            "brand": brand,
            "product-category": sexe,
        }

else:
    params = {"s": product_searched, "post_type": "product", "dgwt_wcas": "1"}


url = "https://pmg.dz/page/"


def product_structure():
    return {
        "image": "",
        "title": "",
        "brand": "",
        "price": "",
        "old_price": "",
        "link": "",
    }


def get_pages_number(params, headers):
    html = BeautifulSoup(
        requests.get("https://pmg.dz/page/1", params=params, headers=headers).text,
        "html.parser",
    ).find("ul", class_="pagination")
    if html:
        number_pages = len(html.find_all("li")) - 1
        return number_pages
    else:
        return 1


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
        db = pymysql.connect(
            host=host,
            database=database,
            password=password,
            user=user,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
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
    return "`{}`".format(column_name.replace("`", "``"))


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
    cols = ", ".join(map(format_query_column, names))
    placeholders = ", ".join(["%({})s".format(name) for name in names])
    query = "INSERT INTO {} ({}) VALUES ({})".format(table_name, cols, placeholders)
    return query


def insert_into_database(products_list):
    user = "root"
    host = "localhost"
    password = "root"
    database = "diaa"
    table_name = "pmg_products"

    connection = create_pymysql_connection(
        host=host, password=password, database=database, user=user
    )
    sql = generate_insert_query(product_structure(), table_name=table_name)
    print(sql)
    with connection.cursor() as cursor:
        cursor.execute("SET SESSION wait_timeout=8000;")
        l = cursor.executemany(sql, (products_list))
    connection.commit()
    connection.close()


def fetch_pages(url, params, headers):
    number_pages = get_pages_number(params=params, headers=headers)
    products_list = []  # Initialize an empty list to store products
    for nb_page in range(1, number_pages + 1):  # Iterate over page numbers
        response = requests.get(
            url=(url + str(nb_page)),
            params=params,
            headers=headers,
        )
        html_page = response.text

        products = BeautifulSoup(html_page, "html.parser").find_all(class_="grid_item")
        print(len(products))
        for prd in products:
            prd_img = prd.find("img")["src"]
            prd_title = prd.find("h3").text
            prd_brand = prd.find("a", class_="brand").text
            prd_link = prd.find("a", class_="product-title").get("href")
            if prd.find("del"):
                prd_old_price = prd.find("del").find("bdi").text
                prd_price = prd.find("ins").find("bdi").text
            else:
                prd_price = prd.find("bdi").text
                prd_old_price = None

            product = product_structure()
            product["image"] = prd_img
            product["title"] = prd_title
            product["brand"] = prd_brand
            product["price"] = prd_price
            product["old_price"] = prd_old_price
            product["link"] = prd_link
            products_list.append(product)

    return products_list


products_list = fetch_pages(url=url, params=params, headers=headers)
insert_into_database(products_list)
print(products_list)
