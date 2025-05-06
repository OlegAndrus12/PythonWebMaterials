"""
The Interface Segregation Principle (ISP) emphasizes the importance of
keeping interfaces slim and relevant to the clients that implement them.
It's one of the SOLID principles, a set of design principles in object-oriented
 software development aimed at making  software designs more understandable,
 flexible, and maintainable.
"""

"""
"Clients should not be forced to depend on methods they do not use."
In simpler terms: split big, bloated interfaces into smaller, role-specific ones.

"""

import requests

# https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11


def pretty_view(data: list[dict]):
    # data preparation
    result = [
        {
            f"{el.get('ccy')}": {
                "buy": float(el.get("buy")),
                "sale": float(el.get("sale")),
            }
        }
        for el in data
    ]
    # data visualisation
    pattern = "|{:^10}|{:^10}|{:^10}|"
    print(pattern.format("currency", "sale", "buy"))
    for el in result:
        currency, *_ = el.keys()
        buy = el.get(currency).get("buy")
        sale = el.get(currency).get("sale")
        print(pattern.format(currency, sale, buy))


if __name__ == "__main__":

    response = requests.get(
        "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    )
    response.raise_for_status()
    data = response.json()
    pretty_view(data)
