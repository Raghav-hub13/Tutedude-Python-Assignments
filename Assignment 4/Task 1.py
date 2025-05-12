try:
    file = open('Sample.txt','r')
    reading_file1 = file.readline(-1)
    reading_file2 = file.readline(-2)
    print("Reading File Content:\n", "Line 1:",reading_file1, "Line 2:", reading_file2)
except FileNotFoundError:
    print("Error: File sample.txt was not found") 
finally:
    print("Thankyou")
file.close()