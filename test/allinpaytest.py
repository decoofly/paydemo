# coding=utf-8
from allinpay import AllInPayClient, AllInPayTestClient


# client = AllInPayClient('00000003', '990440148166000', 'a0ea3fa20dbd7bb4d5abf1d59d63bae8')  # 生产环境
test_client = AllInPayTestClient('00000051', '990581007426001', 'allinpay888')  # 测试环境

# info = client.unitorder.pay('1234567890', 1, 'W01')
info = test_client.unitorder.pay('12345567890', 1, 'W01')
print(info)


def requestAllInPay():
    data = dict(appKey="mbs", appSerialNum="21199627787992317", appCallParam="", platformKey="AllInPay",
                merchantNum="200604000007214", bankKey="ICBC", mobileNum="13693776378",
                identityCard="342423199007271277", customerName="张飞", bankCardNum="6212261001080362559",
                deductAmount="0.08", agreementNum="AIP2559190903001000211", agreementCustomerId="123456",
                deductInstructionDivideDtoList=[
                    {
                        "merchantNum": "200604000007428",
                        "amount": "0.04"
                    },
                    {
                        "merchantNum": "200604000007428",
                        "amount": "0.02"
                    },
                    {
                        "merchantNum": "200604000007428",
                        "amount": "0.02"
                    }

                ])

