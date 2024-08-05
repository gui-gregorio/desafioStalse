from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


##########################################################
########################### 02 ###########################
##########################################################
# CRIANDO O DATAFRAME
df = pd.DataFrame({
    'alunos': ['Renato', 'Fernando', 'Rodrigo', 'Ana', 'Joana', 'Silvio', 'Carolina'],
    'notas': [15.00, 39.58, 62.92, 41.46, 48.33, 63.13, 70.00]
})

# RENDERIZE OS VALORES DO DATAFRAME df EM UMA TABELA HTML DENTRO DA PÁGINA /table.html (CRIE UM HTML PARA ISSO)
#HTML Foi criado dentro de templates com o nome table.html, adicionei a parte onde 
@app.route('/table')
def table():
    return render_template('table.html', df=df)

#Por padrão o Flask roda na porta 8000,. aqui vai o código pra mudar para a porta 5000 como solicitado no desafio
if __name__ == '__main__':
    app.run(debug=True, port=5000)