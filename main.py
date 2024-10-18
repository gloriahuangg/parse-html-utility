from bs4 import BeautifulSoup
import re
import os
import requests

def parse_url(url, output_file, encoding='utf-8'):
    try:
        # Fetch the web page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        html_content = response.text

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the text content
        text_content = soup.get_text()

        # Clean up the text content
        text_content = re.sub(r'\n\s*\n+', '\n\n', text_content)  # Remove multiple empty lines
        text_content = re.sub(r' +', ' ', text_content)  # Replace multiple spaces with a single space

        # Write the content to the output file
        with open(output_file, 'w', encoding=encoding) as file:
            file.write(text_content)

        print(f"Content from {url} has been saved to {output_file}")

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def parse_html_folder(input_folder, output_file, encoding='utf-8'):
    # This function remains unchanged
    with open(output_file, 'a', encoding=encoding) as file:
        for filename in os.listdir(input_folder):
            if filename.endswith(".html"):
                html_file = os.path.join(input_folder, filename)
                with open(html_file, 'r', encoding=encoding) as html:
                    html_content = html.read()

                soup = BeautifulSoup(html_content, 'html.parser')
                text_content = soup.get_text()

                text_content = re.sub(r'\n\s*\n+', '\n\n', text_content)
                text_content = re.sub(r' +', ' ', text_content)

                file.write(text_content)
                file.write('\n\n')  

def main():
    choice = input("Enter '1' to parse a URL or '2' to parse HTML files from a folder: ")
    
    if choice == '1':
        url = input("Enter the URL to parse: ")
        output_file = 'output/url_output.txt'
        parse_url(url, output_file)
    elif choice == '2':
        input_folder = "input"
        output_file = 'output/folder_output.txt'
        parse_html_folder(input_folder, output_file)
    else:
        print("Invalid choice. Please run the script again and enter '1' or '2'.")

if __name__ == "__main__":
    main()