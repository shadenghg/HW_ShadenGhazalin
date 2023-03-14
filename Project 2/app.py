from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt, check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'this_is_a_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = ['png', 'jpeg', 'jpg', 'gif', 'webp']

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), unique=False, nullable=False)
    lastName = db.Column(db.String(50), unique=False, nullable=False)
    Email = db.Column(db.String(50), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    user_role = db.Column(db.String(20), unique=False, nullable=False)
    is_active = db.Column(db.Boolean, unique=False, nullable=False)

    def get_id(self):
        return self.user_id

    def is_authenticated(self):
        return True


class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), unique=False, nullable=False)
    product_price = db.Column(db.Float, unique=False, nullable=False)
    product_quantity = db.Column(db.Integer, unique=False, nullable=False)
    product_description = db.Column(db.String, unique=False, nullable=False)
    filename = db.Column(db.String(100), unique=False, nullable=True)

    def __repr__(self):
        return f"{self.product_name}, price: {self.product_price}"


class Reviews(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=False, nullable=False)
    product_id = db.Column(db.Integer, unique=False, nullable=False)
    reviewer_name = db.Column(db.String(20), unique=False, nullable=False)
    review_text = db.Column(db.String, unique=False, nullable=False)
    review_rate = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"Name: {self.reviewer_name}, Content: {self.review_text}"


class cartList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)


migrate = Migrate(app, db)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/home", methods=["POST", "GET"])
@login_required
def homePage():
    return render_template("homepage.html", user=current_user)


@app.route('/logout', methods=["POST", "GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = Users.query.filter_by(Email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect('/home')
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = Users.query.filter_by(Email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = Users(Email=email, firstName=first_name, lastName=last_name, password=generate_password_hash(
                password1), user_role="Customer", is_active=True)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect('/home')
    return render_template("register.html", user=current_user)


@app.route("/about_us")
def about():
    return render_template("about.html")


@app.route("/products")
def products_data():
    product_data = Products.query.all()
    return render_template("products_info.html", product_data=product_data)


@app.route("/add_data")
def add_data():
    return render_template("add_product.html")


@app.route("/add", methods=["POST", "GET"])
def product_management():
    print(current_user.firstName)
    if request.method == "POST":
        product_name = request.form.get("product_name")
        product_price = request.form.get("product_price")
        product_quantity = request.form.get("product_quantity")
        product_description = request.form.get("product_description")
        file = request.files.get("filename")
        if allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        file_name = file.filename
        product_row = Products(product_name=product_name, product_price=product_price,
                               product_quantity=product_quantity, product_description=product_description,
                               filename=file_name)
        db.session.add(product_row)
        db.session.commit()
        return redirect("/")


@app.route("/display/<filename>")
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename))


@app.route('/product_info/<product_id>')
def product_info(product_id):
    product_specific = Products.query.get(product_id)
    reviews_specific = Reviews.query.filter(Reviews.product_id == product_id)
    return render_template("product_info.html", product_specific=product_specific, reviews_specific=reviews_specific)


@app.route("/add_review", methods=["POST"])
def review_management():
    if request.method == "POST":
        reviewer_name = request.form.get("reviewer_name")
        review_text = request.form.get("review_text")
        product_id = request.form.get("product_id")
        review_rate = request.form.get("review_rate")

        review_row = Reviews(reviewer_name=reviewer_name, review_text=review_text, product_id=product_id,
                             review_rate=review_rate)
        db.session.add(review_row)
        db.session.commit()
        return redirect("/product_info/<product_id>")


@app.route("/delete/<int:product_id>")
def erase(product_id):
    data = Products.query.get(product_id)
    filename = data.filename
    os.remove(f"{app.config['UPLOAD_FOLDER']}/{filename}")
    db.session.delete(data)
    reviews_specific = Reviews.query.filter(Reviews.product_id == product_id)
    for review in reviews_specific:
        db.session.delete(review)
    db.session.commit()
    return redirect("/")


@app.route("/alter_product/<int:product_id>", methods=["POST", "GET"])
def alter_product(product_id):
    if request.method == "POST":
        data = Products.query.get(product_id)
        product_name = request.form.get("product_name")
        product_price = request.form.get("product_price")
        product_quantity = request.form.get("product_quantity")
        product_description = request.form.get("product_description")
        file = request.files.get("filename")
        if allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        file_name = file.filename
        if request.form.get("product_name"):
            data.product_name = product_name
        if request.form.get("product_price"):
            data.product_price = product_price
        if request.form.get("product_quantity"):
            data.product_quantity = product_quantity
        if request.form.get("product_description"):
            data.product_description = product_description
        if request.files.get("filename"):
            data.filename = file_name
        db.session.commit()
        return redirect(url_for('product_info', product_id=product_id))
    else:
        return render_template("alter_product.html")


@app.route("/customers")
def reviews_data():
    reviews = Reviews.query.all()
    return render_template("customers_reviews.html", reviews=reviews)


@app.route('/cart/<int:product_id>')
def add_to_cartlist(product_id):
    products = cartList.query.all()
    _cartList = cartList(product_id=product_id)
    db.session.add(_cartList)
    db.session.commit()
    return redirect(url_for('product_info', product_id=product_id))


@app.route('/cartlist_view')
def display_cartlist():
    cart_id = []
    carts = cartList.query.all()
    for product in carts:
        cart_id.append(product.product_id)
    cart_id = list(set(cart_id))
    products_cart = []
    for _id in cart_id:
        products_cart.append(Products.query.get(_id))
    return render_template('cartList.html', products_cart=products_cart)


@app.route("/delete_product/<int:product_id>")
def erase_product(product_id):
    data = cartList.query.get(product_id)
    filename = data.filename
    os.remove(f"{app.config['UPLOAD_FOLDER']}/{filename}")
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('products_data'))


if __name__ == "__main__":
    app.run(debug=True)
