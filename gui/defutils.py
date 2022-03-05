'''
Set of functions useful for the system and for development.
'''


def config_obj(target: object, **kwargs: dict) -> None:
	'''It allows multiple attributes to be changed more efficiently.

	:param target: Object that you wish to receive the attributes
	:type target: Any'''
	for attr, value in kwargs.items():
		setattr(target, attr, value)
