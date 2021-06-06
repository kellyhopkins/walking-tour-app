from db import db

class LocationModel(db.Model):
    __tablename__ = "locations"

    _id = db.Column(db.Integer, primary_key=True)
    loc_name = db.Column(db.String(80))
    loc_address = db.Column(db.String(80))
    loc_description = db.Column(db.Text)
    loc_category = db.Column(db.String(80))

    def __init__(self, loc_name, loc_address, loc_description, loc_category):
        self.loc_name = loc_name
        self.loc_address = loc_address
        self.loc_description = loc_description
        self.loc_category = loc_category
    
    def json(self):
        return {
            "loc_id": self._id,
            "name": self.loc_name,
            "address": self.loc_address,
            "description": self.loc_description,
            "category": self.loc_category
        }
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(_id=id).first()
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(loc_name=name).first()