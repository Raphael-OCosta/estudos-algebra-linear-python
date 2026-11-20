# 📐 Estudos — *Álgebra Linear com Python* (Rafael F. V. C. Santos)

> **A melhor forma de estudar um livro técnico é ler e praticar ao mesmo tempo.**
> Leia uma seção, feche o livro e escreva o código com as próprias mãos. Só depois confira o gabarito.

Este repositório registra meu estudo do livro *Álgebra Linear com Python: aprenda na prática os principais conceitos*.
Cada capítulo virou um caderno Jupyter. Cada seção aponta para a página do PDF e traz um exercício original para fixar o conteúdo.

## 🔁 O método

| Passo | O que fazer | Onde |
|---|---|---|
| 1. Ler | Ler a seção indicada | PDF do livro (página no caderno) |
| 2. Praticar | Escrever a solução do 🧪 exercício **sem olhar a resposta** | `praticar/capXX_*.ipynb` |
| 3. Conferir | Comparar com o gabarito e entender a diferença | `resolvidos/capXX_*.ipynb` |
| 4. Resumir | Explicar com as próprias palavras nas células 📝 | `praticar/` |
| 5. Registrar | Commit + push, para o progresso ficar visível | GitHub |

## 📚 Conteúdo

| Cap. | Tema | Exercícios |
|---|---|---|
| 1 | Introdução | anotações |
| 2 | Python: ambiente, listas × arrays, funções | 4 |
| 3 | Vetores, matrizes, produto escalar, inversa, fatiamento | 14 |
| 4 | Sistemas de equações lineares | 3 |
| 5 | Determinantes e suas propriedades | 3 |
| 6 | Transformações lineares, autovalores e autovetores | 3 |
| 7 | Aplicações: estatística, criptografia, misturas, PageRank, Fibonacci | 6 |

**Total: 33 exercícios.** Todos foram criados para este estudo e o gabarito é testado automaticamente.

## 🛠️ Melhorias em relação ao livro

- O livro usa o IDLE. Aqui uso **VS Code + Jupyter**: cada seção vira uma célula que dá para rodar, e as anotações ficam ao lado do código.
- **NumPy 2.x** e Python 3.12. O gabarito roda sem avisos nas versões atuais.
- Para autovalores de matrizes simétricas, o gabarito usa `np.linalg.eigvalsh`, que devolve números reais (`eig` pode devolver complexos).
- Exercícios com conferência embutida (`np.allclose`, A·v = λ·v, A = P·D·P⁻¹), para eu ver se acertei e não só se o código rodou.
- O gabarito inteiro é executado por `ferramentas/testar_cadernos.py`.

## ▶️ Como usar

```powershell
# Python 3.12 (python.org) instalado
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-estudos.txt
.venv\Scripts\python.exe ferramentas\gerar_cadernos.py   # recria os cadernos (não sobrescreve praticar/)
.venv\Scripts\python.exe ferramentas\testar_cadernos.py  # roda o gabarito inteiro
.venv\Scripts\python.exe ferramentas\gerar_guia.py       # gera o Guia_de_Estudos.pdf
```

Abra a pasta no VS Code, escolha o kernel `.venv` e comece por `praticar/cap01_introducao.ipynb`.
O [Guia de Estudos (PDF)](Guia_de_Estudos.pdf) explica o passo a passo para iniciantes.

## ⚖️ Direitos autorais

O livro **não** está neste repositório. Para estudar, use a sua própria cópia.
Os exercícios, os cadernos, os scripts e o guia são autorais e estão sob licença [MIT](LICENSE).
