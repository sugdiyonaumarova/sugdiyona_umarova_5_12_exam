# Sug'diyona Umarova N42 

# 1.    Postgresql bazaga python yordamida ulaning. Product nomli jadval yarating  (id,name,price, color,image) . 

# Menda table nomi PRODUCTS. Birinchi shunaqa yozib qo'yganimga o'zgartirmadim.

import psycopg2
from colorama import Fore

conn = psycopg2.connect(host='localhost',
                        database='postgres',
                        user='postgres',
                        password='Iamthebest05$#',
                        port=5432)
cur = conn.cursor()

create_table_query = '''
    create table if not exists products(
        id serial primary key,
        name varchar(100) not null,
        price numeric(10, 2) not null,
        color varchar(100) not null,
        image varchar(255) not null
    );
'''
cur.execute(create_table_query)
conn.commit()

def print_response(message: str):
    print(Fore.BLUE + message + Fore.RESET)

# 2.	Insert_product , select_all_products , update_product,delete_product nomli funksiyalar yarating.

def insert_product():
    name = str(input('Enter product name: '))
    price = input('Enter product price: ')
    color = str(input('Enter the name of the color: '))
    image = str(input('Enter the url of the image: '))
    insert_into_query = "insert into products(name, price, color, image) values (%s, %s, %s, %s);"
    insert_into_params = (name, price, color, image)
    cur.execute(insert_into_query, insert_into_params)
    conn.commit()
    print_response('Product inserted successfully')

def select_all_products():
    select_query = 'select * from products;'
    cur.execute(select_query)
    rows = cur.fetchall()
    for row in rows:
        print_response(str(row))

def update_product():
    select_all_products()
    _id = int(input('Enter product id : '))
    name = str(input('Enter new product name : '))
    price = input('Enter new product price: ')
    color = str(input('Enter new name of the color: '))
    image = str(input('Enter new url of the image: '))
    update_query = 'update books set name = %s, price = %s, color = %s, image = %s where id =%s;'
    update_query_params = (name, price, color, image, _id)
    cur.execute(update_query, update_query_params)
    conn.commit()
    print_response('Updated the product successfully')

def delete_product():
    select_all_products()
    _id = int(input('Enter product id : '))

    delete_query = 'delete from products where id = %s;'
    cur.execute(delete_query, (_id,))
    conn.commit()
    print_response('Deleted the product successfully')

def menu():
    try:
        print('Insert product      => 1')
        print('Select all products => 2')
        print('Delete product      => 3')
        print('Update product      => 4')
        choice = int(input('Enter your choice : '))

    except ValueError as e:

        choice = -1

    return choice

def run():
    while True:
        choice = menu()
        match choice:
            case 1:
                insert_product()
            case 2:
                select_all_products()
            case 3:
                delete_product()
            case 4:
                update_product()
            case _:
                break

if __name__ == '__main__':
    run()

# 3.	Alphabet nomli class yozing .class obyektlarini  iteratsiya qilish imkoni   bo’lsin (iterator).  obyektni for sikli orqali iteratsiya qilinsa 26 ta alifbo xarflari chiqsin

class Alphabet:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration
        else:
            result = self._sequence[self._index]
            self._index += 1
            return result

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sequence1 = Alphabet(alphabet_list)

for item in sequence1:
    print(item)

# 4.	print_numbers va print_leters nomli funksiyalar yarating. print_numbers funksiyasi (1,5) gacha bo’lgan sonlarni , print_letters esa  ‘’ABCDE” belgilarni loop da bitta dan time sleep(1) qo’yib ,parallel 2ta thread yarating.Ekranga parallel ravishda itemlar chiqsin.

import threading

def print_numbers():
    for i in range(1, 5):
        print("Thread 1:", i)

def print_letters():
    for letter in ['A', 'B', 'C', 'C', 'E']:
        print("Thread 2:", letter)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading. Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# 5.	Product nomli class yarating (1 – misoldagi Product ).Product classiga save() nomli object method yarating.Uni vazifasi object attributelari orqali bazaga saqlasin.

# Menda table nomi 'products' bo'lganiga classni ham shu nom ostida yaratdim.

import psycopg2

class products:
    def __init__(self, name, price, color, image):
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self):
        conn = psycopg2.connect(host='localhost',
                                database='postgres',
                                user='postgres',
                                password='Iamthebest05$#',
                                port=5432)
        cur = conn.cursor()
        insert_into_query = "insert into products(name, price, color, image) values (%s, %s, %s, %s);"
        insert_into_params = (self.name, self.price, self.color, self.image)
        cur.execute(insert_into_query, insert_into_params)
        conn.commit()
        conn.close()

product1 = products('phone', 600, 'white', 'phone.jpg')
product1.save()

# 6.	DbConnect nomli ContextManager yarating. Va uning vazifasi python orqali PostGresqlga ulanish (conn, cur)

import psycopg2

db_params = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'Iamthebest05$#',
    'port': 5432
}

class DbConnect:
    def __init__(self, db_params):
        self.db_params = db_params

    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_params)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()

# 7.	Yechgan misollaringni git commandalari orqali githubga add qilinglar.

# https://github.com/sugdiyonaumarova/sugdiyona_umarova_5_12_exam


