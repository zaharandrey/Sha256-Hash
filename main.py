import hashlib


def sha256_hash(message: str) -> str:
    """
    Хешує повідомлення за алгоритмом SHA-256.

    :param message: Рядок для хешування.
    :return: Хеш-значення у шістнадцятковому форматі.
    """
    # Конвертуємо повідомлення у байти
    message_bytes = message.encode('utf-8')

    # Виконуємо хешування
    hash_object = hashlib.sha256(message_bytes)

    # Повертаємо геш у шістнадцятковому форматі
    return hash_object.hexdigest()


# Приклад використання
if __name__ == "__main__":
    input_message = input("Введіть повідомлення для хешування: ")
    hash_result = sha256_hash(input_message)
    print(f"Хеш-значення: {hash_result}")

