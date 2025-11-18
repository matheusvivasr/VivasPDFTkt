from PyPDF2 import PdfWriter, PdfReader
from src.reorder import ordenador


def operador(arquivo, modo):

  arquivo = arquivo + ".pdf"
  livro = ordenador(PdfReader("entrada/" + arquivo).pages, modo)
  
  impressora = PdfWriter()
  for pagina in livro:
    if pagina == 0: impressora.add_blank_page()
    else: impressora.add_page(pagina)

  with open("saida/" + arquivo, 'wb') as livro:
    impressora.write(livro)
    
  print("Pronto!")
  return 0

def rotateHalf(arquivo):
  arquivo = arquivo + ".pdf"
  livro = PdfReader("entrada/" + arquivo).pages
  impressora = PdfWriter()
  
  for i in range(len(livro)):
    #livro[i].rotate(90)
    livro[i].rotate(((90)*(-1)**(i%2)))
    impressora.add_page(livro[i])
    
  with open("saida/" + arquivo, 'wb') as livro:
    impressora.write(livro)
    
  print("Pronto!")
  return 0


def endend(arquivo):
  arquivo = arquivo + ".pdf"
  entrada = PdfReader("entrada/" + arquivo).pages
  #________________________________________
  reorder = []
  L = len(entrada)
  if L%2:L+=1# deixa o numero de pag par
  M = int(L/2)
  if M%2:
    M+=1
    L+=2
  for i in range(0,M,2):
    rlist = [i+1,L-(i+2),L-(i+1),i]
    for n in rlist:
      try:
        reorder.append(entrada[n])
      except:
        reorder.append(0)
  #________________________________________
  impressora = PdfWriter()
  for pagina in reorder:
    if pagina == 0: impressora.add_blank_page()
    else: impressora.add_page(pagina)

  with open("saida/" + arquivo, 'wb') as livro:
    impressora.write(livro)
    
  print("Pronto!")
  return 0