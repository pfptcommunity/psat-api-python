from requests import Response


class ErrorHandler:
    __raise_for_status: bool

    def __init__(self, raise_for_status: bool):
        self.__raise_for_status = raise_for_status

    def handler(self, response: Response, **kwargs) -> Response:
        if response.status_code == 401:
            response.reason = "Authorization Error, Missing Authorization Header, or Expired Token"
        elif response.status_code == 402:
            response.reason = "API Budget Empty"
        elif response.status_code == 403:
            response.reason = "User is not authorized to access this resource with an explicit deny"
        elif response.status_code == 422:
            response.reason = "Invalid Token, Token Decode Error, Invalid Header"
        elif response.status_code == 500:
            response.reason = "Database Error, Internal Server Error"

        if self.__raise_for_status:
            response.raise_for_status()

        return response
