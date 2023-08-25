from psat_api.v3 import *
from psat_api.common import EnrollmentStatus, AssignmentStatus

if __name__ == '__main__':
    api_key_file = open("psat.api_key", "r")
    api_key = api_key_file.read()
    client = Client(Region.US, api_key, True)

    cyberstrength_filter = CyberStrengthFilter()
    cyberstrength_filter.set_page_size(5)
    cyberstrength_filter.set_page_number(1)
    cs_page = client.reports.cyberstrength(cyberstrength_filter)
    for data in cs_page:
        print("Page Size: {}".format(cs_page.get_page_size()))
        print("Current Page Number: {}".format(cs_page.get_current_page_number()))
        print("Last Page Number: {}".format(cs_page.get_last_page_number()))
        print("Total Records: {}".format(cs_page.get_record_count()))
        print("Link Self: {}".format(cs_page.get_self()))
        print("Link First: {}".format(cs_page.get_first()))
        print("Link Last: {}".format(cs_page.get_last()))
        print("Link Next: {}".format(cs_page.get_next()))
        print("Status: {}".format(cs_page.get_status()))
        print("Reason: {}".format(cs_page.get_reason()))
        for page_row in data:
            print(page_row)
        # Break after first page
        break

    enrollments_filter = EnrollmentsFilter()
    enrollments_filter.set_stats([EnrollmentStatus.COMPLETED, EnrollmentStatus.IN_PROGRESS])
    enrollments_filter.set_page_size(5)
    enrollments_filter.set_page_number(1)
    en_page = client.reports.enrollments(enrollments_filter)
    # ef = EnrollmentsFilter()
    for data in en_page:
        print("Page Size: {}".format(en_page.get_page_size()))
        print("Current Page Number: {}".format(en_page.get_current_page_number()))
        print("Last Page Number: {}".format(en_page.get_last_page_number()))
        print("Total Records: {}".format(en_page.get_record_count()))
        print("Link Self: {}".format(en_page.get_self()))
        print("Link First: {}".format(en_page.get_first()))
        print("Link Last: {}".format(en_page.get_last()))
        print("Link Next: {}".format(en_page.get_next()))
        print("Status: {}".format(en_page.get_status()))
        print("Reason: {}".format(en_page.get_reason()))
        for page_row in data:
            print(page_row)
        # Break after first page
        break

    phishing_filter = PhishingFilter()
    phishing_filter.set_page_size(5)
    phishing_filter.set_page_number(1)
    ph_page = client.reports.phishing(phishing_filter)
    for data in ph_page:
        print("Page Size: {}".format(ph_page.get_page_size()))
        print("Current Page Number: {}".format(ph_page.get_current_page_number()))
        print("Last Page Number: {}".format(ph_page.get_last_page_number()))
        print("Total Records: {}".format(ph_page.get_record_count()))
        print("Link Self: {}".format(ph_page.get_self()))
        print("Link First: {}".format(ph_page.get_first()))
        print("Link Last: {}".format(ph_page.get_last()))
        print("Link Next: {}".format(ph_page.get_next()))
        print("Status: {}".format(ph_page.get_status()))
        print("Reason: {}".format(ph_page.get_reason()))
        for page_row in data:
            print(page_row)
        # Break after first page
        break

    phishingext_filter = PhishingExtendedFilter()
    phishingext_filter.set_page_size(5)
    phishingext_filter.set_page_number(1)
    pe_page = client.reports.phishing_extended(phishingext_filter)
    for data in pe_page:
        print("Page Size: {}".format(pe_page.get_page_size()))
        print("Current Page Number: {}".format(pe_page.get_current_page_number()))
        print("Last Page Number: {}".format(pe_page.get_last_page_number()))
        print("Total Records: {}".format(pe_page.get_record_count()))
        print("Link Self: {}".format(pe_page.get_self()))
        print("Link First: {}".format(pe_page.get_first()))
        print("Link Last: {}".format(pe_page.get_last()))
        print("Link Next: {}".format(pe_page.get_next()))
        print("Status: {}".format(pe_page.get_status()))
        print("Reason: {}".format(pe_page.get_reason()))
        for page_row in data:
            print(page_row)
        # Break after first page
        break

    phishalarm_filter = PhishAlarmFilter()
    phishalarm_filter.set_page_size(5)
    phishalarm_filter.set_page_number(1)
    pa_page = client.reports.phishalarm(phishalarm_filter)
    for data in pa_page:
        print("Page Size: {}".format(pa_page.get_page_size()))
        print("Current Page Number: {}".format(pa_page.get_current_page_number()))
        print("Last Page Number: {}".format(pa_page.get_last_page_number()))
        print("Total Records: {}".format(pa_page.get_record_count()))
        print("Link Self: {}".format(pa_page.get_self()))
        print("Link First: {}".format(pa_page.get_first()))
        print("Link Last: {}".format(pa_page.get_last()))
        print("Link Next: {}".format(pa_page.get_next()))
        print("Status: {}".format(pa_page.get_status()))
        print("Reason: {}".format(pa_page.get_reason()))
        for page_row in data:
            print(page_row)
        # Break after first page
        break

    training_filter = TrainingFilter()
    training_filter.set_page_size(5)
    training_filter.set_page_number(1)
    training_filter.set_user_assignment_stats([AssignmentStatus.COMPLETED, AssignmentStatus.IN_PROGRESS])
    tr_page = client.reports.training(training_filter)
    for data in tr_page:
        print("Page Size: {}".format(tr_page.get_page_size()))
        print("Current Page Number: {}".format(tr_page.get_current_page_number()))
        print("Last Page Number: {}".format(tr_page.get_last_page_number()))
        print("Total Records: {}".format(tr_page.get_record_count()))
        print("Link Self: {}".format(tr_page.get_self()))
        print("Link First: {}".format(tr_page.get_first()))
        print("Link Last: {}".format(tr_page.get_last()))
        print("Link Next: {}".format(tr_page.get_next()))
        print("Status: {}".format(tr_page.get_status()))
        print("Reason: {}".format(tr_page.get_reason()))
        for page_row in data:
            print(page_row)
        # Break after first page
        break

    users_filter = UsersFilter()
    users_filter.set_page_size(5)
    users_filter.set_page_number(1)
    us_page = client.reports.users(users_filter)
    for data in us_page:
        print("Page Size: {}".format(us_page.get_page_size()))
        print("Current Page Number: {}".format(us_page.get_current_page_number()))
        print("Last Page Number: {}".format(us_page.get_last_page_number()))
        print("Total Records: {}".format(us_page.get_record_count()))
        print("Link Self: {}".format(us_page.get_self()))
        print("Link First: {}".format(us_page.get_first()))
        print("Link Last: {}".format(us_page.get_last()))
        print("Link Next: {}".format(us_page.get_next()))
        print("Status: {}".format(us_page.get_status()))
        print("Reason: {}".format(us_page.get_reason()))
        for page_row in data:
            print(page_row)
        # Break after first page
        break
