# Proofpoint Security Awareness Training API Package

Library implements all of the functions of the Emerging Threats API via PHP.

### Requirements:

* Python 3.9+
* requests

### Getting Started
The following will dump all reports associated with your PSAT instance.
```python
from psat_api import *

if __name__ == '__main__':
    client = Client(Region.US, Version.V1, "<enter_your_api_key_here>")

    ss_page = client.reports.cyberstrength.get()
    for data in ss_page:
        for page_row in data:
            print(page_row)

    en_page = client.reports.enrollments.get()
    for data in en_page:
        for page_row in data:
            print(page_row)

    ph_page = client.reports.phishing.get()
    for data in ph_page:
        for page_row in data:
            print(page_row)

    pa_page = client.reports.phishalarm.get()
    for data in pa_page:
        for page_row in data:
            print(page_row)

    tr_page = client.reports.training.get()
    for data in tr_page:
        for page_row in data:
            print(page_row)

    us_page = client.reports.users.get()
    for data in us_page:
        for page_row in data:
            print(page_row)
```

### Page Size and Pagination

```python
from psat_api import *

if __name__ == '__main__':
    client = Client(Region.US, Version.V1, "<enter_your_api_key_here>")

    # Create a filter object
    filter = Phishing.FilterOptions()
    
    # Starting page number
    filter.set_page_number(1)
    # Number of records per page
    filter.set_page_size(1000)
    
    # Get the phishing records but apply the filter
    ph_page = client.reports.phishing.get(ph)
    
    # This will request all pages of data
    for page_data in ph_page:
        # Print all of the page data 
        for row in page_data:
            print(row)
        # You can display the page information, this data is updated for every page of data
        print("Page Size: {}".format(ph_page.get_page_size()))
        print("Current Page Number: {}".format(ph_page.get_current_page_number()))
        print("Last Page Number: {}".format(ph_page.get_last_page_number()))
        print("Total Records: {}".format(ph_page.get_record_count()))
        print("Link Self: {}".format(ph_page.get_self()))
        print("Link First: {}".format(ph_page.get_first()))
        print("Link Last: {}".format(ph_page.get_last()))
        print("Link Next: {}".format(ph_page.get_next()))
```

### Limitations
There are currently no known limitations. 

For more information please see: https://proofpoint.securityeducation.com/api/reporting/documentation/#api-Introduction-Introduction
