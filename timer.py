from time import time

class Timer(object):

	def __init__(self, end=-1):
		self._start = 0
		self._stop = 0
		self._pause = 0
		self._pplus = 0
		self._end = end
		self._started = False
		self._paused = False

	def start(self):
		self._start = time()
		self._started = True
		self._paused = False

	def stop(self):
		self._stop = time()
		self._started = False
		self._paused = False

	def pause(self):
		self._pause = time()-self._pplus
		self._paused = True
	
	def resume(self):
		self._pplus = time()-self._pause
		self._paused = False

	def null(self):
		self._start = 0
		self._stop = 0
		self._pause = 0
		self._pplus = 0

	def get_end(self):
		return self._end

	def set_end(self, value):
		if (isinstance(value, float)):
			self._end = value
		elif (isinstance(value, int)):
			self._end = float(value)

	end = property(get_end, set_end)

	def is_started(self):
		if (self._started) and (not self._paused):
			if (time()-self._start-self._pplus <= self._end) or (self._end == -1):
				return self._started
			else:
				return False
		elif (self._started) and (self._paused):
			if (self._pause-self._start <= self._end) or (self._end == -1):
				return self._started
			else:
				return False
		else:
			return self._started

	def is_paused(self):
		return self._paused

	def current(self, mode='float'):
		if (mode == 'float'):
			if (self._started):
				if (not self._paused):
					if (time()-self._start-self._pplus <= self._end)  or (self._end == -1):
						return time()-self._start-self._pplus
					else:
						return self._end
				else:
					if (self._pause-self._start <= self._end) or (self._end == -1):
						return self._pause-self._start
					else:
						return self._end
			elif (not self._started):
				if (self._stop-self._start <= self._end) or (self._end == -1):
					return self._stop-self._start
				else:
					return self._end
		elif (mode == 'int'):
			if (self._started):
				if (not self._paused):
					if (time()-self._start-self._pplus <= self._end)  or (self._end == -1):
						return int(time()-self._start-self._pplus)
					else:
						return int(self._end)
				else:
					if (self._pause-self._start <= self._end) or (self._end == -1):
						return int(self._pause-self._start)
					else:
						return int(self._end)
			elif (not self._started):
				if (self._stop-self._start <= self._end) or (self._end == -1):
					return int(self._stop-self._start)
				else:
					return int(self._end)

	def back_current(self, mode='int'):
		if (mode == 'float'):
			if (self._started):
				if (not self._paused):
					if (time()-self._start-self._pplus <= self._end)  or (self._end == -1):
						return self._end-(time()-self._start)+self._pplus
					else:
						return 0.0
				else:
					if (self._pause-self._start <= self._end) or (self._end == -1):
						return self._end-(self._pause-self._start)
					else:
						return 0.0
			elif (not self._started):
				if (self._stop-self._start <= self._end) or (self._end == -1):
					return self._end-(self._stop-self._start)
				else:
					return 0.0
		elif (mode == 'int'):
			if (self._started):
				if (not self._paused):
					if (time()-self._start-self._pplus <= self._end)  or (self._end == -1):
						return int(self._end-(time()-self._start-1)+self._pplus)
					else:
						return 0
				else:
					if (self._pause-self._start <= self._end) or (self._end == -1):
						return int(self._end-(self._pause-self._start-1))
					else:
						return 0
			elif (not self._started):
				if (self._stop-self._start <= self._end) or (self._end == -1):
					return int(self._end-(self._stop-self._start-1))
				else:
					return 0

	def __str__(self):
		if (self.is_started()):
			if (not self.is_paused()):
				state = "started"
			else:
				state = "paused"
		else:
			state = "stopped"
		return "<Timer current={0} state={1}>".format(self.current(), state)
