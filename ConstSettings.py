import Common.Const

CONST = Common.Const


# 配置值（手工输入）
def define():
    # 客户
    CONST.CUSTOM_NAME = "jiahe"  # 客户名称
    CONST.CUSTOM_CODE = "050"  # 客户code
    CONST.CUSTOM_SERVICE_PORT = "10011"  # 服务端口
    # 项目
    CONST.PROJECT_NAME_EN = "crm"  # 项目名称英文或拼音
    # RabbitMQ
    CONST.RABBITMQ_ADDRESS = "host=localhost:5672"  # 地址
    # Exceptionless
    CONST.EXCEPTIONLESS_CUSTOM_NAME = "昆明佳禾"  # 名称
    CONST.EXCEPTIONLESS_ADDRESS = "http://exceptionless.95sz.cn"  # 地址
    CONST.EXCEPTIONLESS_KEY = "VO9ZoHMDqK4euS9KxUVp4mAAu6oKhjdeMN"  # KEY
    # 服务器IP地址
    CONST.SERVER_IP = "118.31.79.23"
    # 服务号Appid
    CONST.SERVICE_APPID = "wx2789969765e38"
    # 商户号
    CONST.BUSINESS_NO = "1316242108"
    # 域名
    CONST.DOMAIN_PROXY_WS = "http://39.108.58.237:8001"
    CONST.PROXY_WS = "http://39.108.58.237:800"
    # 数据库
    CONST.DATABASE_ADDRESS = "szhz1dat.sqlserver.rds.aliyuncs.com,3433"
    CONST.DATABASE_USER = "ZL"
    CONST.DATABASE_PWD = "83893939"

    # 支付加密
    CONST.PAY_SECRET = "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"


# 配置值（按规则计算）
def insert_values():
    CONST.RABBITMQ_VIRTUAL_HOST = CONST.CUSTOM_NAME + CONST.PROJECT_NAME_EN  # Virtual Hosts
    CONST.DOMAIN = CONST.CUSTOM_NAME + ".95sz.cn"
    CONST.BUSINESS_BACK = CONST.DOMAIN + "/Charge/"
    CONST.CRM_PAY_CONFIG_TOOL = "http://" + CONST.DOMAIN + "/Charge/Send"
    CONST.DATABASE_DTDSQUEUE = CONST.CUSTOM_NAME + "_dtdsqueue"  # 队列库
    CONST.DATABASE_HX1 = CONST.CUSTOM_NAME + "_hx1"  # 核心库1
    CONST.DATABASE_HX2 = CONST.CUSTOM_NAME + "_hx2"  # 核心库2
    CONST.DATABASE_JICHU = CONST.CUSTOM_NAME + "_jichu"  # 基础库
    CONST.DATABASE_PEIZHI = CONST.CUSTOM_NAME + "_peizhi"  # 配置库
    CONST.DATABASE_THRPAY = CONST.CUSTOM_NAME + "_thrpay"  # 第三方支付库
    CONST.DATABASE_YWXQ = CONST.CUSTOM_NAME + "_ywxq"  # 事件详情库
    # ----------------------------------------------------------------------------------------------
    # 服务
    server_no = 1
    server_name = "SnoServer"
    last_server_port = int(CONST.CUSTOM_SERVICE_PORT)

    CONST.SNO_SERVER_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                            ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                            server_name
    CONST.SNO_SERVER_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.SNO_SERVER_PROT = str(last_server_port)
    CONST.SNO_SERVER_ADDRESS = "http://" + CONST.SERVER_IP + ":" + str(last_server_port)
    CONST.SNO_SERVER_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    server_no = server_no + 1
    server_name = "CRMdz"
    last_server_port = last_server_port + 1

    CONST.CRM_DZ_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                        ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                        server_name
    CONST.CRM_DZ_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.CRM_DZ_PROT = str(last_server_port)
    CONST.CRM_DZ_ADDRESS = "http://" + CONST.SERVER_IP + ":" + str(last_server_port)
    CONST.CRM_DZ_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    server_no = server_no + 1
    server_name = "YwDetaildz"
    last_server_port = last_server_port + 1

    CONST.YW_DETAIL_DZ_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                              ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                              server_name
    CONST.YW_DETAIL_DZ_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.YW_DETAIL_DZ_PROT = str(last_server_port)
    CONST.YW_DETAIL_DZ_ADDRESS = "http://" + CONST.SERVER_IP + ":" + str(last_server_port)
    CONST.YW_DETAIL_DZ_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    server_no = server_no + 1
    server_name = "CRMWs"
    last_server_port = last_server_port + 1

    CONST.CRM_WS_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                        ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                        server_name
    CONST.CRM_WS_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.CRM_WS_PROT = str(last_server_port)
    CONST.CRM_WS_ADDRESS = "http://" + CONST.SERVER_IP + ":" + str(last_server_port)
    CONST.CRM_WS_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    server_no = server_no + 1
    server_name = "CRMWeb"

    CONST.CRM_WEB_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                         ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                         server_name
    CONST.CRM_WEB_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.CRM_WEB_PROT = str(last_server_port)
    CONST.CRM_WEB_ADDRESS = CONST.DOMAIN
    CONST.CRM_WEB_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    server_no = server_no + 1
    server_name = "CRMManager"
    last_server_port = last_server_port + 1

    CONST.CRM_MANAGER_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                             ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                             server_name
    CONST.CRM_MANAGER_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.CRM_MANAGER_PROT = str(last_server_port)
    CONST.CRM_MANAGER_ADDRESS = "http://" + CONST.SERVER_IP + ":" + str(last_server_port)
    CONST.CRM_MANAGER_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    server_no = server_no + 1
    server_name = "CrmJichShuj"
    last_server_port = last_server_port + 1

    CONST.CRM_JICHUSHUJU_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                                ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                                server_name
    CONST.CRM_JICHUSHUJU_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.CRM_JICHUSHUJU_PROT = str(last_server_port)
    CONST.CRM_JICHUSHUJU_ADDRESS = "http://" + CONST.SERVER_IP + ":" + str(last_server_port)
    CONST.CRM_JICHUSHUJU_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    server_no = server_no + 1
    server_name = "CRMGuanD"
    last_server_port = last_server_port + 1

    CONST.CRM_GUAND_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                           ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                           server_name
    CONST.CRM_GUAND_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.CRM_GUAND_PROT = str(last_server_port)
    CONST.CRM_GUAND_ADDRESS = "http://" + CONST.SERVER_IP + ":" + str(last_server_port)
    CONST.CRM_GUAND_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    server_no = server_no + 1
    server_name = "CRMPeiZh"
    last_server_port = last_server_port + 1

    CONST.CRM_PEIZH_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                           ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                           server_name
    CONST.CRM_PEIZH_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.CRM_PEIZH_PROT = str(last_server_port)
    CONST.CRM_PEIZH_ADDRESS = "http://" + CONST.SERVER_IP + ":" + str(last_server_port)
    CONST.CRM_PEIZH_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    server_no = server_no + 1
    server_name = "CRMAccRecord"

    CONST.CRM_ACC_RECORD_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                                ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                                server_name
    CONST.CRM_ACC_RECORD_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.CRM_ACC_RECORD_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    server_no = server_no + 1
    server_name = "CRMAccRecordAdd"

    CONST.CRM_ACC_RECORD_ADD_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                                    ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                                    server_name
    CONST.CRM_ACC_RECORD_ADD_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.CRM_ACC_RECORD_ADD_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    server_no = server_no + 1
    server_name = "CRMMQClient"

    CONST.CRM_MQ_CLIENT_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                               ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                               server_name
    CONST.CRM_MQ_CLIENT_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.CRM_MQ_CLIENT_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    server_no = server_no + 1
    server_name = "DataSync"

    CONST.DATA_SYNC_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                           ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                           server_name
    CONST.DATA_SYNC_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.DATA_SYNC_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    server_no = server_no + 1
    server_name = "WeixinCallBack"

    CONST.WX_CALLBACK_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                             ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                             server_name
    CONST.WX_CALLBACK_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.WX_CALLBACK_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    server_no = server_no + 1
    server_name = "CacheBuilder"

    CONST.CACHE_BUILDER_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                               ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                               server_name
    CONST.CACHE_BUILDER_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.CACHE_BUILDER_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    server_no = server_no + 1
    server_name = "Heartbeat"

    CONST.HEART_BEAT_PATH = "C:\\" + CONST.CUSTOM_NAME + "\\" + \
                            ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + \
                            server_name
    CONST.HEART_BEAT_NAME = CONST.CUSTOM_NAME + "_" + server_name
    CONST.HEART_BEAT_REMARK = ("0" if len(str(server_no)) < 2 else "") + str(server_no) + "_" + server_name

    # 支付加密
    CONST.TENPAYV3_MODEL1 = CONST.PAY_SECRET[0:1000]
    CONST.TENPAYV3_MODEL2 = CONST.PAY_SECRET[1000:2000]
    CONST.TENPAYV3_MODEL3 = CONST.PAY_SECRET[2000:3000]
    CONST.TENPAYV3_MODEL4 = CONST.PAY_SECRET[3000:4000]
    CONST.TENPAYV3_MODEL5 = CONST.PAY_SECRET[4000:5000]
    CONST.TENPAYV3_MODEL6 = CONST.PAY_SECRET[5000:6000]
