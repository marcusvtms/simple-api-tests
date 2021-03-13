Feature: Create order

    Scenario: Create order with one item
        Given the request body is set with one item
            And the HEADER param request content type is "application/json"
        When the user sends a POST HTTP request to /order enpoint
            Then you should receive a "200" status code
            And the external id should not be null
            And the list of items should not be empty