#! /bin/bash

# NHS SISTEMAS ELETRONICOS - http://www.nhs.com.br - 2018

# SCRIPT PARA AUTOMATIZACAO DE DESLIGAMENTO DE SERVIDORES UNIX.
# O UNICO PARAMETRO DE ANALISE DO SCRIPT E O PERCENTUAL DE BATERIA
# ALTERAR AS VARIAVEIS DE ACORDO COM A AUTONOMIA E NECESSIDADES
# DE CADA CARGA.

# ESTE SCRIPT PODE SER UTILIZADO POR SI SO, SEM A NECESSIDADE
# DE AGENDAR O CRONTAB, POIS ESTA EM LOOP.

# INTERVALO DE CADA CHECAGEM DO PERCENTUAL
INTERVALO_SEG=10

# LIMIAR NA QUAL DEVE-SE EXECUTAR UMA ACAO
PERCENTUAL_ACAO=20

# OID DE MAPEAMENTO DE PERCENTUAL DE BATERIA
OID_PERCENTUAL_BATERIA='iso.3.6.1.2.1.33.1.2.4.0'

# PARAMETROS DO NOBREAK
IP_NOBREAK='192.168.41.129'
COMUNIDADE_SNMP='public'


# O QUE DEVE SER FEITO SE O PERCENTUAL DA ACAO FOR ATINGIDO
EXECUTAR_ACAO() {
  echo "EXECUTANDO ACAO"
  #poweroff
}

# O QUE DEVE SER FEITO SE O PERCENTUAL DA ACAO NAO FOR ATINGIDO
IDLE_ACAO() {
  echo "NADA A FAZER"
}

# O QUE DEVE SER FEITO SE A COMUNICACAO FOR PERDIDA
TIMEOUT_ACAO() {
  echo "OCORREU UM TIMEOUT"
  #poweroff
}



#                   NAO ALTERAR ABAIXO
#############################################################################

#set -x

CHECAR_ACAO() {

        # E UM NUMERO?
        if [[ ${PERCENTUAL} =~ ^[-\ ]?[0-9]+$ ]]
        then 
          echo "PERCENTUAL DA BATERIA:  ${PERCENTUAL}"

          if [ ${PERCENTUAL} -lt ${PERCENTUAL_ACAO} ]
          then
            EXECUTAR_ACAO
          else
            IDLE_ACAO
          fi

          return
        fi

        TIMEOUT_ACAO
}

for((;;))
do
        PERCENTUAL=`snmpget -v2c -c ${COMUNIDADE_SNMP} ${IP_NOBREAK} ${OID_PERCENTUAL_BATERIA} | cut -d ':' -f2`

        CHECAR_ACAO

        sleep ${INTERVALO_SEG}
done