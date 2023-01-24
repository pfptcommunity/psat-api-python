from psat_api import *

if __name__ == '__main__':
    api_key_file = open("psat.api_key", "r")
    api_key = api_key_file.read()
    client = Client(Region.US, Version.V1, api_key)

    cs_page = client.reports.cyberstrength()
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

    en_page = client.reports.enrollments()
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


    ph_page = client.reports.phishing()
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

    pa_page = client.reports.phishalarm()
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

    tr_page = client.reports.training()
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

    us_page = client.reports.users()
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
