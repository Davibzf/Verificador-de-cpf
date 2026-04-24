"""
cpf.py — Brazilian CPF Validator
=================================
Validates CPF numbers using the official two-digit verification algorithm
defined by Receita Federal do Brasil.

Usage (CLI):
    python cpf.py                    # interactive mode
    python cpf.py 123.456.789-09     # single CPF via argument

Usage (module):
    from cpf import validate_cpf
    validate_cpf("12345678909")      # True / False
"""

import sys
import re


# ─────────────────────────────────────────────────────────────────────────────
# Core logic
# ─────────────────────────────────────────────────────────────────────────────

def _sanitize(cpf: str) -> str:
    """Strip formatting characters (dots, dashes, spaces) from a CPF string."""
    return re.sub(r"[\.\-\s]", "", cpf.strip())


def _compute_digit(digits: list[int], weights: range) -> int:
    """
    Compute a single CPF verification digit.

    Args:
        digits:  List of integer digits to weight.
        weights: Multiplier range (descending), e.g. range(10, 1, -1).

    Returns:
        The computed verification digit (0–9).
    """
    total = sum(d * w for d, w in zip(digits, weights))
    remainder = total % 11
    return 0 if remainder < 2 else 11 - remainder


def validate_cpf(cpf: str) -> bool:
    """
    Validate a Brazilian CPF number.

    Accepts formatted (000.000.000-00) or plain (00000000000) strings.
    Rejects CPFs composed of a single repeated digit (e.g. 111.111.111-11),
    which are structurally valid but officially invalid.

    Args:
        cpf: CPF string in any common format.

    Returns:
        True if the CPF is valid, False otherwise.

    Examples:
        >>> validate_cpf("529.982.247-25")
        True
        >>> validate_cpf("000.000.000-00")
        False
        >>> validate_cpf("123.456.789-09")
        False
    """
    raw = _sanitize(cpf)

    # Must be exactly 11 numeric digits
    if not raw.isdigit() or len(raw) != 11:
        return False

    # Reject sequences of identical digits (e.g. "11111111111")
    if len(set(raw)) == 1:
        return False

    digits = [int(d) for d in raw]

    first_digit  = _compute_digit(digits[:9],  range(10, 1, -1))
    second_digit = _compute_digit(digits[:10], range(11, 1, -1))

    return digits[9] == first_digit and digits[10] == second_digit


def format_cpf(cpf: str) -> str:
    """
    Format a plain 11-digit CPF string as 000.000.000-00.

    Args:
        cpf: Plain 11-digit CPF string.

    Returns:
        Formatted CPF string.

    Raises:
        ValueError: If the input does not contain exactly 11 digits.
    """
    raw = _sanitize(cpf)
    if len(raw) != 11 or not raw.isdigit():
        raise ValueError(f"Expected 11 digits, got: '{cpf}'")
    return f"{raw[:3]}.{raw[3:6]}.{raw[6:9]}-{raw[9:]}"


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

VALID_MSG   = "✅  CPF válido!"
INVALID_MSG = "❌  CPF inválido."
FORMAT_ERR  = "⚠️   Formato incorreto. Digite 11 dígitos numéricos."

BANNER = """
╔══════════════════════════════════╗
║      Verificador de CPF  🇧🇷      ║
║   Algoritmo — Receita Federal    ║
╚══════════════════════════════════╝
"""


def _run_cli(cpf_arg: str | None = None) -> None:
    print(BANNER)

    if cpf_arg:
        # Single-shot mode: argument passed via command line
        cpfs = [cpf_arg]
    else:
        # Interactive mode
        print("Digite 'sair' para encerrar.\n")
        cpfs = []
        while True:
            entry = input("CPF: ").strip()
            if entry.lower() in ("sair", "exit", "q"):
                print("\nEncerrando. Até mais!")
                break
            cpfs.append(entry)
            raw = _sanitize(entry)
            if not raw.isdigit() or len(raw) != 11:
                print(FORMAT_ERR)
            elif validate_cpf(raw):
                print(f"{VALID_MSG}   ({format_cpf(raw)})\n")
            else:
                print(f"{INVALID_MSG}\n")
        return

    # Process argument(s)
    for cpf in cpfs:
        raw = _sanitize(cpf)
        if not raw.isdigit() or len(raw) != 11:
            print(FORMAT_ERR)
        elif validate_cpf(raw):
            print(f"{VALID_MSG}   ({format_cpf(raw)})")
        else:
            print(INVALID_MSG)


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    _run_cli(arg)
