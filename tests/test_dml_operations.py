import pytest
from data.data_generation import generate_test_data
from db.db_connection_fixture import (db_connection)


@pytest.fixture(scope='module')
def dml_table_setup_teardown(db_connection):
    # Setup code for creating the table
    cursor = db_connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS data_source_dml_tests (id SERIAL PRIMARY KEY, primary_city VARCHAR(255), "
        "secondary_city "
        "VARCHAR(255))"
    )
    db_connection.commit()
    yield db_connection  # Fixture teardown occurs after all tests in the module have completed
    # Teardown code for deleting the table
    cursor.execute("DROP TABLE IF EXISTS data_source_dml_tests")
    db_connection.commit()
    db_connection.close()


def test_insert_data(db_connection, dml_table_setup_teardown):
    # Generate test data
    test_records = generate_test_data()

    # Insert test data into the database
    cursor = db_connection.cursor()
    for record in test_records:
        cursor.execute(
            "INSERT INTO data_source_dml_tests (primary_city, secondary_city) VALUES (%s, %s)",
            (record['primary_city'], record['secondary_city'])
        )
        db_connection.commit()

    # Retrieve the inserted data for assertions
    cursor.execute("SELECT * FROM data_source_dml_tests")
    result = cursor.fetchall()

    # Assertions to validate the inserted data
    assert len(result) == len(test_records)  # Check if all records were inserted

    for i, record in enumerate(test_records):
        assert result[i][1] == record['primary_city']  # Check primary_city value
        assert result[i][2] == record['secondary_city']  # Check secondary_city value

    # Close cursor (cleanup)
    cursor.close()


def test_update_data(db_connection, dml_table_setup_teardown):
    # Update data in the table where primary_city is 'Pune'
    update_value = 'Chandigarh'
    cursor = db_connection.cursor()
    cursor.execute("UPDATE data_source_dml_tests SET secondary_city = %s WHERE primary_city = 'Pune'", (update_value,))
    db_connection.commit()

    # Retrieve the updated data for assertions
    cursor.execute("SELECT secondary_city FROM data_source_dml_tests WHERE primary_city = 'Pune'")
    results = cursor.fetchall()

    # Only Assert if there was even an update since the data is random
    if len(results) > 0:  # Check if any rows were updated
        for result in results:
            assert result[0] == update_value  # Validate each updated row's secondary_city value

    # Close cursor (cleanup)
    cursor.close()
