API Automation Tests

Automated API tests for the JSONPlaceholder
 REST API using Python, Pytest, Requests, JSON Schema, and Allure Report.

The project covers the main CRUD operations for the /posts endpoint and validates both HTTP status codes and response data.

Tech Stack
Python 3
Pytest — test framework
Requests — HTTP client for API requests
JSON Schema — response schema validation
Allure — test reporting and test execution details
Project Structure
.
├── test.py
├── conftest.py
└── README.md

test.py

Contains automated API tests for the /posts resource.

The test suite covers:

Getting all posts
Getting a single post
Handling a non-existent post
Creating a post
Updating a post with PUT
Updating a post with PATCH
Deleting a post

Allure annotations are used to organize tests by:

Epic
Feature
Story
Severity

All API operations are also divided into explicit Allure steps for better visibility in the test report.

conftest.py

Contains shared Pytest fixtures used by the test suite:

url — base API URL
post_data — payload for creating a post
put_data — payload for updating a post
patch_data — payload for partially updating a post
schema — JSON Schema used to validate API responses

All fixtures have scope="session".

Installation

Make sure Python 3 is installed.

Create a virtual environment:

Windows
python -m venv venv
venv\Scripts\activate

macOS / Linux
python3 -m venv venv
source venv/bin/activate


Install the required dependencies:

pip install pytest requests allure-pytest jsonschema

Test Cases
GET All Posts

Endpoint:

GET /posts


The test verifies:

Response status code is 200
Response body is a list
The list contains at least one element
GET Single Post

Endpoint:

GET /posts/1


The test verifies:

Response status code is 200
Response body is a dict
The response is not empty
GET Non-Existent Post

Endpoint:

GET /poasts/14885267


The test verifies:

Response status code is 404
Response body is an empty object {}

The endpoint contains the intentional /poasts path to test the API behavior for a non-existent resource.

POST Create Post

Endpoint:

POST /posts


Request payload:

{
  "title": "My Post",
  "body": "Post content",
  "userId": 1
}


The test verifies:

Response status code is 201
Response body conforms to the defined JSON Schema
PUT Update Post

Endpoint:

PUT /posts/1


Request payload:

{
  "id": 1,
  "title": "Updated Title",
  "body": "Updated Body",
  "userId": 1
}


The test verifies:

Response status code is 200
Response body conforms to the defined JSON Schema
PATCH Update Post

Endpoint:

PATCH /posts/1


Request payload:

{
  "title": "Only Title Changed"
}


The test verifies:

Response status code is 200
Response body conforms to the defined JSON Schema
DELETE Post

Endpoint:

DELETE /posts/1


The test verifies:

Response status code is 200
JSON Schema Validation

The project uses the jsonschema library to validate responses returned by the POST, PUT, and PATCH requests.

The expected response structure is:

{
  "type": "object",
  "properties": {
    "id": {
      "type": "number"
    },
    "title": {
      "type": "string"
    },
    "body": {
      "type": "string"
    },
    "userId": {
      "type": "number"
    }
  },
  "required": [
    "id",
    "title",
    "body",
    "userId"
  ]
}


Validation is performed with:

validate(instance=json_data, schema=schema)


This ensures that the API response contains all required fields and that each field has the expected data type.

Running Tests

Run all tests with:

pytest


Run tests with Allure result generation:

pytest --alluredir=allure-results


The command generates an allure-results directory containing the test execution data.

Allure Report

The tests use Allure annotations to provide detailed test reporting.

The test hierarchy includes:

API test
│
├── Get section
│   ├── Get /posts test
│   ├── Get /posts/{id} test
│   └── GET non-existent post
│
├── Post section
│   └── Post /posts test
│
├── Put section
│   └── Put /posts/1 test
│
├── Patch section
│   └── Patch /posts/1 test
│
└── Delete section
    └── Delete /posts/1 test


Critical CRUD tests are marked with:

@allure.severity(allure.severity_level.CRITICAL)


This allows critical tests to be easily identified in the Allure report.

To generate and open the report:

pytest --alluredir=allure-results
allure serve allure-results

API Under Test

The project uses JSONPlaceholder, a free fake REST API for testing and prototyping.

Base URL:

https://jsonplaceholder.typicode.com


The tests interact with the /posts resource.

Test Coverage
HTTP Method	Endpoint	Expected Status	Validation
GET	/posts	200	Response type and non-empty list
GET	/posts/1	200	Response type and non-empty object
GET	/poasts/14885267	404	Empty response object
POST	/posts	201	JSON Schema
PUT	/posts/1	200	JSON Schema
PATCH	/posts/1	200	JSON Schema
DELETE	/posts/1	200	Status code
Key Features
REST API test automation
CRUD endpoint coverage
HTTP status code validation
Response type validation
JSON Schema validation
Reusable Pytest fixtures
Allure test reporting
Allure test steps and test categorization
Critical test severity classification
Notes

JSONPlaceholder is a fake REST API intended for testing and prototyping. The API simulates CRUD operations but does not persist changes like a production database.

This project is intended as an example of API test automation using Python and demonstrates how to combine Pytest, Requests, JSON Schema validation, and Allure reporting.