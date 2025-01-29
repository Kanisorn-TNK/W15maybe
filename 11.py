import fastapi
import mysql.connector
app = fastapi.FastAPI()
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "yumyum"
)
mycursor = mydb.cursor()

@app.get('/select/{table}')
async def selcetdb (table):
    sql = f"SELECT * FROM {table}"
    mycursor.execute(sql)
    show = mycursor.fetchall()
    return show

@app.get('/addcategories/{category_name}')
async def add_categories(category_name):
    sql = "INSERT INTO categories VALUES (%s,%s)"
    val_sql = (None,category_name)
    mycursor.execute(sql,val_sql)
    mydb.commit()
    if mycursor.rowcount >0 :
        return True
    else:
        return False

@app.get('/addproduct/{product_name}/{description}/{price}/{stock}')
async def add_product(product_name,description,price,stock):
    sql = "INSERT INTO products VALUES (%s, %s, %s, %s,%s)"
    val_sql = (None,product_name, description, price, stock)
    mycursor.execute(sql, val_sql)
    mydb.commit()
    if mycursor.rowcount >0 :
        return True
    else:
        return False

@app.get('/addorder/{order_date}/{total_amount}/{status}') #ใส่ / ในวันที่ไม่ได้ ใช้ - แทน ex.24-09-2567
async def add_order(order_date,total_amount,status):
    sql = "INSERT INTO orders VALUES (%s,%s,%s,%s)"
    val_sql = (None,order_date,total_amount,status)
    mycursor.execute(sql,val_sql)
    mydb.commit()   
    if mycursor.rowcount >0 :
        return True    
    else:
        return False

@app.get('/adduser/{username}/{password}/{email}/{user_role}')
def add_user(username,password,email,user_role):
    sql = "INSERT INTO users VALUES (%s,%s,%s,%s,%s)"
    val_sql = (None,username,password,email,user_role)
    mycursor.execute(sql,val_sql)
    mydb.commit()
    if mycursor.rowcount >0 :
        return True
    else:
        return False

@app.get('/delete/{table}/{colum}/{id}')
async def delete(table,colum,id):
    sql = f"DELETE FROM {table} WHERE {colum} = %s"
    val_sql = (id,)
    mycursor.execute(sql,val_sql)
    mydb.commit()
    if mycursor.rowcount >0:
        return True
    else:
        return False

@app.get('/edit/{table}/{columname}/{val}/{columid}/{id}')
def edit(table,columname,val,columid,id):
    sql = f"UPDATE {table} SET {columname} = %s WHERE {columid} = %s"
    val_sql = (val,id)
    mycursor.execute(sql,val_sql)
    mydb.commit()
    if mycursor.rowcount >0:
        return True
    else:
        return False