from conector import Conector

class DML(Conector):

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
    print("Soy la clase DML")