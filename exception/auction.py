# except和raise同时使用

class AuctionException(Exception): pass


class Auction:
    def __init__(self, init_price):
        self.init_price = init_price

    def bid(self, bid_price):
        d = 0.0
        try:
            d = float(bid_price)
        except Exception as e:
            print("转化异常:", e)
            raise AuctionException("必须是数值！")
        if self.init_price > d:
            raise AuctionException("竞拍价必须大于起拍价！")
        init_price = d


def main():
    at = Auction(20.4)
    try:
        at.bid("df")
    except AuctionException as e:
        print("main ex:", e)


main()
