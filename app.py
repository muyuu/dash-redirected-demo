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

# redirect vmap
@app.route('/vmap.xml')
def vmap_fn():
    return redirect('https://pubads.g.doubleclick.net/gampad/ads?sz=640x480&iu=/124319096/external/ad_rule_samples&ciu_szs=300x250&ad_rule=1&impl=s&gdfp_req=1&env=vp&output=vmap&unviewed_position_start=1&cust_params=deployment%3Ddevsite%26sample_ar%3Dpreonly&cmsid=496&vid=short_onecue&correlator=')

# redirect VAST in VMAP
@app.route('/redirect_vast.xml')
def use_local_vmap():
    return render_template('vmap_for_redirect_vast.xml')

@app.route('/vast/<path:path>')
def redirect_vast(path):
    param = '?slotname=/124319096/external/ad_rule_samples&sz=640x480&ciu_szs=300x250&cust_params=deployment%3Ddevsite%26sample_ar%3Dpreonly&url=https://imasdk.googleapis.com/&unviewed_position_start=1&output=xml_vast3&impl=s&env=vp&gdfp_req=1&ad_rule=0&useragent=Mozilla/5.0+(Macintosh%3B+Intel+Mac+OS+X+10_15_7)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/97.0.4692.99+Safari/537.36,gzip(gfe)&vad_type=linear&vpos=preroll&pod=1&ppos=1&lip=true&min_ad_duration=0&max_ad_duration=30000&vrid=5776&cmsid=496&video_doc_id=short_onecue&kfa=0&tfcd=0;'
    print(path)
    return redirect('https://pubads.g.doubleclick.net/' + path + param)


if __name__ == '__main__':
    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.load_cert_chain('cert/server-cert.pem', 'cert/server-key.pem')
    app.run(debug=True, host='0.0.0.0', port=2525, ssl_context=ctx)
