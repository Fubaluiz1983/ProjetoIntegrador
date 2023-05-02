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

@app.route('/cadastro_adotantes')
def cadastro_adotantes():
    return render_template('cadastro_adotantes.html')

@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)

@app.route('/cadastro_animais')
def cadastro_animais():
    return render_template('cadastro_animais.html')

@app.route('/base')
def base():
    return render_template('base.html')

#colocar o site no ar
if __name__ == "__main__":
   app.run(debug=True)
