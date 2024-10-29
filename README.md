# Hongyi-Duan-Cloud-Hosted

[![CI/CD run](https://github.com/nogibjj/Hongyi-Duan-Mini-Project-1/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/Hongyi-Duan-Mini-Project-1/actions/workflows/hello.yml)

This project provides an example of a cloud-hosted Python application that processes and manipulates a dataset using basic data analysis operations. The project includes code that uses `pandas` and `numpy` for data manipulation and `unittest` for automated testing. Additionally, `pylint` and `pytest` are integrated to ensure code quality and test coverage.

## Google Colab Link

https://colab.research.google.com/drive/1388JxGtoxX9tFRxo1uaSQmVpp4B4vVMn#scrollTo=4KjGEdgGtwEN

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Linting](#linting)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Overview

The project showcases how to manipulate a dataset, specifically creating, modifying, and extending a `pandas` DataFrame containing fictional hero data. It also includes a testing suite with `unittest` to verify the functionality of the main code. The setup emphasizes the importance of test-driven development and code quality checks with `pylint`.

## Project Structure

The project structure is as follows:

```
Hongyi-Duan-Cloud-Hosted/
│
├── main.py                  # Main script containing data manipulation functions
├── test_main.py             # Unit tests for main.py
├── Cloud_Hosted.ipynb       # Jupyter notebook for interactive development
├── Makefile                 # Makefile for running linting and testing commands
├── README.md                # Project documentation (this file)
├── requirements.txt         # Python dependencies for the project
└── .github/
    └── workflows/
        └── ci.yml           # GitHub Actions CI pipeline configuration
```

### File Descriptions

- **`main.py`**: This script contains two main functions:
  - `create_heroes_dataframe()`: Initializes a DataFrame with hero data (skills, scores, etc.).
  - `modify_heroes_dataframe()`: Adds new columns and rows to the DataFrame and modifies specific values.

- **`test_main.py`**: Contains unit tests for the functions in `main.py`. It uses the `unittest` module to ensure that:
  - The DataFrame is correctly initialized.
  - The modifications to the DataFrame are applied properly.

- **`Cloud_Hosted.ipynb`**: A Jupyter notebook used for development and experimentation, showing the steps for creating and manipulating a dataset interactively.

- **`Makefile`**: Automates common tasks:
  - `make lint`: Runs `pylint` to check for coding style violations.
  - `make test`: Runs `pytest` to execute tests and calculate code coverage.

- **`.github/workflows/ci.yml`**: Defines the Continuous Integration (CI) pipeline using GitHub Actions. It ensures that linting and tests are automatically run on each commit or pull request.

- **`requirements.txt`**: Lists the dependencies required for the project:
  - `pandas`
  - `numpy`
  - `pytest`
  - `pylint`

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nogibjj/Hongyi-Duan-Cloud-Hosted.git
   cd Hongyi-Duan-Cloud-Hosted
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Running the main script**:
   To run the data manipulation script and see the output:
   ```bash
   python main.py
   ```

   This will print the DataFrame after performing the necessary modifications.

2. **Jupyter Notebook**:
   For an interactive version of the code, you can open the Jupyter notebook:
   ```bash
   jupyter notebook Cloud_Hosted.ipynb
   ```

## Linting

To ensure the code adheres to Python style guidelines (PEP8), run `pylint` using the provided Makefile:

```bash
make lint
```

This will check the code for style issues, unused variables, and other common problems. You can customize the linting rules in the Makefile.

## Testing

The project includes unit tests in `test_main.py`. You can run the tests using `pytest` to verify the correctness of the code:

```bash
make test
```

This command will execute the tests and provide a coverage report, ensuring that the main functions behave as expected.
