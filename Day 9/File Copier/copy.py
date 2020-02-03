

class copier:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.copy()

    def copy(self):
        try:
            source_file = open(self.source, "rb")
            data = source_file.read()
            source_file.close()

            # file data copied

            destination_file = open(self.destination, "wb")
            destination_file.write(data)
            destination_file.close()

            print("Done!")
        except Exception as e:
            print(e)

def main():
    print("==== PyCopy ====")

    file_name = input("Enter File name : ")
    src = input("Enter the source dir: ")
    dst = input("Enter the Dstination dir: ")

    src_path = src + "\\" + file_name
    dst_path = dst + "\\" +file_name

    c = copier(src_path, dst_path)

if __name__ == "__main__":
    main()