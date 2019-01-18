# -*- coding:utf-8 -*-
DEBUG = True
DB_NAME = 'kpages'
DB_HOST = 'localhost'
PORT = 8888
# 指定RequestHandler 所在目录
ACTION_DIR = ('restful', 'testweb')
# http accept ip
BIND_IP = None

# 数据库超时时间
SOCK_TIMEOUT = 10
SOCK_TIMEOUT_MS = None

CPU_MULTIPLE = 5

# SESSION 过期时间(秒)
SESSION_EXPIRE = 30*24*60*60

# 是否启动压缩
GZIP = True
# 指定任务（srvcmd）所在目录
JOB_DIR = "logic"

# 指定TestCase 所在目录
UTEST_DIR = "utest"

# 静态目录名
STATIC_DIR_NAME = "static"

# 模板目录名
TEMPLATE_DIR_NAME = "template"

# COOKIE 加密
COOKIE_SECRET = "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo="

# COOKIE 安全
XSRF_COOKIES = False

# 数据库与缓存是否使用持久连接
PERSISTENT_DB_CONNECTION = False

# 缓存服务器
CACHE_HOST = "localhost"

GFS_NAME = 'gfs'

SERVICE_CHANNEL = "channel1"

SERVICE_LISTKEY = "kpages_cmd_list"

max_buffer_size = 104857600 * 10


RPC_PORT = 8080
RPC_DIR = ('rpc',)

