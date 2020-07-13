import os #os module imported here
import csv

location = os.getcwd() # get present working directory location here
counter = 0 #keep a count of all files found
csvfiles = [] #list to store all csv files found at location
filebeginwithhello = [] # list to keep all files that begin with 'hello'
otherfiles = [] #list to keep any other file that do not match the criteria
delimiters = '\t'
timer = 0

'''
First item = ideally should only have cell ID, but couldn't figure out how to parse cell ID and cluster ID. So the first 
3 barcodes of each line correspond to the cell ID.

First number = total number of clusters

Second number = total number of reads

third number = total number of possible contacts - if following convention that for each Y cluster containing X reads, 
the number of possible contacts in that Y cluster is equal to X(X-1)/2
'''

for file in os.listdir(location):
    try:
        if file.startswith("DPM"): 
            file_to_open = file
            file_name = (os.path.splitext(file_to_open)[0]+os.path.splitext(file_to_open)[1])
#             print(file_to_open)
            with open(file_to_open, 'r') as f:
                reader = csv.reader(f, dialect='excel', delimiter=delimiters)
                data = list(reader)
                row_count = len(data)

            with open(file_to_open, 'r') as f:
                num_cluster = 0
                total_reads = 0
                num_contacts = 0
                new_file = 'one_last_time.txt'
                reader = csv.reader(f, dialect='excel', delimiter=delimiters)
                head = [next(reader) for x in range(row_count)]
                # Break apart into "write" and "append" because otherwise, it just overwrites over the first line...
                # Dunno how to fix it for now, but don't care, IT WORKS
                for line in range(len(head)):
                    len_line = len(head[line])
                    num_cluster += 1
                    total_reads += len_line - 1
                    num_contacts += (len_line-1) * (len_line - 2) / 2
            if timer == 0: 
                with open(new_file, 'w') as f_new:
                    f_new.write(''.join('Cell Barcode ID') + '\t' + ''.join('Num of Clusters') + '\t' + ''.join('Num of Reads') + '\t' + ''.join('Num of Contacts'))
                    f_new.write('\n')
                    f_new.write(''.join(file_name) + '\t')
                    f_new.write(''.join(str(num_cluster)) + '\t')
                    f_new.write(''.join(str(total_reads)) + '\t')
                    f_new.write(''.join(str(int(num_contacts))))
                    f_new.write('\n')
                timer += 1
            else:
                with open(new_file, 'a') as f_new:
                    f_new.write(''.join(file_name) + '\t')
                    f_new.write(''.join(str(num_cluster)) + '\t')
                    f_new.write(''.join(str(total_reads)) + '\t')
                    f_new.write(''.join(str(int(num_contacts))))
                    f_new.write('\n')
                    
    except Exception as e:
        raise e
        print("No files found here!")

# print("Total files found:\t", counter)
# print(location)
