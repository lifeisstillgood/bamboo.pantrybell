

"""
Pantry Bell is a really simple protoypte / throwaway but it is intedned to 
solve a real problem - I want an image of a serever in cloud to be reloaded, and then call out back.



"""

import datetime
from flask import Flask
app = Flask(__name__)

@app.route("/pantrybell/<key>/<hostname>")
def callback(key, hostname):

    open("/tmp/foo.txt", "a").write("%s:%s\n" % (key, hostname))
    return (None, 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
