import os
import signal
import sys

sys.path.append(os.path.dirname(__file__) + '/../../module')
import mybehave

from behave import *

from dogtail.utils import *
from dogtail import tree 
from dogtail.predicate import GenericPredicate


@step('设置后续操作节点为当前应用')
def step_impl(context):
    mybehave.set_node(context, context.app) 


@step('设置后续操作节点为name="{name}",roleName="{rolename}",des="{des}"')
def step_impl(context, name, rolename, des):
    if str(name) == 'None':
        name=''
    if str(rolename) == 'None':
        rolename=''
    if str(des) == 'None':
        des=''

    child = context.app.findChild(predicate.GenericPredicate(name=name, roleName=rolename, description=des))	
    mybehave.set_node(context, child) 


@when('选择元素name="{name}",roleName="{rolename}",des="{des}",输入文本 "{text}"')
def step_impl(context, name, rolename, des, text):
	if str(name) == 'None':
		name=''
	if str(rolename) == 'None':
		rolename=''
	if str(des) == 'None':
		des=''

#	textbuffer = context.app.findChild(predicate.GenericPredicate(name=name, roleName=rolename, description=des))	
	textbuffer = mybehave.get_node(context).findChild(predicate.GenericPredicate(name=name, roleName=rolename, description=des))	
	textbuffer.text = text


@when('选择元素name="{name}",roleName="{rolename}",des="{des}",并且 "{clickFlag}" 击 "{btnFlag}" 键')
def step_impl(context, name, rolename, des, clickFlag, btnFlag):
	if str(name) == 'None':
		name=''
	if str(rolename) == 'None':
		rolename=''
	if str(des) == 'None':
		des=''

	#button = context.app.findChild(predicate.GenericPredicate(name=name, roleName=rolename, description=des))
	button = mybehave.get_node(context).findChild(predicate.GenericPredicate(name=name, roleName=rolename, description=des))
	if clickFlag == '单' and btnFlag == '左':
		button.click()
	elif clickFlag == '双' and btnFlag == '左':
		button.doubleClick()
	elif clickFlag == '单' and btnFlag == '右':
		button.click(3)
	elif clickFlag == '双' and btnFlag == '右':
		button.click(3)


@when('在路径选择窗口中进入 "{path}" 目录')
def step_impl(context, path):
	if path == 'dataPath':
		newpath = context.config.userdata['dataPath']
	elif path == 'tmpPath':
		newpath = context.config.userdata['tmpPath']

	context.execute_steps('当 选择元素name="%s",roleName="label",des="None",并且 "单" 击 "左" 键'%(u"其他位置"))
	context.execute_steps('当 选择元素name="%s",roleName="label",des="None",并且 "单" 击 "左" 键'%(u'计算机'))
	
	for split in newpath.split('/'): 
		if split == '':
			continue

		if hasattr(split,'decode'):
        		context.execute_steps('当 选择元素name="%s",roleName="table cell",des="None",并且 "双" 击 "左" 键'%(split.decode('gbk')))
		else:
        		context.execute_steps('当 选择元素name="%s",roleName="table cell",des="None",并且 "双" 击 "左" 键'%(split))


@then('存在元素name="{name}",roleName="{rolename}",des="{des}",文本不等于 "{text}"')
def step_impl(context, name, rolename, des, text):
	if str(name) == 'None':
		name=''
	if str(rolename) == 'None':
		rolename=''
	if str(des) == 'None':
		des=''

	#child = context.app.findChild(predicate.GenericPredicate(name=name, roleName=rolename, description=des))	
	child = mybehave.get_node(context).findChild(predicate.GenericPredicate(name=name, roleName=rolename, description=des))	
	if child.text != str(text):
		ret = True
	else:
		ret = False

	assert ret


@then('存在元素name="{name}",roleName="{rolename}",des="{des}",文本等于 "{text}"')
def step_impl(context, name, rolename, des, text):
	if str(name) == 'None':
		name=''
	if str(rolename) == 'None':
		rolename=''
	if str(des) == 'None':
		des=''

	#child = context.app.findChild(predicate.GenericPredicate(name=name, roleName=rolename, description=des))	
	child = mybehave.get_node(context).findChild(predicate.GenericPredicate(name=name, roleName=rolename, description=des))	
	if child.text == str(text):
		ret = True
	else:
		ret = False

	assert ret


@then('"{flag}" 在元素name="{name}",roleName="{rolename}",des="{des}"')
def step_impl(context, flag, name, rolename, des):
    if str(name) == 'None':
        name=''
    if str(rolename) == 'None':
        rolename=''
    if str(des) == 'None':
        des=''

    ret = False

    try:
        #child = context.app.findChild(predicate.GenericPredicate(name=name, roleName=rolename, description=des))
        child = mybehave.get_node(context).findChild(predicate.GenericPredicate(name=name, roleName=rolename, description=des))
        if child != None:
            ret = True
    except tree.SearchError:
        ret = False
    
    if flag == '不存':
        ret = not ret
        
    assert ret 
