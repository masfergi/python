print("This is the conclusions from exercise 01 till exercise 21")
print('''
#Exercise 01
penggunaan perintah print() untuk menampilkan string
dengan menulis string di dalam "" maupun ''

#Exercise 02
penggunaan comment, menulis komentar dilakukan dengan
menuliskan karakter # sebelum statement komentar

#Exercise 03
operasi logika dan matematika seperti, ==, >=, <=, +, -, *, /, %
dapat dilakukan di dalam perintah print

#Exercise 04
penggunaan variable, menyimpan nilai maupun string di dalam sebuah varaible
nama_variable = "0" #jika di letakkan di dalam "" maka variable menyimpan string
nama_variable = 0 #jika tidak diletakkan di dalam "" makan variable menyimpan nilai
nama_variable = nama_variable_lain #dapat di gunaakan untuk menyimpan nilai variable lain
nama_variable = False #variable juga dapat di gunakan untuk menyimpan boolean True/False
dalam deklarasi variable juga dapat melakukan operasi matematika seperti +, -, *, /, %

#Exercise 05
penggunaan format pada print
print(f"string {nama_variable} string")
digunakan untuk melakukan print nilai variable dengan memanggil variable yang bersangkutan
di dalam kurung kurawal {}

#Exercise 06
melakukan print variable dengan memamnggil variable itu sendiri langsung pada pertintah print
contoh:
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

#Exercise 07
print("Its fleece was white as {}.".format('snow')) #"{}" pada print bernilai 'snow'
print("." * 10) #melakukan print "." sebanyak 10x

#Exercise 08
membuat formatter, dan melakukan print dengan formatter
formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
maka akan hasil print adalah 1 2 3 4

#Exercise 09
menggunakan \n untuk print enter
dan ''' ''' untuk melakukan print penulisan dengan enter
contoh seperti keterangan ini di tulis di antara ''' '''

#Exercise 10
melakukan tab pada print dnegan menggunakan "\ t" #tanpa spasi
dan menampilkan backslash dengan menggunakan \\\\

#Exercise 11
menggunakan sebuah fungsi input()
untuk melakukan input dari keyboard

#Exercise 12
perintah input juga dapat menampilkan sebuah string sebelum input field muncul
contoh: age = input("How old are you? ")
How old are you akan di print terlebih dahulu baru input field muncul

#Exercise 13
melakukan import argv dan
penggunaan argumen, argv
script di run dari cmd, tidak bisa di run dari editor
menjalankan program dengan mengisi filed yang diperlukan
contoh menjalankan script yang memiliki command argv:
C:/python.exe program.py argumen

#Exercise 14
argumen yang di masukkan saat mengeksekusi program
adalah nilai dari variable deklarasi untuk argv
contoh: saat program ex14.py di jalankan
script, user_name = argv
script akan menyimpan informasi tentang program itusendiri "ex14.py"
sedang user_name akan menyimpan argumen/input yang dimasukkan saat melakukan eksekusi

#Exercise 15
melakukan open file
fungsi open() digunakan untuk membuka file
dengan mengisi fungsi tersebut dengan nama file/text maka file akan terbuka

#Exercise 16
truncate() digunakan untuk menghapus isi daripada file
write() digunakan untuk menulis file dengan suatu string atau nilai
penggunaannya harus diawali dengan
nama_variable_yang_bersangkutan.turnicate()
nama_variable_yang_bersangkutan.write()

#Exercise 17
nama_file.open() melakukan eksekusi sampai atas file bersangkutan sampai close() dijalankan
output dari len() adalah ukuran daripada file
output dari exists() adalah true/false
nama_file.close() menutup file

#Exercise 18
deklarasi fungsi
pendeklarasian fungsi dimulai dengan "def" di depan nama fungsi dan () setelah nama fungsi
dan diikuti dengan :
setelah itu di ikuti dengan statement statement di bawahnya, contoh
def print_none():
    print("I got nothin'.")
dan untuk fungsi dengan sebuah variable, sebagai berikut
def print_one(arg1):
    print(f"arg1: {arg1}")
dan eksekusi daripada fungsi seperti berikut
print_none()
print_one("First!")

#Exercise 19
dalam pemanggilan sebuah fungsi juga dapat dilakukan operasi aritmatika
contoh
fungsi_1(variable_1 + variable_2, variable_a * 10)

#Exercise 20
format dalam fungsi, contoh
def print_a_line(line_count, f):
    print(line_count, f.readline())
current_line = 1
print_a_line(current_line, current_file)

#Exercise 21
return nilai dari sebuah fungsi, contoh
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
age = add(30, 5)

''')
