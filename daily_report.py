#!/usr/bin/python
# -*- coding: utf-8 -*-

# Script para Reportes
# by Favio

import time
import os
import shutil
import subprocess
import string
import smtplib

dia = time.strftime("%d")
mes = time.strftime("%m")
anio = time.strftime("%y")

archivo = "Reporte_Diario_"+dia+"-"+mes+"-"+anio+".txt"

# Copio Password al portapapeles.
from subprocess import Popen, PIPE
p = Popen(['xclip'], stdin=PIPE)
p.communicate(input='69giMUkebu')

# Extraigo cola de correos
output = subprocess.check_output('lynx -dump http://172.17.101.53:8080/status | grep SMTP | cut -d" " -f8', shell=True)

# Copio valor cola de correos sobre archivo.
with open("/home/fbazan/Documentos/Reportes_Diarios/basereport") as f,open(archivo,'w') as o:
    data=f.read()
    data=data.replace("Cantidad total de recipientes al ingreso :","Cantidad total de recipientes al ingreso :\t" + output)
    o.write(data)

# Abro archivo para edición durante el dia.
os.system('mcedit Reporte_Diario_'+dia+'-'+mes+'-'+anio+'.txt') 

#Envio email con reporte.
#os.system( 'cat '+archivo+'| mail -v -s "Reporte Diario ['+dia+'-'+mes+'-'+anio+']" -r favio.bazan@donweb.com -b favio.bazan@donweb.com #entregabilidad@donweb.com,guillermo.rojas@donweb.com ')

#Envio email con reporte
f = open(archivo, 'r')
file_contents = f.read()

HOST = "mail.donweb.com"
SUBJECT = "Reporte Diario ["+dia+"-"+mes+"-"+anio+"]"
EMAILS = ["favio.bazan@donweb.com", "guillermo.rojas@donweb.com", "entregabilidad@donweb.com"]
FROM = "favio.bazan@donweb.com"
BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % ', '.join(EMAILS),
        "Subject: %s" % SUBJECT ,
        "",
        file_contents
        ), "\r\n")
server = smtplib.SMTP(HOST)
server.sendmail(FROM, EMAILS, BODY)
server.quit()

print "Everything Done..."
print "Farewell =)"

