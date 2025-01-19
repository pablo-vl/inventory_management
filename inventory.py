import json
from product import Product


class Inventory:
    def __init__(self):
        self.products = self.load_products()

    def load_products(self):
        try:
            with open("data/inventory.json", "r") as file:
                data = json.load(file)
                return [
                    Product(
                        product_data["name"],
                        product_data["category"],
                        product_data["quantity"],
                        product_data["price"],
                        id=product_data["id"]
                    )
                    for product_data in data    
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_products(self):
        with open("data/inventory.json", "w") as file:
            json.dump([product.__dict__ for product in self.products], file, indent=4)

    def add_product(self, name, category, quantity, price):
        if not self.is_valid_product_data(name, category, quantity, price):
            print("Dados inválidos, produto não adicionado.")
            return

        new_product = Product(name, category, quantity, price)
        self.add_product_to_inventory(new_product)
        print(f"O produto: '{name}' foi adicionado com sucesso!")

    def add_product_to_inventory(self, product):
        self.products.append(product)
        self.save_products()

    def is_valid_product_data(self, name, category, quantity, price):
        validations_and_messages = [
            (name, "O nome é obrigatório."),
            (category, "A categoria é obrigatória."),
            (
                isinstance(quantity, int) and quantity >= 0,
                "A quantidade deve ser um número inteiro não negativo.",
            ),
            (
                isinstance(price, (int, float)) and price >= 0,
                "O preço deve ser um número não negativo.",
            ),
        ]

        for condition, message in validations_and_messages:
            if not condition:
                print(message)
                return False

        return True

    def list_products(self, sort_by=None):
        print(
            f"{'ID':<36} | {'Nome':<20} | {'Categoria':<15} | {'Quantidade':<10} | {'Preço':>10}"
        )
        print("-" * 85)

        filtered_products = self.products

        if sort_by:
            filtered_products = sorted(
                filtered_products, key=lambda product: getattr(product, sort_by)
            )

        for product in filtered_products:
            print(product.display_products())

        if not filtered_products:
            print("Nenhum produto encontrado.")

    def update_product(
        self, product_id, name=None, category=None, quantity=None, price=None
    ):
        product = self.find_product_by_id(product_id)
        if not product:
            print(f"Produto com ID {product_id} não encontrado.")
            return

        if name:
            product.name = name
        if category:
            product.category = category
        if quantity is not None:
            product.quantity = quantity
        if price is not None:
            product.price = price

        self.save_products()
        print(f"Produto '{product_id}' atualizado com sucesso!")

    def delete_product(self, product_id):
        product = self.find_product_by_id(product_id)
        if not product:
            print(f"Produto com ID {product_id} não encontrado.")
            return

        confirm = input(
            f"Tem certeza de que deseja excluir o produto '{product_id}'? (s/n): "
        )
        if confirm.lower() == "s":
            self.products.remove(product)
            self.save_products()
            print(f"Produto '{product_id}' excluído com sucesso!")
        else:
            print("Exclusão do produto cancelada.")

    def find_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                print(product.display_product_details())
                return product
        print("Produto não encontrado.")
        return None
    
    def find_product_by_name(self, name):
        found_products = [
            product for product in self.products if name.lower() in product.name.lower()
        ]

        if found_products:
            print("\nProdutos Encontrados:")
            for product in found_products:
                print(product.display_product_details())
            return found_products
        else:
            print("Nenhum produto encontrado com esse nome.")
            return []
