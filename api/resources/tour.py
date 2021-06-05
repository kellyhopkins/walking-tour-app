from flask_restful import Resource, reqparse
from models.tour import TourModel, TourStop

class Tour(Resource):
    def get(self, name):
        tour = TourModel.find_by_name(name)
        if tour:
            return tour.json()
        return {"message": "Tour not found"}, 404
    

class TourList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('tour_name',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('tour_location',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('tour_num_stops',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )

    def post(self):
        data = TourList.parser.parse_args()
        tour = TourModel(**data)
        tour.save_to_db()
        return {"Message": "Tour added successfully"}
    
    def get(self):
        return {'tours': list(map(lambda x: x.json(), TourModel.query.all()))}