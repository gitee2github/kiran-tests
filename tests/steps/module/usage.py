# -*- coding: utf-8 -*-
import os 
import sys
import argparse

import config

class Args():
    def __init__(self, parser):
        self.parser = parser
        self.__add_parse()

        self.args = self.__parse_args() 

    def __add_parse(self):
        self.parser.add_argument('-v', '--version', action='version', version=self.arg_version(),help='版本信息')

        sub_parser = self.parser.add_subparsers(help='sub-command help')
#        install_parser = sub_parser.add_parser("install", help="安装依赖包")
#        install_parser.set_defaults(func=self.arg_install)

        behave_parser = sub_parser.add_parser("behave", help="behave BDD")
        behave_parser.add_argument("-p", "--parameter", help="behave 参数 \"-f rerun -o xxx.out\"")
        behave_parser.set_defaults(func=self.arg_behave)

    def __parse_args(self):
        return self.parser.parse_args()
        
    def arg_version(self):
        return config.Config.get_version() 

    def arg_behave(self):
        ret = True 

        cmd = 'gsettings set org.gnome.desktop.interface toolkit-accessibility true'
        os.system(cmd)
        
        if self.args.parameter is None:
            cmd = 'behave'
        else:
            cmd = 'behave ' + self.args.parameter

        ret = os.system(cmd)
        if ret == 0:
            ret = True
        else:
            ret = False

        return ret 

#    def arg_install(self):
#        ret = True 

#        py_version = sys.version_info
#        if py_version < (3,0):
#            rpmList = config.Config.get_py2_rpms_path()
#            cmd='rpm -ivh --replacepkgs ' + ' '.join(rpmList)
#            os.system('echo '+cmd)
#            if os.system(cmd) != 0:
#                print('ERROR:python2 install rpms')
#                return False

#            pipList = config.Config.get_py2_pips_path()
#            cmd='pip install ' + ' '.join(pipList)
#        elif py_version > (3,0):
#            pipList = config.Config.get_py3_pips_path()
#            cmd='pip3 install ' + ' '.join(pipList)

#        if os.system(cmd) != 0:
#            print('ERROR:python install pips')
#            ret = False
#        else:
#            ret = True

#        if ret is True:
#            print("\n安装成功!")
#        else:
#            print("\n安装失败...")
            
#        sys.exit(not ret)

    def analyze(self):
        self.args.func() 
        return True
