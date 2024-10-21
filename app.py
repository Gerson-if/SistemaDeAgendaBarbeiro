from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/agendar', methods=['POST'])
def agendar():
    nome = request.form['nome']
    whatsapp = request.form['whatsapp']
    observacoes = request.form['observacoes']
    servico = request.form['servico']
    horario = request.form['horario']

    # Salvar os dados em um arquivo de texto
    with open('relatorios/relatorio.txt', 'a') as f:
        f.write(f"Nome: {nome}, WhatsApp: {whatsapp}, Serviço: {servico}, Horário: {horario}, Observações: {observacoes}\n")
    
    return redirect(url_for('confirmacao'))

@app.route('/confirmacao')
def confirmacao():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
