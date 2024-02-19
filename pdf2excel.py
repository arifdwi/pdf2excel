import os
import glob
import pandas as pd
import tabula

__version__ = "1.0.0"
__author__ = "Arif"

def pdf2excel(input_pdf, output_excel):
    current_path = os.path.dirname(os.path.abspath(__file__))
    tables  = tabula.read_pdf(os.path.join(current_path, input_pdf), pages="all", multiple_tables=True)
    combined_table = pd.concat(tables, ignore_index=True)
    combined_table.to_excel(os.path.join(current_path, output_excel), index=False)

def main():
    pdf_input = glob.glob("*.pdf")

    if not pdf2excel:
        print("No PDF found in files")
    else:
        for pdf_filename in pdf_input:
            excel_output = f"{os.path.splitext(pdf_filename)[0]}.xlsx"
            pdf2excel(pdf_filename, excel_output)

        print("Conversion is complete for all PDF files.")

if __name__ == "__main__":
    print("NOTE: All files PDF must in the same directory with pdf2excel.py")
    main()