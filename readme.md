## Usage

Run the script using Python:

python web_page_parser.py


The script will prompt you to choose between two options:

1. Parse a URL
2. Parse HTML files from a folder

### Parsing a URL

If you choose option 1, you'll be asked to enter a URL. The script will fetch the web page, parse its content, and save the extracted text to `output/url_output.txt`.

### Parsing HTML Files from a Folder

If you choose option 2, the script will look for HTML files in the `input` folder, parse each file, and save the combined extracted text to `output/folder_output.txt`.

## File Structure

- `web_page_parser.py`: The main Python script
- `requirements.txt`: List of Python dependencies
- `input/`: Folder to place HTML files for parsing (when using option 2)
- `output/`: Folder where parsed text files are saved