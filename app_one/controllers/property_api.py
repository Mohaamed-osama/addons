import json
from urllib.parse import parse_qs
from odoo import http
from odoo.http import request


def invalid_response(error, status):
    response_body = {
        'error': error
    }
    return request.make_json_response(response_body, status=status)


def valid_response(data, status):
    response_body = {
        'message': "successful",
        'data': data
    }
    return request.make_json_response(response_body, status=status)


class PropertyApi(http.Controller):

    @http.route("/v1/property", methods=["POST"], type="http", auth="none", csrf=False)
    def post_property(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        if not vals.get('name'):
            return request.make_json_response({
                "message": "Name is required!",
            }, status=400)
        try:
            res = request.env['property'].sudo().create(vals)
            if res:
                return request.make_json_response({
                    "message": "Property has been created successfully",
                    "name": res.name,
                    "id": res.id,
                }, status=200)
        except Exception as error:
            return request.make_json_response({
                "message": error,
            }, status=400)

    @http.route("/v1/property/json", methods=["POST"], type="json", auth="none", csrf=False)
    def post_property_json(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        res = request.env['property'].sudo().create(vals)
        if res:
            return {
                "message": "Property has been created successfully"
            }

    @http.route("/v1/property/<int:property_id>", methods=["PUT"], type="http", auth="none", csrf=False)
    def put_property(self, property_id):
        try:
            property_id = request.env['property'].sudo().search([('id', '=', property_id)])
            if not property_id:
                return request.make_json_response({
                    "message": "ID does not exist",
                }, status=400)
            args = request.httprequest.data.decode()
            vals = json.loads(args)
            property_id.write(vals)
            return request.make_json_response({
                "message": "Property has been updated successfully",
                "name": property_id.name,
                "id": property_id.id,
            }, status=200)
        except Exception as error:
            return request.make_json_response({
                "message": error,
            }, status=400)

    @http.route("/v1/property/<int:property_id>", methods=["GET"], type="http", auth="none", csrf=False)
    def get_property(self, property_id):
        try:
            property_id = request.env['property'].sudo().search([('id', '=', property_id)])
            if not property_id:
                return invalid_response("ID does not exist", status=400)
            return valid_response({
                "name": property_id.name,
                "id": property_id.id,
                "ref": property_id.ref,
                "description": property_id.description,
                "bedrooms": property_id.bedrooms,
            }, status=200)
        except Exception as error:
            return request.make_json_response({
                "message": error,
            }, status=400)

    @http.route("/v1/property/<int:property_id>", methods=["DELETE"], type="http", auth="none", csrf=False)
    def delete_property(self, property_id):
        try:
            property_id = request.env['property'].sudo().search([('id', '=', property_id)])
            if not property_id:
                return request.make_json_response({
                    "message": "ID does not exist",
                }, status=400)
            property_id.unlink()
            return request.make_json_response({
                "message": "Property has been deleted successfully"
            }, status=200)
        except Exception as error:
            return request.make_json_response({
                "message": error,
            }, status=400)

    @http.route("/v1/properties", methods=["GET"], type="http", auth="none", csrf=False)
    def get_property_list(self):
        try:
            params = parse_qs(request.httprequest.query_string.decode('utf-8'))
            property_domain = []
            if params.get('state'):
                property_domain += [('state', '=', params.get('state')[0])]
            property_ids = request.env['property'].sudo().search(property_domain)
            if not property_ids:
                return request.make_json_response({
                    "message": "There are not records",
                }, status=400)
            return valid_response([{
                "name": property_id.name,
                "id": property_id.id,
                "ref": property_id.ref,
                "description": property_id.description,
                "bedrooms": property_id.bedrooms,
            }for property_id in property_ids], status=200)
        except Exception as error:
            return request.make_json_response({
                "message": error,
            }, status=400)
