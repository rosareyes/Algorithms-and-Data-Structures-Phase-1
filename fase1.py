# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
        #create the new node to be inserted
        aux_node = DNode(patient)
        if self.isEmpty():
            self._head = aux_node
        elif self.searchName(patient):
            print("patient already on the list")
            return
        #insert the node at the beginning      
        elif self._head.elem.name >= aux_node.elem.name:         
            aux_node.next = self._head
            aux_node.next.prev = aux_node
            self._head = aux_node
        else:
            search_node = self._head
            #Find the node that will be before the aux node
            while (search_node.next and (search_node.next.elem.name < aux_node.elem.name)):
                search_node = search_node.next

            aux_node.next = search_node.next 

            #if the new node isn't the tail of the list
            if search_node.next:
                aux_node.next.prev = aux_node
               
            search_node.next = aux_node
            aux_node.prev = search_node
        #increase the size of the list  
        self._size+=1
       
          
    def searchName(self, e):
        "search for an specific patient's name on the list"    
        i = 1    
        flag = False    
        #Node current will point to head    
        current = self._head    
            
        #Checks whether the list is empty    
        if(self._head == None):    
            print("List is empty")    
            return 0    
                
        while current:    
            #Compare value to be searched with each node in the list    
            if(current.elem.name == e.name):    
                flag = True    
                return 1    
            current = current.next    
                           
        if not flag:            
            return 0                   
        
    def searchPatients(self,year,covid=None,vaccine=None):
        "search for all patients within the given parameters"
        result = HealthCenter()         
        #Node current will point to head    
        current = self._head    
                   
        #could be an aux method / no need to check if the head is empty bc in that case will return an empty DList.      
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
       result = self
       #Node current will point to head    
       current = other._head      
                      
       while current:
           result.addPatient(current.elem)
           current = current.next   
       return result
    
   

    def minus(self,other):
        "Deletes patients in the invoking center that are in the given center"
        #Makes a copy of self HealthCenter
        result = self
        #Sets the current node for the second list
        current_other = other._head      
        #Goes first through the second list
        while current_other:
           current = result._head
           #Sets an index to know the position of the node in case it has to be deleted
           i = 0
           #Goes through the first list to search for the Patients of second list one by one          
           while current:
               if current_other.elem.name == current.elem.name:
                   #Saves the next pointer before deleting the node at i position
                   current = current.next                                
                   result.removeAt(i)                              
               else:
                   #Sets the next position in case it didn't find the element
                    current = current.next                  
               i = i + 1
           current_other = current_other.next   	
        return result
    
    def inter(self,other):
        "Intersects patients of the invoking center with the patients of the given one"
        result = HealthCenter()
        #Sets the current node for the second list
        current_other = other._head      
        #Goes first through the second list
        while current_other:
           current = self._head
           #Sets an index to know the position of the node in case it has to be deleted

           #Goes through the first list to search for the Patients of second list one by one          
           while current:
               if current_other.elem.name == current.elem.name:
                   #Saves the next pointer before deleting the node at i position
                   result.addPatient(current.elem)                                  
               current = current.next                  

           current_other = current_other.next   	
        return result
                
    
     
if __name__ == '__main__':
    gst=HealthCenter('data/LosFrailes.tsv')
    print(gst)
    
    #Puedes añadir más llamadas a funciones para probarlas
    