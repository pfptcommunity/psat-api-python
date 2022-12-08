from psat_api import Client, Version, Region
from psat_api.reports.Phishing import FilterOptions as PFO
from psat_api.reports.CyberStrength import FilterOptions as SSFO

if __name__ == '__main__':
    api_key_file = open("psat.api_key", "r")
    api_key = api_key_file.read()
    client = Client(Region.US, Version.V1, api_key)

    print(client.reports.cyberstrength.uri)
    print(client.reports.phishalarm.uri)
    print(client.reports.phishing.uri)
    print(client.reports.training.uri)
    print(client.reports.users.uri)
    print(client.reports.enrollments.uri)

    pfo = PFO()
    pfo.set_page_number(1)
    pfo.set_page_size(1000)
    # .set_event_start_date(datetime.datetime.now() - datetime.timedelta(days=1))
    # .set_event_end_date(datetime.datetime.now())
    #pfo.add_campaign_name("APACBaselineNov2022Group1")
    # .set_campaign_start_date(datetime.datetime(2022, 11, 6))
    # .set_campaign_end_date(datetime.date.today())
    # .set_include_no_action(False)
    # .set_include_archived_campaigns(False)
    # .set_include_deleted_users(False)
    # .set_filter_user_tag("custom", "tag")
    # .add_user_mail_address("pgoud@blueplanet.com")

    for page in client.reports.phishing.query(pfo):
        for entry in page:
            print("{} {} - {}".format(entry['attributes']['userfirstname'], entry['attributes']['userlastname'], entry['attributes']['campaignstatus']))
            #print(entry)

    csfo = SSFO()
    csfo.set_page_number(1)
    csfo.set_page_size(1000)
    csfo.add_assignment_name("BoogieWoogie").add_assignment_name("BoogieWoogie2")
    csfo.add_assessment_type("AssessWoogie").add_assessment_type("AssessWoogie2")
    print(csfo)

    #for page in client.reporting.phishing.query(csfo):
    #    for entry in page:
    #        #print("{} {} - {}".format(entry['attributes']['userfirstname'], entry['attributes']['userlastname'], entry['attributes']['campaignstatus']))
    #        print(entry)