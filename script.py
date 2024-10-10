from collections import Counter
import socket
import os

# Count the total number of words in a file
def numWordsInFile(fileName):
  fileObject = open(fileName, "r")
  return len(fileObject.read().split())

# Identify the top 3 most frequent words and their respective counts in a file
def top3WordsInFile(fileName):
  fileObject = open(fileName, "r")
  words = fileObject.read().lower().split()
  fileObject.close()
  words = [word.strip(".,!?:;\"'()[]{}") for word in words]
  
  frequencies = Counter(words)
  return frequencies.most_common(3)

# Handle contractions (e.g., I'm, can't, don't) by splitting them into individual words,
# then find the top 3 most frequent words and their respective counts in 
# AlwaysRememberUsThisWay.txt 
def handleContractions(fileName):
  fileObject = open(fileName, "r")
  words = fileObject.read().lower().split()
  fileObject.close()
  
  noContractions = "noContractions.txt"
  noContractionsFile = open(noContractions, "w")
  
  contractions = {"can't": "can not", 
                  "couldn't": "could not", 
                  "don't": "do not", 
                  "i'll": "i will", 
                  "i'm": "i am", 
                  "it's": "it is", 
                  "that's": "that is",
                  "won't": "will not", 
                  "you're": "you are"}
  
  for word in words:
    if "'" in word:    
      noContractionsFile.write(contractions.get(word) + " \n")
    else:
      noContractionsFile.write(word + " \n")
  
  noContractionsFile.close()
  frequencies = top3WordsInFile(noContractions)
  os.remove(noContractions)
  return frequencies

# Determine the IP address of the machine running the container
def machineIP():
  return socket.gethostbyname(socket.gethostname())

# print all results to command line
def printFromResult():
  file = open("output/result.txt", "r")
  print(file.read())
  file.close()

# run all actions for assignment
def scriptActions():
  # open text files to read from
  IFtxt = "IF.txt"
  ARUTWtxt = "AlwaysRememberUsThisWay.txt"
  
  # Count the total number of words in each text file located at /home/data
  wordsIF = numWordsInFile(IFtxt)
  wordsARUTW = numWordsInFile(ARUTWtxt)
  
  # Calculate the grand total of words across both files.
  totalWords = wordsIF + wordsARUTW
  
  # Identify the top 3 most frequent words and their respective counts in IF.txt
  top3FreqIF = top3WordsInFile(IFtxt)
  
  # remove contractins and get the 3 most frequent words in the file
  top3FreqNoContractions = handleContractions(ARUTWtxt)
  
  # Get the IP address of the machine running the container
  ip_address = machineIP()
  
  # Write the results to a text file at /home/data/output/result.txt.
  if (not os.path.exists("output")):
    os.mkdir("output")
  result = open("output/result.txt", "w")
  
  result.write(f"There are {wordsIF} words in IF.txt\n")
  result.write(f"There are {wordsARUTW} words in IF.txt\n")
  result.write(f"There are {totalWords} words in the two files combined\n")
  result.write("\nThe top 3 most frequent words in IF.txt:\n")
  for word, count in top3FreqIF:
    result.write(f"{word}: {count}\n")
  result.write("\nThe top 3 most frequent words in AlwaysRememberUsThisWay.txt (CONTRACTIONS REMOVED):\n")
  for word, count in top3FreqNoContractions:
    result.write(f"{word}: {count}\n")
  result.write(f"\nThe IP address of the machine is: {ip_address}\n")
  
  result.close()
  
  printFromResult()

if __name__ == "__main__":
  scriptActions()