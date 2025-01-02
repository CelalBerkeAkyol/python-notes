def read_file(file_name):
    """Reads in a file."""
    with open(file_name, 'r') as f:
        file_contents = f.read()
        print(file_contents)
    return file_contents

def read_file_into_list(file_name):
    """Reads in a file and stores each line as an element in a list."""
    with open(file_name, 'r') as f:
        file_contents = f.readlines()  # \n karakterlerini koruyarak okuyun
    return file_contents

def write_first_line_to_file(file_contents, output_filename):
    """Writes the first line of a string to a file."""
    first_line = file_contents.split('\n')[0] + '\n'  # İlk satırı al ve \n ekle
    with open(output_filename, 'w') as f:
        f.write(first_line)

def read_even_numbered_lines(file_name):
    """Reads in the even-numbered lines of a file."""
    even_lines = []
    with open(file_name, 'r') as f:
        lines = f.readlines()  # Satırları \n ile birlikte al
        even_lines = [lines[i] for i in range(1, len(lines), 2)]  # Çift indeksli satırları seç
    return even_lines

def read_file_in_reverse(file_name):
    """Reads a file and returns a list of the lines in reverse order."""
    with open(file_name, 'r') as f:
        lines = f.readlines()  # Satırları \n ile birlikte oku
    reversed_lines = list(reversed(lines))  # Tersine çevir
    return reversed_lines

def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()