#!/usr/bin/env python
# coding: utf-8
#
import json
from wxbot import *
import urllib3
urllib3.disable_warnings()
import requests
import stt
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class MyWXBot(WXBot):

    short_url_host = u"http://ypurl.cn"
    short_url_getUrl = short_url_host+u"/short-url"

    def handle_msg_all(self, msg):

        # if 'user' in msg['content'] and len(msg['content']['user']['name'])>3 and msg['content']['user']['name'][0:4] == u'dyyp':


        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            #self.send_msg_by_uid(u'hi', msg['user']['id'])
            self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            #self.send_file_msg_by_uid("img/1.png", msg['user']['id'])


        # 给自己发
        elif msg['msg_type_id'] == 1 and msg['content']['type'] == 3:
            print self.get_msg_img(msg['msg_id'])
            # text =  stt.speech_file_to_text(u"temp/"+self.get_msg_img(msg['msg_id']))
            # url = u"http://m.dayuyoupin.com/getSearchImage?searchCode=" + text+"&pageId=0"
            # r = requests.post(u"http://ypurl.net/short-url", {'url':url})
            # self.send_msg_by_uid(r.text, msg['user']['id'])
            #files = {'file': open(u"temp/"+self.get_msg_img(msg['msg_id']), 'rb')}
            # r = requests.post("http://search.deepbaytech.com/upimage", data={}, files=files)
            # print r.content
            # data = json.loads(r.content)
            # url = u"http://search.deepbaytech.com/search?tfsid=" + data['data']
            # r = requests.post(u"http://ypurl.net/short-url", {'url':url})
            # self.send_msg_by_uid(r.text, msg['user']['id'])
            #self.send_img_msg_by_uid(u"temp/"+self.get_msg_img(msg['msg_id']), msg['user']['id'])

        elif msg['msg_type_id'] == 1 and msg['content']['type'] == 0 and msg['content']['data'][0:2] == u'搜索':
            r = requests.post(self.short_url_getUrl, {'url':u'http://m.dayuyoupin.com/search?text='+msg['content']['data'][2:]+u"&pageId=0"})

            self.send_msg_by_uid(r.text, msg['user']['id'])



        elif msg['msg_type_id'] == 1 and msg['content']['type'] == 4 :
            # files = {'file': open(u"temp/"+self.get_voice(msg['msg_id']), 'rb')}
            # stream = ffmpeg.input(u"temp/"+self.get_voice(msg['msg_id']))
            # # stream = ffmpeg.hflip(stream)
            # stream = ffmpeg.filter_(stream,'acodec',"pcm_s16le")
            # stream = ffmpeg.filter_(stream,'f',"s16le")
            # stream = ffmpeg.filter_(stream,'ac',1)
            # stream = ffmpeg.filter_(stream,'ar',16000)
            # stream = ffmpeg.output(stream,u"temp/"+msg['msg_id']+".pcm")
            # ffmpeg.run(stream)
            # print msg

            print self.get_msg_img(msg['msg_id'])
            text = stt.speech_file_to_text(u"temp/"+self.get_voice(msg['msg_id']))
            url = u"http://m.dayuyoupin.com/search?text=" + text.decode("utf-8")[0:2]+"&pageId=0"
            print url
            # url = u"http://m.dayuyoupin.com/search?text=1111&pageId=0"
            r = requests.post(self.short_url_getUrl, {'url':url})
            print r.text
            self.send_msg_by_uid(r.text, msg['user']['id'])


        elif msg['msg_type_id'] == 3 and msg['content']['type'] == 4 :
            # print self.get_msg_img(msg['msg_id'])
            text = stt.speech_file_to_text(u"temp/"+self.get_voice(msg['msg_id']))


            text = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"),text.decode("utf-8"))

            url = u"http://m.dayuyoupin.com/search?text=" + text+"&pageId=0"

            # print url
            # url = u"http://m.dayuyoupin.com/search?text=1111&pageId=0"
            r = requests.post(self.short_url_getUrl, {'url':url})
            # print r.text
            self.send_msg_by_uid(r.text, msg['user']['id'])

        elif msg['msg_type_id'] == 3 and msg['content']['type'] == 3:
            print self.get_msg_img(msg['msg_id'])
            files = {'file': open(u"temp/"+self.get_msg_img(msg['msg_id']), 'rb')}
            r = requests.post("http://search.deepbaytech.com/upimage", data={}, files=files)
            print r.content
            data = json.loads(r.content)
            url = u"http://m.dayuyoupin.com/getSearchImage?searchCode=" + data['data']+"&pageId=0"
            r = requests.post(self.short_url_getUrl, {'url':url})
            self.send_msg_by_uid(r.text, msg['user']['id'])

        elif msg['msg_type_id'] == 3 and msg['content']['type'] == 0 and msg['content']['data'][0:2] == u'搜索':
            # print u'http://search.deepbaytech.com/s?text='+msg['content']['data'][2:]
            r = requests.post(self.short_url_getUrl, {'url':u'http://m.dayuyoupin.com/search?text='+msg['content']['data'][2:]+u"&pageId=0"})

            self.send_msg_by_uid(r.text, msg['user']['id'])



'''
    def schedule(self):
        self.send_msg(u'张三', u'测试')
        time.sleep(1)
'''


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()
