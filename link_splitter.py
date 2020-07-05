import os
f = open("links.txt", 'r')
links = []
for x in f:
  links.append(x)

counter = 0
file_names =[]

while counter <= (len(links) // 100 -1):
  file_name = "links" + str(counter) + ".txt"
  file_names.append(file_name)
  if os.path.exists(file_name):
    os.remove(file_name)
    print(file_name + " removed")
  with open(file_name, "w") as f:
    print(counter * 100, (counter * 100) + 100)
    for i in range(counter * 100, (counter * 100) + 100):
      f.write(links[i])
      f.write("\n")
  counter += 1

file_name = "links" + str(counter) + ".txt"
file_names.append(file_name)
with open(file_name, "a") as f:
  for i in range((counter -1) * 100, len(links)):
    f.write(links[i])
    f.write("\n")

f.close

#for file in file_names:
#  command = "python3 google_news.py " + file
 # os.system(command)
