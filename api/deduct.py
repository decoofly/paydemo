import requests
from sqlalchemy import create_engine
from api import basepay
engine = create_engine("mysql+pymysql://root:root@localhost:3306/vpc", echo=True)
conn = engine.connect()


class DeductRequest(basepay.BasePay):

    def psrseParam(self):
        pass

    def request(self):
        #根据接口获取对应的url
        url = conn.execute("select * from t_interface t where t.interface_key = %s" %self.interface_key)
        requests.post(url, self.reqdata)


if __name__ == '__main__':

    result = conn.execute("select * from t_bank")
    print([i for i in result.cursor.fetchall()])