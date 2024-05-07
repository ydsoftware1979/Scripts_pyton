from pysnmp.hlapi import *
import time
from datetime import datetime
import subprocess
import logging

# Carrega e configura as Variaveis

ip_address = '172.16.31.121'
community_string = 'public'
oid_bateria = ObjectIdentity('iso.3.6.1.2.1.33.1.3.3.1.3.1')
oid_uptime = ObjectIdentity('iso.3.6.1.2.1.33.1.4.1.0')
oid_carga_bateria = ObjectIdentity('iso.3.6.1.2.1.33.1.2.4.0')
oid_tempo_bateria = ObjectIdentity('iso.3.6.1.2.1.33.1.2.3.0')
oid_modo_bateria = ObjectIdentity('iso.3.6.1.2.1.33.1.2.2.0')
desligamento_executado = False
contador_leituras_bateria_carregando = 0
contador_leituras_bateria_descarga = 0
ligar_executado = False

# Configuração do log
log_file = 'nobreak.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')


subprocess.run(["wakeonlan", "d0:94:66:ac:9c:00"])
subprocess.run(["wakeonlan", "48:4d:7e:fe:12:e8"])
ligar_executado = True
log_msg =f"Ligando.....wakeonlan", "d0:94:66:ac:9c:00"
logging.info(log_msg)

time.sleep(45)  

subprocess.run(["wakeonlan", "d0:94:66:ac:9c:00"])
subprocess.run(["wakeonlan", "48:4d:7e:fe:12:e8"])
ligar_executado = True
log_msg =f"Ligando.....wakeonlan", "d0:94:66:ac:9c:00"
logging.info(log_msg)
