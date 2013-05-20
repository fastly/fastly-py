import sys, fastly

def purge_url():
  if len(sys.argv) < 4:
    print "not enough arguments!"
    exit()
  else:
    auth_key = sys.argv[1]
    url_host = sys.argv[2]
    url_path = sys.argv[3]

  api = fastly.API()
  api.authenticate_by_key(auth_key)
  api.purge_url(url_host,url_path)

