import psutil
import json

pid_processo = int(input('Digite o PID do processo:'))

def gerar_processos(pid):
    process = psutil.Process(pid)
    conexao = process.connections()
    print(json.dumps(conexao, indent=2, sort_keys=True))
    
gerar_processos(pid_processo)