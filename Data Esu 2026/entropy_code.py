# === TO BUILD: load your dataset (file path, URL, or pasted text) ===
sample_sum = open("Exp_20_clean.txt", encoding="utf-8").read()
sample_no_sum = open("Carta de José Salvany 1-2.txt", encoding="utf-8").read()
sample_no_sum2 = open("Salvany 1-2-3.txt", encoding="utf-8").read()

print('sample_sum length:', len(sample_sum.split()), 'words')
print('sample_no_sum length:', len(sample_no_sum.split()), 'words')
print('sample_no_sum length:', len(sample_no_sum2.split()), 'words')


# === Get the tokens and types ===
import numpy as np, math
import urllib.request
import matplotlib.pyplot as plt
from collections import Counter

tokens_sum = [w.lower().strip('.,;:!?') for w in sample_sum.split()]
tokens_no_sum = [w.lower().strip('.,;:!?') for w in sample_no_sum.split()]
tokens_no_sum2 = [w.lower().strip('.,;:!?') for w in sample_no_sum2.split()]

print(len(tokens_sum), 'tokens,', len(set(tokens_sum)), 'types')
print(len(tokens_no_sum), 'tokens,', len(set(tokens_no_sum)), 'types')
print(len(tokens_no_sum2), 'tokens,', len(set(tokens_no_sum2)), 'types')

a = len(tokens_sum)
b = len(tokens_no_sum)
c = len(tokens_no_sum2)

type_a = len(set(tokens_sum))
type_b = len(set(tokens_no_sum))
type_c = len(set(tokens_no_sum2))

# === Calculate the entropy levels ===
import math
def entropy(items):
    n=len(items); from collections import Counter as C
    return -sum((c/n)*math.log2(c/n) for c in C(items).values())

print('entropy of summary text:', round(entropy(tokens_sum),3))
print('entropy of non summary text:', round(entropy(tokens_no_sum),3))
print('entropy of non summary text:', round(entropy(tokens_no_sum2),3))

ent_a = round(entropy(tokens_sum),3)
ent_b = round(entropy(tokens_no_sum),3)
ent_c = round(entropy(tokens_no_sum2),3)

print(ent_a, ent_b, ent_c)

# === TO BUILD: one plot that shows your result. Rough is fine. ===
# plt.bar(...); plt.title('...'); plt.show()
#print('Make one plot here.')

import matplotlib.pyplot as plt

textos = ["Summary", "Non Summary 1", "Non Summary 2"]
entropias = [ent_a, ent_b, ent_c]
tokens = [a, b, c]
types = [type_a, type_b, type_c]

x = np.arange(len(textos))
width = 0.25   # más angosto porque ahora hay 3 barras por grupo

fig, ax1 = plt.subplots(figsize=(9, 6))

# Barra 1: entropía (eje izquierdo)
bars1 = ax1.bar(x - width, entropias, width, label='Entropía (bits)', color='steelblue')
ax1.set_ylabel('Entropía (bits/símbolo)', color='steelblue')
ax1.tick_params(axis='y', labelcolor='steelblue')
ax1.set_xticks(x)
ax1.set_xticklabels(textos)

# Barras 2 y 3: comparten el eje derecho (misma escala: cantidad de palabras)
ax2 = ax1.twinx()
bars2 = ax2.bar(x, tokens, width, label='N° de palabras', color='darkorange')
bars3 = ax2.bar(x + width, types, width, label='Palabras únicas', color='seagreen')
ax2.set_ylabel('Cantidad de palabras', color='gray')

# Etiquetas con valores
ax1.bar_label(bars1, fmt='%.2f', padding=3)
ax2.bar_label(bars2, fmt='%d', padding=3)
ax2.bar_label(bars3, fmt='%d', padding=3)

# Leyenda combinada (porque están en ejes distintos)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(
    lines1 + lines2, labels1 + labels2,
    loc='upper center',
    bbox_to_anchor=(0.5, -0.12),   # centrado horizontalmente, debajo del eje X
    ncol=3,
    frameon=False
)


plt.title('Entropía, palabras totales y palabras únicas por texto')
fig.tight_layout()
plt.show()