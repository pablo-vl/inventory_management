# 🌟 AgilStore Inventory Management System

The AgilStore Inventory Management System is a Python-based application crafted with Object-Oriented Programming (OOP) principles. It provides a seamless way to manage product inventories via a user-friendly command-line interface. The system is designed for customization and scalability, making it ideal for small to medium-sized businesses.

## ✨ Key Features

- 🧩 Object-Oriented Design: Modular and reusable structure using classes and methods.
- ➕ Add Products: Easily add new items with attributes such as name, category, quantity, and price.
- ✏️ Update Products: Modify product details efficiently.
- ❌ Delete Products: Securely remove products with confirmation.
- 🔍 Search Products: Search by product ID or partial name match.
- 📋 List Products: View all products, sorted by name, quantity, or price.
- 💾 Persistent Storage: Automatically save and retrieve data from a JSON file.
- 🎨 Customizable: Easily extend features or adapt the interface to specific business needs.
- 📂 Project Structure

.
├── data/
│   └── inventory.json      # JSON file for storing product data
├── product.py              # Product class definition
├── inventory.py            # Inventory management logic
├── interface.py            # Command-line interface
├── main.py                 # Application entry point
└── README.md               # Project documentation

## 🚀 Getting Started

Pre-requisites:
Python 3.6 or higher: Ensure Python is installed on your system.

### Installation
Clone the Repository:
git clone https://github.com/yourusername/agilstore.git
cd agilstore
Set Up Dependencies:
No external libraries are required. Just ensure your Python environment is set up.
Prepare the Data File:
Create the data directory if it doesn’t exist and initialize an empty inventory.json file:
mkdir data
echo "[]" > data/inventory.json

## 🎮 How to Use
Run the application from the command line:
python main.py

### Menu Options
1 - List Products: View all products with sorting options.
2 - Add Product: Add a new product to the inventory.
3 - Update Product: Modify an existing product’s details.
4 - Delete Product: Remove a product from the inventory.
5 - Search Product: Find products by ID or name.
6 - Exit: Close the application.

## 🛠️ Customization
The system is designed to be easily customizable:
Extend Functionality: Add new features such as category-based filters or advanced analytics.
Interface Enhancements: Replace the command-line interface with a graphical user interface (GUI) or web-based dashboard.
Integration: Connect to external databases or APIs for enhanced storage and functionality.

## 🧑‍💻 Code Overview
Object-Oriented Design Highlights
Encapsulation: Each class encapsulates specific responsibilities.
Modularity: Independent components for better readability and maintenance.
Reusability: Core logic is structured for seamless reuse.

## Key Components

*product.py*
Defines the Product class:
Attributes: id, name, category, quantity, price
Methods: generate_id, display_products, display_product_details

*inventory.py*
Implements the Inventory class:
Core Logic: Load, save, add, update, delete, and search products.
Validation: Ensures data integrity with input validation.

*interface.py*
Manages the command-line interface:
Menu Navigation: User-friendly menu and options.
Action Handling: Interacts with the Inventory class for operations.

*main.py*
Entry point of the application:
Initializes the Inventory and Interface classes.
Runs the main application loop.

# Start managing your inventory with ease and efficiency using AgilStore! 🎉
