'''
Classes and utilities for working with vizualization.

Note: Some of these classes are of a lower level.
'''


import pygame
from typing import Callable
from gui.defutils import config_obj


class WindowParams:
	'''
	Basic attributes and behaviors of a PygameGUI window.
	'''

	alive: bool = True
	window_title: str = 'Title'
	window_icon: str = None
	
	_window_width: int = 500
	_window_height: int = 500
	_window_size: tuple[int, int] = (_window_width, _window_height)

	_display: object = None
	# Instance of the highest hierarchy container in the window
	_window_root: object = None

	@property
	def window_width(self):
		return self._window_width

	@window_width.setter
	def window_width(self, new_width: int):
		self._window_width = new_width
		self._window_size = (self._window_width, self._window_height)

	@property
	def window_height(self):
		return self._window_height

	@window_height.setter
	def window_height(self, new_height: int):
		self._window_height = new_height
		self._window_size = (self._window_width, self._window_height)

	@property
	def window_size(self):
		return self._window_size

	@window_size.setter
	def window_size(self, new_size: int):
		self._window_size = new_size
		self._window_width = self._window_size[0]
		self._window_height = self._window_size[1]

	@property
	def window_root(self):
		return self._window_root

	@window_root.setter
	def window_root(self, new_root: int):
		self._window_root = new_root
		self._display.main = self._window_root

	@property
	def display(self):
		return self._display


class WindowDisplayerParams:
	main: object = None
	background_color: tuple[int, int, int] = (255, 255, 255)


class WindowDisplayer(WindowDisplayerParams):
	'''
	This is what actually builds the window and displays the components.
	'''

	def __init__(self,
				window_icon: str, 
				window_title: str,
				window_size: tuple[int, int],
				**kwargs: dict):
		
		config_obj(target=self,
			window_icon=window_icon,
			window_title=window_title,
			window_size=window_size,
			**kwargs)

		self.make_window()

	def make_window(self) -> None:
		self._window = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.window_title)
		if self.window_icon is not None:
			pygame.display.set_icon(self.window_icon)

	def show(self) -> None:
		self._window.fill(self.background_color)
		if self.main and self.main is not None:
			self.main._draw(self._window)

	def update(self) -> None:
		pygame.display.flip()


class WindowEventListener:
	'''Responsible for listening to the user's interaction with the window.'''

	def __init__(self):
		self.listeners = {}

	def bind(self, event_code: int, callback: Callable):
		self.listeners[event_code] = callback

	def listen(self):
		for event in pygame.event.get():
			if event.type in self.listeners.keys():
				self.listeners[event.type](event)


class MainWindow(WindowParams):
	'''Main program window.'''
	__started__ = False

	def __init__(self, **kwargs: dict):
		config_obj(target=self, **kwargs)
		self._display = WindowDisplayer(
			window_icon=self.window_icon,
			window_title=self.window_title,
			window_size=self.window_size
		)
		self.listener = WindowEventListener()

		self.on_create()

	####### Auxiliary Methods ######
	def get_display_surface(self):
		return self.display._window

	def on_create(self):
		'''Method called when the window is being created.

		Ideal for declaring variables and instantiating classes'''
		pass

	def on_start(self):
		'''Method called when the user interface is visible and usable.'''
		pass

	def on_exit(self, evt: object):
		'''Method called when the user clicks to close the window.

		Of course, by default it closes the window.'''
		pygame.quit()
		exit()

	def update(self):
		'''Method called on each user interface update.

		Run your code that needs constant updating here.'''
		pass

	def bind_events(self):
		'''Method for adding event listeners to the main window.'''
		self.listener.bind(pygame.QUIT, self.on_exit)

	def show(self):
		'''Starts the main window loop.'''
		self.bind_events()
		while self.alive:
			self._display.show()
			# Calls the 'on_start' method if not already called
			if not self.__started__:
				self.__started__ = True
				self.on_start()

			self.listener.listen()
			self.update()
			self._display.update()
