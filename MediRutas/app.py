from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def ingresar_codigos():
	return "" \
	"<html>" \
        "<body>" \
		"<h1>Menu Inicial</h1> <!-- Esto es un comentario: H1 significa titulo principal-->" \
	"</body>" \
	"</html>"

	#Siempre escribir flask run

@app.route("/menu") #Aca se importa lo creado en la carpeta templates 
def menu():
	return render_template("menu.html")
if __name__=="__main__": # Para ejecutar la app sin escribir flask run
	app.run() 
