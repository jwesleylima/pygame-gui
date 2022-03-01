'''
Classes and utilities for working with vizualization.

Note: Some of these classes are of a lower level.
'''


import pygame
from typing import Any


class WindowParams:
	'''
	Basic attributes and behaviors of a PygameGUI window.
	'''
	
	window_title: str = 'Title'
	window_icon: str = None
	
	_window_width: int = 500
	_window_height: int = 500
	_window_size: tuple[int, int] = (_window_width, _window_height)

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
