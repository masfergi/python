from sys import argv
script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).") # kalau tekan CTRL-C otomatis inexecute the program
print("If you do want that, hit RETURN.") # return mean enter

input("?") # menampilkan karakter "?" dan menunggu apakah user menekan enter atau CTRL-C

print("Opening the file...")
target = open(filename, 'w') # variable berisi fungsi membuka file, mengisi dengan karakter 'w'

print("Truncating the file. Goodbye!")
target.truncate() # memotong/menghapus isi file

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ") # mengisi variable line1 dan otomatis enter
line2 = input("line 2: ") # mengisi variable line2 dan otomatis enter
line3 = input("line 3: ") # mengisi variable line3 dan otomatis enter

print("I'm going to write these to the file.")

target.write(line1) # menulis isi file
target.write("\n")  # menulis enter
target.write(line2) # menulis isi file
target.write("\n")  # menulis enter
target.write(line3) # menulis isi file
target.write("\n")  # menulis enter

print("And finally, we close it.")
target.close() # menutup target
