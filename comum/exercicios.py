"""Exercícios práticos criados para estudar o livro, um ou mais por seção.

Formato: (capítulo, início do título da seção, nome, enunciado em Markdown, solução em Python).
Os exemplos são originais (não copiados do livro): o objetivo é praticar o que o capítulo explica.
"""

EXERCICIOS = [
    # ---------------- Capítulo 2 — Python ----------------
    (2, "2.1", "Qual Python estou usando?",
     "Mostre a versão do Python e o caminho do executável (`sys.version` e `sys.executable`). "
     "O caminho deve terminar em `.venv\\Scripts\\python.exe`; se não terminar, o kernel escolhido está errado.",
     'import sys\nprint(sys.version)\nprint(sys.executable)'),
    (2, "2.4", "Bibliotecas instaladas",
     "Importe `numpy` e `matplotlib` e mostre a versão de cada uma.",
     'import numpy, matplotlib\nprint("numpy", numpy.__version__)\nprint("matplotlib", matplotlib.__version__)'),
    (2, "2.6", "Média sem NumPy",
     "Escreva uma função `media(valores)` que recebe uma lista de números e devolve a média, "
     "usando só `for` (sem `sum` nem NumPy). Teste com `[4, 8, 15, 16, 23, 42]` (resposta: 18.0).",
     'def media(valores):\n    total = 0\n    for v in valores:\n        total += v\n    return total / len(valores)\n\nprint(media([4, 8, 15, 16, 23, 42]))'),
    (2, "2.6", "Lista vs. array",
     "Crie a lista `l = [1, 2, 3]` e o array `a = np.array([1, 2, 3])`. Compare `l * 2` com `a * 2` e "
     "`l + l` com `a + a`. Escreva num comentário por que os resultados são diferentes.",
     'l = [1, 2, 3]\na = np.array([1, 2, 3])\nprint(l * 2, a * 2)   # lista repete; array multiplica cada elemento\nprint(l + l, a + a)   # lista concatena; array soma elemento a elemento'),

    # ---------------- Capítulo 3 — Conceitos básicos ----------------
    (3, "3.1", "Escalar, vetor e matriz",
     "Crie um escalar `k = 3`, um vetor `v` com 4 elementos e uma matriz `M` 2×3. "
     "Para cada um, mostre `np.ndim` e `np.shape`.",
     'k = np.array(3)\nv = np.array([2, 4, 6, 8])\nM = np.array([[1, 2, 3], [4, 5, 6]])\nfor nome, x in [("k", k), ("v", v), ("M", M)]:\n    print(nome, "ndim =", x.ndim, "shape =", x.shape)'),
    (3, "3.2", "Galeria de matrizes especiais",
     "Crie, com funções do NumPy: identidade 4×4, matriz de zeros 2×3, matriz diagonal com `[1, 5, 9]` "
     "e a triangular superior de `np.arange(1, 10).reshape(3, 3)`.",
     'print(np.eye(4))\nprint(np.zeros((2, 3)))\nprint(np.diag([1, 5, 9]))\nprint(np.triu(np.arange(1, 10).reshape(3, 3)))'),
    (3, "3.2", "É simétrica?",
     "Escreva `eh_simetrica(A)` que devolve `True` quando `A` é igual à sua transposta. "
     "Teste com `[[1, 7], [7, 2]]` (sim) e `[[1, 2], [3, 4]]` (não).",
     'def eh_simetrica(A):\n    A = np.asarray(A)\n    return A.shape[0] == A.shape[1] and np.array_equal(A, A.T)\n\nprint(eh_simetrica([[1, 7], [7, 2]]), eh_simetrica([[1, 2], [3, 4]]))'),
    (3, "3.3", "Vetor e escalar",
     "Com `v = np.array([10, 20, 30])`, calcule `v + 5`, `v * 0.5` e `v / 10`. "
     "Depois faça o mesmo com um laço `for` e confira que dá igual.",
     'v = np.array([10, 20, 30])\nprint(v + 5, v * 0.5, v / 10)\nprint([x * 0.5 for x in v])'),
    (3, "3.4", "Produto escalar, norma e ângulo",
     "Para `u = [3, 4]` e `w = [4, 3]`: calcule o produto escalar (`np.dot`), a norma de cada um (`np.linalg.norm`) "
     "e o ângulo entre eles em graus, usando cos θ = u·w / (|u||w|).",
     'u = np.array([3, 4]); w = np.array([4, 3])\nprod = np.dot(u, w)\nnu, nw = np.linalg.norm(u), np.linalg.norm(w)\nangulo = np.degrees(np.arccos(prod / (nu * nw)))\nprint(prod, nu, nw, round(angulo, 2))'),
    (3, "3.4", "Vetores ortogonais",
     "Dois vetores são ortogonais quando o produto escalar é zero. Verifique quais pares são ortogonais: "
     "`([1, 2], [-2, 1])`, `([1, 1], [1, -2])`, `([2, 0, 1], [0, 5, 0])`.",
     'pares = [([1, 2], [-2, 1]), ([1, 1], [1, -2]), ([2, 0, 1], [0, 5, 0])]\nfor a, b in pares:\n    print(a, b, "ortogonais" if np.dot(a, b) == 0 else "não ortogonais")'),
    (3, "3.5", "Reajuste de preços",
     "Uma matriz guarda preços de 3 produtos (linhas) em 2 lojas (colunas): `[[10, 12], [5, 4.5], [30, 28]]`. "
     "Aplique um reajuste de 8% multiplicando a matriz por um escalar.",
     'P = np.array([[10, 12], [5, 4.5], [30, 28]])\nprint(P * 1.08)'),
    (3, "3.6", "Total da compra",
     "A matriz `P` do exercício anterior (preços por loja) e o vetor `q = [2, 6, 1]` (quantidades). "
     "Calcule quanto a compra custa em cada loja com `q @ P` e diga qual loja é mais barata.",
     'P = np.array([[10, 12], [5, 4.5], [30, 28]])\nq = np.array([2, 6, 1])\ntotais = q @ P\nprint(totais, "-> loja mais barata:", int(np.argmin(totais)) + 1)'),
    (3, "3.6", "Girar um ponto 90°",
     "A matriz de rotação de 90° é `R = [[0, -1], [1, 0]]`. Aplique `R` ao ponto `(2, 1)` e depois "
     "aplique 4 vezes seguidas. O que acontece?",
     'R = np.array([[0, -1], [1, 0]])\np = np.array([2, 1])\nprint(R @ p)\nx = p\nfor _ in range(4):\n    x = R @ x\nprint(x, "-> voltou ao ponto inicial")'),
    (3, "3.7", "A ordem importa",
     "Com `A = [[1, 2], [3, 4]]` e `B = [[0, 1], [1, 0]]`, calcule `A @ B` e `B @ A`. São iguais? "
     "Compare também com `A * B` (produto elemento a elemento).",
     'A = np.array([[1, 2], [3, 4]]); B = np.array([[0, 1], [1, 0]])\nprint(A @ B)\nprint(B @ A)\nprint(A * B)'),
    (3, "3.7", "Transposta do produto",
     "Gere duas matrizes aleatórias 3×3 e confira que (A·B)ᵀ = Bᵀ·Aᵀ com `np.allclose`.",
     'rng = np.random.default_rng(0)\nA = rng.integers(0, 10, (3, 3)); B = rng.integers(0, 10, (3, 3))\nprint(np.allclose((A @ B).T, B.T @ A.T))'),
    (3, "3.8", "Inversa e identidade",
     "Calcule a inversa de `A = [[4, 7], [2, 6]]` e confira que `A @ inv(A)` dá a identidade.",
     'A = np.array([[4, 7], [2, 6]])\nAi = np.linalg.inv(A)\nprint(Ai)\nprint(A @ Ai)\nprint(np.allclose(A @ Ai, np.eye(2)))'),
    (3, "3.8", "Matriz sem inversa",
     "Tente inverter `S = [[1, 2], [2, 4]]`. Use `try/except np.linalg.LinAlgError` para mostrar uma "
     "mensagem amigável. Por que ela não tem inversa? (dica: compare as linhas)",
     'S = np.array([[1, 2], [2, 4]])\ntry:\n    np.linalg.inv(S)\nexcept np.linalg.LinAlgError:\n    print("S não tem inversa: a 2ª linha é o dobro da 1ª (matriz singular)")'),
    (3, "3.9", "Fatiar e alterar",
     "Com `M = np.arange(1, 17).reshape(4, 4)`: mostre a 2ª linha, a última coluna, o bloco 2×2 do centro, "
     "e troque por 0 todos os valores pares (máscara booleana).",
     'M = np.arange(1, 17).reshape(4, 4)\nprint(M[1])\nprint(M[:, -1])\nprint(M[1:3, 1:3])\nM2 = M.copy(); M2[M2 % 2 == 0] = 0\nprint(M2)'),

    # ---------------- Capítulo 4 — Sistemas ----------------
    (4, "4 ", "Sistema 2×2",
     "Resolva com `np.linalg.solve`: 2x + y = 7 e x − y = −1. Confira substituindo a solução nas equações.",
     'A = np.array([[2, 1], [1, -1]]); b = np.array([7, -1])\nx = np.linalg.solve(A, b)\nprint(x)\nprint(A @ x, "deve ser", b)'),
    (4, "4 ", "Problema dos ingressos",
     "Um cinema vendeu 200 ingressos e arrecadou R$ 5.200. Inteira custa R$ 30 e meia, R$ 15. "
     "Monte o sistema e descubra quantos de cada tipo foram vendidos.",
     '# i + m = 200 ; 30i + 15m = 5200\nA = np.array([[1, 1], [30, 15]]); b = np.array([200, 5200])\ninteiras, meias = np.linalg.solve(A, b)\nprint(f"inteiras = {inteiras:.0f}, meias = {meias:.0f}")'),
    (4, "4 ", "Sistema 3×3 pela inversa",
     "Resolva x + y + z = 6, 2y + 5z = −4, 2x + 5y − z = 27 de dois jeitos: `solve` e `inv(A) @ b`. "
     "Os resultados batem?",
     'A = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]]); b = np.array([6, -4, 27])\nprint(np.linalg.solve(A, b))\nprint(np.linalg.inv(A) @ b)'),

    # ---------------- Capítulo 5 — Determinantes ----------------
    (5, "5.1", "Determinante na mão",
     "Escreva `det2(M)` que calcula o determinante de uma matriz 2×2 pela fórmula ad − bc. "
     "Compare com `np.linalg.det` para `[[3, 8], [4, 6]]`.",
     'def det2(M):\n    (a, b), (c, d) = M\n    return a * d - b * c\n\nM = [[3, 8], [4, 6]]\nprint(det2(M), np.linalg.det(M))'),
    (5, "5.1", "Determinante zero",
     "Calcule o determinante de `[[2, 4], [1, 2]]` e explique, num comentário, o que um determinante zero "
     "diz sobre a inversa e sobre o sistema linear.",
     'S = np.array([[2, 4], [1, 2]])\nprint(np.linalg.det(S))\n# det = 0: a matriz não tem inversa e o sistema não tem solução única'),
    (5, "5.1", "Propriedades",
     "Com matrizes aleatórias 3×3, confira: det(A·B) = det(A)·det(B) e det(Aᵀ) = det(A). "
     "Depois veja que o determinante de uma triangular é o produto da diagonal.",
     'rng = np.random.default_rng(1)\nA = rng.integers(-5, 6, (3, 3)); B = rng.integers(-5, 6, (3, 3))\nd = np.linalg.det\nprint(np.isclose(d(A @ B), d(A) * d(B)), np.isclose(d(A.T), d(A)))\nT = np.triu(A)\nprint(np.isclose(d(T), np.prod(np.diag(T))))'),

    # ---------------- Capítulo 6 — Autovalores ----------------
    (6, "6.1", "Transformar um quadrado",
     "Os cantos de um quadrado são as colunas de `Q = [[0, 1, 1, 0, 0], [0, 0, 1, 1, 0]]`. "
     "Aplique a escala `[[2, 0], [0, 0.5]]` e o cisalhamento `[[1, 1], [0, 1]]` e desenhe os três "
     "contornos com `plt.plot`.",
     'Q = np.array([[0, 1, 1, 0, 0], [0, 0, 1, 1, 0]])\nE = np.array([[2, 0], [0, 0.5]]); C = np.array([[1, 1], [0, 1]])\nfor M, rot in [(np.eye(2), "original"), (E, "escala"), (C, "cisalhamento")]:\n    P = M @ Q\n    plt.plot(P[0], P[1], label=rot)\nplt.axis("equal"); plt.legend(); plt.show()'),
    (6, "6.2", "Autovalores e autovetores",
     "Calcule autovalores e autovetores de `A = [[2, 1], [1, 2]]` com `np.linalg.eig` e confira, "
     "para cada par, que A·v = λ·v.",
     'A = np.array([[2, 1], [1, 2]])\nvalores, vetores = np.linalg.eig(A)\nfor lam, v in zip(valores, vetores.T):\n    print(lam, v, np.allclose(A @ v, lam * v))'),
    (6, "6.2", "Remontar a matriz",
     "Com os autovetores (colunas de P) e autovalores (diagonal de D) do exercício anterior, "
     "confira que A = P·D·P⁻¹.",
     'A = np.array([[2, 1], [1, 2]])\nvalores, P = np.linalg.eig(A)\nD = np.diag(valores)\nprint(np.allclose(A, P @ D @ np.linalg.inv(P)))'),

    # ---------------- Capítulo 7 — Aplicações ----------------
    (7, "7.1", "Média e covariância com matrizes",
     "Gere `X` com 100 linhas e 3 colunas (`rng.normal`). Calcule a média de cada coluna com "
     "`np.ones(n) @ X / n` e a matriz de covariância com `Xc.T @ Xc / (n - 1)`, onde Xc é X centralizada. "
     "Compare com `X.mean(axis=0)` e `np.cov(X, rowvar=False)`.",
     'rng = np.random.default_rng(42)\nX = rng.normal(size=(100, 3)); n = len(X)\nmedia = np.ones(n) @ X / n\nXc = X - media\ncov = Xc.T @ Xc / (n - 1)\nprint(np.allclose(media, X.mean(axis=0)), np.allclose(cov, np.cov(X, rowvar=False)))'),
    (7, "7.2", "Mensagem secreta",
     "Transforme `\"ALGEBRA\"` em números (A=1, B=2, ..., espaço=0), arrume em pares (colunas de uma matriz 2×n, "
     "completando com 0) e codifique multiplicando pela chave `K = [[3, 1], [2, 1]]`. "
     "Depois decodifique com a inversa de K e volte para texto.",
     'K = np.array([[3, 1], [2, 1]])\ntexto = "ALGEBRA"\nnums = [0 if c == " " else ord(c) - 64 for c in texto]\nif len(nums) % 2: nums.append(0)\nM = np.array(nums).reshape(-1, 2).T\ncod = K @ M\nprint(cod)\ndec = np.rint(np.linalg.inv(K) @ cod).astype(int)\nprint("".join(" " if x == 0 else chr(x + 64) for x in dec.T.flatten()).strip())'),
    (7, "7.3", "Mistura de rações",
     "Três rações têm (proteína, gordura, fibra) em gramas por kg: R1 = (20, 5, 10), R2 = (10, 10, 5), "
     "R3 = (30, 2, 8). Quantos kg de cada uma misturar para obter 230 g de proteína, 75 g de gordura e 98 g de fibra?",
     'A = np.array([[20, 10, 30], [5, 10, 2], [10, 5, 8]])\nb = np.array([230, 75, 98])\nprint(np.linalg.solve(A, b))'),
    (7, "7.4", "PageRank de 4 páginas",
     "Páginas: 1→2, 1→3, 2→3, 3→1, 4→1, 4→3. Monte a matriz de transição (coluna j = para onde a página j "
     "aponta, dividido pelo nº de links), use fator de amortecimento 0.85 e calcule o ranking "
     "pelo método da potência (repita r = G·r até estabilizar).",
     'links = {1: [2, 3], 2: [3], 3: [1], 4: [1, 3]}\nn = 4\nT = np.zeros((n, n))\nfor j, destinos in links.items():\n    for i in destinos:\n        T[i - 1, j - 1] = 1 / len(destinos)\nG = 0.85 * T + 0.15 / n\nr = np.ones(n) / n\nfor _ in range(100):\n    r = G @ r\nprint(r.round(3), "-> ordem:", (np.argsort(-r) + 1).tolist())'),
    (7, "7.5", "Fibonacci com potência de matriz",
     "Com `F = [[1, 1], [1, 0]]`, o elemento [0, 1] de Fⁿ é o n-ésimo Fibonacci. "
     "Calcule F(1..15) com `np.linalg.matrix_power` e compare com um laço comum.",
     'F = np.array([[1, 1], [1, 0]])\nmat = [int(np.linalg.matrix_power(F, n)[0, 1]) for n in range(1, 16)]\nlaco, a, b = [], 0, 1\nfor _ in range(15):\n    a, b = b, a + b\n    laco.append(a)\nprint(mat)\nprint(mat == laco)'),
    (7, "7.5", "Fibonacci pelos autovalores",
     "Os autovalores de F são φ = (1+√5)/2 e ψ = (1−√5)/2. Calcule-os com `np.linalg.eigvalsh` (versão para matrizes simétricas) e use "
     "F(n) = (φⁿ − ψⁿ)/√5 para obter F(30). Confira com o método do exercício anterior.",
     'F = np.array([[1, 1], [1, 0]])\nphi, psi = sorted(np.linalg.eigvalsh(F), reverse=True)  # eigvalsh: F é simétrica, autovalores reais\nn = 30\nprint(round((phi**n - psi**n) / np.sqrt(5)), int(np.linalg.matrix_power(F, n)[0, 1]))'),
]
