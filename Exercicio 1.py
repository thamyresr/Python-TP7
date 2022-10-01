import psutil
import netifaces
import json

def imprimir_dados():
    endereco_ip = psutil.net_if_addrs()['Ethernet'][1][1]
    gateway = netifaces.gateways()
    gateway_formatado = gateway['default'][netifaces.AF_INET][0]
    maskara = psutil.net_if_addrs()['Ethernet'][1][2]
    formatacao = 'Endereço IP: '+ str(endereco_ip),'Gateway: ' + str(gateway_formatado),'Mascara de rede: ' + str(maskara)
    
    print(json.dumps(formatacao, indent=4, sort_keys=True))
    
imprimir_dados()