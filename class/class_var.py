# 类变量
class Address:
    detail = "广州"
    post_code = '510660'

    def info(self):
        # 报错
        # print(detail)
        print(Address.detail)
        print(Address.post_code)


print(Address.detail)
addr = Address()
addr.info()

Address.detail = "佛山"
Address.post_code = '460110'
addr.info()
