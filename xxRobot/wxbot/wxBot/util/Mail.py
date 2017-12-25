#!/usr/bin/env python
# coding: utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import time
import base64

from util import ZkCli

class Mail(object):



    ISOTIMEFORMAT = "%Y-%m-%d %X"
    HOST = "smtp.mxhichina.com"
    SUBJECT = u"微信登录"+"("+time.strftime( ISOTIMEFORMAT, time.localtime() )+")"
    TO = "chaojiang@deepbaytech.com"
    FROM = "chaojiang@deepbaytech.com"

    @staticmethod
    def addimg(src,imgid):
        fp = open(src, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', imgid)
        return msgImage

    @staticmethod
    def printBase64(src):
        f = open(src, 'rb')
        ls_f=base64.b64encode(f.read())
        f.close()
        print ls_f
        zk = ZkCli.pushImg(ls_f)
        # zk.stop()


    @staticmethod
    def send(path):

        msg = MIMEMultipart('related')
        msgtext = MIMEText("<font color=blue>请使用手机微信扫描登录:<br><img src=\"cid:wxlogin\" border=\"1\">","html","utf-8")
        msg.attach(msgtext)
        msg.attach(Mail.addimg(path,"wxlogin"))

        #发送
        msg['Subject'] = Mail.SUBJECT
        msg['From']=Mail.FROM
        msg['From']=Mail.FROM
        msg['To']=Mail.TO
        try:
            server = smtplib.SMTP()
            server.connect(Mail.HOST,"25")
            #server.starttls()
            server.login("chaojiang@deepbaytech.com","Xizil000")
            server.sendmail(Mail.FROM, Mail.TO, msg.as_string())
            server.quit()
            print "邮件发送成功！"
        except Exception, e:
            print "失败："+str(e)

if __name__ == '__main__':
    Mail.send()