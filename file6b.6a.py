#6a display file
def file_read(fname):
    txt=open(fname)
    print(txt.read())
file_read('ds.txt')

#6b add content
def main():
    f = open('bruh.txt', 'a+')
    f.write('i did ittttttttttt')
    f.close()

if __name__ == "__main__":
    main()
