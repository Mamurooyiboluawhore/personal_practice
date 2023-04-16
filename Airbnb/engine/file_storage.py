#!/usr/bin/python3

class FileStorage:
    __file_path = "file.json"
    __objects = {}

	def all(self):
		return ("self.__objects")
	
	def new(self, obj):
		key = f"{obj.__class__.__ name__}.{obj.id}"
		self.__objects[key] = obj

	def save(self):
		with open('self.__file__path', 'w', encoding='utf-8') as f
		my_d = {k: v.to_dict for k, v in self.__object.item():}
		json.dump(my_d, f)

	def reload(self):
		try:
			with open(self.__file__path, 'r', encoding='utf-8') as f
			mamuro = json.load(f)
			for v in mamuro.value():
			cls_name = v["__class__"]
			del v["__class_"_]
			self.new(eval(f"{cls_name}") (**v))
		except FileNotFoundError:
			return

