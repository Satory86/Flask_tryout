from flask import Flask, Markup
app=Flask(__name__)
@app.route('/')
def hello_world():
    return Markup("&lt;p&gt;Hello docent Peter! Na veel problemen met running flask maak ik deze les na bijna 8 uur af!!&lt;/p&gt;")
if __name__== '__main__':
    app.run(poort=5000, debug=True)
