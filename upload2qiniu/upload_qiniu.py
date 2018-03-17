# -*- coding: utf-8 -*-
from datetime import datetime
import smtplib
from email.header import Header
from email.mime.text import MIMEText

from config import EMAIL_PWD, EMAIL_PORT, EMAIL_HOST, EMAIL_ACCOUNT, RECV_ACCOUNT, Access_Key, Secret_Key, Bucket_Name


def upload_file(file_name):
    from qiniu import Auth, put_file, etag
    # 需要填写你的 Access Key 和 Secret Key
    access_key = Access_Key
    secret_key = Secret_Key
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = Bucket_Name
    # 上传到七牛后保存的文件名
    key = file_name
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    # 要上传文件的本地路径
    localfile = file_name
    ret, info = put_file(token, key, localfile)
    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)


import os, os.path
import zipfile


def zip_dir(dirname, zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        # print arcname
        zf.write(tar, arcname)
    zf.close()


# 生成upload文件夹的zip
def gen_upload_zip():
    zip_dir('E:/python/learning', 'E:/python/learning/zip.zip')
    return 'E:/python/learning/zip.zip'


# 按时间生成的几个文件
def gen_backup_name():
    now = datetime.now()
    prefix_name = "%04d-%02d-%02d@04_00" % (now.year, now.month, now.day)
    return [
               prefix_name + ".properties",
               prefix_name + ".zip",
               # prefix_name + "FanRuanReport.zip"
           ], now


def send_alert_mail(sub, content, to_list):
    # Create SMTP Object
    smtp = smtplib.SMTP()
    print 'connecting ...'

    # show the debug log
    smtp.set_debuglevel(1)

    # connet
    try:
        print smtp.connect(EMAIL_HOST, EMAIL_PORT)
    except:
        print 'CONNECT ERROR ****'
    # gmail uses ssl
    smtp.starttls()
    # login with username & password
    try:
        print 'loginning ...'
        smtp.login(EMAIL_ACCOUNT, EMAIL_PWD)
    except:
        print 'LOGIN ERROR ****'
    # fill content with MIMEText's object
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = '%s <%s>' % (EMAIL_ACCOUNT, EMAIL_ACCOUNT)
    msg['To'] = '%s <%s>' % (to_list, to_list)
    msg['Subject'] = Header(sub, 'utf8').encode()
    print msg.as_string()
    smtp.sendmail(EMAIL_ACCOUNT, to_list, msg.as_string())
    smtp.quit()


if __name__ == "__main__":
    try:
        lst_file_name, now = gen_backup_name()
        for file_name in lst_file_name:
            upload_file("D:\Seeyon\A8\Backup\%d\%d/" % (now.year, now.month) + file_name)
    except:
        send_alert_mail("告警", "备份到七牛云失败", RECV_ACCOUNT)
