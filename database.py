import pyodbc
class db():
    
    """def conn():
        server='DESKTOP-VD2A6PD'
        usu='antony'
        passw='antony'
        db = 'CONTACT_CENTER'
        conn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};SERVER='+server+';DATABASE='+db+';UID='+usu+';PWD='+passw)
        print('conección exitosa')"""
    
    def __init__(self):
        self.conec = pyodbc.connect("""DRIVER={ODBC Driver 17 for SQL server}; 
                            SERVER=localhost;
                            DATABASE=CONTACT_CENTER; 
                            UID=antony; 
                            PWD=antony""")
        print("se conecto")
        self.cursor = self.conec.cursor()
        self.conec.commit()

    def insert(self,id,usu,cli,dni,tel,dis,dir,cla,nro_cla,fecha,ref,blo,base,comen,obs):
        self.cursor.execute("""insert into prueba
                            (ID,USUARIO,CLIENTE,DNI,TELEFONO,DISTRITO,DIRECCION,CLASIFICACION,NRO_CLASIFICACION,FECHA,REFERIDO,BLOQUEADO,BASE_ADMI,COMENTARIOS_ADMI,OBSERVACIONES_USU) 
                            values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                            (id,usu,cli,dni,tel,"dis","dir",cla,nro_cla,fecha,ref,blo,base,comen,"obs"))
        self.conec.commit()  
        

        