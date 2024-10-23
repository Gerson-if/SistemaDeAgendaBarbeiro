from flask import Flask, render_template, request

# Inicializa a aplicação Flask
app = Flask(__name__)

@app.route('/')
def index():
    """
    Rota principal da aplicação.
    Retorna a página inicial.
    """
    return render_template('index.html')

@app.route('/agendar')
def agendar():
    """
    Rota para a página de agendamentos.
    Retorna a página onde o usuário pode agendar um corte.
    """
    return render_template('agendar.html')

@app.route('/cortes')
def cortes():
    """
    Rota para a página de cortes.
    Retorna a página que exibe os diferentes tipos de cortes disponíveis.
    """
    return render_template('cortes.html')

@app.route('/horarios')
def horarios():
    """
    Rota para a página de horários disponíveis.
    Retorna a lista de horários disponíveis para agendamento.
    """
    # Exemplo de horários disponíveis. Isso pode ser substituído por uma consulta a um banco de dados.
    horarios_disponiveis = ['10:00', '11:00', '14:00', '15:00']
    return render_template('horarios.html', horarios=horarios_disponiveis)

@app.route('/confirmacao', methods=['GET', 'POST'])
def confirmacao():
    """
    Rota para a página de confirmação de agendamentos.
    Se o método da requisição for POST, processa os dados do formulário.
    Retorna uma mensagem de confirmação.
    """
    if request.method == 'POST':
        # Aqui você pode processar os dados do formulário e, se necessário, armazená-los em um banco de dados.
        # Por exemplo:
        # nome_cliente = request.form.get('nome')
        # horario_selecionado = request.form.get('horario')
        return render_template('confirmacao.html', mensagem="Agendamento confirmado!")
    
    # Se não for uma requisição POST, apenas renderiza a página de confirmação.
    return render_template('confirmacao.html')

if __name__ == '__main__':
    # Inicia o servidor em modo debug para facilitar o desenvolvimento.
    app.run(debug=True)
