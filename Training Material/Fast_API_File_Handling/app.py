
test_file= open('test.txt', 'r')
print(test_file.read())
test_file.close()




with  open('test.txt', 'rb') as f:
    content=f.read()
    f.seek(0) # this is the method that will again set the position at beggining of the file
    print(content)

print(f.closed)





with  open('test.txt', 'r') as f:
    content=f.readlines()
    print(content)

with  open('test.txt', 'r') as f:
    content=f.readline()
    print(content)

with  open('test-copy.txt', 'w') as f:
    f.write("Hello world")





import os 
import json
text_folder = "data"




for i in range(0,5):
    # Create JSON data
    text_data = {"name":"Hello world"}
    text_filename = f"{i}.json"
    text_path_full = os.path.join(text_folder, text_filename)

    # Write JSON data to file
    with open(text_path_full, "w") as file:
        json.dump(text_data,file)
        print(f"JSON file saved: {text_filename}")





for filename in os.listdir(text_folder):
    if filename.endswith('.json'):
        file_path = os.path.join(text_folder, filename)
        with open(file_path, 'r') as file:
            data = json.load(file)

        data["name"] = "soham"

        with open(file_path, 'w') as file:
                json.dump(data, file, indent=2)










try:
    result = 10 / 0  
    print (result)
except Exception as e:
    print("An unexpected error occurred:", e)




try:
    print (result)
except Exception as e:
    print("An unexpected error occurred:", e)




try:
    with open('testasdf.txt', 'rb') as f:
        print(f.read())
    
except Exception:
    print("File not found")

except Exception as e:
    print("An unexpected error occurred:", e)