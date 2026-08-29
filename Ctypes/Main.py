import ctypes
lib = ctypes.CDLL("./legacy.dll")

#Calling int * ------------------------

# lib.increment.argtypes = [ctypes.POINTER(ctypes.c_int)]
# lib.increment.restype = None
value = ctypes.c_int(20)
lib.increment(ctypes.byref(value))
print(value.value) # need to study more

#Passing Array------------------------------------------

lib.process.argtypes = [
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int
]
lib.process.restype = None

size = 5
input_data = (ctypes.c_int * size)(1, 2, 3, 4, 5)
output_data = (ctypes.c_int * size)()

lib.process(
    input_data,
    output_data,
    size
)
print(list(output_data))


#C struct *----------------------------------

class Employee(ctypes.Structure):_fields_=[
    ("id", ctypes.c_int),
    ("salary", ctypes.c_float)
]
lib.increase_salary.argtypes=[ctypes.POINTER(Employee)]
lib.increase_salary.restype = None

employee = Employee(id=101, salary=5000)

lib.increase_salary(ctypes.byref(employee))
print(employee.id)
print(employee.salary)

# char *----------------------------------
lib.uppercase.argtypes = [ctypes.POINTER(ctypes.c_char)]
lib.uppercase.restype = None
text = ctypes.create_string_buffer(b"Hello World")
lib.uppercase(text)
print(text.value)

#Pointer-to-Pointer ---------------------
# lib.create_number.argtypes = [
#     ctypes.POINTER(ctypes.POINTER(ctypes.c_int))
# ]
# value = ctypes.c_int()
# lib.create_number(ctypes.byref(value))
# print(value.value)


#memory ownership--------------------------
ptr = lib.get_name()
