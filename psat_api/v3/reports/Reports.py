"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: psat_api
Version: 0.1.1
License: MIT
"""
#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from psat_api.web.Resource import Resource
from psat_api.v3.reports.Phishing import Phishing
from psat_api.v3.reports.PhishingExtended import PhishingExtended
from psat_api.v3.reports.CyberStrength import CyberStrength
from psat_api.v3.reports.PhishAlarm import PhishAlarm
from psat_api.v3.reports.Training import Training
from psat_api.v3.reports.Users import Users
from psat_api.v3.reports.Enrollments import Enrollments


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
        self.__phishing_extended = Phishing(self, "phishing_extended")
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
