

<div align="center">

# 🐍📚 **Vivas PDF Toolkit**
### *Um conjunto modular de ferramentas para organizar, otimizar e preparar PDFs para impressão profissional*

![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge)
![PDFTools](https://img.shields.io/badge/PDF-Tools-orange?style=for-the-badge)

</div>

---

Bem-vindo ao **Vivas PDF**, um repositório dedicado a um
conjunto de ferramentas para reorganização e reestruturação de PDFs em
formatos otimizados.\
O objetivo é permitir que usuários transformem documentos extensos em
versões mais compactas, organizadas e adequadas para impressão em
múltiplas folhas por página --- incluindo formatos de **2**,
**4**, **8** páginas por folha no formato de **livretos**.

------------------------------------------------------------------------

## 📚 Índice

1.  [Sobre o Projeto](#sobre-o-projeto)
2.  [Funcionalidades](#funcionalidades)
3.  [Estrutura do Repositório](#estrutura-do-repositório)
4.  [Como Usar](#como-usar)
5.  [Exemplos](#exemplos)
6.  [Links Úteis](#links-úteis)
7.  [Contribuição](#contribuição)
8.  [Licença](#licença)

------------------------------------------------------------------------

## 📝 Sobre o Projeto

O **Vivas PDF** nasceu da necessidade de manipular arquivos PDF de forma
prática e automatizada.\
Ele permite reorganizar páginas em diferentes layouts e exportar versões
prontas para impressão.

O foco inicial do projeto é:\
- Reduzir o número de folhas utilizadas;\
- Criar impressões organizadas e com boa legibilidade;\
- Facilitar a produção de **livretos**, onde a ordem das páginas é
reestruturada automaticamente.

 Ferramentas úteis para reorganizar PDFs em formatos 2, 4 ou 8 páginas por folha, reduzindo o gasto de papel em impressões.

Este projeto nasceu da necessidade prática de imprimir materiais de estudo de maneira mais compacta e econômica. Use com responsabilidade — e sempre respeitando direitos autorais.
> Obs: Ideal para quem imprime apostilas gigantes e não quer falir comprando papel.

------------------------------------------------------------------------

## ⚙️ Funcionalidades

-   📄 **Reorganização de PDFs** em layouts de múltiplas páginas por
    folha;\
-   🖨️ **Preparação de livreto** com ordenação automática de páginas;\
-   🧩 Combinação e divisão de arquivos PDF;\
-   🎨 Preservação de resolução e margens configuráveis;\
-   🚀 Scripts simples de usar e fáceis de modificar.

------------------------------------------------------------------------

## 🗂️ Estrutura do Repositório

    Vivas-PDF/
    │
    ├── src/
    │   ├── arranger.py          # Funções principais para manipulação de páginas
    │   ├── booklet.py           # Módulo responsável pela lógica de livreto
    │   ├── utils.py             # Funções auxiliares
    │   └── __init__.py
    │
    ├── examples/
    │   ├── exemplo_2up.pdf
    │   ├── exemplo_4up.pdf
    │   └── exemplo_booklet.pdf
    │
    ├── README.md
    └── requirements.txt

------------------------------------------------------------------------

## ▶️ Como Usar

### 🔧 Instalação

``` bash
pip install -r requirements.txt
```

### ▶️ Executar script principal

``` bash
python src/arranger.py input.pdf --modo 4up --saida output.pdf
```

### 🧾 Gerar livreto

``` bash
python src/booklet.py input.pdf --saida livreto.pdf
```

------------------------------------------------------------------------

## 📌 Exemplos

### 🔹 2 páginas por folha

![2up](https://link)

### 🔹 Livreto (ordenação especial)

![Booklet](https:/link)

------------------------------------------------------------------------

## 🔗 Links Úteis

-   📘 *Documentação do PyPDF2*:\
    https://pypdf.readthedocs.io/en/stable/

-   🎨 *Ferramentas online de visualização*:\
    https://www.ilovepdf.com

------------------------------------------------------------------------

## 🤝 Contribuição

Contribuições são sempre bem-vindas!\
Se quiser adicionar novos formatos, melhorar a lógica de livreto ou
expandir os utilitários, fique à vontade para abrir Pull Requests.

------------------------------------------------------------------------

## 📄 Licença

Este modelo de README usa uma licença livre e pode ser adaptado como
preferir.