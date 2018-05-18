from flask import Flask, g


app = Flask(__name__)
app.config['SERVER_NAME'] = 'example.com:5000'


@app.url_value_preprocessor
def get_site(endpoint, values):
    g.site = values.pop('subdomain')
    # g.site = None
    
    
@app.route('/', subdomain='<subdomain>')
def index():
    return g.site
