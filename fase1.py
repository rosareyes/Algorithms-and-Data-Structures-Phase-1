# -*- coding: utf-8 -*-
"""
Lab Case 1:
Rosa Reyes
Ines Sanz
"""

from dlist import DList
from dlist import DNode

import csv
import os.path

class Patient:
    """Class to represent a Patient"""
    def __init__(self,name,year,covid,vaccine):
        self.name=name
        self.year=year
        self.covid=covid
        self.vaccine=vaccine
        
    def __str__(self):
        return self.name+'\t'+str(self.year)+'\t'+str(self.covid)+'\t'+str(self.vaccine)


class HealthCenter(DList):
    """Class to represent a Health Center"""
    def __init__(self,filetsv=None):
        super(HealthCenter, self).__init__()
        print(filetsv)
        if filetsv is None or not os.path.isfile(filetsv):
            self.name=''

        else: 
            print('loading the data for the health center from the file ',filetsv)    
            self.name=filetsv.replace('.tsv','')
            tsv_file = open(filetsv)
            read_tsv = csv.reader(tsv_file, delimiter="\t")   
            for row in read_tsv:
                name=row[0]
                year=int(row[1])
                covid=False
                
                if int(row[2])==1:
                    covid=True

                vaccine=int(row[3])
                self.addLast(Patient(name,year,covid,vaccine))                
                
                
    
    def addPatient(self,patient):
        "add a new patient in alphabetic order"
        
        if self.isEmpty():
            self.addFirst(patient)
        
        else:
            aux= self._head      
            pos=0
            #This will tell us if the patient is already stored in the list or not                
            inside_list=False    

            while aux and not inside_list:

                if aux.elem.name==patient.name:   #If running through the list we find the the patient is already added
                                                    # to the list we wont do anything
                    inside_list=True
                elif aux.elem.name > patient.name:        #We run throught the list and we find the exact position at which to
                                                        # insert the patient
                    self.insertAt(pos,patient)
                    inside_list=True
                else:                               #This is used to continue running through the list,updating aux and pos
                    aux=aux.next
                    pos+=1


            if not aux:                #This means that we have run through the whole list and the only option is to                                   
                self.addLast(patient)
       
                                  
    def searchPatients(self,year,covid=None,vaccine=None):
        "search for all patients within the given parameters"
        result = HealthCenter()         
        #Node current will point to head    
        current = self._head    
                   
        #no need to check if the head is empty bc in that case will return an empty DList.      
        while current:
            if year == 2021 or year >= current.elem.year:               
                if covid == None:
                    if vaccine == None:
                        #Retrieves all the patients of the list or the one that matches the input year.
                        result.addLast(current.elem)
                    elif vaccine == current.elem.vaccine:
                        result.addLast(current.elem)
                elif covid == current.elem.covid:
                    if vaccine == None:
                        result.addLast(current.elem)
                    elif vaccine == current.elem.vaccine:
                        result.addLast(current.elem)           
            current = current.next
        return result  
    
    def statistics(self):
        "Gives statistics about the invoking HealthCenter"
        numcovid = numcovid1950 = novaccine = novaccine1950 = numvaccine1 = numvaccine2 = numpatients1950 = 0

        #Node current will point to head    
        current = self._head    
   
        #Checks whether the list is empty    
        if(self._head == None):    
            print("List is empty")    
            return None   
                
        while current:
            if current.elem.covid:
                numcovid = numcovid + 1
            if (current.elem.year <= 1950):
                numpatients1950 = numpatients1950 + 1
            if (current.elem.year <= 1950) and current.elem.covid == True:
                numcovid1950 = numcovid1950 + 1
            if current.elem.vaccine == 0:
                novaccine = novaccine + 1
            if current.elem.year <= 1950 and current.elem.vaccine == 0:
                novaccine1950 = novaccine1950 + 1
            if current.elem.vaccine == 1:
                numvaccine1 = numvaccine1 + 1
            if current.elem.vaccine == 2:
                numvaccine2 = numvaccine2 + 1
            current = current.next   
        
        numcovid = round(numcovid/self._size,2)
        numcovid1950 = round(numcovid1950/numpatients1950,2)
        novaccine = round(novaccine/self._size,2)
        novaccine1950 = round(novaccine1950/numpatients1950,2)
        numvaccine1 = round(numvaccine1/self._size,2)
        numvaccine2 = round(numvaccine2/self._size,2)
        
        return(numcovid,numcovid1950,novaccine,novaccine1950,numvaccine1,numvaccine2)   

    def merge(self,other):
       "Merges the patients of two health centers"
       #result = self
       #Node current will point to head    
       current = other._head      
                      
       while current:
           self.addPatient(current.elem)
           current = current.next   
       return self
    
    def minus(self,other):
        "Deletes patients in the invoking center that are in the given center"
        new_center=HealthCenter()
        aux=self._head  
        aux_other=other._head
        
        while aux:
            #If it founds two similar patients
            found=False
            #If smaller is True, goes to the next element because it wont find it in the rest of the list.
            smaller=False

            while aux_other and not found and not smaller:
                if aux.elem.name==aux_other.elem.name:
                    found=True
                #"aux comes before aux other"
                elif aux.elem.name<aux_other.elem.name:
                    smaller=True
                 #"aux other comes before aux"
                elif aux.elem.name>aux_other.elem.name:
                    aux_other=aux_other.next

            if not found:
                new_center.addPatient(aux.elem)

            aux=aux.next

        return new_center
    
    def inter(self,other):
        "Intersects patients of the invoking center with the patients of the given one"
        new_center=HealthCenter()
        aux=self._head
        aux_other=other._head

        while aux:
            found=False
            #If smaller is True, goes to the next element because it wont find it in the rest of the list.
            smaller=False
            while aux_other and not found and not smaller:
                if aux.elem.name==aux_other.elem.name:
                    found=True

                #"aux comes before aux other"
                if aux.elem.name<aux_other.elem.name:
                    smaller=True

                 #"aux other comes before aux"
                if aux.elem.name>aux_other.elem.name:
                    aux_other=aux_other.next

            if found:
                new_center.addPatient(aux.elem)

            aux=aux.next

        return new_center
                
    
     
if __name__ == '__main__':
    gst=HealthCenter('data/LosFrailes.tsv')
    print(gst)
    
    #Puedes añadir más llamadas a funciones para probarlas
    