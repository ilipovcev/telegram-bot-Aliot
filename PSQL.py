import psycopg2

class DataBase:
	def __init__(self):
		self.name_db = 'AliotDB'
		self.user_db = 'postgres'
		self.pass_db = '5FB6Az3X'
		self.host_db = '127.0.0.1'
		self.port_db = '5432'

	def find_user(self, id, name, balance):
		conn = psycopg2.connect(database=self.name_db,user=self.user_db,password=self.pass_db,host=self.host_db,port=self.port_db)
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM public.""user"" WHERE id = %s", [int(id)])
		user = cursor.fetchall()
		if len(user) != 0:
			return True
		else:
			cursor.execute("INSERT INTO public.user(id, name, balance) VALUES (%s, %s, %s)", [int(id), str(name), int(balance)])
			conn.commit()
			conn.close()
			return False

	def get_user_balance(self, id):
		conn = psycopg2.connect(database=self.name_db,user=self.user_db,password=self.pass_db,host=self.host_db,port=self.port_db)
		cursor = conn.cursor()
		cursor.execute("SELECT get_balance(%s)", [int(id)])
		balance = cursor.fetchall()
		conn.commit()
		conn.close()
		return balance[0][0]

	def get_stock_id(self, name):
		conn = psycopg2.connect(database=self.name_db,user=self.user_db,password=self.pass_db,host=self.host_db,port=self.port_db)
		cursor = conn.cursor()
		cursor.execute("SELECT id FROM public.stock WHERE name = %s", [str(name)])
		id_stock = cursor.fetchall()
		conn.commit()
		conn.close()
		return int(id_stock[0][0])

	def update_balance(self, id, new_balance):
		conn = psycopg2.connect(database=self.name_db,user=self.user_db,password=self.pass_db,host=self.host_db,port=self.port_db)
		cursor = conn.cursor()
		cursor.execute("UPDATE public.user SET balance = %s WHERE id = %s", [int(new_balance), int(id)])
		conn.commit()
		conn.close()

	def add_stocks(self, id_user, id_stock, amount, price):
		conn = psycopg2.connect(database=self.name_db,user=self.user_db,password=self.pass_db,host=self.host_db,port=self.port_db)
		cursor = conn.cursor()
		cursor.execute("SELECT add_stocks(%s, %s, %s, %s)", [int(id_user), int(id_stock), int(amount), int(price)])
		conn.commit()
		conn.close()

	def sold_stock(self, id_user, id_stock, amount):
		conn = psycopg2.connect(database=self.name_db,user=self.user_db,password=self.pass_db,host=self.host_db,port=self.port_db)
		cursor = conn.cursor()
		cursor.execute("SELECT sold_stock(%s, %s, %s)", [int(id_user), int(id_stock), int(amount)])
		old_price = cursor.fetchall()
		conn.commit()
		conn.close()
		return int(old_price[0][0])

db = DataBase()
print(db.sold_stock(5, 0, 6))