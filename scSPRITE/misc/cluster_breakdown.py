import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import sys
import re
import os

'''
cluster_breakdown = breaks each sonication data to determine the number of clusters in the following categories
'''

def cluster_breakdown(sonication_data):
    data = pd.read_csv(sonication_data, sep=" ",header=None)
    
    all_clusters = []
    singleton = 0
    cluster2to10 = 0
    cluster11to100 = 0
    cluster101to1000 = 0
    cluster1001to10000 = 0
    cluster10001to100k = 0
    over100k = 0

    for cluster in range(len(data)):
        '''
        s.find('word'): Gives the initial index where the word is found 
        -Therefore if the word is found, then the index positioning is >=0
        -If the word isn't found, then the value is -1 
        '''
        text_split = data[0][cluster].split('\t')
        cluster_size = len(text_split) - 1 # removes DPM-O-E-Y barcode from cluster size

        if cluster_size == 1:
            singleton += 1
        elif cluster_size <= 10:
            cluster2to10 += 1
        elif cluster_size <= 100:
            cluster11to100 += 1
        elif cluster_size <= 1000:
            cluster101to1000 += 1
        elif cluster_size <= 10000:
            cluster1001to10000 += 1
        elif cluster_size <= 100000:
            cluster10001to100k += 1
        else:
            over100k += 1
    
    all_clusters.extend([singleton, cluster2to10, cluster11to100, cluster101to1000, cluster1001to10000, cluster10001to100k, over100k])
    
    return singleton, cluster2to10, cluster11to100, cluster101to1000, cluster1001to10000, cluster10001to100k, over100k, all_clusters


'''
ultra_cluster_breakdown = breaks sonication data to list each cluster in the following categories
'''

def ultra_cluster_breakdown(sonication_data):
    data = pd.read_csv(sonication_data, sep=" ",header=None)
    
    all_ultra_clusters = []
    
    singleton = 0
    cluster2to10 = 0
    cluster11to100 = 0
    cluster101to1000 = 0
    cluster1001to10000 = 0
    cluster10001to100k = 0
    over100k = 0

    for cluster in range(len(data)):
        '''
        s.find('word'): Gives the initial index where the word is found 
        -Therefore if the word is found, then the index positioning is >=0
        -If the word isn't found, then the value is -1 
        '''
        text_split = data[0][cluster].split('\t')
        cluster_size = len(text_split) - 1 # removes DPM-O-E-Y barcode from cluster size

        if cluster_size == 1:
            singleton += 1
            all_ultra_clusters.append(cluster_size)
        elif cluster_size <= 10:
            cluster2to10 += 1
            all_ultra_clusters.append(cluster_size)
        elif cluster_size <= 100:
            cluster11to100 += 1
            all_ultra_clusters.append(cluster_size)
        elif cluster_size <= 1000:
            cluster101to1000 += 1
            all_ultra_clusters.append(cluster_size)
        elif cluster_size <= 10000:
            cluster1001to10000 += 1
            all_ultra_clusters.append(cluster_size)
        elif cluster_size <= 100000:
            cluster10001to100k += 1
            all_ultra_clusters.append(cluster_size)
        else:
            over100k += 1
            all_ultra_clusters.append(cluster_size)
    
    all_ultra_clusters.sort() #super duper important to sort from smallest to largest cluster size
    # important for condense_clusters_reads program
    
    return all_ultra_clusters

'''
condense_read_clusters - takes breakdown from ultra_cluster_breakdown and condenses it to num of reads and clusters of a given size
'''

def condense_read_clusters(ultra_breakdown):
    cluster_size = []
    num_clusters = []
    num_reads = []
    
    counter = 0 #need a way to keep track of position (i.e cluster sizes) in ultra_breakdown
    len_breakdown = len(ultra_breakdown)
    final_size = ultra_breakdown[len_breakdown-1]
    
    for size in range(final_size-1): #ideally range(final_size) but testing
        # remember size = 0 when initialized - need to start at size + 1 to make sure it goes through list
        current_size = ultra_breakdown[counter]
        cluster_count = 0
        
        if current_size == size+1: 
            cluster_size.append(current_size)
            while current_size == size+1:
                cluster_count += 1
                counter += 1
                current_size = ultra_breakdown[counter]
            else:
                num_clusters.append(cluster_count)
    
    '''
    For last size - add to cluster size list (apparently breaks from the for loop)
    '''
    cluster_size.append(current_size)
    num_clusters.append(1) # there should only be one of the last cluster size
    
    for position in range(len(num_clusters)):
        num_reads.append(cluster_size[position] * num_clusters[position]) 
    
    return cluster_size, num_clusters, num_reads

'''
read_breakdown = breaks each sonication data to determine the abs num of reads in the following categories
'''

def read_breakdown(sonication_data):
    data = pd.read_csv(sonication_data, sep=" ",header=None)
    
    all_reads = []
    read1 = 0
    read2to10 = 0
    read11to100 = 0
    read101to1000 = 0
    read1001to10000 = 0
    read10001to100k = 0
    over100k = 0

    for cluster in range(len(data)):
        '''
        s.find('word'): Gives the initial index where the word is found 
        -Therefore if the word is found, then the index positioning is >=0
        -If the word isn't found, then the value is -1 
        '''
        text_split = data[0][cluster].split('\t') 
        
        '''
        read_size: 
        1) removes DPM-O-E-Y barcode from cluster size
        2) determines the number of reads for every unique barcode (i.e. the size of the cluster)
        '''
        read_size = len(text_split) - 1 # removes DPM-O-E-Y barcode from cluster size

        if read_size == 1:
            read1 += read_size
        elif read_size <= 10:
            read2to10 += read_size
        elif read_size <= 100:
            read11to100 += read_size
        elif read_size <= 1000:
            read101to1000 += read_size
        elif read_size <= 10000:
            read1001to10000 += read_size
        elif read_size <= 100000:
            read10001to100k += read_size
        else:
            over100k += read_size
            
    all_reads.extend([read1, read2to10, read11to100, read101to1000, read1001to10000, read10001to100k, over100k])
    
    return read1, read2to10, read11to100, read101to1000, read1001to10000, read10001to100k, over100k, all_reads


# List of reads/cluster distribution
# all_sizes = ['Singleton', 'From 2 to 10', 'From 11 to 100', 'From 101 to 1000', 'From 1001 to 10k', 'From 10001 to 100k', 'Over 100k']
all_sizes = ['1', '2 to 10', '11 to 100', '101 to 1000', '1001 to 10k', '10001 to 100k', 'Over 100k']


# testing new definition cluster_breakdown
one, two, three, four, five, six, seven, clusters_0s = cluster_breakdown('clusters_all')

total_clusters = one + two + three + four + five + six + seven

print('Clusters Singleton: ' + str(one))
print('Clusters From 2-10: ' + str(two))
print('Clusters From 11-100: ' + str(three))
print('Clusters From 101-1000: ' + str(four))
print('Clusters From 1001-10000: ' + str(five))
print('Clusters From 10001-100k: ' + str(six))
print('Clusters Over 100k: ' + str(seven))
print('Total clusters: ' + str(total_clusters))


# testing new definition cluster_breakdown
sonic_sc1min = ultra_cluster_breakdown('clusters_all')

'''
Compile all information about clusters and reads into a new file
'''
timer = 0
location = os.getcwd()
for file in range(len(sonic_sc1min)):
    try:
        new_file = 'all_clusters_all'
        if timer == 0: 
            with open(new_file, 'w') as f_new:
                f_new.write(''.join('Cluster Size'))
                f_new.write('\n')
                f_new.write(''.join(str(sonic_sc1min[file])) + '\t')
                f_new.write('\n')
            timer += 1
        else:
            with open(new_file, 'a') as f_new:
                f_new.write(''.join(str(sonic_sc1min[file])) + '\t')
                f_new.write('\n')
    except Exception as e:
        raise e
        print("No files found here!")

# testing new definition read_breakdown
one, two, three, four, five, six, seven, reads_0s = read_breakdown('clusters_all')

total_reads = one + two + three + four + five + six + seven

print('Reads Singleton: ' + str(one))
print('Reads From 2-10: ' + str(two))
print('Reads From 11-100: ' + str(three))
print('Reads From 101-1000: ' + str(four))
print('Reads From 1001-10000: ' + str(five))
print('Reads From 10001-100k: ' + str(six))
print('Reads Over 100k: ' + str(seven))
print('Total reads: ' + str(total_reads))


'''
Compile all information about clusters and reads into a new file
'''
timer = 0
location = os.getcwd()
for file in range(len(all_sizes)):
    try:
        new_file = 'all_clusters&reads.txt'
        if timer == 0: 
            with open(new_file, 'w') as f_new:
                f_new.write(''.join('Size') + '\t' + ''.join('# of Clusters') + '\t' + ''.join('# of Reads'))
                f_new.write('\n')
                f_new.write(''.join(str(all_sizes[file])) + '\t')
                f_new.write(''.join(str(clusters_0s[file])) + '\t')
                f_new.write(''.join(str(reads_0s[file])) + '\t')
                f_new.write('\n')
            timer += 1
        else:
            with open(new_file, 'a') as f_new:
                f_new.write(''.join(str(all_sizes[file])) + '\t')
                f_new.write(''.join(str(clusters_0s[file])) + '\t')
                f_new.write(''.join(str(reads_0s[file])) + '\t')
                f_new.write('\n')
    except Exception as e:
        raise e
        print("No files found here!")

def cluster_reads_to_file(ultra_breakdown, file_name):
    cluster_size, num_clusters, num_reads = condense_read_clusters(ultra_breakdown)

    '''
    Compile all information about clusters and reads into a new file
    '''
    timer = 0
    location = os.getcwd()
    for file in range(len(cluster_size)):
        try:
            new_file = file_name
            if timer == 0: 
                with open(new_file, 'w') as f_new:
                    f_new.write(''.join('Size') + '\t' + ''.join('# of Clusters') + '\t' + ''.join('# of Reads'))
                    f_new.write('\n')
                    f_new.write(''.join(str(cluster_size[file])) + '\t')
                    f_new.write(''.join(str(num_clusters[file])) + '\t')
                    f_new.write(''.join(str(num_reads[file])) + '\t')
                    f_new.write('\n')
                timer += 1
            else:
                with open(new_file, 'a') as f_new:
                    f_new.write(''.join(str(cluster_size[file])) + '\t')
                    f_new.write(''.join(str(num_clusters[file])) + '\t')
                    f_new.write(''.join(str(num_reads[file])) + '\t')
                    f_new.write('\n')
        except Exception as e:
            raise e
            print("No files found here!")
    
    return

cluster_reads_to_file(sonic_sc1min, 'all_clusters_reads.txt')
