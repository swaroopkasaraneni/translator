import PyPDF2
import docx
import pandas as pd

# read data from PDF
def from_pdf(pdf_path):
  reader = PyPDF2.PdfReader(pdf_path)
  text = ''
  for page in reader.pages:
    text += page.extract_text()
  return text
# read data from word document
def from_docx(docx_path):
  doc = docx.Document(docx_path)
  text = ''
  for para in doc.paragraphs:
    text += para.text
  return text
# read data from text file
def from_txt(txt_path):
  with open(txt_path, 'r') as f:
    text = f.read()
  return text

def from_excel(excel_path):
  df = pd.read_excel(excel_path)
  text = df['text'].values()
  return text

def from_csv(csv_path):
  df = pd.read_csv(csv_path)
  text = df['text'].values()
  return text