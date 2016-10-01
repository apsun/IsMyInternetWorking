#!/usr/bin/env python3
import os
import cherrypy

class Server:
    @cherrypy.expose
    def index(self):
        return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Is my internet working?</title>
    <style type="text/css">
        #text {
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            font-family: "Georgia", sans-serif;
            font-size: 96pt;
            text-align: center;
        }
    </style>
</head>
<body>
    <span id="text">Yes.</span>
</body>
</html>
"""

if __name__ == "__main__":
    cherrypy.tree.mount(Server(), "/")
    cherrypy.config.update({
        "server.socket_host": "0.0.0.0",
        "server.socket_port": int(os.environ.get("PORT", "8080"))
    })
    cherrypy.engine.start()
    cherrypy.engine.block()
