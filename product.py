import random
import string


class Product:
    def __init__(self, name, category, quantity, price, id=None):
        self.id = id if id else self.generate_id()  # Gera um ID se não for passado
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def generate_id(self):
        return "".join(random.choices(string.ascii_letters + string.digits, k=4))

    def __str__(self):
        return f"Produto: {self.name}, ID: {self.id}, Preço: ${self.price}, Quantidade: {self.quantity}, Categoria: {self.category}"

    def display_products(self):
        return f"{self.id:<36} | {self.name:<20} | {self.category:<15} | {self.quantity:<10} | {self.price:>10.2f}"
    

    def display_product_details(self):
        return (
            f"\nProduto Detalhado\n"
            f"{'ID:':<15} {self.id}\n"
            f"{'Nome:':<15} {self.name}\n"
            f"{'Categoria:':<15} {self.category}\n"
            f"{'Quantidade:':<15} {self.quantity}\n"
            f"{'Preço:':<15} ${self.price:,.2f}\n"
            f"{'-' * 50}"
        )
    