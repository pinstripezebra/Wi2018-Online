# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 11:58:22 2018

@author: seelc
"""

import datetime

'''Donor class stores all the information for an individual donor'''            
class donor:
    
    #Declares donor object and verifies that user inputs valid object parameters
    def __init__(self, name_request, donation_amount):
        if isinstance(name_request, str):
            self.name = name_request
        else:
            raise TypeError("Donor name must be a string!")
        
        #Testing to determine if donation_amount is of acceptable type and value
        try: 
            int_donation_amount = int(donation_amount)
            if int_donation_amount > 0:
                self.donation = int(donation_amount)
                self.donation_times = 1
                self.avg_donation = round(int(self.donation)/self.donation_times)
                
            else:
                raise ValueError("Donation must be positive!")
        except TypeError:
            print("Donation must be capable of being cast to integer") 
            
        
'''Donor storage allows for the aggregation of multiple donors and contains a 
method for each action required of the mailroom program'''        
class donor_storage(object):
    
    #Uses a list to store all the donor objects
    def __init__(self):
        self.donor_object_storage = list()
    
    #Adds a new donor to the donor list, or updates existing donor    
    def update_donor_list(self,my_donor):
        
        #If the donor isnt the first one in the data base
        if len(self.donor_object_storage) > 0:
            recurring_donor = False
            for i in range(len(self.donor_object_storage)):
                
                #If the donor has previously donated
                if my_donor.name == self.donor_object_storage[i].name:
                    
                    self.donor_object_storage[i].donation = my_donor.donation + self.donor_object_storage[i].donation
                    self.donor_object_storage[i].donation_times = self.donor_object_storage[i].donation_times + 1
                    self.donor_object_storage[i].avg_donation = self.donor_object_storage[i].donation/self.donor_object_storage[i].donation_times
                    recurring_donor = True
                    #print(self.donation, self.donation_times)
                    
            #If the donor is neither a recurring donor or the first donor
            if not recurring_donor:
                self.donor_object_storage.append(my_donor)
                
        #If its a new donor who is also the first donor
        else:
            self.donor_object_storage.append(my_donor)
            print("Updated donor list with new donor")
                
        
    #prints the list of donors in a report format    
    def print_report(self):
        max_name_length = 0
        max_donor_length = 0
        avg_gift_length = 0
        default_header = "Donor Name"+" "+ "|" +"Total Given" + "  |" + "Num Gifts" + "|" + "Average Gift"
        default_length = len(default_header)
        
        for i in range(len(self.donor_object_storage)):
            #Determining max length of donor names
            if len(self.donor_object_storage[i].name) > max_name_length:
                max_name_length = len(self.donor_object_storage[i].name)
                
            #determining max length of donation amounts
            if len(str(self.donor_object_storage[i].donation)) > max_donor_length:
                max_donor_length = len(str(self.donor_object_storage[i].donation))
                
            #determing max length of avg donation amount
            if len(str(round(self.donor_object_storage[i].donation/self.donor_object_storage[i].donation_times, 2))) >avg_gift_length:
                avg_gift_length = len(str(round(self.donor_object_storage[i].donation/self.donor_object_storage[i].donation_times, 2)))
                
        required_length = max_name_length + max_donor_length + avg_gift_length + 4
        
        #Prints the first line with properly spaced column headers
        first_column = max(max_name_length, len("Donor Name"))
        second_column = max(max_donor_length, len("Total Given"))
        third_column = max(avg_gift_length, len("Average Gift"))
        
        #Print statement that deals with printing each donors information in a 
        #correctly formatted fashion
        print("Donor Name" + " "*max(max_name_length - len("Donor Name"), 0)+  "|",
              "Total Given" + " " * max(max_donor_length - len("Total Given"), 0) + "|",
              "Num Gifts" + "|" + " "*max(avg_gift_length - len("Average Gift") ,0),
              "Average Gift")
        
        #prints the second line with the correct number of dashes
        print("-"*max(default_length, required_length))
        
        #Prints data for each donor object one line at a time
        for i in range(len(self.donor_object_storage)):
            print(self.donor_object_storage[i].name,
                  " "*(first_column - len(self.donor_object_storage[i].name)),
                  " "* (second_column - len(str(self.donor_object_storage[i].donation))),
                  str(self.donor_object_storage[i].donation),
                  " "*(len("Num Gifts")- len(str(self.donor_object_storage[i].donation_times))),
                  str(self.donor_object_storage[i].donation_times),
                  " "*(third_column - len(str(self.donor_object_storage[i].avg_donation))),
                  str(self.donor_object_storage[i].avg_donation))
    
    #Writes a thank you letter to a separate file for each donor     
    def send_group_thanks(self):
        
        #Running through the list of names and writing a thank you letter for each donor
        for i in range(len(self.donor_object_storage)):
            #Creating a new text file   
            dateSent = str(datetime.date.today())
            group_Thanks = open("{}_{}".format(self.donor_object_storage[i].name, dateSent), "w")
            line_1 = "Dear {},\n\nThank you for your generous donation of ${},"
            line_2 = "it will be put to good use.\n\n-Sincerely, the team\n\n"
            group_Thanks.write((line_1 + line_2).format(self.donor_object_storage[i].name,  self.donor_object_storage[i].donation))
           
def main():
    overall_storage = donor_storage()
    
    #promting the user to choose a main action
    userAction = ""
    while userAction !="4":
        userAction = input( "Choose an action: \n1- Send a thank you\n2-Create a Report\n3-Send a thank you to everyone\n4-Quit\n")
        
        #Throws an exception if userAction isnt 1, 2, or 3
        try:
            assert userAction in ["1", "2", "3", "4"]
            #if the user chooses to send a thank you
            if userAction == "1":
                name_request = input("Please select a name: ")
                donation_amount = input("Please enter a donation amount: ")
                
                #Creates a new donor with the current name_request and donation_amount
                my_donor = donor(name_request, donation_amount)
                #Adds the new donor to the donor database
                overall_storage.update_donor_list(my_donor)
        
            #if the user chooses to create a report
            elif userAction == "2":
                overall_storage.print_report()
                
            #if the user chooses to send a thank you to everyone
            elif userAction == "3":
                overall_storage.send_group_thanks()
                
            #if none of the above options are chosen quits the program
            elif userAction == "4":
                print("Quiting program")
                break
            
        except ValueError:
            print("The value entered must be 1, 2, 3, or 4")

if __name__ == '__main__':
    main()         
    
    