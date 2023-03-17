from flask_restful import  Resource,reqparse
from flask import jsonify

from wscrape import plantFinder


wscrape_get_args=reqparse.RequestParser()
wscrape_get_args.add_argument("leaf_name",type=str,help="Leaf name is required",required=True)



class Name(Resource):
    def get(self):
        args = wscrape_get_args.parse_args()
        leaf_name = args['leaf_name']
        res = plantFinder(leaf_name)
        output = {"common_name":res}
        return jsonify(output)