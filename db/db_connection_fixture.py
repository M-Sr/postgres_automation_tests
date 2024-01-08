import pytest
from db.db_connection_factory import DatabaseConnectionFactory
from db.postgres_manager import start_postgres_container


@pytest.fixture(scope="module")
def db_connection():
    """Fixture to yield a connection"""
    postgres_container = start_postgres_container()
    try:
        # Getting the container hostname or IP
        postgres_host = postgres_container.attrs['NetworkSettings']['IPAddress']

        # Creating a database connection using the factory
        db_connection = DatabaseConnectionFactory.create_connection(
            db_name="test_db", db_user="test_user", db_password="test_password", db_host=postgres_host
        )
        yield db_connection
    finally:
        # Cleanup: Closing the connection and removing the container
        db_connection.close()
        postgres_container.stop()
        postgres_container.remove()
