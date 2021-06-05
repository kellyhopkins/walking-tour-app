from flask_restful import Resource, reqparse
from models.location import LocationModel


class Location(Resource):
    def get(self, id):
        loc = LocationModel.find_by_id(id)
        if loc:
            return loc.json()
        
        return {'message': 'location not found'}, 404

class LocationList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('loc_name',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('loc_address',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('loc_description',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('loc_category',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )

    def get(self):
        return {'locations': list(map(lambda x: x.json(), LocationModel.query.all()))}
    
    def post(self):
        data = LocationList.parser.parse_args()
        # location = LocationModel(data["loc_name"], data["loc_address"], data["loc_description"], data["loc_category"])
        location = LocationModel(**data)
        location.save_to_db()
        return {"message": "location added successfully"}
