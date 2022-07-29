from flask import Flask, render_template
from threading import Thread
app = Flask('')
@app.route('/')

def main():
      
    	return """<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inconsolata:wght@300&display=swap" rel="stylesheet">
  <title>Раб</title>
</head>

<body style="
  margin:0;
  padding:0;
  background-color:#9370DB;
  cursor:default;
">
<div style="
  width:100%;
  height:100%;
  margin-top:15%;
  text-align:center;
  display:flex;
  justify-content:center;
">
<h2 style="
color:white; 
font-family: 'Roboto', sans-serif;
margin-bottom:5px;
">
Раб работает
</h2>
</div>

<footer style="
  text-align:center;
  width:100%;
  height:100%;
  font-family: 'Inconsolata', monospace;
  font-size:20px;
  color:white;
">
©ankeer
</footer>

</body>
</html>"""
def run():
  app.run(host="0.0.0.0", port=8080)
def keep_alive():
    server = Thread(target=run)
    server.start()