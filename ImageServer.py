from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
import threading
import json
import time
	
class ImageServerRequestHandler(BaseHTTPRequestHandler):
	
	def do_GET(self):
		request_path = self.path.split("/")[1:]
		
		#print(self.headers['Origin'])
		
		# Aircraft and image system status
		if request_path[0] == "status":
			message = self.server.get_status()
			
			self.send_response(200)
			self.send_header("Content-Type", "application/json")
			self.send_header("Access-Control-Allow-Origin", self.headers['Origin'])
			self.end_headers()
			self.wfile.write(json.dumps(message))
			return
		
		if request_path[0] == "finish":
			self.server.finish()
			
			self.send_response(200)
			self.send_header("Content-Type", "text/plain")
			self.send_header("Access-Control-Allow-Origin", self.headers['Origin'])
			self.end_headers()
			self.wfile.write("OK")
			return

		if request_path[0] == "picture":
			self.server.take_picture()
			
			self.send_response(200)
			self.send_header("Content-Type", "text/plain")
			self.send_header("Access-Control-Allow-Origin", self.headers['Origin'])
			self.end_headers()
			self.wfile.write("OK")
			return

		if request_path[0] == "zoomin":
			self.server.zoom_in()
			
			self.send_response(200)
			self.send_header("Content-Type", "text/plain")
			self.send_header("Access-Control-Allow-Origin", self.headers['Origin'])
			self.end_headers()
			self.wfile.write("OK")
			return

		if request_path[0] == "zoomout":
			self.server.zoom_out()
			
			self.send_response(200)
			self.send_header("Content-Type", "text/plain")
			self.send_header("Access-Control-Allow-Origin", self.headers['Origin'])
			self.end_headers()
			self.wfile.write("OK")
			return
		
		self.send_error(404)

class ImageServer(HTTPServer):
	
	statusmsg = "Status unavailable"
	# csvfile = ""
	# zipfile = ""
	finish_mission = False
	status_lock = threading.Lock()

	def __init__(self, servaddr, cam):
		HTTPServer.__init__(self, servaddr, ImageServerRequestHandler)
		self.cam = cam
		print 'Starting server, use <Ctrl-C> to stop'
		self.server_thread = threading.Thread(target=self.serve_forever)
		self.server_thread.start()
		
	def get_status(self):
		self.status_lock.acquire()
		retval = {}
		retval['status'] = self.statusmsg
		# retval['csvfile'] = self.csvfile
		# retval['zipfile'] = self.zipfile
		# retval['cam1'] = self.cam1.status()
		self.status_lock.release()
		return retval
	
	def set_status(self, msg):
		print(msg)
		self.status_lock.acquire()
		self.statusmsg = msg
		self.status_lock.release()
		return

	def take_picture(self):
		pass

	def zoom_in(self):
		pass

	def zoom_out(self):
		pass
		
	# def set_csvfile(self, msg):
	# 	self.status_lock.acquire()
	# 	self.csvfile = msg
	# 	self.status_lock.release()
	# 	return
		
	# def set_zipfile(self, msg):
	# 	self.status_lock.acquire()
	# 	self.zipfile = "<a href=\"/agribotix/data/"+msg+"\">"+msg+"</a>"
	# 	self.status_lock.release()
	# 	return
		
	def finish(self):
		self.finish_mission = True
		
	def is_finished(self):
		return self.finish_mission

if __name__ == "__main__":
	server = ImageServer(servaddr)
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		server.shutdown()