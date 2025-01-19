import os

class Interface:
    def __init__(self, inventory):
        self.inventory = inventory

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def pause(self):
        input("\nPressione Enter para continuar...")

    def display_menu(self):
        self.clear_screen()
        print("\n********** Bem-vindo à AgilStore! **********")
        print("Escolha uma opção:")
        print("1 - Listar produtos")
        print("2 - Adicionar produto")
        print("3 - Atualizar produto")
        print("4 - Excluir produto")
        print("5 - Buscar produto")
        print("6 - Sair")
        print("***************************************")

    def get_user_choice(self):
        while True:
            try:
                choice = int(input("\nEscolha uma opção: "))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Opção inválida. Por favor, escolha entre 1 e 6.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

    def list_products(self):
        self.clear_screen()
        print("\nEscolha o critério de ordenação:")
        print("1 - Nome")
        print("2 - Quantidade")
        print("3 - Preço")
        sort_option = input("Digite o número correspondente (deixe em branco para não ordenar): ").strip()

        sort_by = None
        if sort_option == "1":
            sort_by = "name"
        elif sort_option == "2":
            sort_by = "quantity"
        elif sort_option == "3":
            sort_by = "price"
        self.clear_screen()
        self.inventory.list_products(sort_by)
        self.pause()

    def add_product(self):
        self.clear_screen()
        print("\n********** Adicionar Produto **********")
        name = input("Digite o nome do produto: ")
        category = input("Digite a categoria do produto: ")
        quantity = int(input("Digite a quantidade em estoque: "))
        price = float(input("Digite o preço do produto: "))
        self.inventory.add_product(name, category, quantity, price)
        self.pause()

    def update_product(self):
        self.clear_screen()
        print("\n********** Atualizar Produto **********")
        product_id = input("Digite o ID do produto a ser atualizado: ")
        name = input("Novo nome (deixe em branco para não alterar): ")
        category = input("Nova categoria (deixe em branco para não alterar): ")
        quantity = input("Nova quantidade (deixe em branco para não alterar): ")
        price = input("Novo preço (deixe em branco para não alterar): ")

        quantity = int(quantity) if quantity else None
        price = float(price) if price else None
        
        self.inventory.update_product(product_id, name, category, quantity, price)
        self.pause()

    def delete_product(self):
        self.clear_screen()
        print("\n********** Excluir Produto **********")
        product_id = input("Digite o ID do produto a ser excluído: ")
        self.inventory.delete_product(product_id)
        self.pause()

    def search_product(self):
        self.clear_screen()
        print("\n********** Escolha uma opção de busca **********")
        print("1 - Buscar por ID")
        print("2 - Buscar por Nome")
        choice = input("Escolha a opção (1 ou 2): ").strip()

        if choice == '1':
            self.clear_screen()
            product_id = input("Digite o ID do produto: ").strip()
            product = self.inventory.find_product_by_id(product_id)
            self.pause()
            if product:
                return product
            else:
                self.clear_screen
                print(f"Produto com ID {product_id} não encontrado.")
                self.pause()
        
        elif choice == '2':
            self.clear_screen()
            search_term = input("Digite parte do nome do produto: ").strip()
            results = self.inventory.find_product_by_name(search_term)
            self.clear_screen()
            if results:
                print(f"\n{'ID':<36} | {'Nome':<20} | {'Categoria':<15} | {'Quantidade':<10} | {'Preço':>10}")
                print("-" * 85)
                for product in results:
                    print(product.display_products())
            else:
                print("Nenhum produto encontrado com esse nome.")
        
        else:
            print("Opção inválida. Tente novamente.")
        
        self.pause()

    def run(self):
        while True:
            self.display_menu()
            user_choice = self.get_user_choice()

            if user_choice == 1:
                self.list_products()
            elif user_choice == 2:
                self.add_product()
            elif user_choice == 3:
                self.update_product()
            elif user_choice == 4:
                self.delete_product()
            elif user_choice == 5:
                self.search_product()
            elif user_choice == 6:
                print("Saindo da AgilStore. Até logo!")
                break
