# UserAgent Generator

This project aims to create a simple user-agent generator that can be used to mimic different browsers and devices. This can be particularly useful for web scraping and testing purposes.

## Getting Started v1.6

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip

### Installation

Follow these steps to set up the project:

```bash
$ pip install GenUserAgent

```
### Generate User-Agent Facebook
```Python

from Gen import UserAgentGenerator

headers = {
'User-agent': UserAgentGenerator().generate_user_agent(),
'X-Tigon-Is-Retry': 'False',
'X-Fb-Device-Group': '7948',
'X-Graphql-Request-Purpose': 'fetch',
'X-Fb-Privacy-Context': '3643298472347298',
'X-Fb-Friendly-Name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
}

```
### Logger console
```Python

from Gen import UserAgentGenerator 
from Gen.utils import logger


user_agent = UserAgentGenerator().generate_user_agent()

from Gen.utils import logger
import requests

result =  requests.get("https://api.myip.com")
if result.status_code == 200:
    logger.info(f"SUCCESS - IP : {result.json()['ip']}")
else:
    logger.warning("Not found result !")
