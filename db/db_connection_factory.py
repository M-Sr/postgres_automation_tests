import psycopg2


class DatabaseConnectionFactory:
    @staticmethod
    def create_connection(db_name, db_user, db_password, db_host='localhost', db_port='5432'):
        """Method to create a Connection to the PostGres DB"""
        return psycopg2.connect(
            dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port
        )
