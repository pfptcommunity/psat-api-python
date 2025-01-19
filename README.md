# Proofpoint Security Awareness Training API Package
[![PyPI Downloads](https://static.pepy.tech/badge/psat-api)](https://pepy.tech/projects/psat-api). 
Library implements all of the functions of the PSAT API via Python.

### Requirements:

* Python 3.9+
* requests
* pysocks

### Installing the Package

You can install the API library using the following command directly from Github.

```
pip install git+https://github.com/pfptcommunity/psat-api-python.git
```

or can install the API library using pip.

```
pip install psat-api
```

### PSAT API Versions

Selecting the version of the PSAT API is done at time of import.

Proofpoint notified they will be ending support of the v0.1.0 endpoints on September 30, 2023. Support also confirmed
v0.2.0 was never meant to be a public release. In version 3.1.0 and higher of this library, v0.1.0 and v0.2.0 have been
removed accordingly.

```python
# Version v0.3.0 
from psat_api.v3 import *
```

### Creating an API client object

```python
from psat_api.v3 import *

if __name__ == '__main__':
    client = Client(Region.US, "<enter_your_api_key_here>")
```

### Querying CyberStrength Reports

```python
from psat_api.v3 import *

if __name__ == '__main__':
    client = Client(Region.US, "<enter_your_api_key_here>")

    cs_page = client.reports.cyberstrength()
    for data in cs_page:
        print("Page Size: {}".format(cs_page.page_size))
        print("Current Page Number: {}".format(cs_page.current_page_number))
        print("Last Page Number: {}".format(cs_page.last_page_number))
        print("Total Records: {}".format(cs_page.record_count))
        print("Link Self: {}".format(cs_page.self))
        print("Link First: {}".format(cs_page.first))
        print("Link Last: {}".format(cs_page.last))
        print("Link Next: {}".format(cs_page.next))
        print("Status: {}".format(cs_page.status))
        print("Reason: {}".format(cs_page.reason))
        for page_row in data:
            print(page_row)
```

### Querying Enrollments Reports

```python
from psat_api.v3 import *

if __name__ == '__main__':
    client = Client(Region.US, "<enter_your_api_key_here>")

    en_page = client.reports.enrollments()
    # ef = EnrollmentsFilter()
    for data in en_page:
        print("Page Size: {}".format(en_page.page_size))
        print("Current Page Number: {}".format(en_page.current_page_number))
        print("Last Page Number: {}".format(en_page.last_page_number))
        print("Total Records: {}".format(en_page.record_count))
        print("Link Self: {}".format(en_page.self))
        print("Link First: {}".format(en_page.first))
        print("Link Last: {}".format(en_page.last))
        print("Link Next: {}".format(en_page.next))
        print("Status: {}".format(en_page.status))
        print("Reason: {}".format(en_page.reason))
        for page_row in data:
            print(page_row)
```

### Querying Phishing Reports

```python
from psat_api.v3 import *

if __name__ == '__main__':
    client = Client(Region.US, "<enter_your_api_key_here>")

    ph_page = client.reports.phishing()
    for data in ph_page:
        print("Page Size: {}".format(ph_page.page_size))
        print("Current Page Number: {}".format(ph_page.current_page_number))
        print("Last Page Number: {}".format(ph_page.last_page_number))
        print("Total Records: {}".format(ph_page.record_count))
        print("Link Self: {}".format(ph_page.self))
        print("Link First: {}".format(ph_page.first))
        print("Link Last: {}".format(ph_page.last))
        print("Link Next: {}".format(ph_page.next))
        print("Status: {}".format(ph_page.status))
        print("Reason: {}".format(ph_page.reason))
        for page_row in data:
            print(page_row)
```

### Querying Phishing Extended Reports

These phishing exteneded was added in v0.3.0

```python
from psat_api.v3 import *

if __name__ == '__main__':
    client = Client(Region.US, "<enter_your_api_key_here>")

    pe_page = client.reports.phishing_extended()
    for data in pe_page:
        print("Page Size: {}".format(pe_page.page_size))
        print("Current Page Number: {}".format(pe_page.current_page_number))
        print("Last Page Number: {}".format(pe_page.last_page_number))
        print("Total Records: {}".format(pe_page.record_count))
        print("Link Self: {}".format(pe_page.self))
        print("Link First: {}".format(pe_page.first))
        print("Link Last: {}".format(pe_page.last))
        print("Link Next: {}".format(pe_page.next))
        print("Status: {}".format(pe_page.status))
        print("Reason: {}".format(pe_page.reason))
        for page_row in data:
            print(page_row)
```

### Querying Phish Alarm Reports

```python
from psat_api.v3 import *

if __name__ == '__main__':
    client = Client(Region.US, "<enter_your_api_key_here>")

    pa_page = client.reports.phishalarm()
    for data in pa_page:
        print("Page Size: {}".format(pa_page.page_size))
        print("Current Page Number: {}".format(pa_page.current_page_number))
        print("Last Page Number: {}".format(pa_page.last_page_number))
        print("Total Records: {}".format(pa_page.record_count))
        print("Link Self: {}".format(pa_page.self))
        print("Link First: {}".format(pa_page.first))
        print("Link Last: {}".format(pa_page.last))
        print("Link Next: {}".format(pa_page.next))
        print("Status: {}".format(pa_page.status))
        print("Reason: {}".format(pa_page.reason))
        for page_row in data:
            print(page_row)
```

### Querying Training Reports

```python
from psat_api.v3 import *

if __name__ == '__main__':
    client = Client(Region.US, "<enter_your_api_key_here>")

    tr_page = client.reports.training()
    for data in tr_page:
        print("Page Size: {}".format(tr_page.page_size))
        print("Current Page Number: {}".format(tr_page.current_page_number))
        print("Last Page Number: {}".format(tr_page.last_page_number))
        print("Total Records: {}".format(tr_page.record_count))
        print("Link Self: {}".format(tr_page.self))
        print("Link First: {}".format(tr_page.first))
        print("Link Last: {}".format(tr_page.last))
        print("Link Next: {}".format(tr_page.next))
        print("Status: {}".format(tr_page.status))
        print("Reason: {}".format(tr_page.reason))
        for page_row in data:
            print(page_row)
```

### Querying User Reports

```python
from psat_api.v3 import *

if __name__ == '__main__':
    client = Client(Region.US, "<enter_your_api_key_here>")

    us_page = client.reports.users()
    for data in us_page:
        print("Page Size: {}".format(us_page.page_size))
        print("Current Page Number: {}".format(us_page.current_page_number))
        print("Last Page Number: {}".format(us_page.last_page_number))
        print("Total Records: {}".format(us_page.record_count))
        print("Link Self: {}".format(us_page.self))
        print("Link First: {}".format(us_page.first))
        print("Link Last: {}".format(us_page.last))
        print("Link Next: {}".format(us_page.next))
        print("Status: {}".format(us_page.status))
        print("Reason: {}".format(us_page.reason))
        for page_row in data:
            print(page_row)
```

### Page Size and Pagination

```python
from psat_api.v3 import *

if __name__ == '__main__':
    client = Client(Region.US, "<enter_your_api_key_here>")

    # Create a filter object
    filter = PhishingFilter()

    # Starting page number
    filter.page_number = 1
    # Number of records per page
    filter.page_size = 1000

    # Get the phishing records but apply the filter
    ph_page = client.reports.phishing(filter)

    # This will request all pages of data
    for page_data in ph_page:
        # You can display the page information, this data is updated for every page of data
        print("Page Size: {}".format(ph_page.page_size))
        print("Current Page Number: {}".format(ph_page.current_page_number))
        print("Last Page Number: {}".format(ph_page.last_page_number))
        print("Total Records: {}".format(ph_page.record_count))
        print("Link Self: {}".format(ph_page.self))
        print("Link First: {}".format(ph_page.first))
        print("Link Last: {}".format(ph_page.last))
        print("Link Next: {}".format(ph_page.next))
        print("Status: {}".format(ph_page.status))
        print("Reason: {}".format(ph_page.reason))
        # Print all of the page data
        for row in page_data:
            print(row)
```

### Filtering Options

Every report type has it's own set of filters which can be applied.

```python
from psat_api.v3 import *

if __name__ == '__main__':
    client = Client(Region.US, "<enter_your_api_key_here>")

    # Create a filter object
    cyberstrength_filter = CyberStrengthFilter()
    enrollments_filter = EnrollmentsFilter()
    phishalarm_filter = PhishAlarmFilter()
    phishing_filter = PhishingFilter()
    phishingext_filter = PhishingExtendedFilter()
    training_filter = TrainingFilter()
    users_filter = UsersFilter()

    # Get the phishing records and apply the filter
    cs_page = client.reports.cyberstrength(cyberstrength_filter)
    en_page = client.reports.enrollments(enrollments_filter)
    pa_page = client.reports.phishalarm(phishalarm_filter)
    ph_page = client.reports.phishing(phishing_filter)
    pe_page = client.reports.phishing_extended(phishingext_filter)
    tr_page = client.reports.training(training_filter)
    us_page = client.reports.users(users_filter)
```

### Custom Filter Types

Some filter methods such as Training and Enrollments take defined types

```python
from psat_api.v3 import *
from psat_api.common.AssignmentStatus import AssignmentStatus
from psat_api.common.EnrollmentStatus import EnrollmentStatus

enrollments_filter = EnrollmentsFilter()
enrollments_filter.set_stats([EnrollmentStatus.COMPLETED, EnrollmentStatus.IN_PROGRESS])

training_filter = TrainingFilter()
training_filter.set_user_assignment_stats([AssignmentStatus.COMPLETED, AssignmentStatus.IN_PROGRESS])
```

### Proxy Support

Socks5 Proxy Example:

```python
from psat_api.v3 import *

if __name__ == '__main__':
    client = Client(Region.US, "<enter_your_api_key_here>")
    credentials = "{}:{}@".format("proxyuser", "proxypass")
    client.session.proxies = {'https': "{}://{}{}:{}".format('socks5', credentials, '<your_proxy>', '8128')}
```

HTTP Proxy Example (Squid):

```python
from psat_api.v3 import *

if __name__ == '__main__':
    client = Client(Region.US, "<enter_your_api_key_here>")
    credentials = "{}:{}@".format("proxyuser", "proxypass")
    client.session.proxies = {'https': "{}://{}{}:{}".format('http', credentials, '<your_proxy>', '3128')}

```

### HTTP Timeout Settings

```python
from psat_api.v3 import *

if __name__ == '__main__':
    client = Client(Region.US, "<enter_your_api_key_here>")
    # Timeout in seconds, connect timeout
    client.timeout = 600
    # Timeout advanced, connect / read timeout
    client.timeout = (3.05, 27)
```

### Limitations

There are currently no known limitations.

For more information please
see: https://proofpoint.securityeducation.com/api/reporting/documentation/#api-Introduction-Introduction
