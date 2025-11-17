import jpg2pdf

with jpg2pdf.create('teste.pdf') as pdf:
    pdf.add('foto.jpg')
