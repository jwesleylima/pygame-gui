'''
Classes and utilities for working with vizualization.

Note: Some of these classes are of a lower level.
'''


import pygame
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
		return self._window_height

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
