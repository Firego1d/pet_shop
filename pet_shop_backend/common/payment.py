from alipay import AliPay

from pet_shop import settings


class Pay:
    # 应用ID
    app_id = '9021000122686657'
    # 商户号:
    pid = '2088721004048916'
    # 支付的网关地址
    base_url = 'https://openapi-sandbox.dl.alipaydev.com/gateway.do'
    # 是否开启调试模式(沙箱环境下使用)
    debug = True
    # 支付成功前端跳转的页面地址
    # return_url = 'http://localhost:8080/#/pages/order/paysuccess?status=1'
    return_url = None
    # 支付成功的回调接口地址
    # notify_url = 'http://120.22.12.11:8888/api/order/alipay/callback/'
    notify_url = None

    def __init__(self):
        # 公钥和私钥
        public_key = open(settings.BASE_DIR / 'common/alipay_public_key.pem').read()
        private_key = open(settings.BASE_DIR / 'common/app_private_key.pem').read()

        self.pay_obj = AliPay(
            # 应用ID
            appid=self.app_id,
            # 私钥
            app_private_key_string=private_key,
            # 公钥
            alipay_public_key_string=public_key,
            # 开启Debug模式(沙箱环境下开启)
            debug=self.debug,
        )

    def mobile_pay_url(self, order_on, amount):
        """
        生成手机应用的支付地址
        :param order_on: 订单编号
        :param amount: 支付金额
        :return:
        """
        # H5网页支付
        url = self.pay_obj.api_alipay_trade_wap_pay(
            # 支付页面的标题
            subject='宠物商城订单支付',
            # 商户生成的订单号(自己系统中订单的编号)
            out_trade_no=order_on,
            # 订单支付的金额
            total_amount=amount,
            # 需要将产品部署到服务器再进行配置
            return_url=self.return_url,
            notify_url=self.notify_url,
        )
        # app支付
        # url = self.pay_obj.api_alipay_trade_app_pay(
        #     # 支付页面的标题
        #         subject='朴朴生鲜商城订单支付',
        #         # 商户生成的订单号(自己系统中订单的编号)
        #         out_trade_no=order_on,
        #         # 订单支付的金额
        #         total_amount=amount,
        #         # 需要将产品部署到服务器再进行配置
        #         return_url=self.return_url,
        #         notify_url=self.notify_url,
        # )
        #
        pay_url = self.base_url + url
        return pay_url

    def get_pay_result(self, order_on):
        """获取支付结果"""
        return self.pay_obj.api_alipay_trade_query(out_trade_no=order_on)
