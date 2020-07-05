f = open("links.txt", 'r')
links = []
for x in f:
  links.append(x)

counter = 0

with open("./articles.txt", "a") as f:
  for article in articles:
    f.write(article[0])
    f.write("|")
    f.write(article[1])
    f.write("|")
    f.write(article[2])
    f.write('\n')

while counter <= (len(links) // 100):
  file_name = "links" + str(counter) + ".txt"
  with open(file_name, "a") as f:
    for i in range(counter * 100, (counter * 100) + 100):
      f.write(links[i])
      f.write("\n")

    
  counter += 1

file_name = "links" + str(counter) + ".txt"
with open(file_name, "a") as f:
  for i in range((counter -1) * 100, len(links)):
    f.write(links[i])
    f.write("\n")


f.close