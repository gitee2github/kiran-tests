import os
import shutil 
import sys
import signal

sys.path.append(os.path.dirname(__file__) + '/steps/module')
import mybehave

from dogtail import tree
from dogtail.utils import *


def before_feature(context, feature):
    mybehave.set_node(context,None)

def before_all(context):
	try:
	    import sys
	    reload(sys)
	    sys.setdefaultencoding('utf8')
	except NameError:
	    import importlib
	    importlib.reload(sys)

	cmd = 'gsettings set org.gnome.desktop.a11y.applications screen-reader-enabled true'
	os.system(cmd)
	
#	context.config.userdata['dataPath']=os.path.join(os.getcwd(),context.config.userdata['dataName'])
	if os.path.isdir(context.config.userdata['dataPath']):
		assert True
	else:
		assert False

#	context.config.userdata['tmpPath']=os.path.join(os.getcwd(),context.config.userdata['tmpName'])
	if os.path.exists(context.config.userdata['tmpPath']):
		shutil.rmtree(context.config.userdata['tmpPath'])	
	os.makedirs(context.config.userdata['tmpPath'])

def after_all(context):
	if os.path.exists(context.config.userdata['tmpPath']):
		shutil.rmtree(context.config.userdata['tmpPath'])	
