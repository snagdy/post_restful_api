# post_restful_api

## Command Line Tool

The syntax for the command line tool is:

`cat input_file.json | python nest.py nest_level_1 nest_level_2 ... nest_level_n`

Example:

`cat input.json | python.exe nest.py currency country city`

## RESTful API Service

Queries to this service must be POST requests, passing JSON in the following format:

`{"hierarchy":[],"data":[{}]}`

Where "*hierarchy*" is a list of strings specifying the nesting order, and *data* is a list of dictionaries with all the attributes we want to nest.

**Example Query:**

`curl -u john:matrix http://localhost:5000/api -H "Content-Type: application/json" -d '{"hierarchy":["currency","country","city"],"data":[{"country":"US","city":"Boston","currency":"USD","amount":100},{"country":"FR","city":"Paris","currency":"EUR","amount":20},{"country":"FR","city":"Lyon","currency":"EUR","amount":11.4},{"country":"ES","city":"Madrid","currency":"EUR","amount":8.9},{"country":"UK","city":"London","currency":"GBP","amount":12.2},{"country":"UK","city":"London","currency":"FBP","amount":10.9}]}'`
  
This app uses very basic authentication, where the username and password are stored in the source code.
In production, these would be hashed and stored / retrieved from a database.
Our service, for the sake of simplicity and to show its key features, does not include an extensive authentication setup, although this could be implemented.

**Example Response:**

`{
  "EUR": {
    "ES": {
      "Madrid": [
        {
          "amount": 8.9
        }
      ]
    },
    "FR": {
      "Lyon": [
        {
          "amount": 11.4
        }
      ],
      "Paris": [
        {
          "amount": 20
        }
      ]
    }
  },
  "FBP": {
    "UK": {
      "London": [
        {
          "amount": 10.9
        }
      ]
    }
  },
  "GBP": {
    "UK": {
      "London": [
        {
          "amount": 12.2
        }
      ]
    }
  },
  "USD": {
    "US": {
      "Boston": [
        {
          "amount": 100
        }
      ]
    }
  }
}`

This example response shows the nesting order of currency, country, and city, with remaining keys added to the dictionary inside the list of the final nesting layer.
