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
        elif self.searchNode(patient):
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
            if search_node.next is not None:
                aux_node.next.prev = aux_node
               
            search_node.next = aux_node
            aux_node.prev = search_node
        #increase the size of the list  
        self._size+=1
        print(self)
          
    def searchNode(self, e):
        "search for an specific patient's name on the list"    
        i = 1;    
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
            i = i + 1    
                
        if(flag):            
            return 1     
        else:    
            return 0  

                

        
        
    def searchPatients(self,year,covid=None,vaccine=None):
       ...
    
    def statistics(self):
        ...

    def merge(self,other):
       ...
    
    
    def minus(self,other):
       ...
    
    def inter(self,other):
        ...
                
    
     
if __name__ == '__main__':
    gst=HealthCenter('data/LosFrailes.tsv')
    print(gst)
    
    #Puedes añadir más llamadas a funciones para probarlas
    