from flask import Flask, render_template, redirect
import ssl

app = Flask(__name__)

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = "*"
    return response

@app.route('/redirect.mpd')
def redirect_fn():
    return redirect('https://dash.akamaized.net/akamai/bbb_30fps/bbb_30fps.mpd')

@app.route('/manifest.mpd')
def manifest():
    return render_template('bbb_30fps.mpd')

@app.route('/segment/<path:path>')
def segment_fn(path):
    print(path)
    return redirect('https://dash.akamaized.net/akamai/bbb_30fps/' + path)

if __name__ == '__main__':
    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.load_cert_chain('cert/server-cert.pem', 'cert/server-key.pem')
    app.run(debug=True, host='0.0.0.0', port=2525, ssl_context=ctx)
