from flask import Flask, render_template

app = Flask(__name__)

#criar a primeira página do site
#route é o endereço da homepage do site por exemplo meusite.com/ é o end da homepage
#app é o nome do site
#def = função que é o que vc quer exibir na página
#template são os htmls criados e que devem ser guardados na pasta templates
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)

#colocar o site no ar
if __name__ == "__main__":
   app.run(debug=True)