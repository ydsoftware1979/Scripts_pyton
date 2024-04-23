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


# Função para realizar a consulta SNMP e retornar o valor
def snmp_get(ip_address, community_string, oid):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community_string),
        UdpTransportTarget((ip_address, 161)),
        ContextData(),
        ObjectType(oid)
    )

    error_indication, error_status, error_index, var_binds = next(iterator)

    if error_indication:
        print(error_indication)
    elif error_status:
        print(f'{error_status.prettyPrint()} at {error_index}')
    else:
        for var_bind in var_binds:
            value_str = str(var_bind[1])
            return value_str  # Retorna o valor da OID


while True:
    valor_bateria = int(snmp_get(ip_address, community_string, oid_bateria))
    valor_uptime = snmp_get(ip_address, community_string, oid_uptime)
    valor_carga_bateria = snmp_get(ip_address, community_string, oid_carga_bateria)
    valor_tempo_bateria = int(snmp_get(ip_address, community_string, oid_tempo_bateria))
    valor_modo_bateria = int(snmp_get(ip_address, community_string, oid_modo_bateria))
    data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if valor_uptime == '5':
        #log_msg = f"{data_hora_atual} - Falta Energia na bateria - Carga bateria: {valor_carga_bateria} % - Autonomia bateria: {valor_tempo_bateria} minutos - Tempo bateria: {valor_modo_bateria} Segundos"
        #logging.info(log_msg)
        contador_leituras_bateria_carregando = 0
        contador_leituras_bateria_descarga += 1
        #print(f": {desligamento_executado} ")
        
        # o tempo atuando em modo Bateria é unidade de segundo para 10 min valor = 600
        if valor_modo_bateria > 600 and not desligamento_executado: 
            subprocess.run(["shutdown", "-s", "-t", "30", "-m", "\\\\PC123"])
            print(f"Equipamento desligando...")
            desligamento_executado = True
            #contador_leituras_bateria = 0
            ligar_executado = False

    if contador_leituras_bateria_descarga < 2 and contador_leituras_bateria_carregando <1 :
             log_msg = f"{data_hora_atual} - Falta Energia na bateria - Carga bateria: {valor_carga_bateria} % - Autonomia bateria: {valor_tempo_bateria} minutos - Tempo bateria: {valor_modo_bateria} Segundos"
             logging.info(log_msg)
    
    # A ação será realizado após a apxomimadamente 5 minutos após o retorno da energia equivalente a 20 Ciclos (1 ciclo é aproximadamente 10s )
    elif contador_leituras_bateria_carregando > 20 and not ligar_executado:
          subprocess.run(["wakeonlan", "d0:94:66:ac:9c:00"])
          ligar_executado = True
          log_msg =f"Ligando.....wakeonlan", "d0:94:66:ac:9c:00"
          logging.info(log_msg)
          
    
    if valor_uptime == '3':
        print(f"{data_hora_atual} - Energia OK: {valor_bateria} V - Carga bateria: {valor_carga_bateria} %")
        contador_leituras_bateria_carregando += 1
        contador_leituras_bateria_descarga = 0
        #print(f": {contador_leituras_bateria} ")
        desligamento_executado = False

        if contador_leituras_bateria_carregando < 2:
             log_msg = f"{data_hora_atual} - Energia OK: {valor_bateria} V - Carga bateria: {valor_carga_bateria} %"
             logging.info(log_msg)
    
    #Tempo de espera entre os loops 10 segundos 
    time.sleep(10)  
    print(f"Status desligamento executado    {desligamento_executado}  - Status Religar realizado {ligar_executado} - Contador de Ciclos de Leituras  {contador_leituras_bateria_carregando} - {contador_leituras_bateria_descarga} ")
    
