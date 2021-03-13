Feature: List order by id

    Scenario: List order with at least one item
        Given the order has an id of "8ccdb422-b259-42f6-8bf4-8829381d7ed4"
            And the HEADER param request content type is "application/json"
        When the user sends a GET HTTP request to /order enpoint
            Then you should receive a "200" status code
            And the external id should not be null
            And the list of items should not be empty
            And the order status should be "paid"
            And the total order should be the sum of the list of orders prices
            And the last update time should be greater than or the same time of creation
            And the wallet should not be empty

