from datetime import datetime
from config import db, ma

class Avocado(db.Model):
    __tablename__ = 'avocado'
    avocado_id = db.Column(db.Integer, primary_key=True, index=True)
    avgprice = db.Column(db.REAL)
    totalvol = db.Column(db.Integer)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.REAL)
    avo_c = db.Column(db.REAL)
    regionid = db.Column(db.Integer)
    type = db.Column(db.Integer)
    date = db.Column(db.Date, default=datetime.utcnow, onupdate=datetime.utcnow)

class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Avocado
        sqla_session = db.session
        load_instance = True