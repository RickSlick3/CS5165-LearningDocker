import socket
from collections import Counter

# Count the total number of words in each text file located at /home/data
def numWordsInFile(fileName):
  fileObject = open(fileName, "r")
  return len(fileObject.read().split())

# Identify the top 3 most frequent words and their respective counts in IF.txt
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
  
  return top3WordsInFile(noContractions)

# Determine the IP address of the machine running the container
def machineIP():
  return socket.gethostbyname(socket.gethostname())

# Write the results to a text file at /home/data/output/result.txt. When the container is 
# executed, it should print the contents of result.txt to the console before exiting.
def writeResultsToOutput():
  return


if __name__ == "__main__":
  # open text files to read from
  IFtxt = "IF.txt"
  ARUTWtxt = "AlwaysRememberUsThisWay.txt"
  
  # Count the total number of words in each text file located at /home/data
  wordsIF = numWordsInFile(IFtxt)
  print(wordsIF)
  wordsARUTW = numWordsInFile(ARUTWtxt)
  print(wordsARUTW)
  
  # Calculate the grand total of words across both files.
  totalWords = wordsIF + wordsARUTW
  print(totalWords)
  
  # Identify the top 3 most frequent words and their respective counts in IF.txt
  top3FreqIF = top3WordsInFile(IFtxt)
  print(top3FreqIF)
  # top3FreqARUTW = top3WordsInFile(ARUTWtxt)
  # print(top3FreqARUTW)
  
  # Handle contractions (e.g., I'm, can't, don't) by splitting them into individual words,
  # then find the top 3 most frequent words and their respective counts in 
  # AlwaysRememberUsThisWay.txt 
  # top3FreqNoContractions = handleContractions(IFtxt)
  # print(top3FreqNoContractions)
  top3FreqNoContractions = handleContractions(ARUTWtxt)
  print(top3FreqNoContractions)
  
  # Determine the IP address of the machine running the container
  ip_address = machineIP()
  print(ip_address)