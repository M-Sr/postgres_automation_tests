from db.db_connection_fixture import db_connection


def test_create_table(db_connection):
    # Create a new table
    cursor = db_connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS data_source_ddl_tests (id SERIAL PRIMARY KEY, primary_city VARCHAR(255), "
        "secondary_city "
        "VARCHAR(255))"
    )
    db_connection.commit()

    # Check if the table was created
    cursor.execute("SELECT * FROM information_schema.tables WHERE table_name='data_source_ddl_tests'")
    result = cursor.fetchone()

    # Assertion to validate table creation
    assert result is not None

    # Check if the columns are created
    cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'data_source_ddl_tests'")
    columns = cursor.fetchall()
    column_names = [col[0] for col in columns]

    assert 'primary_city' in column_names
    assert 'secondary_city' in column_names

    # Close cursor (cleanup)
    cursor.close()


def test_drop_table(db_connection):
    # Drop the table created in the test
    cursor = db_connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS data_source_ddl_tests")
    db_connection.commit()

    # Check if the table was dropped
    cursor.execute("SELECT * FROM information_schema.tables WHERE table_name='data_source_ddl_tests'")
    result = cursor.fetchone()

    # Assertion to validate table drop
    assert result is None

    # Close cursor (cleanup)
    cursor.close()
