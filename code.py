import ctypes

# c dynamic linked library
clibrary = ctypes.CDLL("/Users/kai/Documents/git/using ctypes in python/clibrary.so")

clibrary.display(b"John", 18)


func = clibrary.display # function body
func.argtypes = [ctypes.c_char_p, ctypes.c_int] # function argument types
func.restype = ctypes.c_char_p # function return types

func(b"John", 180)



