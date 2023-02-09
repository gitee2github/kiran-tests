import os
import signal
import re

from behave import *

from dogtail.utils import *
from dogtail import tree 
from dogtail.predicate import GenericPredicate
from dogtail.config import config
from dogtail import rawinput


@given('存在应用程序 "{execname}"')
def step_impl(context,execname):
	ret = os.system("which "+execname+" &>/dev/null")
	if ret != 0:
		assert False 
	else:
		context.execname = execname 

@given('存在name="{name}",roleName="{rolename}",des="{des}",则点击其中 name="{name1}",roleName="{rolename1}",des="{des1}" 元素')
def step_impl(context,name,rolename,des,name1,rolename1,des1):
    if str(name) == 'None':
        name=''
    if str(rolename) == 'None':
        rolename=''
    if str(des) == 'None':
        des=''
    if str(name1) == 'None':
        name1=''
    if str(rolename1) == 'None':
        rolename1=''
    if str(des1) == 'None':
        des1=''

    try:
        obj = context.app.child(name,rolename,des,retry=False)
        obj.child(name1,rolename1,des1).click()
    except tree.SearchError:
        pass
        


@when('打开应用,应用名称为 "{appname}"')
def step_impl(context,appname):
	context.execute_steps('那么 关闭应用 "%s"'%(appname)) 
	
	context.pid = run(context.execname,timeout=5)
	context.app = tree.root.application(appname)


@when('打开应用,全局搜索应用名称为 "{appname}"')
def step_impl(context,appname):
	context.execute_steps('那么 关闭应用 "%s"'%(appname)) 
	
	context.pid = run(context.execname,timeout=5)
	context.app = None 
	apps = tree.root.applications()

	for app in apps:
		if len(app.children) > 0 and app.name == appname:
			context.app = app
			break


@step('休眠 "{sleeptime}" 秒')
def step_impl(context, sleeptime):
    doDelay(float(sleeptime))


@then('打开应用窗口名称为 "{windowname}"')
def step_impl(context,windowname):
        ret = is_windowname(context.app,windowname)
        assert ret


@then('打开应用,其中一个窗口名称为 "{windowname}"')
def step_impl(context,windowname):
	ret = is_framesname(context.app, windowname)
	assert ret


@then('打开的对话框名称为 "{windowname}"')
def step_impl(context,windowname):
	ret = is_dialogname(context.app,windowname)
	assert ret


@then('"{appname}" 应用被打开,打开应用窗口名称为 "{windowname}"')
def step_impl(context, appname, windowname):
	doDelay(2)
	context.execapp = tree.root.application(appname)
	if context.execapp == None:
		assert False
		return False
	
	ret = is_windowname(context.execapp,windowname)
	
	return ret

	
@then('关闭对应应用')
def step_impl(context):
	ret = 1
	if context.app.name == 'Firefox':
		while(1):
			rawinput.keyCombo('<Ctrl>w')
			try:
				context.app.children
			except GLib.Error:
				break
		ret = 0
	else:
		cmd = 'kill -9 %d > /dev/null'%(context.pid)
		ret = os.system(cmd)

	assert ret == 0


@then('关闭应用 "{app}"')
def step_impl(context, app):
	cmd = 'ps -ef | grep %s | grep -v grep > /dev/null'%(app)
	ret = os.system(cmd)
	if ret != 0:
		assert True
	else:
		cmd = 'killall %s > /dev/null'%(app)
		ret = os.system(cmd)
#		assert ret == 0


@then('"{zh_path}" 下存在文件 "{filename}",文件内容为 "{text}"')
def step_impl(context, zh_path, filename, text):
    context.execute_steps('那么 "%s" 下存在文件 "%s"'%(zh_path,filename))
    
    ret = False

    path = behave_deal_path(context, zh_path)
    filepath = os.path.join(path,filename)

    fd = open(filepath)
    fd_text = fd.read()
    if text.strip() == fd_text.strip():
        ret = True
    else:
        ret = False
    fd.close()

    assert ret
    return ret
    
    
@then('"{zh_path}" 下存在文件 "{filename}"')
def step_impl(context, zh_path, filename):
    path = behave_deal_path(context, zh_path)

    filepath = os.path.join(path,filename)
    isfile = os.path.isfile(filepath)
    #os.remove(filepath)

    assert isfile


@then('删除 "{zh_path}" 目录中存在文件 "{filename}"')
def step_impl(context, zh_path, filename):
    path = behave_deal_path(context, zh_path)
    filepath = os.path.join(path,filename)
    isfile = os.path.isfile(filepath)
    os.remove(filepath)


####################################
## TODO: 路径处理函数
#
def behave_deal_path(context, path):
    if '主目录' == path:
        dealPath = os.environ['HOME']
    elif '桌面' == path:
        dealPath = os.environ['HOME'] + '/桌面'
    elif 'dataPath' == path:
        dealPath = context.config.userdata['dataPath']
    elif 'tmpPath' == path:
        dealPath = context.config.userdata['tmpPath']
    else:
        dealPath = path

    return dealPath
    

## TODO: 判断app对象,对话框中是否存在"windowname"名称的窗口
#
def is_dialogname(app,dialogname):
        if app == None:
                assert False
                return False
        if str(dialogname) == 'None':
                assert True
                return True

        ret = False

        dialog = app.dialog(dialogname)
        if dialog != None:
                ret = True

        return ret


## TODO: 模糊匹配.判断app对象,多frame中是否存在"windowname"名称的窗口
#
def is_framesname(app,framename):
        if app == None:
                assert False
                return False
        if str(framename) == 'None':
                assert True
                return True

        ret = False
	
        nameRe = re.compile(framename)
        nameList = nameRe.findall(framename)

        window_frame_list = app.findChildren(predicate.GenericPredicate(roleName='frame'))
        for window_frame in window_frame_list:
            if window_frame != None:
                get_win_name = window_frame.name
                for name in nameList:
                    if name in get_win_name:
                        ret = True
                        break

        return ret


## TODO: 判断app对象,单frame中是否存在"windowname"名称的窗口
#
def is_framename(app,framename):
        if app == None:
                assert False
                return False
        if str(framename) == 'None':
                assert True
                return True

        ret = False
        window = app.window(windowname)
        if window != None:
                ret = True

        return ret


## TODO: 判断app对象中(单frame,dialog，多frame)中是否存在"windowname"名称的窗口
#
def is_windowname(app,windowname):
        if app == None:
                assert False
                return False
        if str(windowname) == 'None':
                assert True
                return True

        ret = False
        window = None

        orig = config.searchCutoffCount
        config.searchCutoffCount=2

        try:
                window = app.window(windowname)
        except tree.SearchError:
                try:
                        window = app.dialog(windowname)
                except tree.SearchError:
                    window_frame_list = app.findChildren(predicate.GenericPredicate(roleName='frame'))
                    for window_frame in window_frame_list:
                        if window_frame != None:
                            get_win_name = window_frame.name
                            if windowname in get_win_name:
                                ret = True
                                break
        if window != None:
                ret = True

        config.searchCutoffCount = orig

        return ret
