from db import conectar_db


def guardar_noticias(lista_noticias):
    
    conn = conectar_db() # abrir conn
    cursor = conn.cursor() # sobre esa conn podedemos ejecutar "sql"

    guardadas = 0 
    for noticia in lista_noticias:
        titulo = noticia.get("title")
        descripcion = noticia.get("description")

        cursor.execute(
            "SELECT * FROM noticias WHERE titulo = %s",
            (titulo,)
        )

        existe = cursor.fetchone()

        if not existe:
            cursor.execute(
                "INSERT INTO noticias (titulo, descripcion) VALUES (%s, %s)",
                (titulo, descripcion)
            )
            guardadas += 1

    conn.commit()
    cursor.close()
    conn.close()

    return guardadas


        





    

