from PyPDF2 import PdfFileReader
import json

infile = "Assignment-1.pdf"
pdf_reader = PdfFileReader(open(infile, "rb"))

dictionary = pdf_reader.getFormTextFields() # returns a python dictionary
print(dictionary)
my_field_value = str(dictionary['Surname']) # use field name (dictionary key) to access field value (dictionary value)

json_data=json.dumps(dictionary) # returns field name and field value in Key-Value pairs of JSON Format
print(json_data)