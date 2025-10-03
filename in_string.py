def check_vowels():
    # Código a implementar utilizando input.

    user = input("")

    vowels = "aeiou"

    for i in vowels:
        j = i in user.lower()
        print(f"Contiene {i}: {j}")

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`

check_vowels()