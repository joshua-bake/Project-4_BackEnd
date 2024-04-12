from sqlalchemy.ext.hybrid import hybrid_property
from app import db, bcrypt


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=True)

    decks = db.relationship("DeckModel", backref="creator")
    collaborators = db.relationship("CollaboratorModel", backref="users")

    @hybrid_property
    def password(self):
        pass

    @password.setter
    def password(self, password_plaintext):
        print("here is the plain pw: ", password_plaintext)
        print("hashing password", self)
        encoded_hashed_pw = bcrypt.generate_password_hash(password_plaintext)
        self.password_hash = encoded_hashed_pw.decode("utf-8")

    def validate_password(self, login_password):
        return bcrypt.check_password_hash(self.password_hash, login_password)
