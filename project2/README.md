This is the code for a Flask web application. The application has several routes, including "/", "/about_us", "/products", "/add_data", and "/product_info/int:product_id". The application uses a SQL database (SQLite) with SQLAlchemy and Flask-Migrate for database management. The "Products" and "Reviews" models are defined for the database, and the "cartList" model is also defined. The allowed file formats for image uploads are specified in the "ALLOWED_EXTENSIONS" list. The "/add" route allows the creation of new products in the database, and the "/add_review" route allows for adding reviews for the products.

Product Catalog
Product Catalog is a web application for managing products, reviews, and shopping carts. The application is built using Flask, SQLAlchemy and HTML.

Requirements
Before running the application, the following packages must be installed:

Features
Product Management: Add, view, and delete products.
Product Review: Add reviews for a specific product.
Shopping Cart: Add products to a shopping cart.
Screenshots
Homepage
Product Management
Product Information

Contributing
Fork the repository
Create your feature branch: git checkout -b feature/new-feature
Commit your changes: git commit -am 'Add some new feature'
Push to the branch: git push origin feature/new-feature
Submit a pull request.
License
This project is licensed under the MIT License. See LICENSE for details

Flask
Flask-SQLAlchemy
Flask-Migrate
Running the application
Clone the repository
shell
Copy code
$ git clone https://github.com/shadenghg/HW_ShadenGhazalin
Navigate to the project directory
shell
Copy code
$ cd product_catalog
Run the following command to start the application:
ruby
Copy code
$ python app.py
Open your web browser and navigate to http://localhost:5000/ to access the application.
Features
Product Management: Add, view, and delete products.
Product Review: Add reviews for a specific product.

Shopping Cart: Add products to a shopping cart.
Screenshots
Homepage
Product Management
Product Information

Contributing
Fork the repository
Create your feature branch: git checkout -b feature/new-feature
Commit your changes: git commit -am 'Add some new feature'
Push to the branch: git push origin feature/new-feature
Submit a pull request.
License
This project is licensed under the MIT License. See LICENSE for details.

