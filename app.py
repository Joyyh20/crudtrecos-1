# Importa as dependências do aplicativo
from flask import Flask, render_template, request

# Cria um aplicativo Flask chamado "app"
app = Flask(__name__)

# Cria um usuário "fake" para testes
# No futuro, isso virá de um cookie
usuario = {
    'nome': 'Joca da Silva',
    'id': '1'
}
# Extrai apenas o primeiro nome do usuário
usuario['pnome'] = usuario['nome'].split()[0]


@app.route("/")  # Rota raiz, equivalente a página inicial do site (index)
def index():  # Função executada ao acessar a rota raiz

    # Dados, variáveis e valores a serem passados para o template HTML
    pagina = {
        'titulo': 'CRUDTrecos',
        'usuario': usuario
    }

    # Renderiza o template HTML, passando valores (pagina) para ele
    return render_template('index.html', **pagina)


# Rota para a página de cadastro de novo treco
@app.route('/novo', methods=['GET', 'POST'])
def novo():  # Função executada para cadastrar novo treco

    # Se o formulário foi enviado
    if request.method == 'POST':

        # Obtém os dados preenchidos na forma de dicionário
        form = dict(request.form)

        # Teste de mesa (comente depois dos testes)
        # Verifica se os dados do formulário chegaram ao back-end
        print('\n\n\n', form, '\n\n\n')

        # Em breve: grava os dados no banco de dados e segue o fluxo

    # Dados, variáveis e valores a serem passados para o template HTML
    pagina = {
        'titulo': 'CRUDTrecos - Novo Treco',
        'usuario': usuario
    }

    # Renderiza o template HTML, passaod valores para ele
    return render_template('novo.html', **pagina)


@app.route('/login', methods=['GET', 'POST'])  # Rota para login de usuário
def login():

    # Dados, variáveis e valores a serem passados para o template HTML
    pagina = {
        'titulo': 'CRUDTrecos - Login',
        'usuario': usuario
    }

    return render_template('login.html', **pagina)


# Executa o servidor HTTP se estiver no modo de desenvolvimento
# Remova / comente essas linhas no modo de produção
if __name__ == '__main__':
    app.run(debug=True)
