import jpg2pdf

with jpg2pdf.create('meupdf.pdf') as pdf:
    pdf.add('1.jpg')
    pdf.add('2.jpg')
