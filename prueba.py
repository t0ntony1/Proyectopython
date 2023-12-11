

from database import *
import pandas as pa
import time

inicio = time.time()




conn=db()

#datos= pa.read_excel('D:\ANTONY\PROYECTO\PRUEBA\prueba.xlsx')
datos= pa.read_excel('prueba.xlsx')

for i in range(0,max(datos['Unnamed: 0'])):
    id=datos['DOC-ID'][i]
    usu=datos['USUARIO'][i]
    cli=datos['NOMBRE'][i]
    dni=id[0:8]
    tel=id[9:]
    dis=datos['DISTRITO'][i]
    dir=datos['DIRECCION'][i]
    cla=datos['CLASIFICACION'][i]
    nro_cla=int(datos['N° CLAS.'][i])
    fecha=datos['FECHA'][i]
    ref=datos['REFERIDO'][i]
    blo=datos['BLOQUEADOS'][i]
    base=datos['BASE'][i]
    comen=datos['COMENTARIOS CARGA'][i]
    obs=datos['OBSERVACIONES DE GESTION'][i]
    conn.insert(id,usu,cli,dni,tel,"dis","dir","cla",nro_cla,fecha,"AE","bl","base","comen",'obs')

#for i in range(0,max(datos['Unnamed: 0'])):
    #conn.insert("id","usu",cli,"dni","tel","dis","dir","cla",1,"2022-12-12","re","bb","base","comen","obs")


#print(max(datos['Unnamed: 0']))
#print("ocla")










































final=time.time()
final=final-inicio
print(final)





#df = pa.read_excel(path)
#df.to_sql(name = table ,con = engine , if_exists = "append", index = False)