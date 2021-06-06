from db import db

class StopModel(db.Model):
    __tablename__ = "stops"

    _id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations._id'))
    tour_id = db.Column(db.Integer, db.ForeignKey('tours._id'))
    stop_number = db.Column(db.Integer)

    location = db.relationship('LocationModel', backref="StopModel", lazy="subquery")
    tour = db.relationship('TourModel')

    def __init__(self, location_id, tour_id, stop_number):
        self.location_id = location_id
        self.tour_id = tour_id
        self.stop_number = stop_number
    
    def json(self):
        return {
            "location_id": self.location_id,
            "tour_id": self.tour_id,
            "stop_number": self.stop_number,
            "location_information": self.location.json() #[x.json() for x in self.location]
        }
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()