# import requests

# # Download a web page
# response = requests.get("https://api.github.com")
# print(response.status_code)  # Should print 200


def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


shopping_cart = [
    {"name": "apple", "price": 0.5, "quantity": 6},
    {"name": "banana", "price": 0.3, "quantity": 8},
]

print(calculate_total(shopping_cart))
