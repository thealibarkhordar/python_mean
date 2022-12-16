import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name, 'r') as fin:
        reader = csv.reader(fin)
        l = []
        k = []
        a = dict()

        for row in reader:
            name = row [0]
            l.append(name)
            for adad in row[1:]:
                k.append(float(adad))
            ave = mean(k)
            a[name] = ave
            k = []

    with open(output_file_name, 'w') as fout:
        writer = csv.writer(fout)
        for i in range(0, len(l)):
            writer.writerow([l[i], a[l[i]]])
            
    


def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name, 'r') as fin:
        reader = csv.reader(fin)
        h = []
        k = []
        l = []
        a = dict()
        for row in reader:
            name = row[0]
            for adad in row[1:]:
                k.append(float(adad))
            ave = mean(k)
            a[name] = ave
            l.append(float(ave))
            k = []
            h.append(name)
            a[0] = -10
            

    with open(output_file_name, 'w') as fout:
        writer = csv.writer(fout)
        l.sort()
        for j in range(0, len(l)):
            for i in range(0, len(h)):
                if a[h[i]] == l[j]:
                    writer.writerow([h[i], a[h[i]]])
                    h[i] = 0

    


def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name, 'r') as fin:
        reader = csv.reader(fin)
        k = []
        l = []
        h = []
        a = dict()
        for row in reader:
            name = row[0]
            for adad in row[1:]:
                k.append(float(adad))
            ave = mean(k)
            a[name] = ave
            l.append(float(ave))
            k = []
            h.append(name)
            a[0] = -10

    with open(output_file_name, 'w') as fout:
        writer = csv.writer(fout)
        l.sort()
        for i in range (0, len(h)):
            if a[h[i]] == l[-1]:
                writer.writerow([h[i], a[h[i]]])
                h[i] = 0
                break
        for i in range(0, len(h)):
            if a[h[i]] == l[-2]:
                writer.writerow([h[i], a[h[i]]])
                h[i] = 0
                break
        for i in range(0, len(h)):
            if a[h[i]] == l[-3]:
                writer.writerow([h[i], a[h[i]]])
                h[i] = 0
                break


def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name, 'r') as fin:
        reader = csv.reader(fin)
        k = []
        l = []
        for row in reader:
            for adad in row[1:]:
                k.append(float(adad))
            ave = mean(k)
            l.append(float(ave))
            k = []

    with open(output_file_name, 'w') as fout:
        writer = csv.writer(fout)
        l.sort()
        writer.writerow([l[0]])
        writer.writerow([l[1]])
        writer.writerow([l[2]])
    


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name, 'r') as fin:
        reader = csv.reader(fin)
        k = []
        l = []
        for row in reader:
            for adad in row[1:]:
                k.append(float(adad))
            ave = mean(k)
            l.append(float(ave))
            k = []

    with open(output_file_name, 'w') as fout:
        writer = csv.writer(fout)
        l.sort()
        writer.writerow([mean(l)])
# after runnig codes type the function names and put the file address into the ()
