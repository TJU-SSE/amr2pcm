import os

print("Wechat Audio Converter")
print("Convert Wechat audio from amr(silk) format to pcm format.")
print("Author：MSRA team of Tongji University")

file_in = input("Input the name of Wechat audio:")
file_out = input("Input the name of output audio:")

fs_in = open(file_in,"rb")
fs_out = open("silk/temp.amr","wb")

if not fs_in.read(1) == b'#':
    fs_in.seek(1,0)

fs_out.write(fs_in.read())

if not os.path.exists("silk/decoder"):
    print("Compiling the decoer...")
    os.chdir("silk")
    os.system("make")
    print("Finished!")
else:
    os.chdir("silk")

os.system("./decoder "+"temp.amr "+file_out)

os.remove("temp.amr")

print("input:  " + file_in)
print("output: " + file_out)
print("Convertion finished!")
