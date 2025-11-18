modos = ["meia", "quarto", "oitavo"]

ordens = [
    [1, 4, 2, 3],
    [1, 8, 4, 5, 7, 2, 6, 3],
    [1, 16, 8, 9, 15, 2, 10, 7, 3, 14, 6, 11, 13, 4, 12, 5],
  ]


def ordenador(entrada, modo):
  # fazer com que o modo escolha a ordenação das paginas
  # pode ser para "meia", "quarto", "oitavo".
  ordem = ordens[modos.index(modo)]
  L = len(entrada)
  D = len(ordem)

  # Faz o numero de pag ser "fechado"
  P = L + (D - L % D)

  # variaveis do loop
  reordered = []
  step = -1

  for i in range(P):
    #  Selecionamos as paginas na ordem que queremos
    d = i % D
    if not d: step += 1
    page = (ordem[d] + step * D) - 1

    # Caso tenham paginas que sobram
    if page >= L: reordered.append(0)
    else:
      # Paginas a rodar
      if (d % 4 == 0) or (d % 4 == 1): entrada[page].rotate(180)
        
      # Enfim, adiciona a pagina
      reordered.append(entrada[page])

  return reordered