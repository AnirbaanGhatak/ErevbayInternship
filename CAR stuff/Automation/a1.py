from PyPDF2 import PdfReader

reader = PdfReader("MOHD AABED ZAKIUDDIN FAROOQUI  cibill report pl.pdf")

list1 = []

n = reader.getNumPages()

for x in range(0, n):
    
    page = reader.getPage(page_number)
        page_content = page.extractText()
        if search_term in page_content:
            result = {
                "page": page_number,
                "content": page_content
            }
            result_list.append(result)

    


# page = reader.pages[3]

# print(page.extract_text())

# importing required modules
# import PyPDF2

# # creating a pdf file object
# pdf_file = open('YESHU.pdf', 'rb')

# # creating a pdf reader object
# read_pdf = PyPDF2.PdfFileReader(pdf_file)

# # printing number of pages in pdf file
# num_Of_Pages = read_pdf.getNumPages()
# # creating a page object

# for page_number in range(num_Of_Pages):
#     page = read_pdf.getPage(page_number)
#     page_Content = page.extractText()
#     print(page_Content)