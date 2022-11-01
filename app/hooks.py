from flask import Flask, request, g, abort
app=Flask(__name__)

@app.after_request
def after_request(response):
    print("after_request() called")
    return response

@app.errorhandler(404)
def http_404_handler(error):
    return "<p>HTTP 404 Error Encountered</p>", 404

@app.errorhandler(500)
def http_500_handler(error):
    return "<p>HTTP 500 Error Encountered</p>", 500

@app.route("/")
def index():
    # print("index() called")
    # return '<p>Testings Request Hooks</p>'
    abort(500)

if __name__ == "__main__":
    app.run(debug=True)
    
      