import aiohttp

from datetime import datetime, timedelta
from typing import Optional, List

from configuration import api_url
from utility import return_currency


async def get_currency_from_api(day_param: int, currency: Optional[List[str]] = None):
    if day_param > 10:
        raise ValueError("You can check no later than 10 days.")

    day_today = datetime.now().date()
    before = day_today - timedelta(days=day_param-1)

    result = []
    async with aiohttp.ClientSession() as session:

        while before <= day_today:
            before_str = before.strftime("%d.%m.%Y")
            url = f"{api_url}date={before_str}"

            async with session.get(url) as response:

                if response.ok:
                    result_curr = return_currency(await response.json(), currency)
                    result.append(result_curr)
                else:
                    raise f"Problem with get currency. Status Code: {response.status}"
                before += timedelta(days=1)

    return result
