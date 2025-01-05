# Define three URLs with different protocols
url1 = "https://www.example.com"
url2 = "ftp://ftp.example.org"
url3 = "http://api.example.net"

filename = "data_2022_01_15.csv"
 # Extract the protocol using slicing by character

protocol1 = url1[:url1.index(":")]
protocol2 = url2[:url2.index(":")]
protocol3 = url2[:url2.index(":")]

file_ext = filename[filename.index(".")+1:]

print( "Protocol 1: " , protocol1)
print( "Protocol 2: " , protocol2)
print( "Protocol 3: " , protocol3)
print("File Extention Type: ", file_ext)