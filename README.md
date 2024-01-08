# PostGres operations Tests using Python

This project is a small idea to test the DML and DDL operations for a PostGres DB using Python and PyTest

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running Tests Locally](#running-tests-locally)
- [Running Tests in Pipeline](#running-tests-in-pipeline)

## About

This project is a small idea to test the DML and DDL operations for a PostGres DB using Python and PyTest.
I have used PostGres DB container in a dockerized environment. It is a basic container with dummy username
and password and other connection settings. It spins up a container and runs the tests for DML and DDL
operations categorized under test_dml_operations and test_ddl_operations modules respectively.

This project also includes a Jenkinsfile which can be used to run tests on
a Jenkins pipeline. I have kept it simple for the assignment scope.

## Installation

The tests require Python and PyTest to run.
A requirements.txt file is provided to have all the required packages to be installed for the tests to run.
The execution also requires an underlying Docker environment, for example, Docker Desktop for Windows to
get the Postgres container running for test execution.

### Prerequisites

- Python [3.9.2]
- Please install dependencies from the requirements.txt provided along with the code

### Setup

1. Create and activate a virtual environment (recommended):

   ```bash
   # Using virtualenv
   python3 -m venv venv
   venv\Scripts\activate
   ```

2. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running Tests Locally

1. Navigate to the project directory and

    ```bash
    pytest
    ```

### Running Tests in Pipeline

Please use the Jenkinsfile provided under the project root
