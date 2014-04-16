from flask import Flask
from flask import request, Response

import xmltodict
import requests
import json

app = Flask(__name__)

@app.route('/ssr')
def ssrSok():
    query = request.args.get('q', '')
    print 'https://ws.geonorge.no/SKWS3Index/ssr/sok?navn='+query+'*&antPerSide=9&epsgKode=4258&eksakteForst=true'
    r = requests.get('https://ws.geonorge.no/SKWS3Index/ssr/sok?navn='+query+'*&antPerSide=9&epsgKode=4258&eksakteForst=true', verify=False)
    print r
    doc = xmltodict.parse(r.text)
    js = json.dumps(doc)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.debug = True
    app.run()


