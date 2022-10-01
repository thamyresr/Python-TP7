import psutil
import time
import json

nomes = []
def imprimir_dados_rede(nomes):
    io_status = psutil.net_io_counters(pernic=True)
    for stats in io_status:
        nomes.append(str(stats))
    for nome in nomes:
        formata_texto = nome, str(io_status[nome])
        print(json.dumps(formata_texto, indent=4, sort_keys=True))
    for contador in range(4):
        time.sleep(1)
        io_status = psutil.net_io_counters(pernic=True)
    for nome in nomes:
        formata_nomes = nome, str(io_status[nome])
        print(json.dumps(formata_nomes, indent=4, sort_keys=True))

imprimir_dados_rede(nomes)