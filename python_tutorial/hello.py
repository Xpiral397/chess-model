import math

def parity_energy_cascade_signature(sequence, right):
    signature = []
    if not isinstance(sequence, list) or not isinstance(right, int):
        raise ValueError("Input must be a list of integers and an integer threshold")

    system_key = (right // 2) % 2

    for num in sequence:
        if not isinstance(num, int):
            continue
        if num % 2 == system_key:
            base = num if num > 10 else 0.5
            signature.append(base)
            dy, dx = 1.0, 1.0
            for r in range(num):
                try:
                    dy = r / (num * math.sqrt(base * dx)) if base * dx != 0 else 0
                    dx = dy / 2 if dy != 0 else 0
                    signature.append(dy ** 2)
                    signature.append(math.sqrt(abs(dx)))
                except (ZeroDivisionError, ValueError):
                    continue
    return signature

print(parity_energy_cascade_signature([5, 13, 20, 8, 7], 6))
