from psat_api.web.Resource import Resource


class Training(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)
