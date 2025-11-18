from PyPDF2 import PdfWriter, PdfReader
from src.handler import operador

def opERM(arquivo):
  livro = PdfReader("entrada/"+arquivo+".pdf").pages
  capa = PdfReader("entrada/"+arquivo+".pdf").pages

  impressora = PdfWriter()
  for pagina in capa:
    impressora.add_page(pagina)
  for i in range(len(livro)):
    if i < 2:pass
    else:impressora.add_page(livro[i])
  with open("entrada/"+arquivo+".pdf", 'wb') as saida:
    impressora.write(saida)
    
  print("ate aqui tudo ok")
  operador(arquivo,"meia")
  return 0