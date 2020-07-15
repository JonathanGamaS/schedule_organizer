from flask import Flask
from orchestrator_programming import execute_orchestrator_programming

app = Flask(__name__)


@app.route('/programacao/RPC')
def hello():
    response = execute_orchestrator_programming()
    return response

if __name__ == '__main__':
    app.run()