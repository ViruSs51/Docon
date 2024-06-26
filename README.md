# Docon

- All orders: [`exit`](#command-exit), [`help`](#command-help), [`new`](#command-new)

This project allows you to create files containing folders for different individuals - you indicate the information yourself (future updates will include internet search systems).

Docon can be used both through the terminal and through the interface.

## Security

Data security is built from scratch following my concept. Docon encrypts all data in such a way that the password is not saved anywhere, only in the user's mind - making it impossible to bypass security.

The only drawback to this security lies in the fact that the password is quite long, and making it shorter is not possible. Therefore, this product is not suitable for a large user base as it is not very convenient.

## New

- Update code structure

## Installation

Follow these steps to set up the Docon application on your system:

1. **Download Git:**
    - Download and install [Git](https://git-scm.com/downloads).

2. **Open Command Prompt/Terminal:**
    - Open your command prompt or terminal.

3. **Run the following commands:**
    ```bash
    cd Desktop
    git clone https://github.com/ViruSs51/Docon.git
    ```

    Alternatively, you can download the ZIP file directly from the [GitHub repository](https://github.com/ViruSs51/Docon) and extract it.

4. **Install Python:**
    - If you don't have Python installed, download [it](https://www.python.org/).
    - Ensure that Python is installed correctly by running the following command in your command prompt or terminal:
        ```bash
        python --version
        ```

5. **Navigate to the Docon Folder:**
    - Change directory to the Docon folder or open a command prompt/terminal in the installed folder.

    ```bash
    cd Docon
    ```

6. **Install Dependencies and Run the Application:**
    ```bash
    pip install -r requirements.txt
    python main.py
    ```

    Now you are in the Docon application. Read below to explore its functionality.

## Docon Usage

### Commands description:
- <a name="command-exit"></a>`exit` <--- Close Docon
- <a name="command-help"></a>`help` <--- Display all available commands and their usage explanations
- <a name="command-new"></a>`new <object-type> [parameters]` <--- Create a new object in Docon

    **Object Types:**
    - `hash-key [parameters]` <--- Generate a key for the hasher and save it

        **Parameters:**    
        - `key-name` <--- The name for the key that can be used to access it in the future.

Feel free to explore and utilize the functionality of Docon using these commands.
