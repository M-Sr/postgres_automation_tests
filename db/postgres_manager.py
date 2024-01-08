import docker
import time


def start_postgres_container():
    """Starts the PostGre container to be used for Test Case execution
    This can be made better using the config from a separate file
    bsed on different configs for different Environments: DEV, QA etc."""
    client = docker.from_env()
    try:
        container = client.containers.run(
            "postgres",
            detach=True,
            ports={"5432/tcp": 5432},
            environment={
                "POSTGRES_DB": "test_db",
                "POSTGRES_USER": "test_user",
                "POSTGRES_PASSWORD": "test_password",
            },
        )
        # Waiting for a few seconds to ensure PostgreSQL container is up and running
        time.sleep(5)
        return container
    except docker.errors.APIError as e:
        print(f"Error starting Postgres container: {e}")
        return None
