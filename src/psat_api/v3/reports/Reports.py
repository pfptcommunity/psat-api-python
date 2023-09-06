"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat-api
License: MIT
"""

from psat_api.web import Resource
from . import *


class Reports(Resource):
    __phishing = Phishing
    __phishing_extended = PhishingExtended
    __cyberstrength = CyberStrength
    __phishalarm = PhishAlarm
    __training = Training
    __users = Users
    __enrollments = Enrollments

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)
        self.__phishing = Phishing(self, "phishing")
        self.__phishing_extended = PhishingExtended(self, "phishing_extended")
        self.__cyberstrength = CyberStrength(self, "cyberstrength")
        self.__phishalarm = PhishAlarm(self, "phishalarm")
        self.__training = Training(self, "training")
        self.__users = Users(self, "users")
        self.__enrollments = Enrollments(self, "trainingenrollments")

    @property
    def phishing(self):
        return self.__phishing

    @property
    def phishing_extended(self):
        return self.__phishing_extended

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
