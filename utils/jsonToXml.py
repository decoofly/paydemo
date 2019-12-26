import json

import xmltodict


def xmltojson(xmlstr):
    # parse是的xml解析器
    xmlparse = xmltodict.parse(xmlstr)
    # json库dumps()是将dict转化成json格式，loads()是将json转化成dict格式。
    # dumps()方法的ident=1，格式化json
    jsonstr = json.dumps(xmlparse, indent=1)
    return jsonstr


def jsontoxml(jsonstr):
    # xmltodict库的unparse()json转xml
    xmlstr = xmltodict.unparse(jsonstr)
    return xmlstr


if __name__ == '__main__':
    json = {'student': {
                'course': {'name': 'math', 'score': '90'},
                'info': {'sex': 'male', 'name': 'name'},
                'stid': '10213'
            }
    }

    print(jsontoxml(json))

    xml = '''
    <AIPG> 
    <INFO>
    <TRX_CODE>100011</TRX_CODE>
    <VERSION>04</VERSION>
    <DATA_TYPE>2</DATA_TYPE>
    <LEVEL>5</LEVEL>
    <USER_NAME>20060400000449704</USER_NAME>
    <USER_PASS>111111</USER_PASS>
    <REQ_SN>200604000004497-1525923303530</REQ_SN>
    <SIGNED_MSG>59c0d5ec49866bb2240af577f871c8bb38f22f176eae0a1e7567ad62f356ef59d9f71fd725c1aa0db2802a58956a0c3e57573cbd4dcc6dc2bb39843a755c71417624708801c73dd995b7c97faae63c09c85a21c8640b4c95f1db9ed3ded215017043e31331d27d017e20efc56a17ad396e3aef73d1034c01ab28bfc3af937ac9</SIGNED_MSG>
    </INFO>
    <TRANS>
    <BUSINESS_CODE>19900</BUSINESS_CODE>
    <MERCHANT_ID>200604000004497</MERCHANT_ID>
    <SUBMIT_TIME>20180510113503</SUBMIT_TIME>
    <BANK_CODE>0302</BANK_CODE>
    <ACCOUNT_NO>62178808000104315861</ACCOUNT_NO>
    <ACCOUNT_NAME>zhang000001</ACCOUNT_NAME>
    <ACCOUNT_PROP>0</ACCOUNT_PROP>
    <AMOUNT>20000</AMOUNT>
    <CURRENCY>CNY</CURRENCY>
    <ID_TYPE>0</ID_TYPE>
    <ID>120221198606121502</ID>
    <TEL></TEL>
    <CUST_USERID>252523524253xx</CUST_USERID>
    </TRANS>
    </AIPG>
            '''
    print(xmltojson(xml))
