from http.server import HTTPServer, BaseHTTPRequestHandler

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>VayuX</title>
<style>
body{
    margin:0;
    background:#000;
    color:white;
    font-family:Arial,sans-serif;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
}
.card{
    text-align:center;
}
img{
    width:300px;
    max-width:90%;
    border-radius:15px;
    box-shadow:0 0 20px #00bfff;
}
h1{
    color:#00bfff;
}
p{
    font-size:22px;
}
</style>
</head>
<body>
<div class="card">
    <img src="/logo.jpg">
    <h1>Welcome to VayuX</h1>
    <p>Shivanshu Jha is the Founder and CEO of VayuX</p>
</div>
</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/logo.jpg":
            with open("logo.jpg","rb") as f:
                self.send_response(200)
                self.send_header("Content-type","image/jpeg")
                self.end_headers()
                self.wfile.write(f.read())
        else:
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(HTML.encode())

print("Open http://127.0.0.1:8000")

HTTPServer(("0.0.0.0",8000), Handler).serve_forever()