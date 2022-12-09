from psat_api import *

if __name__ == '__main__':
    api_key_file = open("psat.api_key", "r")
    api_key = api_key_file.read()
    client = Client(Region.US, Version.V1, api_key)

    ss = CyberStrength.FilterOptions()
    en = Enrollments.FilterOptions()
    ph = Phishing.FilterOptions()
    pa = PhishAlarm.FilterOptions()
    tr = Training.FilterOptions()
    us = Users.FilterOptions()

    for page in client.reports.cyberstrength.query():
        for entry in page:
            print(entry)

    for page in client.reports.enrollments.query():
        for entry in page:
            print(entry)

    for page in client.reports.phishing.query():
        for entry in page:
            print(entry)

    for page in client.reports.phishalarm.query():
        for entry in page:
            print(entry)

    for page in client.reports.training.query():
        for entry in page:
            print(entry)

    for page in client.reports.users.query():
        for entry in page:
            print(entry)
