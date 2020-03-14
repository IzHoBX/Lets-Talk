import http.server
import socketserver
import KeywordExtract.ExtractKeyword
import EmojiText.EmojiVec
import requests
import urllib
import json
import socket
import os

from http.server import BaseHTTPRequestHandler, HTTPServer

PREFIX = "/agent?sentence="
RETURN_LIMIT = 5

def takeScore(x):
    return x[1]

class MyHandler(BaseHTTPRequestHandler):

    emoji2Vec = EmojiText.EmojiVec.EmojiVec()

    def do_GET(self):
        sentence = self.getSentence(self.path)

        ans = []
        for word in KeywordExtract.ExtractKeyword.extractKeyword(sentence):
            link, score =self.emoji2Vec.getEmoji(word)
            ans.append((link, score))
        if len(ans) > RETURN_LIMIT:
            ans.sort(reverse=True, key=takeScore)
            ans = ans[:RETURN_LIMIT]

        x = {}
        for i in range(0, len(ans)):
            x[str(i)] = ans[i][0]
        x = json.dumps(x)

        self.send_response(200)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(bytes(x,"utf-8"))
        self.wfile.close()


        return

    def getSentence(self, inx):
        inx = inx[len(PREFIX):]
        for i in range(0, len(inx)):
            if inx[i] == "+":
                inx = inx[:i]+ " "+inx[i+1:]
        return inx




def main():

    print('starting server on port ' + os.environ.get("PORT", 7777) + "...")

    server_address = (socket.gethostbyname("text-emoji2.herokuapp.com"), os.environ.get("PORT", 7777))
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()

    url = "http://localhost:8081/agent"
    dara = urllib.parse.urlencode({"sentence":"I am happy"})

main()
