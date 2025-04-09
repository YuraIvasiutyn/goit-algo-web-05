from typing import List, Optional


def return_currency(data_dict: dict, currency: Optional[List[str]] = None):
    if currency is None:
        currency = ["EUR", "USD"]

    date = data_dict.get("date")
    exchange_rate_list = data_dict.get("exchangeRate")

    result = {date: {}}

    for rate in exchange_rate_list:
        curr = rate.get("currency")
        if curr in currency:
            result[date][curr] = {
                "sale": rate.get("saleRate"),
                "purchase": rate.get("purchaseRate")
            }

    return result



