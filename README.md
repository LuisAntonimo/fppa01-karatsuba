# Inplementação Algoritmo de Karatsuba

Este é um projeto de implementação em Python do Algoritmo de Karatsuba para a matéria de Fundamentos de Projeto e Análise de Algoritmos

## O Problema

> "Dados números naturais *u* e *v* com no máximo *n* dígitos cada, calcular a expansão decimal do produto *u* × *v*."

Multiplicar dois números inteiros parece uma tarefa simples quando consideramos pequenas quantidades. Agora, multiplicar dois números inteiros de grande extensão (por exemplo: 109876 x 12345 ) já se mostra um pouco mais complicado, pelo menos para se executar de forma eficiente (o algoritmo usual de multiplicação resolve este problema em um tempo de *n²*).

Karatsuba resolve esse problema a partir do método de divisão e conquista. Divide-se ambos números pela metade para então serem resolvidos de forma recursiva, combinando os resultados ao final.

### Explicação linha a linha

```python
    if len(str(x)) <= 3 or len(str(y)) <= 3:
        return x * y
```
**Condição de parada**: Se o número de dígitos de `x` ou `y` for menor ou igual a 3, a função retorna o produto direto de `x` e `y`.

```python
    n = max(len(str(x)), len(str(y)))
```

**Número de dígitos**: `n` é o número máximo de dígitos entre `x` e `y`. Isso é necessário para dividir os números em partes iguais.

```python
    m = n // 2
```

**Divisão dos números**: `m` é a metade do número de dígitos `n`. Isso é usado para dividir os números `x` e `y` em duas partes.

```python
    a = x // 10**m
    b = x % 10**m
```

**Divisão de `x`**: `a` é a parte mais significativa de `x`, ou seja, os primeiros `n/2` dígitos de `x`. `b` é a parte menos significativa de `x`, ou seja, os últimos `n/2` dígitos de `x`.


```python
    c = y // 10**m
    d = y % 10**m
```

**Divisão de `y`**: `c` é a parte mais significativa de `y`, ou seja, os primeiros `n/2` dígitos de `y`. `d` é a parte menos significativa de `y`, ou seja, os últimos `n/2` dígitos de `y`.

```python
    ac = karatsuba(a, c)
```

**Multiplicação recursiva**: `ac` é o produto das partes mais significativas de `x` e `y`, calculado recursivamente.

```python
    bd = karatsuba(b, d)
```

**Multiplicação recursiva**: `bd` é o produto das partes menos significativas de `x` e `y`, calculado recursivamente.

```python
    adbc = karatsuba(a + b, c + d) - ac - bd
```

**Cálculo de `ad + bc`**: `adbc` é calculado como o produto de `(a + b)` e `(c + d)`, subtraindo `ac` e `bd`. Isso é feito porque `(a + b)(c + d) = ac + ad + bc + bd`, então `ad + bc = (a + b)(c + d) - ac - bd`.

```python
    return ac * 10**(2*m) + adbc * 10**m + bd
```

**Resultado final**: O produto final é calculado como `ac * 10^(2m) + adbc * 10^m + bd`. Isso combina as partes `ac`, `adbc` e `bd` de volta ao número original, ajustando as potências de 10 para alinhar corretamente os dígitos.


## Análise Ciclomática

![alt text](https://media.discordapp.net/attachments/851447897697681431/1345194243916042312/image.png?ex=67c3a944&is=67c257c4&hm=5bd1316157c9058f481693c533de635f3b68d8cdbe36e95296695134d4fe24c4&=&format=webp&quality=lossless&width=419&height=505)

| 01 | Início da função.                                                       |
|----|-------------------------------------------------------------------------|
| 02 | Verificação ``if len(str(x)) <= 3 or len(str(y)) <= 3``                 |
| 03 | Retorno da multiplicação direta ``return x * y``                        |
| 04 | Cálculo de ``n = max(len(str(x)), len(str(y)))``                        |
| 05 | Cálculo de ``m = n // 2``                                               |
| 06 | Divisão de x em a e b                                                   |
| 07 | Divisão de y em c e d                                                   |
| 08 | Chamada recursiva karatsuba(a, c)                                       |
| 09 | Chamada recursiva karatsuba(b, d)                                       |
| 10 | Chamada recursiva karatsuba(a + b, c + d)                               |
| 11 | Cálculo de ``adbc = karatsuba(a + b, c + d) - ac - bd``                 |
| 12 | Combinação dos resultados ``return ac * 10**(2*m) + adbc * 10**m + bd`` |
| 13 | Fim da função       

- 1 → 2: Fluxo inicial para a verificação.

- 2 → 3: Se a condição for verdadeira.

- 2 → 4: Se a condição for falsa.

- 4 → 5: Fluxo após calcular n.

- 5 → 6: Fluxo após calcular m.

- 6 → 7: Fluxo após dividir x.

- 7 → 8: Fluxo após dividir y.

- 8 → 9: Fluxo após calcular ac.

- 9 → 10: Fluxo após calcular bd.

- 10 → 11: Fluxo após calcular (a + b)(c + d).

- 11 → 12: Fluxo após calcular adbc.

- 12 → 13: Retorno do resultado final.

- 3 → 13: Retorno direto no caso base.
                                       |


### Cálculo da complexidade Ciclomática

- E = 13 (número de arestas).
- N = 13 (número de nós)
- P = 1

> ### M=13−13+2⋅1=2