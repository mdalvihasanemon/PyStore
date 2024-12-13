from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_file="merged.pdf"):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()
    print(f"Merged PDF saved as {output_file}")

merge_pdfs(["file1.pdf", "file2.pdf"])
