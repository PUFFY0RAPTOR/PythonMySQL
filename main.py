from dml import DML

if __name__ == "__main__":
    conex = DML("localhost", "3306", "root", "", "pruebaDB")

    #resultado = conex.insertar("categoria", idcategoria = 4, nombre = "Anime")
    #print(resultado)
    
    #resultado = conex.insertar("producto", nombre = "Papel", descripcion = "Revistas nueva", precio = 15000,  categoria_idcategoria = 4)
    #print(resultado)
    
    resultado = conex.eliminar("categoria", idcategoria = 4, nombre = "Anime")
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