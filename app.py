from sanic import Sanic
from sanic.response import json, html
import flag

app = Sanic('binchk-app')


INDEX = '''
    <html>
        <body>
            <h1>BIN CHK API!</h1>
            <h3>Stable bin Database</h3>

        </body>
    </html>
    '''


@app.route('/')
def index(request):
    return html(INDEX)


@app.route('/flag=<query>')
def binn(request, query):
    data = flag.flag(code)    
    return data


    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
