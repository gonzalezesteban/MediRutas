from Flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def ingresar_codigos():
	return render_template("inicio.html")

	#Siempre escribir flask run

@app.route("/crearcuenta") #Aca se importa lo creado en la carpeta templates 
def crearcuenta():
	return render_template("crearcuenta.html")

@app.route("/ingresarcodigos.html")
def ingresar_codigos():
	return render_template("ingresarcodigos.html")

@app.route("/menuadmin")
def menuadmin():
	return render_template("menuadmin.html")

@app.route("/menuconductor")
def menuconductor():
	return render_template("menuconductor.html")

@app.route("/menuadminlider")
def menuadminlider():
	return render_template("menuadminlider.html")

@app.route("/inicioadmin")
def inicioadmin():
	return render_template("inicioadmin.html")

@app.route("/inicioconductor")
def inicioconductor():
	return render_template("inicioconductor.html")

@app.route("/inicioadmminlider")
def inicioadmminlider():
    return render_template("inicioadminlider.html")

@app.route("/documentacionderutas")
def documentacionderutas():
	return render_template("documentacionderutas.html")

@app.route("/reportarproblemas")
def reportarproblemas():
	return render_template("reportarproblemas.html")

@app.route("/vercuentahistorica")
def vercuentahistorica():
	return render_template("vercuentashistorica.html")

@app.route("/verlistadeusuarios")
def verlistadeusuarios():
	return render_template("verlistadeusuarios.html")

@app.route("/vercuentasactuales")
def vercuentasactuales():
	return render_template("vercuentasactuales.html")

@app.route("/crearcuentadecobro")
def crearcuentadecobro():
	return render_template("crearcuentadecobro.html")

@app.route("/crearrutas")
def crearrutas():
	return render_template("crearrutas.html")

@app.route("/verrutasconductor")
def verrutasconductor():
	return render_template("verrutasconductor.html")

@app.route("/verrutasadmin")
def verrutasadmin():
	return render_template("verrutasadmin.html")




if __name__=="__main__": # Para ejecutar la app sin escribir flask run
	app.run() 
