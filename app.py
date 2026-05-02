from flask import Flask, request, render_template 
import sqlite3 
 
app = Flask(__name__) 
 
@app.route("/") 
def home(): 
    return render_template("index.html") 
 
@app.route("/add") 
def add(): 
    task = request.args.get("task") 
    if not task or task.strip()=="" : 
        return "Enter a valid task ^<a href='/'^>Back^</a^>"  
    conn = sqlite3.connect("database.db") 
    cur = conn.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, name TEXT)") 
    cur.execute("INSERT INTO tasks (name) VALUES (?)", (task,)) 
    conn.commit() 
    conn.close() 
    return "Task Added ^<a href='/'^>Back^</a^>"  
 
@app.route("/tasks") 
def tasks(): 
    conn = sqlite3.connect("database.db") 
    cur = conn.cursor() 
    cur.execute("SELECT * FROM tasks") 
    data = cur.fetchall() 
    conn.close() 
    return render_template("tasks.html", data=data) 
 
if __name__ == "__main__": 
    app.run(debug=True)
