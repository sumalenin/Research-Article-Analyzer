#To Check if Index Terms are written in a senctence and follow the following rules :
#   1.All articles must contain Index Terms
#   2.Index Terms should appear in Alphabetical order
#   3.The first term of the Index Terms list must be capitalized and the list should end with full stop.
#   4.Acronyms must be capitalized
#To list the names of all Scientists used in the research paper 
#and to check if they are started with a capital letter since they are proper names

class team_3:
    #Constructor
    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code # The entire LaTex code is in the form of string in the latex_code string
        self.text_begin = text_begin # location of \begin

    def run(self): # will be invoked by wrapper, shouldn't take arguments
        output = []
        text = self.latex_code
        # use self
        str = '='*50
        self.scientistName(text,output)
        output.append(str+'\n\t\t\t\t\t\tIndex Related Comments\n'+str)
        output.extend(self.indexCheck())
        
        
        return output
    
    def scientistName(self,text,output):
        scientist_names_used=set()
        scientist_names={'Isaac Newton','Newton','Albert Einstein','Einstein','Galileo Galilei','Niels Bohr','Bohr','Marie Curie',
                         'Max Planck','Planck','James Clerk Maxwell','Maxwell','Werner Heisenberg','Heisenberg','Richard Feynman',
                         'Feynman','Erwin Schrödinger','Schrödinger','Enrico Fermi','Stephen Hawking','Hawking','Michael Faraday',
                         'Faraday','Dmitri Mendeleev','Carl Sagan','Andrei Sakharov','Lise Meitner',
                         'Edwin Hubble','Jocelyn Bell Burnell','Chandrasekhar Subrahmanyan',
                         'Gaussian','Doppler'}
        for word in text.split(' '):
            if word in scientist_names:
                scientist_names_used.add(word)
        str1=''
        for word in scientist_names_used:
            if str1=='':
                str1=word
            else:
                str1=str1+', '+word
        output.append('Scientist Names Used = '+str1+'\n')
            

    """
    Make seperate functions for whatever you do and call it in run
    """

    def indexCheck(self):
        text = self.latex_code
        output = []
        
        start_index = text.find(r"\begin{IEEEkeywords}")
        if start_index == -1:
            output.append("Index Terms not present in document")
            return output
        
        end_index = text.find(r"\end{IEEEkeywords}") 
        
        index_text = text[start_index+21:end_index].rstrip() # 21 is to offset \begin{IEEEkeywords}

        """
        Checking alphabetical order 
        """
        
        comma_list = [i.strip()[0].lower() for i in index_text.split(",") if i.strip()[0].isalpha()]
        
        if comma_list != sorted(comma_list):
            output.append("Index terms are not in alphabetical order")

        index_text_list = index_text.replace(","," ").split(" ")
        reference_text = index_text.capitalize()
        reference_text_list = reference_text.replace(","," ").split(" ")
        
        """
        Checking if index terms are in Sentence case
        Only exception is Acronyms Considering Acronyms 
        as having All capital letters, last alphabet
        can be small
        """
        
        for i,j in zip(index_text_list,reference_text_list):
            if not i[:-1].isupper():
                if i != j:
                    output.append(f"Word {i} is not in proper format")
        """
        Checking for full stop at the end of index terms
        """
        
        if index_text_list[-1][-1] !=".":  # last character should be .
            output.append(f"Full stop not present at the end of index")
        return output
