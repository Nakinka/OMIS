class ProductModel:
    def __init__(self):
        self.products = []  # Изначально таблица пуста

    def get_all_products(self):
        return self.products

    def add_product(self, kind, number, date):
        """Добавить новый продукт"""
        new_id = len(self.products) + 1
        self.products.append({"id": new_id, "kind": kind, "number": number, "date": date})

    def delete_product(self, product_id):
        """Удалить продукт по ID"""
