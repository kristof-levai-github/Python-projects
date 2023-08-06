from pypdf import PdfReader
import pdfplumber
import fitz

'''
pip install pypdf
from pypdf import PdfReader

pip install pdfplumber
import pdfplumber

pip install pymupdf
import fitz 
'''

#-------------------- links -------------------- #


'''
https://pythonology.eu/what-is-the-best-python-pdf-library/
https://www.youtube.com/watch?v=G0PApj7YPBo
https://pymupdf.readthedocs.io/en/latest/
https://pypdf2.readthedocs.io/en/3.0.0/
https://github.com/jsvine/pdfplumber
'''


#------------- pypdf ------------#

reader = PdfReader('test.pdf')

#the length of the pages:
print(len(reader.pages))

#grab the first page
page = reader.pages[0]

#grab the text of the first page
print(page.extract_text())

#extract the text of every page: 
for i in range(len(reader.pages)):
    page = reader.pages[i]
    print(page.extract_text())

#extract all the images and save them to a folder:
for i in page.images:
    with open(i.name, 'wb') as f:
        f.write(i.data)


# ----------------- pdfplumber ------------------#

#getting the tables from a pdf
with pdfplumber.open('test.pdf') as f:
    for i in f.pages:
        print(i.extract_tables())


# ---------------- pymupdf --------------------#

#open the file, get the number of pages
doc = fitz.open('test.pdf')
print(doc.page_count)

#get the metadata of the pdf
print(doc.metadata)

#access page1, grab the text from page1
page = doc.load_page(0)
print(page.get_text())

#get the actual page numbers of the page:
#num = page.number

#turn one page into image
pix = page.get_pixmap()
pix.save(f"page{page.number}.png")

'''
#turn the whole pdf into images

for i in range(len())
pixall = page.get_pixmap()
pixall.save(f"page{page.number}.png")

'''

#get all the links from the pdf: 
links = page.get_links()
print(links)