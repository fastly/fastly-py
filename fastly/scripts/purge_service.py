import sys, fastly

def purge_service():
  if len(sys.argv) < 3:
    print "not enough arguments!"
    exit()
  else:
    auth_key = sys.argv[1]
    svc_key = sys.argv[2]

  api = fastly.API()
  api.authenticate_by_key(auth_key)
  api.purge_service(svc_key)

