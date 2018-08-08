# formatter sebenarnya adalah "string" tapi karena ber isi "{}"
# maka "{}" dapat menjadi wadah untuk nilai/string/boolean
formatter = "{} {} {} {}"

# melakukan print dengan format di isi dengan integer
print(formatter.format(1,2,3,4))

# melakukan print dengan isi formatter adalah string
print(formatter.format("one","two","three","four"))

# melakukan print dengan isi formatter adalah boolean
print(formatter.format(True,False,False,True))

# melakukan print dengan isi formatter adalah string daripada formatter itu sendiri
print(formatter.format(formatter,formatter,formatter,formatter))

# melakukan print dengan isi formatter adalah kumpulan string
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear."
))
