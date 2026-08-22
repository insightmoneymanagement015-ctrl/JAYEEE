from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from blockchain import Blockchain


blockchain = Blockchain()


class NodeHandler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):
        response = json.dumps(data, indent=2).encode()

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()

        self.wfile.write(response)

    def do_GET(self):

        if self.path == "/":
            self.send_json({
                "network": "JAYEEEE Network",
                "coin": "JAYE",
                "status": "online"
            })

        elif self.path == "/chain":
            self.send_json({
                "chain": blockchain.chain,
                "supply": blockchain.total_supply
            })

        else:
            self.send_json({
                "error": "Endpoint tidak ditemukan"
            }, 404)

    def log_message(self, format, *args):
        return


def start_node(host="0.0.0.0", port=5000):

    server = HTTPServer(
        (host, port),
        NodeHandler
    )

    print("================================")
    print("       JAYEEEE NODE")
    print("================================")
    print("Network :", "JAYEEEE Network")
    print("Coin    :", "JAYE")
    print("Port    :", port)
    print("Status  : ONLINE")
    print()
    print("Explorer lokal:")
    print(f"http://127.0.0.1:{port}/chain")
    print()

    server.serve_forever()


if __name__ == "__main__":
    start_node()
