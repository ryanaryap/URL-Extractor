# URL Extractor

URL Extractor is a simple Python code designed to extract the domain name from a list of URLs stored in a text file. This application provides a convenient way to extract and process URLs efficiently.

## How to Use

⚠️ Make sure you have a suitable Python installation on your system.

1. Prepare a text file containing a list of URLs, with one URL per line, e.g., **urls.txt**.
2. Run the URL Extractor script using Python: **`python url_extractor.py`**.
3. The program will prompt you to enter the name of the text file containing the URLs, e.g., **urls.txt**.
4. After entering the file name, the program will read the list of URLs from the file.
5. The domain name will be extracted from each valid URL, and the protocol (http:// or https://) will be added to the domain name.
6. The resulting URLs with the added protocol will be displayed on the screen and **saved in the result.txt file**.
7. Finished! You can find the output in the **result.txt** file in the same directory as the executed Python script.

## Notes

- **Make sure the text file contains one URL per line** for accurate results.
- Invalid URLs will be displayed with an error message.
- The output URLs with the added protocol will also be saved in the **result.txt** file for future reference and use.
- URL Extractor helps you quickly and easily extract domain names from a text file, speeding up the URL extraction process in various scenarios such as data analysis, text processing, or information gathering from existing URL lists.
- Ensure that the usage of this application complies with the laws and regulations applicable in your region. The developer is not responsible for any illegal or unauthorized use.
