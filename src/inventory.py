class InventoryManager:
    """Mengelola data stok barang secara in-memory."""

    def __init__(self):
        self._items = {}

    def add_item(self, item_id: str, name: str, quantity: int, price: float) -> dict:
        if quantity < 0 or price < 0:
            raise ValueError("Kuantitas dan harga tidak boleh bernilai negatif.")
        self._items[item_id] = {
            "name": name.strip(),
            "quantity": quantity,
            "price": price,
        }
        return self._items[item_id]

    def update_stock(self, item_id: str, delta: int) -> int:
        if item_id not in self._items:
            raise KeyError(f"Barang dengan ID {item_id} tidak ditemukan.")
        new_qty = self._items[item_id]["quantity"] + delta
        if new_qty < 0:
            raise ValueError("Stok barang tidak mencukupi.")
        self._items[item_id]["quantity"] = new_qty
        return new_qty

    def get_total_valuation(self) -> float:
        return sum(
            item["quantity"] * item["price"] for item in self._items.values()
        )