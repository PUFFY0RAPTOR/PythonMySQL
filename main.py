from ntpath import join
import mysql.connector

class Conector:
    motor = "mysql"   #mariadb, mysql, postgres
    
    def __init__(self, host="localhost", port="3306", user="", passw="", db=""):
        """Parámetros a usar (Nota: todos son strings y deben ir dentro de comillas):\n
        host -> es la máquina\n
        port -> puerto que usa el motor de base de datos\n
        user -> usario con privilegios de conexión\n
        passw -> contraseña, use comillas si no tiene ""\n
        deb -> Base de datos a usar
        """
        self.host = host
        self.port = port
        self.user = user
        self.passw = passw
        self.db = db
        self.__estado = False
        self.conex = None
        self.cursor = None

    def conectar(self):
        try:
            if Conector.motor == "mariadb" or Conector.motor == "mysql":
                self.conex = mysql.connector.connect(host = self.host,port = self.port,user = self.user,password = self.passw,database = self.db)
                #, charset='utf8'
            elif Conector.motor == "postgres":
                pass
                #en construcción
            else:
                raise Exception("***Lo siento, este motor no lo tenemos contemplado...")

            self.__estado = True
            self.cursor = self.conex.cursor()
            print("Conectado!!")
        except Exception as e:
            self.__estado = False
            print(f"Error conectando: {e}")

    def estado(self):
        return self.__estado

    def desconectar(self):
        self.conex.close()
        
    def commit(self):
        self.conex.commit()

class Mydb(Conector):

    def consultar(self, tabla, **kwargs):
        """tabla -> string obligatorio: nombre de la tabla como primer argumento.\n
        [] -> Otros argumentos: deben ir en forma de 'clave = valor'
        """
        conex.conectar()
        
        if conex.estado():
            try:
                sql = "SELECT * FROM %s" % (tabla,)

                #revisar posible sql injection en esta construcción
                i = 0
                for key, value in kwargs.items():
                    if i == 0:
                        sql += " WHERE "
                    else:
                        sql += " AND "
                    sql += "{}='{}'".format(key, value)
                    i += 1
                sql += ";"
                #----

                self.cursor.execute(sql)
                registros = self.cursor.fetchall()
                return registros
            except Exception as e:
                print(f"Ocurrió un errror: {e}\n--------SQL: {self.cursor._executed} ----------")
            
            conex.desconectar()
        else:
            print(f"Lo siento se perdió la comunicación con *** {Conector.motor}")
            
    def insertar(self, tabla, **kwargs):
        conex.conectar()
        
        if conex.estado():
            try:
                sql = "INSERT INTO %s " % (tabla,)
                
                campos = ""
                valores = ""
                i = 0
                for key, value in kwargs.items():
                    #print(f"Ciclo {key} - {value}")
                    if i == 0:
                        campos += key
                        valores += "'" + str(value) + "'"
                    else:
                        campos += "," + key
                        valores += ", '" + str(value) + "'"
                    i += 1
                    
                #print(f"campos: {campos}")
                #print(f"valores: {valores}")
                
                sql += "("+ campos + ") VALUES ("+ valores +")"
                
                print(sql)

                self.cursor.execute(sql)
                conex.commit()
                return "OK"
            
            except Exception as e:
                print(f"Ocurrió un errror: {e}\n--------SQL: {self.cursor._executed} ----------")
            
            conex.desconectar()
        else:
            print(f"Lo siento se perdió la comunicación con *** {Conector.motor}")
            

if __name__ == "__main__":
    conex = Mydb("localhost", "3307", "root", "", "pruebaDB")


    resultado = conex.insertar("categoria", idcategoria = 4, nombre = "nueva")
    print(resultado)
    
    resultado = conex.insertar("producto", nombre = "Revista", descripcion = "Revistas nueva", precio = 15000,  categoria_idcategoria = 4)
    print(resultado)
    
    """resultado = conex.consultar("categoria")
    #SELECT * FROM categoria;
    if resultado:
        for r in resultado:
            print(r)
    else:
        print("La consulta no trajo ningún registro")

    resultado = conex.consultar("categoria", idcategoria=1)
    #SELECT * FROM categoria WHERE idcategoria=2;
    if resultado:
        for r in resultado:
            print(r)
    else:
        print("***La consulta no trajo ningún registro")

    resultado = conex.consultar("categoria", idcategoria=2, nombre='Revistas')
    #SELECT * FROM categoria WHERE idcategoria=2 AND nombre='Revistas';
    if resultado:
        for r in resultado:
            print(r)
    else:
        print("La consulta no trajo ningún registro")






    resultado = conex.consultar("producto")
    #SELECT * FROM producto;
    if resultado:
        for r in resultado:
            print(r)
    else:
        print("[]")
    """