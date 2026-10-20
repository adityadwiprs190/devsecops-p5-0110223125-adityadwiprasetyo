import re

def sanitize_input(text: str) -> str:
    """Membersihkan karakter berbahaya dari input string."""
    if not isinstance(text, str):
        raise TypeError("Input harus berupa string.")
    cleaned = re.sub(r"[<>\"';]", "", text)
    return cleaned.strip()

def calculate_discount(price: float, discount_percent: float) -> float:
    """Menghitung harga setelah diskon dengan validasi rentang."""
    if price < 0:
        raise ValueError("Harga tidak boleh negatif.")
    if not (0 <= discount_percent <= 100):
        raise ValueError("Persentase diskon harus antara 0 hingga 100.")
    return round(price * (1 - discount_percent / 100.0), 2)