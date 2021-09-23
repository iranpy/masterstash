import os
import argparse
import sys

from masterstash.initiator import logger_initiator

class Cli(object):
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        os.environ['SETTINGS_CONF']= kwargs.get('config')
        os.environ['IS_SETTINGS_CONF'] = 'true'
        logger_initiator()
        res = self.run(*args, **kwargs)
        return res

    def run(self, *args, **kwargs):
        raise NotImplementedError('must be implement in subclasses')
    
    def add_preload_params(self, parser):
        parser.add_subparsers()

    def create_parse(self, prog_name):
        parser = argparse.ArgumentParser(prog=prog_name, description='some jobs cli')
        parser.add_argument('-cf', '--config', metavar="DIR",
                            help='Directory of configuration files')
        self.add_commands(parser)
        return parser

    def add_commands(self, parser):
         raise NotImplementedError('must be implement in subclass')

    def execute_cli(self, argv=None, **extra):
        if not argv:
            arg_list = list(sys.argv)
        prog_name = arg_list[0]
        args = arg_list[1:]
        parser = self.create_parse(prog_name)
        options = vars(parser.parse_args(args))
        return self(**options)