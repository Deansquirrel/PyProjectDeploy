import Common.Const
CONST = Common.Const


def define():
    # 客户
    CONST.CUSTOM_NAME = "jiahe"             #客户名称
    CONST.CUSTOM_CODE = "050"               #客户code
    #项目
    CONST.PROJECT_NAME_EN = "crm"           #项目名称英文或拼音
    #RabbitMQ
    CONST.RABBITMQ_ADDRESS = "host=localhost:5672"        #地址
    #Exceptionless
    CONST.EXCEPTIONLESS_CUSTOM_NAME = "昆明佳禾"       #名称
    CONST.EXCEPTIONLESS_ADDRESS = "http://exceptionless.95sz.cn"                    #地址
    CONST.EXCEPTIONLESS_KEY = "VO9ZoHMDqK4euS9KxUVp4mAAu6oKhjdeMN"                        #KEY
    #服务器IP地址
    CONST.SERVER_IP = "118.31.79.23"
    #服务号Appid
    CONST.SERVICE_APPID = "wx2789969765e38"
    #商户号
    CONST.BUSINESS_NO = "1316242108"
    #域名
    CONST.DOMAIN_PROXY_WS = "http://39.108.58.237:8001"
    CONST.PROXY_WS = "http://39.108.58.237:800"
    #数据库
    CONST.DATABASE_ADDRESS = "szhz1dat.sqlserver.rds.aliyuncs.com,3433"
    CONST.DATABASE_USER = "ZL"
    CONST.DATABASE_PWD = "83893939"



def insert_values():
    CONST.RABBITMQ_VIRTUAL_HOST = CONST.CUSTOM_NAME + CONST.PROJECT_NAME_EN   # Virtual Hosts
    CONST.DOMAIN = CONST.CUSTOM_NAME + ".95sz.cn"
    CONST.BUSINESS_BACK = CONST.DOMAIN + "/Charge/"
    CONST.CRM_PAY_CONFIG_TOOL = "http://" + CONST.DOMAIN + "/Charge/Send"
    CONST.DATABASE_DTDSQUEUE = CONST.CUSTOM_NAME + "_dtdsqueue"     #队列库
    CONST.DATABASE_HX1 = CONST.CUSTOM_NAME + "_hx1"  # 核心库1
    CONST.DATABASE_HX2 = CONST.CUSTOM_NAME + "_hx2"  # 核心库2
