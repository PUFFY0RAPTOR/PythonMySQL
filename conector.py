import mysql.connector

class Conector:
    motor = "mysql"   #mariadb, mysql, postgres
    
    def __init__(self, host="localhost", port="3306", user="SebastianPertuzG", passw="sebas1001821018", db="pruebaDB"):
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
                self.conex = mysql.connector.connect(host = self.host, port = self.port, user = self.user, password = self.passw, database = self.db)
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

if __name__ == "__main__":
    print("Soy la clase Conector")