

from database import *
import pandas as pa
import time

inicio = time.time()




conn=db()

#datos= pa.read_excel('D:\ANTONY\PROYECTO\PRUEBA\prueba.xlsx')
datos= pa.read_excel('prueba.xlsx')


datos.dropna()
datos.fillna('', inplace=True)

for i in range(0,max(datos['Unnamed: 0'])):
    id=datos['DOC-ID'][i]+datos['FECHA'][i]
    usu=datos['USUARIO'][i]
    cli=datos['NOMBRE'][i]
    dni=id[0:8]
    tel=id[9:17]
    dis=datos['DISTRITO'][i]
    dir=datos['DIRECCION'][i]
    cla=(str(datos['CLASIFICACION'][i])).strip()
    nro_cla=int(datos['N° CLAS.'][i])
    fecha=datos['FECHA'][i]
    ref=datos['REFERIDO'][i]
    blo=datos['BLOQUEADOS'][i]
    base=datos['BASE'][i]
    comen=datos['COMENTARIOS CARGA'][i]
    obs=datos['OBSERVACIONES DE GESTION'][i]
    print(i)
    #print(id,usu,cli,dni,tel,dis,dir,cla,nro_cla,fecha,ref,blo,base,comen,obs)
    conn.insert(id,usu,cli,dni,tel,dis,dir,cla,nro_cla,fecha,ref,blo,base,comen,obs)

#for i in range(0,max(datos['Unnamed: 0'])):
    #conn.insert("id","usu",cli,"dni","tel","dis","dir","cla",1,"2022-12-12","re","bb","base","comen","obs")


#print(max(datos['Unnamed: 0']))
#print("ocla")










































final=time.time()
final=final-inicio
print(final)





#df = pa.read_excel(path)
#df.to_sql(name = table ,con = engine , if_exists = "append", index = False)