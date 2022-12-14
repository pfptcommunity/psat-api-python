from psat_api import *

if __name__ == '__main__':
    api_key_file = open("psat.api_key", "r")
    api_key = api_key_file.read()
    client = Client(Region.US, Version.V1, api_key)

    ss_page = client.reports.cyberstrength.get()
    for data in ss_page:
        for page_row in data:
            print(page_row)

        print("Page Size: {}".format(ss_page.get_page_size()))
        print("Current Page Number: {}".format(ss_page.get_current_page_number()))
        print("Last Page Number: {}".format(ss_page.get_last_page_number()))
        print("Total Records: {}".format(ss_page.get_record_count()))
        print("Link Self: {}".format(ss_page.get_self()))
        print("Link First: {}".format(ss_page.get_first()))
        print("Link Last: {}".format(ss_page.get_last()))
        print("Link Next: {}".format(ss_page.get_next()))

    en_page = client.reports.enrollments.get()
    for data in en_page:
        for page_row in data:
            print(page_row)
        print("Page Size: {}".format(en_page.get_page_size()))
        print("Current Page Number: {}".format(en_page.get_current_page_number()))
        print("Last Page Number: {}".format(en_page.get_last_page_number()))
        print("Total Records: {}".format(en_page.get_record_count()))
        print("Link Self: {}".format(en_page.get_self()))
        print("Link First: {}".format(en_page.get_first()))
        print("Link Last: {}".format(en_page.get_last()))
        print("Link Next: {}".format(en_page.get_next()))

    ph_page = client.reports.phishing.get()
    for data in ph_page:
        for page_row in data:
            print(page_row)
        print("Page Size: {}".format(ph_page.get_page_size()))
        print("Current Page Number: {}".format(ph_page.get_current_page_number()))
        print("Last Page Number: {}".format(ph_page.get_last_page_number()))
        print("Total Records: {}".format(ph_page.get_record_count()))
        print("Link Self: {}".format(ph_page.get_self()))
        print("Link First: {}".format(ph_page.get_first()))
        print("Link Last: {}".format(ph_page.get_last()))
        print("Link Next: {}".format(ph_page.get_next()))

    pa_page = client.reports.phishalarm.get()
    for data in pa_page:
        for page_row in data:
            print(page_row)
        print("Page Size: {}".format(pa_page.get_page_size()))
        print("Current Page Number: {}".format(pa_page.get_current_page_number()))
        print("Last Page Number: {}".format(pa_page.get_last_page_number()))
        print("Total Records: {}".format(pa_page.get_record_count()))
        print("Link Self: {}".format(pa_page.get_self()))
        print("Link First: {}".format(pa_page.get_first()))
        print("Link Last: {}".format(pa_page.get_last()))
        print("Link Next: {}".format(pa_page.get_next()))

    tr_page = client.reports.training.get()
    for data in tr_page:
        for page_row in data:
            print(page_row)
        print("Page Size: {}".format(tr_page.get_page_size()))
        print("Current Page Number: {}".format(tr_page.get_current_page_number()))
        print("Last Page Number: {}".format(tr_page.get_last_page_number()))
        print("Total Records: {}".format(tr_page.get_record_count()))
        print("Link Self: {}".format(tr_page.get_self()))
        print("Link First: {}".format(tr_page.get_first()))
        print("Link Last: {}".format(tr_page.get_last()))
        print("Link Next: {}".format(tr_page.get_next()))

    us_page = client.reports.users.get()
    for data in us_page:
        for page_row in data:
            print(page_row)
        print("Page Size: {}".format(us_page.get_page_size()))
        print("Current Page Number: {}".format(us_page.get_current_page_number()))
        print("Last Page Number: {}".format(us_page.get_last_page_number()))
        print("Total Records: {}".format(us_page.get_record_count()))
        print("Link Self: {}".format(us_page.get_self()))
        print("Link First: {}".format(us_page.get_first()))
        print("Link Last: {}".format(us_page.get_last()))
        print("Link Next: {}".format(us_page.get_next()))
