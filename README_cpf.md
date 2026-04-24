# 🇧🇷 Verificador de CPF

> Validação de CPF em Python com o algoritmo oficial da **Receita Federal do Brasil** — usável como script CLI ou módulo importável.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen?style=flat)

---

## ✨ Funcionalidades

- ✅ Valida CPF via **algoritmo de dois dígitos verificadores** (Receita Federal)
- ✅ Aceita CPF **formatado** (`000.000.000-00`) ou **somente dígitos** (`00000000000`)
- ✅ Rejeita sequências inválidas como `111.111.111-11` e `000.000.000-00`
- ✅ **Modo CLI interativo** — valide múltiplos CPFs sem sair do terminal
- ✅ **Modo argumento** — integre em scripts e pipelines
- ✅ **Importável como módulo** — use `validate_cpf()` em qualquer projeto Python

---

## 🚀 Como usar

### Modo interativo

```bash
python cpf.py
```

```
╔══════════════════════════════════╗
║      Verificador de CPF  🇧🇷      ║
║   Algoritmo — Receita Federal    ║
╚══════════════════════════════════╝

Digite 'sair' para encerrar.

CPF: 529.982.247-25
✅  CPF válido!   (529.982.247-25)

CPF: 123.456.789-09
❌  CPF inválido.

CPF: sair
Encerrando. Até mais!
```

### Via argumento (single-shot)

```bash
python cpf.py 529.982.247-25
# ✅  CPF válido!   (529.982.247-25)

python cpf.py 12345678909
# ❌  CPF inválido.
```

### Como módulo Python

```python
from cpf import validate_cpf, format_cpf

validate_cpf("529.982.247-25")   # True
validate_cpf("12345678909")      # False
validate_cpf("111.111.111-11")   # False — sequência inválida

format_cpf("52998224725")        # "529.982.247-25"
```

---

## 🧠 Como funciona o algoritmo

O CPF tem 11 dígitos: **9 dígitos base** + **2 dígitos verificadores**.

### 1º dígito verificador

Multiplica os 9 primeiros dígitos pelos pesos de 10 a 2, soma os resultados e calcula o resto da divisão por 11.

```
D₁ = (d₀×10 + d₁×9 + ... + d₈×2) mod 11
Se D₁ < 2  →  dígito = 0
Se D₁ ≥ 2  →  dígito = 11 - D₁
```

### 2º dígito verificador

Repete o processo com os 9 dígitos base + o 1º dígito verificador, usando pesos de 11 a 2.

```
D₂ = (d₀×11 + d₁×10 + ... + d₉×2) mod 11
```

Se ambos os dígitos calculados coincidem com os dígitos 10 e 11 do CPF — **o CPF é válido**.

---

## 📁 Estrutura

```
verificador-de-cpf/
│
├── cpf.py        # Lógica de validação + CLI
└── README.md
```

---

## ⚙️ Requisitos

- Python **3.10+**
- Sem dependências externas — apenas biblioteca padrão

---

## 👤 Autor

**Davi** — [github.com/Davibzf](https://github.com/Davibzf)
