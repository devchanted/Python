# Define three URLs with different protocols
url1 = "https://www.example.com"
url2 = "ftp://ftp.example.org"
url3 = "http://api.example.net"

 # Extract the protocol using slicing by character

protocol1 = url1[:url1.index(":")]
protocol2 = url2[:url2.index(":")]
protocol3 = url2[:url2.index(":")]

print( "Protocol 1: " , protocol1)
print( "Protocol 2: " , protocol2)
print( "Protocol 3: " , protocol3)