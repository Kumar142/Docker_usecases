from flask import Flask
import psycopg2
app = Flask(__name__)
@app.route("/")
def visiting_app():
    dbname = "your_database"
    user = "your_username"
    password = "your_password"
    host = "db"  # Use the container name, not 'localhost'
    #port = "5432"
    # Connect to the database
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)#, port=port)
    #conn = psycopg2.connect(dbname=dbname,host=host)
    cur = conn.cursor()
    # Create a table if it doesn't exist
    cur.execute("CREATE TABLE IF NOT EXISTS example1 (count1 INTEGER);")
    # Get the current visit count
    cur.execute("SELECT count1 FROM example1")
    
    count = cur.fetchone()

    if count:
        count = count[0]
        #return str(count)
    else:
        count = 0
        cur.execute("INSERT INTO example1 (count1) VALUES (%s);", (count,))

    count = int(count)
    #data_to_insert = "Hello, Gaurav!"
    #cur.execute("UPDATE example (count) VALUES (%d);", (count1+1,))
    cur.execute("UPDATE example1 SET count1 = (%s);", (count + 1,))

    #cur.execute("UPDATE example SET count1 = %s", (count1 + 1))
    #cur.execute("UPDATE users SET age = %s WHERE id = %s", (35, 1))
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
    return str(count)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)


