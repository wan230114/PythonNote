import locale
import re
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


class convertToCNY(object):
    """
    Usage: 
    只考虑币种：美元(USD, $)，英镑(GBP, £)，欧元(EUR, €)，港币(HKD, HK$)，日元(JPY, ¥)
    """

    def __init__(self, SDK, price):
        self.SDK = SDK
        self.price = price
        self.DicConver = {"$": "USD", "£": "GBP", "€": "EUR",
                          "HK$": "HKD", "¥": "JPY"}

    def get(self, tar):
        L_re = re.findall('(.*?)(\d.*)', self.price)
        unit, price_str = L_re[0]
        price = locale.atof(price_str)
        if unit in self.DicConver:
            unit = self.DicConver[unit]
        tar_price = (price / self.SDK['rates'][self.SDK['base']]
                     * self.SDK['rates'][tar])  # 计算
        # return tar, tar_price
        return '%.2f' % tar_price


if __name__ == "__main__":
    import requests
    import json
    req = requests.get('https://app-cdn.2q10.com/api/v2/currency')
    SDK = json.loads(req.text)
    # from pprint import pprint
    # pprint(SDK)
    for testdata in ["$1,999.00",
                     "HKD2399",
                     "EUR499.99",
                     "€499.99",
                     "$1"]:
        price = convertToCNY(SDK, testdata).get("CNY")
        print(price)
