from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    addr = db.Column(db.String(80), nullable=False)

db_created = False

@app.before_request
def create_tables():
    global db_created
    if not db_created:
        db.create_all()
        if not Product.query.first():
            db.session.add(Product(name='Baseball', price=100.0, addr=''))
            db.session.add(Product(name='Richard Stallman', price=200.0,addr=''))
            db.session.add(Product(name='LGBTQ+ pride flag', price=300.0,addr=''))
            db.session.add(Product(name='Iphone 3k', price=400.0,addr=''))
            db.session.add(Product(name='Omnitrix', price=500.0,addr=''))
            db.session.add(Product(name='Rasengan', price=600.0,addr=''))
        db.session.commit()
        db_created = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/order/<int:product_id>', methods=['GET', 'POST'])
def order(product_id):
    product = Product.query.get_or_404(product_id)
    
    if request.method == 'POST':
        address = request.form['address']
        print(address)
        query = text(f"UPDATE product SET addr = '{address}' WHERE id = {product_id}")
        try:
            db.session.execute(query)
            db.session.commit()
        except:
            pass

        return redirect(url_for('products'))

    return render_template('order.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
