from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)


product_category = db.Table('product_category',
                                db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
                                db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
                                )


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('product', lazy=True))
    category = db.relationship("Category" , secondary=product_category)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)



