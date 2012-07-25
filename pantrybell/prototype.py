
"""
Pantry Bell is a really simple protoypte / throwaway but it is
intedned to solve a real problem - I want an image of a serever in
cloud to be reloaded, and then call out back.



"""

import datetime
from flask import Flask
import rackspace
import requests

from rhaptos2.common import conf
confd = conf.get_config("pantrybell")

class PantryBellError(Exception):
    pass

app = Flask(__name__)


    #jobname:([servers_to_reimage], jenkins_job_after)
LOOKUP={'test': (['www-baseserver',], "http://jenkins.frozone.mikadosoftware.com:8080/job/build_racksapce_devweb/build"),
       }

messageq = {'www': "http://jenkins.frozone.mikadosoftware.com:8080/job/build_racksapce_devweb/build"} 

@app.route("/pantrybell/<key>/<hostname>")
def callback(key, hostname):
    if key != confd['pantrybell_secretkey']:
        raise PantryBellError("secret key failed to match")
    open("/tmp/foo.txt", "a").write("\n%s:%s" % (key, hostname))
    jenkinsjob = messageq[hostname]
    open("/tmp/foo.txt", "a").write("\ncalling %s" % jenkinsjob)
    requests.get(jenkinsjob)
    return ("", 200)

@app.route("/pantrybell/job/<jobname>")
def startjob(jobname):
    reimage, jenkinscall = LOOKUP[jobname]
    rackspace.reimage_server(reimage[0])    
    messageq["www"] = jenkinscall
    return repr(messageq)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
