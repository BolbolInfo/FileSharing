# File Sharing Web App

This is a simple Python-based web application built with Flask that allows users to share files over a local network or the internet.

## Features

- Upload files to the server
- Generate unique download links for shared files
- Download files using the generated links

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/BolbolInfo/FileSharing
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Access the application in your web browser:

    ```
    http://localhost:5000/
    ```

3. Upload files using the provided form and get download links for shared files.

## Configuration

- The maximum file size allowed for upload can be modified in `app.py` using `app.config['MAX_CONTENT_LENGTH']`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [GNU General Public License v3.0 (GPL-3.0)](LICENSE).



