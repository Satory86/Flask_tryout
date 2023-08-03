from flask import Flask, Markup
app=Flask(__name__)
@app.route('/')
def hello_world():
    return Markup("&lt;p&gt;Hello World!&lt;/p&gt;")
if __name__== '__main__':
    app.run(poort=5000, debug=True)
