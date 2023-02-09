import os
import signal

from behave import *

from dogtail.utils import *
from dogtail import tree 
from dogtail.predicate import GenericPredicate
from dogtail.config import config


@then('"{label}" 为 "{productName}"')
def step_impl(context, label, productName):
	product = context.app.child(name=label,roleName='label')
	parent = product.parent
	if product == None or parent == None :
		assert False
		return False
	ret = False

	tmpobj = parent.child(name=productName,roleName='label')
	if tmpobj != None:
		ret = True


	assert ret
	return ret


@then('产品版本同.kyinfo保持一致')
def step_impl(context):
	product = context.app.child(name='产品版本:',roleName='label')
	parent = product.parent
	if product == None or parent == None :
		assert False
		return False
	ret = False

	childs = parent.findChildren(predicate.GenericPredicate(roleName='label'))
	for child in childs:
		if child.name != '产品版本:':
			version = child.name
	
	cmd = 'cat /etc/.kyinfo | grep "milestone = %s" > /dev/null'%(version)
	if os.system(cmd) == 0:
		ret = True 

	assert ret
	return ret

@then('注册状态包含 "{state}" 字眼时,质保期显示 "{deadline}"')
def step_impl(context, state, deadline):
    stateStrObj = context.app.child(name='注册状态:',roleName='label')
    parent = stateStrObj.parent
    if stateStrObj == None or parent == None :
        assert False
        return False
    ret = False
    
    childs = parent.findChildren(predicate.GenericPredicate(roleName='label'))
    for child in childs:
        if str(state) in child.name:
            deadlineObj = context.app.child(name='质保期:',roleName='label').parent.findChild(predicate.GenericPredicate(name=deadline,roleName='label'))
            if deadlineObj != None:
                ret = True
        else:
            ret = True
    
    assert ret
    return ret
