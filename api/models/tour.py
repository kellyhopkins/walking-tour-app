from db import db

class TourModel(db.Model):
    __tablename__ = "tours"

    _id = db.Column(db.Integer, primary_key=True)
    tour_name = db.Column(db.String(80))
    tour_location = db.Column(db.String(80))
    tour_num_stops = db.Column(db.Integer)

    stops = db.relationship('TourStop', lazy='dynamic')

    def __init__(self, tour_name, tour_location, tour_num_stops, stops):
        self.tour_name = tour_name
        self.tour_location = tour_location
        self.tour_num_stops = tour_num_stops
        self.stops = stops
    
    def json(self):
        return {
            "tour_name": self.tour_name,
            "tour_location": self.tour_location,
            "num_stops": self.tour_num_stops,
            "stops": self.stops.all()
        }
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(_id=id).first()
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(tour_name=name).first()


class TourStop(db.Model):
    __tablename__ = "tourstops"

    _id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations._id'))
    tour_id = db.Column(db.Integer, db.ForeignKey('tours._id'))
    stop_number = db.Column(db.Integer)

    location = db.relationship('LocationModel')
    tour = db.relationship('TourModel')

    def __init__(self, location_id, tour_id, stop_number):
        self.location_id = location_id
        self.tour_id = tour_id
        self.stop_number = stop_number
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()