import sys
import asyncio

from currency_service import get_currency_from_api


if __name__ == "__main__":
    try:
        days = int(sys.argv[1]) if len(sys.argv) > 1 else 1
        currency = sys.argv[2].split(",") if len(sys.argv) > 2 else None
        print(asyncio.run(get_currency_from_api(days, currency)))
    except ValueError:
        print("Please enter a valid number of days (1-10)")
    except Exception as e:
        print(f"Error: {e}")

