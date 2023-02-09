import os
import signal

from behave import *

from dogtail.utils import *
from dogtail import tree 
from dogtail.predicate import GenericPredicate


@when('输入文本 "{text}"')
def step_impl(context, text):
    textbuffer = context.app.findChildren(GenericPredicate(roleName='text'))[-1]
    textbuffer.text = text


@when('点击按钮 "{name}"')
def step_impl(context, name):
    savebutton = context.app.button(name)
    savebutton.click()


@when('选择弹窗 "{dialog_roleName}"')
def step_impl(context, dialog_roleName ):
    context.dialog = context.app.child(roleName=dialog_roleName)


@when('在弹窗中，修改文本框 "{roleName}" 中的内容为 "{text}"')
def step_impl(context, roleName , text):
    context.dialog.child(roleName = roleName).text = text 


@when('在弹窗中，点击对象，名称为 "{roleName}" 描述为 "{des}"')
def step_impl(context, roleName , des):
    context.dialog.child(roleName=roleName , description=des).click()


@when('在弹窗中，点击按钮 "{name}"')
def step_impl(context, name):
    context.dialog.button(name).click()
