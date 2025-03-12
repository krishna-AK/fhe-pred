# House Price Prediction with FHE - Project Documentation

## Introduction

This document outlines the steps taken to build a house price prediction model using Fully Homomorphic Encryption (FHE). The goal is to train a regression model on unencrypted data and then use it to classify encrypted data under FHE, ensuring that the entire inference occurs under encryption.

## Project Architecture

The project is structured as follows:

1.  **Data Preparation:** Load the training dataset, split it into training and validation sets, and preprocess the data (scaling, normalization, etc.).
2.  **Model Training:** Train a Linear Regression model using conventional machine learning techniques.
3.  **FHE Implementation:** Implement FHE-based inference using OpenFHE-Python. This involves:
    *   Setting up the CKKS cryptocontext with the parameters specified in the `config.json` file.
    *   Encrypting the input data using the provided public key.
    *   Performing the inference on the encrypted data using the trained model.
    *   Ensuring that the entire inference occurs under encryption.
4.  **Output Generation:** Generate the encrypted output vector containing the predicted house price.
5.  **CLI Implementation:** Implement the command-line interface (CLI) as specified in the challenge description.
6.  **Validation:** Validate the solution locally using the `fherma-validator` docker image.

## Steps Taken

1.  **Project Setup:**
    *   Created a directory named `fhe_house_price_prediction` in the root directory.
    *   Created the following files inside the directory:
        *   `data_preparation.py`: For loading, preprocessing, and splitting the dataset.
        *   `model_training.py`: For training the Linear Regression model.
        *   `fhe_inference.py`: For implementing FHE-based inference using OpenFHE-Python.
        *   `cli.py`: For implementing the command-line interface.
        *   `config.json`: For storing the configuration parameters for the CKKS cryptocontext.
        *   `requirements.txt`: For listing the project dependencies.
2.  **Data Preparation and Model Training:**
    *   Attempted to download the training dataset using `wget` and `curl`, but both failed.
    *   The user manually downloaded the `X_train.csv` and `y_train.csv` files and provided the local file paths.
    *   Modified the `data_preparation.py` and `model_training.py` files to use the provided file paths.
    *   Ran the `data_preparation.py` and `model_training.py` scripts.
3.  **FHE Implementation:**
    *   Created the `fhe_inference.py` file with the code for implementing FHE-based inference using OpenFHE-Python.
4.  **CLI Implementation:**
    *   Created the `cli.py` file with the code for implementing the command-line interface.
5.  **Validation:**
    *   Attempted to run the `fherma-validator` docker image, but the `docker` command was not recognized.
    *   The user requested to validate the project without using Docker.
    *   Read the `test_case.json` file and determined how to use it to validate the solution.
    *   Modified the `fhe_inference.py` script to load the model and scaler, preprocess the input data from the `test_case.json` file, perform FHE inference, and decrypt the output.
    *   The user provided the path to the secret key file.
    *   Modified the `fhe_inference.py` script to load the secret key and decrypt the prediction.
6.  **Dependency Management:**
    *   Created a `setup.py` script to create a virtual environment and install the project dependencies.
    *   Attempted to run the `setup.py` script, but the `openfhe-python==0.8.8` package could not be found.
    *   Modified the `requirements.txt` file to remove the version number for the `openfhe-python` package.
    *   Attempted to run the `setup.py` script again, but the `openfhe-python` package could still not be found.
    *   Attempted to upgrade pip and then install the `openfhe-python` package again.
## Current Status

The project is currently in a state where the `openfhe-python` package could not be installed. Here are the possible ways to install it:

1.  **Using pip (for Ubuntu):**
    ```
    pip install openfhe==<openfhe_package_version>
    ```
    Find the release for your version of Ubuntu at [Python Package Index OpenFHE Releases](https://pypi.org/manage/project/openfhe/releases/).

2.  **Running from Docker:**
    See [Instructions for the Docker setup](docker/README.md) in the `openfhe-python` repository.

3.  **Building from Source:**
    *   Install the dependencies:
        *   [OpenFHE 1.1.3+](https://github.com/openfheorg/openfhe-development)
        *   [Python 3.6+](https://www.python.org/)
        *   [pybind11](https://pybind11.readthedocs.io/en/stable/installing.html)
    *   Clone the `openfhe-python` repository.
    *   Run the following commands:
        ```bash
        pip install "pybind11[global]"
        mkdir build
        cd build
        cmake ..  # Alternatively, cmake .. -DCMAKE_PREFIX_PATH=/path/to/installed/openfhe if you installed OpenFHE elsewhere
        make
        make install  # You may have to run sudo make install
        ```

## Running with Docker

1.  Create a `Dockerfile` in the root directory of the project.
2.  Build the Docker image: `docker build -t fhe-pred .`
3.  Run the Docker container: `docker run -it fhe-pred`

## Running Tests

Run tests with [pytest](https://docs.pytest.org), which may be called `pytest-3` on your system. See the [testing readme](tests/README.md) for more information.

```bash
pytest [--run-long]
```

## Project Structure

```
fhe_house_price_prediction/
├── cli.py          # Command-line interface
├── CMakeLists.txt  # CMake configuration file
├── config.json     # Configuration parameters for the CKKS cryptocontext
├── data_preparation.py  # Data loading, preprocessing, and splitting
├── fhe_inference.py # FHE-based inference using OpenFHE-Python
├── main.cpp        # Main C++ file
├── model_training.py  # Linear Regression model training
├── README.md       # Project documentation
├── requirements.txt  # Project dependencies
├── secret_key      # Secret key file
├── setup.py        # Script to create a virtual environment and install dependencies
├── test_case.json  # Test case for validation
├── X_train.csv     # Training data (features)
└── y_train.csv     # Training data (target)
```

The next step is to try installing the `openfhe-python` package using one of the methods described above.