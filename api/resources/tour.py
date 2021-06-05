from flask_restful import Resource, reqparse
from models.tour import TourModel
from models.tourstop import TourStop

class Tour(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('location_id',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('tour_id',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('stop_number',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )

    def post(self, name):
        tour = TourModel.find_by_id(name)
        if tour:
            data = Tour.parser.parse_args()
            print(TourStop)
            stop = TourStop(**data)
            stop.save_to_db()
            return {"Message": "Tour stop added successfully"}
        
        return {"Message": "Tour does not exist, stop can't be added"}

    def get(self, name):
        tour = TourModel.find_by_id(name)
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
    
class TourStop(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('location_id',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('tour_id',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('stop_number',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )

    def post(self, tour_id):
        tour = TourModel.find_by_id(tour_id)
        if tour:
            data = TourStop.parser.parse_args()
            stop = TourStop(**data)
            stop.save_to_db()
            return {"Message": "Tour stop added successfully"}
        
        return {"Message": "Tour does not exist, stop can't be added"}