try:
    f = open("names.pdf","r")
    data = f.read().upper()
    new_data = data
    word_count = len(new_data.split())
    f.close()

    #printing the processed data into a new file
    s = open("newfile.pdf","w")
    s.write(new_data)
    s.write(f"\nWord count: {word_count}")
    s.close()

except FileNotFoundError:
    print("File not found")

finally:
    print("File processing completed successfully.")