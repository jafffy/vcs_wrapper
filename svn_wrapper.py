import os
import vcs_wrapper
import sqlite3

class svn_wrapper(vcs_wrapper.vcs_wrapper):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.conn = sqlite3.connect('transaction.db')

    def init(self):
        pass

    def checkout(self, url, dest):

        url = url + '/trunk'

        self.do_command('checkout', [url, dest])

    def add(self, targets):
        self.do_command('add', [targets])

    def rm(self, targets):
        self.do_command('rm', [targets])

    def commit(self, msg):
        msg = '-m \"' + msg + '\"'
        self.do_command('commit', [msg])
        pass

    def push(self):
        pass

    def update(self):
        self.do_command('update', [])

    def revert(self):
        pass

    def do_command(self, command, parameters=[]):
        username = self.username
        password = self.password

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