##Python for Biologists by Dr. Martin Jones
 

#Applying the print() function 

#print("Hello world!")
#print('Hello world!')
        
#escaping characters 
#print("The name is \\\"test\".")

#printing on a new line
#print("Hello \nworld!")

#storing strings in variables

my_dna = "ATGCGTA"
print(my_dna)

#concatenation 
my_dna = "AATT" + "GGCC"
print(my_dna)

upstream = "AAA"
my_dna = upstream + "ATCG"
print(my_dna)

print("Hello" + " " + "world!")

#Applying the len() function

len("ATCG") #outputs a value that can be stored, the return value, which must be stored in a variable

dna_length = len("AGTC")
print(dna_length) 


#remember, str and int can't be concatenated. use str() function to change int data type into str data type

my_dna = "ATGCGAGT"
dna_length = len(my_dna)
print("The length of the DNA sequence is " + str(dna_length))


#a method is a function that belongs to a particular type. e.g. lower() belongs to the str type. 
#print my_dna in lower case

#print(my_dna.lower())
#len(my_dna)

#Applying replace method 

protein = "vlspadktnv"
#print(protein.replace("v","y"))
#print(protein.replace("vls","ymt"))
#print(protein)

#Extracting part of a string

#print(protein[3:5]) #positions start at 0, not 1
#print(protein[0:6]) #if you state a number beyond last position, it will print last position
                    #positions are inclusive at the start but exclusive at the stop


protein = "vlspadktnv"
#counting aa residues 

valine_count = protein.count('v')
lsp_count = protein.count('lsp')
tryptophan_count = protein.count('w')


#print the counts
#print("valines: " + str(valine_count))
#print("lsp: " + str(lsp_count))
#print("tryptophans: " +str(tryptophan_count)) # remember str method converts output to str for print()
                                              # function, which takes only the same type 

#Applying the find method

#print(str(protein.find('p')))
#print(str(protein.find('v')))
#print(str(protein.find('pad')))


#Exercises for Ch1+2
 
 #Calculating AT content 
 my_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
 a_count = my_seq.count('A')
 t_count = my_seq.count('T')
 c_count = my_seq.count('C')
 g_count = my_seq.count('G')
 
 at_content = ((a_count + t_count) / (a_count + t_count + c_count + g_count)) * 100 

 print(at_content)

#Complement of DNA 
my_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

def complement(seq):
  if n in seq == {"A", "T", "G", "C"}.union.(seq): 
 
    seq = seq.replace("A", "T").replace("C", "G").replace("T", "A").replace("G","C") 

  else:
    return "Invalid sequence. Please recheck DNA sequence."
 
  print(complement(my_seq))


