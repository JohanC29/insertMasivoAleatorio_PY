from tkinter import TRUE
import psycopg2
class conexionPostgres:

    def conexion(self):
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                user="postgres",
                password = "postgres",
                database="postgres",
                port="5432"
            )
            self.connection.autocommit = TRUE
            return 1
        except Exception as ex:
            print(ex)
            return 0
    
    def insert(self,query):

        connection = self.conexion()        
        if  connection == 0:
            print("Error")
            return 0

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            row = cursor.rowcount
            cursor.close()
        except Exception as ex:
            print(ex)
            return 0

        finally:
            self.connection.close()

        return row
    
    def select(self,query):
        result = []
        connection = self.conexion()        
        if  connection == 0:
            print("Error")
            return result

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
        except Exception as ex:
            print(ex)
            return result

        finally:
            self.connection.close()

        return result

        
        


        
        