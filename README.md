# asencis Python API Module

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0cffb15bf0844a8aa4b7a9a62f05d89a)](https://app.codacy.com/gh/asencis/asencis-python?utm_source=github.com&utm_medium=referral&utm_content=asencis/asencis-python&utm_campaign=Badge_Grade)

The asencis Python library provides convenient access to the asencis API from applications written in the Python language. It includes a pre-defined set of classes for API resources that initialize themselves dynamically from API responses which makes it compatible with a wide range of versions of the asencis API.

## Documentation

See the [Asencis Documentation](https://asensis.com/documentation).

## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```sh
pip install --upgrade asencis
```

Install from source with:

```sh
python setup.py install
```

### Requirements

-   Python 3.6+ (PyPy supported)

## Example Usage

Example usage for publicaly available endpoints can be found in the `/examples` dir for this repository.

```python
import asencis

# List all Datasets:
response = asencis.Datasets.list()
print(response.json())

# Retreive a Dataset by uuid attribute:
response = asencis.Datasets.retrieve(uuid="e7133620-954e-4db4-a4a4-ac98792fee9e")
print(response.json())

# List all Domains:
response = asencis.Domains.list()
print(response.json())

# List all Prefixes:
response = asencis.Prefixes.list()
print(response.json())

# List all Quantities:
response = asencis.Quantities.list()
print(response.json())
```

## Further Information

The asencis API comes in two "flavours": the RESTful API and the GraphQL API.

The REST API is built upon RESTful principles, meaning the API has predictable resource-oriented URLs, enforces acceptable throttling limits and accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, permission based access and standard HTTP verbs.

Responses are also standardised, and will return results in either JSON or paginated JSON (in maximum page sizes of 30), and follows the latest JSONAPI specification returning a content-type of `application/vnd.api+json`. With asencis, the retrieving, querying, and browsing functions do not require authentication and are openly available to anyone. However, the creation, updating, and destruction of resources within the system can only be done by either the object owner, in the case of datasets, their respective meta records, and file entities, or system administrators, in the case of domains and measurements *OR* by ensuring that the request user object has the correct permissions for the requested resource (i.e., is the resource owner).

The RESTful API exposes `Datasets` (and their related Meta, DOI (Digital Object Identifier) and File models, as well as the browsable API), `Domains` and `Measurements`.

Authentication for the API is available in two flavours: JSON Web Tokens (JWT) and OAuth2. JSON Web Tokens are an open, industry standard RFC 7519 method for representing claims securely between two parties. In essence, JWT allows asencis to determine that your authorised to use the system by providing your username and password, at which point we can begin to ascertain resource permissions for various restricted resources. OAuth2 authentication to asencis will enable applications to obtain limited access to institutional accounts over HTTP by delegating user authentication to the service that hosts the institution's account, and authorizing third-party applications to access that account.

As mentioned, to ensure stability of the system, rate limiting, or request throttling, is enforced for API endpoints. As with permissions, multiple simultaneous throttle rates are applied to the API. asencis applies a more restrictive throttle for unauthenticated requests, and a less restrictive throttle for authenticated requests. Anonymous requests are limited to a maximum of 100/hour (giving a potential of 2400 per day), and authenticated requests of 100000 per day.

The GraphQL API is built upon the principles of the Graph querying language, meaning that all resource queries are routed to one URL, usually `/graphql`, without a versioning history, whilst providing a complete and understandable description of the data of the API. GraphQL APIs allow for powerful querying and resource matching functionality: retrieving many interlinked resources in a single request whilst asking only for what you need. Responses are also standardised, and will return results in GZip content-encoded (compressed) JSON and follows the latest JSONAPI specification returning a content-type of `application/vnd.api+json`.

The GraphQL API is an alternative to the RESTful API. However, it currently only supports queries, but not mutations (i.e., create or update actions, e.g. registering a new dataset), so they are optimally used in tandem.
