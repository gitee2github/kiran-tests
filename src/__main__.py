#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse

sys.path.append(os.path.dirname(__file__) + '/../tests/steps/module')

import usage,config

CATTAIL_CONFIG= 'behave.ini'
CATTAIL_VERSION='1.0.0'

def main():
    cfg = config.Config(os.path.dirname(__file__) + '/../tests/', CATTAIL_VERSION)
    print(os.path.dirname(__file__) + '/../tests/')
    if cfg.load_config(CATTAIL_CONFIG) is False:
        sys.exit(1)

    parser = argparse.ArgumentParser()
    arg = usage.Args(parser)
    ret = arg.analyze()
    
    sys.exit(ret)

if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    main()
    
