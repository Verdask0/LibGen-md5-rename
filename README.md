# File Renamer and Cleaner

This Python script automatically renames files based on metadata fetched from specific URLs and cleans up files by language criteria.

## Overview

The script processes files within a specified directory, fetching metadata from a pre-defined URL structured around each file's MD5 hash. It renames files without extensions based on a combined result of the title and additional metadata. Furthermore, it checks the language of each file, retaining only those in Arabic, English, or German, and deleting all others.

## Features

- **Renaming**: Renames files without extensions using a title and extension (Keeps only the first 6 Words from the Title).
- **Language Filtering**: Deletes files if their content language is not Arabic, English, or German.


## Usage

1. **Installation**: Ensure Python is installed on your system along with the `requests` and `lxml` libraries. These can be installed via pip:
   ```bash
   pip install requests lxml
   ```

2. **Configuration**: Modify the `directory` and the `languages` variables in the script to the path of the files you want to process, and the languages you want to keep.

3. **Execution**: Run the script from your command line:
   ```bash
   python3 script.py
   ```

## Requirements

- Python 3.x
- requests
- lxml

## Contributions

Feel free to fork this repository and propose changes via pull requests.

## Acknowledgements

This code was developed with the assistance of ChatGPT, an AI by OpenAI, which helped in writing and debugging the Python script.
