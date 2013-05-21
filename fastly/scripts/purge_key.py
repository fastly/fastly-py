import sys, fastly

def purge_key():
  if len(sys.argv) < 4:
    print "not enough arguments!"
    exit()
  else:
    auth_key = sys.argv[1]
    svc_key = sys.argv[2]
    purge_key = sys.argv[3]

  api = fastly.API()
  api.authenticate_by_key(auth_key)
  api.purge_key(svc_key, purge_key)

