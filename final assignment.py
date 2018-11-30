# CMPT 120
# Final Assignment
# Stanley Chan, Taalib Bhatti, Carina Li

## TO READ FROM CSV INPUT FILE

def read_csv_into_list_of_lists(IN_file):
    '''
    PROVIDED. CMPT 120
    A csv file should be available in the folder (where this program is)
    A string with the name of the file should be passed as argument to this function
    when invoking it
    (the string would include the csv extension, e.g "ID_data.csv")
    '''

    import csv

    lall = []

    print("\n.... TRACE - data read from the file\n")
    with open(IN_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for inrow in csv_reader:
            print(".......",inrow)
            lall.append(inrow)
    return lall

def convert_lall_to_separate_lists(lall):
    '''
      RECOMMENDED THAT YOU DEVELOP THIS FUNCTION

      input parameter: list of lists with all the data
      as returned from read_csv_into_list_of_lists(...)
      
      return: several lists:
          dates of draws,
          numbers drawn for each draw,
          jackpot for each draw
          number of winners for each draw

     these lists would be such that accross the lists,
     the same index refers to one draw.
    '''

## TO WRITE TO CSV INPUT FILE 
            
def append_1_draw_to_output_list(lout,date,lfreq_ran,avg_paid):
    '''
    PROVIDED. CMPT 120
    this function would append one line (the result associated to one draw)
    to a list. (this list will later be used to create the output file)
    
    
    The input parameters to this function are:
        - the list used to incorporate all the results
        - a string representing the date of this one draw to be appended
        - the list with the range frequency distribution for this draw
        - the average paid to each winner for this draw
    '''
    
    lout.append("'" + date + "'" + ",")
    for freq in lfreq_ran:
        lout.append(str(freq) + ",")
    lout.append(str(avg_paid) + "\n")
    return


def write_list_of_output_lines_to_file(lout,file_name):
    '''
    PROVIDED. CMPT 120
    Assumptions:
    1) lout is the list containing all the lines to be saved in the output file
    2) file_name is the parameter receiving a string with the exact name of the output file
       (with the csv extension, e.g "OUT_results.csv")
    3) after executing this function the output file will be in the same
       directory (folder) as this program 
    4) the output file contains just text representing one draw data per line 
    5) after each line in the file  there is the character "\n"
       so that the next draw is in the next line, and also
       there is (one single) "\n" character after the last line
    6) after the output file was created you should be able to open it
       with Excell as well
    '''
    
    fileRef = open(file_name,"w") # opening file to be written
    for line in lout:
        fileRef.write(line)
                                    
    fileRef.close()  
    return

# END OF PROVIDED CODE

welcome="Welcome to the CMPT 120 6-49 Processing system!"
print(welcome)
print("="*len(welcome))
print()

print("You first need to provide the input file name")
print("You will be asked to provide the output file name later")
print()

print("The input file should be in this  folder")
print("The output file will be created in this folder")
print()
