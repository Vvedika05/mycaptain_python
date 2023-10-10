filename =input("Input the Filename: ")
f_ext = filename.split(".")
#repr() function returns a string containing a printable representation of an object.
print ("The extension of the file is : " + repr(f_ext[-1]))