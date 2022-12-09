# Proofpoint Security Awareness Training API Package

Library implements all of the functions of the Emerging Threats API via PHP.

### Requirements:

* Python 3.9+

### Getting Started
The following will dump all data associated with your PSAT instance.
```
from psat_api import *

if __name__ == '__main__':
    client = Client(Region.US, Version.V1, "<enter_your_api_key_here>")

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
```

### Limitations
There are currently no known limitations. 
