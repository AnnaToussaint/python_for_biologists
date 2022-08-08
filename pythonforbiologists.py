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








