from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
import threading
import json
import time
	
class ImageServerRequestHandler(BaseHTTPRequestHandler):
	
	def do_GET(self):
		print("GOT")
		request_path = self.path.split("/")[1:]
		
		# Aircraft and image system status
		if request_path[0] == "status":
			message = self.server.get_status()
			
			self.send_response(200)
			self.send_header("Content-Type", "application/json")
			self.end_headers()
			self.wfile.write(json.dumps(message))
			return
		
		if request_path[0] == "finish":
			self.server.finish()
			
			self.send_response(200)
			self.send_header("Content-Type", "text/plain")
			self.end_headers()
			self.wfile.write("OK")
			return

		if request_path[0] == "picture":
			self.server.take_picture()
			print("Picture!")
			
			self.send_response(200)
			self.send_header("Content-Type", "text/plain")
			self.end_headers()
			self.wfile.write("OK")
			return

		if request_path[0] == "zoomin":
			self.server.zoom_in()
			print("Zoom In!")
			
			self.send_response(200)
			self.send_header("Content-Type", "text/plain")
			self.end_headers()
			self.wfile.write("OK")
			return

		if request_path[0] == "zoominfull":
			self.server.zoom_in_full()
			print("Zoom In Full!")
			
			self.send_response(200)
			self.send_header("Content-Type", "text/plain")
			self.end_headers()
			self.wfile.write("OK")
			return

		if request_path[0] == "zoomout":
			self.server.zoom_out()
			print("Zoom Out!")
			
			self.send_response(200)
			self.send_header("Content-Type", "text/plain")
			self.end_headers()
			self.wfile.write("OK")
			return

		if request_path[0] == "zoomoutfull":
			self.server.zoom_out_full()
			print("Zoom Out Full!")
			
			self.send_response(200)
			self.send_header("Content-Type", "text/plain")
			self.end_headers()
			self.wfile.write("OK")
			return
		
		self.send_error(404)

class ImageServer(HTTPServer):
	
	statusmsg = "Status unavailable"
	finish_mission = False
	status_lock = threading.Lock()

	def __init__(self, servaddr,cam):
		HTTPServer.__init__(self, servaddr, ImageServerRequestHandler)
		self.cam = cam
		print 'Starting server, use <Ctrl-C> to stop'
		self.server_thread = threading.Thread(target=self.serve_forever)
		self.server_thread.start()
		
	def get_status(self):
		self.status_lock.acquire()
		retval = {}
		retval['status'] = self.statusmsg
		self.status_lock.release()
		return retval
	
	def set_status(self, msg):
		print(msg)
		self.status_lock.acquire()
		self.statusmsg = msg
		self.status_lock.release()
		return

	def take_picture(self):
		self.status_lock.acquire()
		self.cam.actTakePicture()
		self.status_lock.release()
		pass

	def zoom_in(self):
		self.status_lock.acquire()
		self.cam.zoomIn()
		self.status_lock.release()

	def zoom_in_full(self):
		self.status_lock.acquire()
		self.cam.zoomInFull()
		self.status_lock.release()

	def zoom_out(self):
		self.status_lock.acquire()
		self.cam.zoomOut()
		self.status_lock.release()

	def zoom_out_full(self):
		self.status_lock.acquire()
		self.cam.zoomOutFull()
		self.status_lock.release()
		
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