import os
import vcs_wrapper
import sqlite3

class svn_wrapper(vcs_wrapper.vcs_wrapper):
    def __init__(self):
        pass

    def init(self):
        pass

    def checkout(self, url, dest, username=None, password=None):

        url = url + '/trunk'

        self.do_command('checkout', [url, dest], username, password)

    def add(self, targets, username=None, password=None):
        self.do_command('add', [targets], username, password)

    def rm(self, targets, username=None, password=None):
        self.do_command('rm', [targets], username, password)

    def commit(self, msg, username=None, password=None):
        msg = '-m \"' + msg + '\"'
        self.do_command('commit', [msg], username, password)
        pass

    def push(self):
        pass

    def update(self, username=None, password=None):
        self.do_command('update', [], username, password)

    def revert(self):
        pass

    def do_command(self, command, parameters=[], username=None, password=None):
        vcs = 'svn '
        vcs_command = command + ' '

        parameter_str = ''

        for p in parameters:
            parameter_str = parameter_str + p + ' '

        options = " --non-interactive --trust-server-cert -q "

        if username is None:
            username = ''
        else:
            username = '--username ' + username + ' '

        if password is None:
            password = ''
        else:
            password = '--password ' + password + ' '


        command = vcs + vcs_command + parameter_str + options + username + password

        os.system(command)