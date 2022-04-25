
print("Hello, welcome to our Protein-Bacteria Matching Program!")
print("By: Rana and Lujain")
print("for information, type [info]")
print("to run the prorgam, type [run]")
print("to exit the program, type [exit]")
command = input('\n>> ')

while command != 'exit':
    if command == 'info':
        print('This program is designed to help find the most appropriate bacterial vector to use for producing a specific protein')
        print('The program will suggest the most appropriate bacteria for use, but you can select any bacteria to produce a report')
        print('What to expect in your output: The bacterial sequence, the number of mismatches, the location of mismatches, the type of mismatches')
        print('')
        print('in order to find your best match bacteria, your input file should be:')
        print('a text file containing your amino acid sequence with each amino acid in a seperate row, for example:')
        print('Methionine')
        print('Leucine')
        print('Serine')
        print('TerminationCodon')
        command = input('\n>> ')

    elif command =='run':
        import pandas as pd

        df = pd.read_excel("AminoAcid_DB.xlsx")
        df = df.fillna(0)
        fname = input('What ins the name of the file with your desired amino acid sequence? ')
        f = open(fname, "r")
        content = f.read()
        aa = content.split('\n')
        l = len(aa)
        f.close()

        from itertools import product

        pr = list(product(df[aa[0]], df[aa[1]], df[aa[2]], df[aa[3]], df[aa[4]], df[aa[5]], df[aa[6]]))

        ans = [i for i in pr if 0 not in i]

        n = list()
        f = list()
        t = list()

        for i in range(len(ans)):
            t = ' '.join(str(item) for item in ans[i])
            n = t.replace(" ", "")
            f.append(n)
        print(f)
        print(len(f))

        seqdf = pd.DataFrame(f, columns=['sequence'])

        seqdf.to_csv('seq.csv', index=False)

        # ADD PART FROM RANA

        print('Report Downloaded.')
        print('The most appropriate bacteria is: Bacteria ')  # add this part from rana
        yn = input('Would you like to download the detailed report for base-pair changes? [Yes or No] ')
        if yn == 'yes':
            b = input('Which bacteria would you like?')
            # dowload the report
            print('Report Downloaded.')
            print('Thank you for using our program!')
        else:
            print('Thank you for using our program!')
        command = input('\n>> ')




#for information, type "Info"
#to run the prorgam, type "Run"

#Info
#This program is designed to help find the most appropriate bacterial vector to use for producing a specific protein
#The program will suggest the most appropriate bacteria for use, but you can select any bacteria to produce a report
#What to expect in your output: The bacterial sequence, the number of mismatches, the location of mismatches, the type of mismatches

#in order to find your best match bacteria, your input file should be:
#a text file containing your amino acid sequence with each amino acid in a seperate row, for example:
#Methionine
#Leucine
#Serine
#TerminationCodon

#Run
#Promt the user: "What is the name of the file with your desired amino acid sequence?"
#After the running is complete, save general report and print "Report dowloaded!"
#print "The most appropriate bacteria is Bacteria []"
#prompt "Would you like to download the detailed report for base-pair changes?" [Yes or No]

#Yes
#prompt "Which Bacteria would you like?" [A, B, C]
#print "Report Dowloaded"
#print "Thank you for using our program!"

#No
#print "Thank you for using our program!"