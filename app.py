from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# Declarar estoque como global
estoque = {'lixas': 0, 'luvas': 0}

# Carregar dados de agendamentos e serviços (inicialmente vazios)
def carregar_dados():
    global agendamentos, estoque
    try:
        with open('agendamentos.json', 'r') as f:
            agendamentos = json.load(f)
    except FileNotFoundError:
        agendamentos = []

    try:
        with open('estoque.json', 'r') as f:
            estoque = json.load(f)  # Atualizar a variável global estoque
    except FileNotFoundError:
        pass  # Manter o estoque inicial se o arquivo não existir

carregar_dados()  # Carregar os dados ao iniciar o aplicativo

servicos = {'pe': 25, 'mao': 23, 'pe_e_mao': 40}

# Página inicial
@app.route('/')
def index():
    carregar_dados()  # Recarregar os dados a cada requisição
    return render_template('index.html', agendamentos=agendamentos, estoque=estoque, servicos=servicos)

# Agendar serviço
@app.route('/agendar_servico', methods=['POST'])
def agendar_servico():
    global agendamentos, estoque
    cliente = request.form['cliente']
    contato = request.form['contato']
    servico = request.form['servico']
    data = request.form['data']
    hora = request.form['hora']

    agendamentos.append({'cliente': cliente, 'contato': contato, 'servico': servico, 'data': data, 'hora': hora})

    # Atualizar estoque
    estoque['lixas'] -= 1
    estoque['luvas'] -= 1

    # Salvar dados atualizados
    with open('agendamentos.json', 'w') as f:
        json.dump(agendamentos, f)
    with open('estoque.json', 'w') as f:
        json.dump(estoque, f)

    return redirect(url_for('index'))

# Excluir agendamento
@app.route('/excluir_agendamento', methods=['POST'])
def excluir_agendamento():
    global agendamentos
    try:
        index = int(request.form['index'])
        if 0 <= index < len(agendamentos):
            print(f"Excluindo agendamento de índice: {index}")  # Log para depuração
            del agendamentos[index]
            with open('agendamentos.json', 'w') as f:
                json.dump(agendamentos, f)
            return jsonify({'success': True, 'message': 'Agendamento excluído com sucesso', 'agendamentos': agendamentos})
        else:
            return jsonify({'success': False, 'message': 'Índice de agendamento inválido'})
    except (ValueError, KeyError) as e:
        print(f"Erro ao excluir agendamento: {e}")  # Log para depuração
        return jsonify({'success': False, 'message': 'Erro ao excluir agendamento'})


# Registrar entrada de materiais
@app.route('/registrar_entrada', methods=['POST'])
def registrar_entrada():
    global estoque
    material = request.form['material']
    quantidade = int(request.form['quantidade'])
    estoque[material] += quantidade
    with open('estoque.json', 'w') as f:
        json.dump(estoque, f)
    return jsonify({'success': True, 'message': 'Entrada registrada com sucesso', 'estoque': estoque})

# Calcular ganhos semanais
@app.route('/calcular_ganhos', methods=['GET'])
def calcular_ganhos():
    ganhos_semana = {}
    for agendamento in agendamentos:
        servico = agendamento['servico']
        if servico not in ganhos_semana:
            ganhos_semana[servico] = 0
        ganhos_semana[servico] += servicos[servico]
    return jsonify(ganhos_semana)

if __name__ == '__main__':
    app.run(debug=True)
