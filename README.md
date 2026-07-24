# Proofpoint Security Awareness Training API Package

[![PyPI Downloads](https://static.pepy.tech/badge/psat-api)](https://pepy.tech/projects/psat-api)  
Library implements the Proofpoint ZenGuide Results API via Python.

### Requirements:

* Python 3.11+
* klarient
* requests

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
v0.2.0 was never meant to be a public release. This Klarient-based version of the library models the v0.3.0 REST API.

```python
# Version v0.3.0
from psat.v0_3_0 import PSATClient
```

### Creating an API client object

```python
from psat import Region
from psat.v0_3_0 import PSATClient

if __name__ == '__main__':
    client = PSATClient(Region.US, "<enter_your_api_key_here>")
```

### Endpoint Examples

Endpoint-focused examples are available under `examples/`.

```text
examples/
  cyberstrength.py
  enrollments.py
  phishalarm.py
  phishing.py
  phishing_extended.py
  training.py
  users.py
```

Copy `examples/settings.example.json` to `settings.json` at the project root and add your API token to run them
locally. The examples also accept `examples/settings.json` if you prefer to keep local example settings beside the
example files.

### Maintainer Smoke Tests

Release smoke tests live under `tools/live_smoke/`. They are separate from the user-facing examples and require live
PSAT API credentials.

See `tools/live_smoke/README.md`.

### Resource Paths

The API is modeled as a resource tree. Each resource exposes its path and URL, which can be useful when learning or
debugging the wrapper.

```python
from psat import Region
from psat.v0_3_0 import PSATClient

if __name__ == '__main__':
    client = PSATClient(Region.US, "<enter_your_api_key_here>")

    print(client.reports.path)
    # /api/reporting/v0.3.0

    print(client.reports.phishing.path)
    # /api/reporting/v0.3.0/phishing

    print(client.reports.phishing.url)
    # https://.../api/reporting/v0.3.0/phishing
```

### Modeled Report Resources

The v0.3.0 API is modeled under `client.reports`.

```text
client.reports.cyberstrength
client.reports.enrollments
client.reports.phishalarm
client.reports.phishing
client.reports.phishing_extended
client.reports.training
client.reports.users
```

Each report action returns `PagedResponse[RowType]`. Use `.page` when you want the first page object, `.data` when you
want the first page rows, iterate the result when you want page objects, or call `.items()` when you intentionally want
rows flattened across pages.

### Querying CyberStrength Reports

```python
from psat import Region
from psat.v0_3_0 import PSATClient

if __name__ == '__main__':
    client = PSATClient(Region.US, "<enter_your_api_key_here>")

    cs_page = client.reports.cyberstrength.retrieve().page
    print("Page Size: {}".format(cs_page.page_size))
    print("Current Page Number: {}".format(cs_page.current_page_number))
    print("Last Page Number: {}".format(cs_page.last_page_number))
    print("Total Records: {}".format(cs_page.record_count))
    print("Link Self: {}".format(cs_page.self_link))
    print("Link First: {}".format(cs_page.first_link))
    print("Link Last: {}".format(cs_page.last_link))
    print("Link Next: {}".format(cs_page.next_link))
    print("Status: {}".format(cs_page.status))
    print("Reason: {}".format(cs_page.reason))
    for page_row in cs_page.data:
        print(page_row.attributes.user_email_address)
        print(page_row.attributes.assignment_name)
        print(page_row.attributes.user_assignment_status)
```

### Querying Enrollments Reports

```python
from psat import Region
from psat.v0_3_0 import PSATClient

if __name__ == '__main__':
    client = PSATClient(Region.US, "<enter_your_api_key_here>")

    en_page = client.reports.enrollments.retrieve().page
    # ef = TrainingEnrollmentsFilter()
    print("Page Size: {}".format(en_page.page_size))
    print("Current Page Number: {}".format(en_page.current_page_number))
    print("Last Page Number: {}".format(en_page.last_page_number))
    print("Total Records: {}".format(en_page.record_count))
    print("Link Self: {}".format(en_page.self_link))
    print("Link First: {}".format(en_page.first_link))
    print("Link Last: {}".format(en_page.last_link))
    print("Link Next: {}".format(en_page.next_link))
    print("Status: {}".format(en_page.status))
    print("Reason: {}".format(en_page.reason))
    for page_row in en_page.data:
        print(page_row.attributes.user_email_address)
        print(page_row.attributes.assignment_name)
        print(page_row.attributes.module_name_user)
        print(page_row.attributes.module_attempt_status)
```

### Querying Phishing Reports

```python
from psat import Region
from psat.v0_3_0 import PSATClient

if __name__ == '__main__':
    client = PSATClient(Region.US, "<enter_your_api_key_here>")

    ph_page = client.reports.phishing.retrieve().page
    print("Page Size: {}".format(ph_page.page_size))
    print("Current Page Number: {}".format(ph_page.current_page_number))
    print("Last Page Number: {}".format(ph_page.last_page_number))
    print("Total Records: {}".format(ph_page.record_count))
    print("Link Self: {}".format(ph_page.self_link))
    print("Link First: {}".format(ph_page.first_link))
    print("Link Last: {}".format(ph_page.last_link))
    print("Link Next: {}".format(ph_page.next_link))
    print("Status: {}".format(ph_page.status))
    print("Reason: {}".format(ph_page.reason))
    for page_row in ph_page.data:
        print(page_row.attributes.user_email_address)
        print(page_row.attributes.campaign_name)
        print(page_row.attributes.event_type)
        print(page_row.attributes.template_subject)
```

### Querying Phishing Extended Reports

These phishing extended reports were added in v0.3.0.

```python
from psat import Region
from psat.v0_3_0 import PSATClient

if __name__ == '__main__':
    client = PSATClient(Region.US, "<enter_your_api_key_here>")

    pe_page = client.reports.phishing_extended.retrieve().page
    print("Page Size: {}".format(pe_page.page_size))
    print("Current Page Number: {}".format(pe_page.current_page_number))
    print("Last Page Number: {}".format(pe_page.last_page_number))
    print("Total Records: {}".format(pe_page.record_count))
    print("Link Self: {}".format(pe_page.self_link))
    print("Link First: {}".format(pe_page.first_link))
    print("Link Last: {}".format(pe_page.last_link))
    print("Link Next: {}".format(pe_page.next_link))
    print("Status: {}".format(pe_page.status))
    print("Reason: {}".format(pe_page.reason))
    for page_row in pe_page.data:
        print(page_row.attributes.user_email_address)
        print(page_row.attributes.campaign_name)
        print(page_row.attributes.ip_address)
        print(page_row.attributes.browser)
        print(page_row.attributes.user_agent)
```

### Querying Phish Alarm Reports

```python
from psat import Region
from psat.v0_3_0 import PSATClient

if __name__ == '__main__':
    client = PSATClient(Region.US, "<enter_your_api_key_here>")

    pa_page = client.reports.phishalarm.retrieve().page
    print("Page Size: {}".format(pa_page.page_size))
    print("Current Page Number: {}".format(pa_page.current_page_number))
    print("Last Page Number: {}".format(pa_page.last_page_number))
    print("Total Records: {}".format(pa_page.record_count))
    print("Link Self: {}".format(pa_page.self_link))
    print("Link First: {}".format(pa_page.first_link))
    print("Link Last: {}".format(pa_page.last_link))
    print("Link Next: {}".format(pa_page.next_link))
    print("Status: {}".format(pa_page.status))
    print("Reason: {}".format(pa_page.reason))
    for page_row in pa_page.data:
        print(page_row.attributes.user_email_address)
        print(page_row.attributes.campaign_name)
        print(page_row.attributes.action)
        print(page_row.attributes.reported_date)
```

### Querying Training Reports

```python
from psat import Region
from psat.v0_3_0 import PSATClient

if __name__ == '__main__':
    client = PSATClient(Region.US, "<enter_your_api_key_here>")

    tr_page = client.reports.training.retrieve().page
    print("Page Size: {}".format(tr_page.page_size))
    print("Current Page Number: {}".format(tr_page.current_page_number))
    print("Last Page Number: {}".format(tr_page.last_page_number))
    print("Total Records: {}".format(tr_page.record_count))
    print("Link Self: {}".format(tr_page.self_link))
    print("Link First: {}".format(tr_page.first_link))
    print("Link Last: {}".format(tr_page.last_link))
    print("Link Next: {}".format(tr_page.next_link))
    print("Status: {}".format(tr_page.status))
    print("Reason: {}".format(tr_page.reason))
    for page_row in tr_page.data:
        print(page_row.attributes.user_email_address)
        print(page_row.attributes.assignment_name)
        print(page_row.attributes.module_name_user)
        print(page_row.attributes.module_attempt_status)
```

### Querying User Reports

```python
from psat import Region
from psat.v0_3_0 import PSATClient

if __name__ == '__main__':
    client = PSATClient(Region.US, "<enter_your_api_key_here>")

    us_page = client.reports.users.retrieve().page
    print("Page Size: {}".format(us_page.page_size))
    print("Current Page Number: {}".format(us_page.current_page_number))
    print("Last Page Number: {}".format(us_page.last_page_number))
    print("Total Records: {}".format(us_page.record_count))
    print("Link Self: {}".format(us_page.self_link))
    print("Link First: {}".format(us_page.first_link))
    print("Link Last: {}".format(us_page.last_link))
    print("Link Next: {}".format(us_page.next_link))
    print("Status: {}".format(us_page.status))
    print("Reason: {}".format(us_page.reason))
    for page_row in us_page.data:
        print(page_row.attributes.user_email_address)
        print(page_row.attributes.user_first_name)
        print(page_row.attributes.user_last_name)
        print(page_row.attributes.timezone)
```

### Typed Response Objects

Report responses are lazy paged responses. The first page is available through `.page`, and each row has a stable wrapper
type with a nested `attributes` object for the report fields returned by the API.

```python
from klarient import Page, PagedResponse
from psat import Region
from psat.v0_3_0 import PSATClient
from psat.v0_3_0.reports import (
    PhishingExtendedRow,
    PhishingExtendedAttributes,
)

if __name__ == '__main__':
    client = PSATClient(Region.US, "<enter_your_api_key_here>")

    result: PagedResponse[PhishingExtendedRow] = client.reports.phishing_extended.retrieve()
    page: Page[PhishingExtendedRow] = result.page
    row: PhishingExtendedRow = page[0]
    attributes: PhishingExtendedAttributes = row.attributes

    print(row.id)
    print(row.type)

    print(attributes.user_email_address)
    print(attributes.campaign_name)
    print(attributes.event_type)
    print(attributes.ip_address)
    print(attributes.browser)
    print(attributes.mobile_device_used)
    print(attributes.afr)
```

Unknown or newly-added API fields are still available through dictionary-style access.

```python
value = row.attributes.get("new_field_from_api")
```

### Page Size and Pagination

```python
from psat import Region
from psat.v0_3_0 import PSATClient
from psat.v0_3_0.reports import PhishingFilter

if __name__ == '__main__':
    client = PSATClient(Region.US, "<enter_your_api_key_here>")

    # Create a filter object
    filter = PhishingFilter()

    # Starting page number and number of records per page
    filter.with_page(1, 1000)

    # Get the phishing records but apply the filter
    ph_page = client.reports.phishing.retrieve(filter).page

    print("Page Size: {}".format(ph_page.page_size))
    print("Current Page Number: {}".format(ph_page.current_page_number))
    print("Last Page Number: {}".format(ph_page.last_page_number))
    print("Total Records: {}".format(ph_page.record_count))
    print("Link Self: {}".format(ph_page.self_link))
    print("Link First: {}".format(ph_page.first_link))
    print("Link Last: {}".format(ph_page.last_link))
    print("Link Next: {}".format(ph_page.next_link))
    print("Status: {}".format(ph_page.status))
    print("Reason: {}".format(ph_page.reason))
    for row in ph_page.data:
        print(row.attributes.user_email_address)
        print(row.attributes.campaign_name)
```

Paged responses can also walk through pages for you. Iterating the response yields page objects. Calling `items()`
flattens page boundaries and yields rows.

```python
from psat import Region
from psat.v0_3_0 import PSATClient

if __name__ == '__main__':
    client = PSATClient(Region.US, "<enter_your_api_key_here>")

    users = client.reports.users.retrieve()

    for page in users:
        print("Page: {}".format(page.current_page_number))
        for user in page:
            print(user.attributes.user_email_address)

    for user in client.reports.users.retrieve().items():
        print(user.attributes.user_email_address)
```

### Filtering Options

Every report type has its own set of filters which can be applied.

```python
from psat import Region
from psat.v0_3_0 import PSATClient
from psat.v0_3_0.reports import (
    CyberStrengthFilter,
    PhishAlarmFilter,
    PhishingExtendedFilter,
    PhishingFilter,
    TrainingEnrollmentsFilter,
    TrainingFilter,
    UsersFilter,
)

if __name__ == '__main__':
    client = PSATClient(Region.US, "<enter_your_api_key_here>")

    # Create a filter object
    cyberstrength_filter = CyberStrengthFilter()
    enrollments_filter = TrainingEnrollmentsFilter()
    phishalarm_filter = PhishAlarmFilter()
    phishing_filter = PhishingFilter()
    phishingext_filter = PhishingExtendedFilter()
    training_filter = TrainingFilter()
    users_filter = UsersFilter()

    # Get the report records and apply the filter.
    cs_result = client.reports.cyberstrength.retrieve(cyberstrength_filter)
    en_result = client.reports.enrollments.retrieve(enrollments_filter)
    pa_result = client.reports.phishalarm.retrieve(phishalarm_filter)
    ph_result = client.reports.phishing.retrieve(phishing_filter)
    pe_result = client.reports.phishing_extended.retrieve(phishingext_filter)
    tr_result = client.reports.training.retrieve(training_filter)
    us_result = client.reports.users.retrieve(users_filter)

    print(cs_result.page.status)
    print(en_result.data)
```

### User Tags

User tags are returned when `enable_user_tags()` is set on the filter. Tags are custom fields, so they are exposed as an
open dictionary from `row.attributes.user_tags`. Tag names are tenant-defined, so the response cannot be modeled as a
fixed class with known properties.

```python
from psat import Region
from psat.v0_3_0 import PSATClient
from psat.v0_3_0.reports import UsersFilter

if __name__ == '__main__':
    client = PSATClient(Region.US, "<enter_your_api_key_here>")

    users = client.reports.users.retrieve(
        UsersFilter()
        .with_page(1, 100)
        .enable_user_tags()
    )

    for user in users.data:
        tags = user.attributes.user_tags
        if isinstance(tags, dict):
            print(tags.get("Department"))
            print(tags.get("Manager Email Address"))
```

Use `with_user_tag()` when the report should be filtered by one custom tag value.

```python
from psat import Region
from psat.v0_3_0 import PSATClient
from psat.v0_3_0.reports import PhishingFilter

if __name__ == '__main__':
    client = PSATClient(Region.US, "<enter_your_api_key_here>")

    events = client.reports.phishing.retrieve(
        PhishingFilter()
        .with_page(1, 100)
        .enable_user_tags()
        .with_user_tag("Department", "Security")
    )

    for event in events.data:
        print(event.attributes.user_email_address)
        print(event.attributes.user_tags)
```

### Custom Filter Types

Some filter methods such as Training and Enrollments take defined types.

```python
from psat import AssignmentStatus, EnrollmentStatus
from psat.v0_3_0.reports import TrainingEnrollmentsFilter, TrainingFilter

enrollments_filter = TrainingEnrollmentsFilter()
enrollments_filter.add_status(EnrollmentStatus.COMPLETED)
enrollments_filter.add_status(EnrollmentStatus.IN_PROGRESS)

training_filter = TrainingFilter()
training_filter.add_user_assignment_status(AssignmentStatus.COMPLETED)
training_filter.add_user_assignment_status(AssignmentStatus.IN_PROGRESS)
```

### Network Options

Network settings such as proxy, timeout, and SSL verification are configured with `RequestsOptions`.

```python
from klarient import RequestsOptions, RequestsTimeout
from psat import Region
from psat.v0_3_0 import PSATClient

if __name__ == '__main__':
    client = PSATClient(
        Region.US,
        "<enter_your_api_key_here>",
        options=RequestsOptions(
            timeout=RequestsTimeout(connect=10, read=600),
            proxy="http://proxy.example.com:3128",
            verify_ssl=True,
        ),
    )
```

### Proxy Support

A single proxy URL is used for both HTTP and HTTPS requests.

SOCKS5 proxy example:

```python
from klarient import RequestsOptions
from psat import Region
from psat.v0_3_0 import PSATClient

if __name__ == '__main__':
    client = PSATClient(
        Region.US,
        "<enter_your_api_key_here>",
        options=RequestsOptions(
            proxy="socks5h://proxyuser:proxypass@proxy.example.com:8128",
        ),
    )
```

HTTP proxy example:

```python
from klarient import RequestsOptions
from psat import Region
from psat.v0_3_0 import PSATClient

if __name__ == '__main__':
    client = PSATClient(
        Region.US,
        "<enter_your_api_key_here>",
        options=RequestsOptions(
            proxy="http://proxyuser:proxypass@proxy.example.com:3128",
        ),
    )
```

If your environment requires different proxies by scheme, pass a requests-style mapping:

```python
from klarient import RequestsOptions
from psat import Region
from psat.v0_3_0 import PSATClient

if __name__ == '__main__':
    client = PSATClient(
        Region.US,
        "<enter_your_api_key_here>",
        options=RequestsOptions(
            proxy={
                "http": "http://proxy.example.com:3128",
                "https": "http://secure-proxy.example.com:3128",
            },
        ),
    )
```

If your environment already uses standard proxy variables, those can also be used.

```bash
export HTTP_PROXY="http://proxy.example.com:3128"
export HTTPS_PROXY="http://proxy.example.com:3128"
```

### HTTP Timeout Settings

```python
from klarient import RequestsOptions, RequestsTimeout
from psat import Region
from psat.v0_3_0 import PSATClient

if __name__ == '__main__':
    client = PSATClient(
        Region.US,
        "<enter_your_api_key_here>",
        options=RequestsOptions(timeout=RequestsTimeout(connect=10, read=600)),
    )
```

### Limitations

There are currently no known limitations.

For more information please
see: https://proofpoint.securityeducation.com/api/reporting/documentation/#api-Introduction-Introduction
