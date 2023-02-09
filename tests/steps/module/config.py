# -*- coding: utf-8 -*-
import os
try:
    import configparser
except:
    import ConfigParser as configparser


class MyConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr

class Config():
    version = ''
    sysPath = {'rootPath':''
            ,'configFile':''
            ,'dataPath':''
#            ,'pkgPath':''
            }

    py2_RPMS = [] 
    py2_PIPS = []
    py3_PIPS = [] 

    def __init__(self, rootPath, version):
        Config.sysPath['rootPath'] = rootPath 
        Config.version = version 

    def __is_valid(self):
        for path in Config.sysPath.values():
            if os.path.isdir(path) is False:
                if os.path.isfile(path) is False:
                    print('%s: No such file or directory'%(path))
                    return False

        for rpmPath in Config.get_py2_rpms_path():
            if os.path.isfile(rpmPath) is False:
                print('%s: No such file'%(rpmPath))
                return False

        for pipPath in Config.get_py2_pips_path():
            if os.path.isfile(pipPath) is False:
                print('%s: No such file'%(pipPath))
                return False

        for pipPath in Config.get_py3_pips_path():
            if os.path.isfile(pipPath) is False:
                print('%s: No such file'%(pipPath))
                return False

        return True

    def load_config(self, configName):
        rootPath = Config.sysPath['rootPath']
        configFile = os.path.join(rootPath, configName)
        if os.path.isfile(configFile) is False:
            return False
        Config.sysPath['configFile'] = configFile

        cf = MyConfigParser()
        cf.read(configFile)

        dataName = cf.get('behave.userdata','dataName')
#        Config.sysPath['dataPath'] = os.path.join(rootPath, '../' + dataName)
        Config.sysPath['dataPath'] = cf.get('behave.userdata','dataPath')

#        pkgName = cf.get('behave.userdata','pkgName')
#        Config.sysPath['pkgPath'] = os.path.join(rootPath,pkgName) 
       
#        tmplist = cf.get('cattail','py2_rpms').split(',')
#        for tmpobj in tmplist:
#            Config.py2_RPMS.append(tmpobj.strip())

#        tmplist = cf.get('cattail','py2_pips').split(',')
#        for tmpobj in tmplist:
#           Config.py2_PIPS.append(tmpobj.strip())

#        tmplist = cf.get('cattail','py3_pips').split(',')
#        for tmpobj in tmplist:
#            Config.py3_PIPS.append(tmpobj.strip())

        ret = self.__is_valid()
        if ret is True:
            cf.set('behave.userdata', 'dataPath', Config.sysPath['dataPath'])
            tmpName = cf.get('behave.userdata','tmpName')
            cf.set('behave.userdata', 'tmpPath', os.path.join(rootPath, tmpName))

            fd = open(configFile, 'w')
            cf.write(fd)
            fd.close()

        return ret
        
    @classmethod
    def get_version(cls):
        return cls.version

    @classmethod
    def get_root_path(cls):
        return cls.sysPath['rootPath']

    @classmethod
    def get_data_path(cls):
        return cls.sysPath['dataPath']

#    @classmethod
#    def get_pkg_path(cls):
#        return cls.sysPath['pkgPath']
    
    @classmethod
    def get_py2_rpms_path(cls):
        rpmList = []

        for rpmName in Config.py2_RPMS:
            rpmPath = os.path.join(Config.get_pkg_path(), rpmName) 
            rpmList.append(rpmPath)

        return rpmList
    
    @classmethod
    def get_py2_pips_path(cls):
        pipList = []

        for pipName in Config.py2_PIPS:
            pipPath = os.path.join(Config.get_pkg_path(), pipName) 
            pipList.append(pipPath)

        return pipList
    
    @classmethod
    def get_py3_pips_path(cls):
        pipList = []

        for pipName in Config.py3_PIPS:
            pipPath = os.path.join(Config.get_pkg_path(), pipName) 
            pipList.append(pipPath)

        return pipList
