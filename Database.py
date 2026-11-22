# To connect idle to PostgreSQL
#
import pg8000.dbapi

conn = pg8000.dbapi.connect(
    user="postgres",
    password="your_password",
    host="localhost",
    port=5432,
    database="your_db"
)
cur = conn.cursor()
cur.execute("SELECT version();")
print(cur.fetchone())
conn.close()


# import psycopg2
#
# conn = psycopg2.connect(
#     database="python",
#     user="postgres",
#     password="1234",
#     host="localhost",
#     port="5432"
# )
#
# print("DB Connected Successfully")

# #####creating an table
cur = conn.cursor()
#
# cur.execute("""
# CREATE TABLE employee(
#     id INT PRIMARY KEY,
#     name VARCHAR(50),
#     salary FLOAT
#     )
# """)
#
# conn.commit()
# print("Table Created Successfully")
#

# To insert one value in the table
# cur.execute(
# "INSERT INTO employee VALUES(%s,%s,%s)",
# (108,'Sabari',60000)
# )
# conn.commit()


#
# # To insert multiple value in the table
# data=[
#     (102,'Sanjay',40000),
#     (103,'Nithya',50000),
#     (104,'Dinesh',60000)]
#
# cur.executemany(
# "INSERT INTO employee VALUES(%s,%s,%s)",
# data
# )
# conn.commit()
# print("Values Added Successfully")




