# -*- coding: utf-8 -*-
from qiniu import Auth, put_file

access_key = '2ADNY-ZDGQLg7kO0kR76HKescEULSynwPntZotb2'
secret_key = 'W-72fNXMzWsGuuGVqk52nZ6Ftha89GLEeuxTMTPi'
bucket_name = 'whthas'


q = Auth(access_key, secret_key)
PostFile = u'测试.txt'

token = q.upload_token(bucket_name, PostFile)
FilePath = u'.\\测试.txt'

ret, info = put_file(token, PostFile, FilePath)

