# -*- coding: utf-8 -*-

## 获取当前需要进行操作Node
#
def get_node(context):
    curnode = None
    if context.curNode is None:
        curnode = context.app
    else:
        curnode = context.curNode

    return curnode

## 获取当前需要进行操作Node
#
def set_node(context, curNode):
    context.curNode = curNode
