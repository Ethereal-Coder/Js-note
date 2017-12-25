#!/usr/bin/env python
# coding: utf-8

from kazoo.client import KazooClient

import logging
from sys import argv

logging.basicConfig()
script, uuid = argv

zk = KazooClient(hosts='192.168.1.155:2181')

zk.start()

# 微信zk节点路径
WX_NODE_PATH = "deepbay/wx"
# 子节点路径
WX_THE_NODE_PATH = WX_NODE_PATH + "/nodes/" + uuid
# 子节点命令路径
WX_COMMAND_PATH = WX_NODE_PATH + "/commands/" + uuid
# 子节点图片路径
WX_PICTURE_PATH = WX_NODE_PATH + "/images/" + uuid

wx_states = {"login": b"login", "logined": b"logined"}

"""推送图片到zk服务器"""


def pushImg(baseImg):
    try:

        # Ensure a path, create if necessary
        zk.ensure_path(WX_NODE_PATH)

        # Create a node with data
        zk.create(WX_THE_NODE_PATH, wx_states["login"], ephemeral=True, makepath=True)

        zk.create(WX_COMMAND_PATH, ephemeral=True, makepath=True)
        # Create a node with data
        zk.create(WX_PICTURE_PATH, bytes(baseImg), ephemeral=True, makepath=True)
    except Exception as e:
        print "error:", repr(e)



def updateState(newState):
    try:
        zk.set(WX_THE_NODE_PATH, newState)
    except Exception as e:
        print "error:", repr(e)

def stop():
    zk.stop()
