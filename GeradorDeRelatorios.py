import pdfkit
from flask import Flask,render_template, make_response,Markup


app = Flask(__name__)


@app.route('/')
def index():
	return redirect(url_for('login'))


@app.route('/pdf')
def pdf():
	Emitido = '10/10/1999'
	Periodo = '10/10/1000 a 10/10/1100'
	Acionamento = 'Na Faixa'
	NomeDoSensor = 'Sensor 1'
	SID = 'SBL000'
	Unidade = Markup('&deg;C')
	LeituraMinima = 10
	LeituraMaxima = 10

	ListaDados = [['10/10/100','12:30:20','80%','50.50'],['10/10/100','12:30:20','80%','50.50'],['10/10/100','12:30:20','80%','50.50']]
	

	rendered = render_template('pdf_template.html',Emitido=Emitido,Periodo=Periodo,Acionamento=Acionamento,NomeDoSensor=NomeDoSensor,SID=SID,LeituraMinima=LeituraMinima,LeituraMaxima=LeituraMaxima,ListaDados=ListaDados,Unidade=Unidade)
	path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
	config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf) # comentar quando colocar no servidor
	pdf = pdfkit.from_string(rendered,False, configuration=config) # remover , configuration=config quando colocar no servidor
	# é necessario instalar wkhtmltopdf com apt-get install no servidor para funcionar 

	response = make_response(pdf)
	response.headers['Content-Type'] = 'application/pdf'
	response.headers['Content-Disposition'] = 'inline'; 'filename=output.pdf' #

	return response

if __name__ == '__main__':
	app.run(debug=True)
