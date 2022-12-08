from psat_api.web.Resource import Resource
from psat_api.reports.Phishing import Phishing
from psat_api.reports.CyberStrength import CyberStrength
from psat_api.reports.PhishAlarm import PhishAlarm
from psat_api.reports.Training import Training
from psat_api.reports.Users import Users
from psat_api.reports.Enrollments import Enrollments


class Reports(Resource):
    __phishing = Phishing
    __cyberstrength = CyberStrength
    __phishalarm = PhishAlarm
    __training = Training
    __users = Users
    __enrollments = Enrollments

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)
        self.__phishing = Phishing(self, "phishing")
        self.__cyberstrength = CyberStrength(self, "cyberstrength")
        self.__phishalarm = CyberStrength(self, "phishalarm")
        self.__training = Training(self, "training")
        self.__users = Training(self, "users")
        self.__enrollments = Training(self, "trainingenrollments")

    @property
    def phishing(self):
        return self.__phishing

    @property
    def cyberstrength(self):
        return self.__cyberstrength

    @property
    def phishalarm(self):
        return self.__phishalarm

    @property
    def training(self):
        return self.__training

    @property
    def users(self):
        return self.__users

    @property
    def enrollments(self):
        return self.__enrollments
