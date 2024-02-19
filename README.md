# PDF to Excel Converter (pdf2excel.py)

## Description
The PDF to Excel Converter (pdf2excel.py) is a Python script that simplifies the process of converting PDF files into Excel (.xlsx) format. This tool leverages the `tabula` library for extracting tables from PDFs and the `pandas` library for combining and exporting the data into Excel spreadsheets.

## Features
- **Batch Conversion:** Convert multiple PDF files in the same directory to Excel format with a single execution.
- **Full Page Extraction:** Extracts tables from all pages of the input PDF files.
- **Efficient Data Handling:** Utilizes the `tabula` library to handle multiple tables within a PDF document efficiently.
- **Automatic Output Naming:** Generates output Excel filenames based on the input PDF filenames.
- **User-Friendly:** The script provides clear messages about the conversion process, making it easy for users to understand the outcome.

## How to Use
1. **Requirements:**
   - Ensure that you have Python installed on your system.
   - Install required libraries using: `pip install pandas tabula-py`.

2. **Executing the Script:**
   - Place the `pdf2excel.py` script in the same directory as the PDF files you want to convert.
   - Open a terminal or command prompt in the script's directory.

3. **Run the Script:**
   - Execute the script by running the command: `python pdf2excel.py`.
   - Follow the instructions provided in the terminal.

4. **Output:**
   - The converted Excel files (`.xlsx`) will be generated in the same directory as the PDF files.

## Note
- Ensure that all PDF files are located in the same directory as the `pdf2excel.py` script.
- The script is designed to handle multiple PDF files in the specified directory.

Feel free to contribute, report issues, or suggest improvements to enhance the functionality of this PDF to Excel converter. Happy converting!
