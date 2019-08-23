#PF-Tryout
import re

flight_details="Good Evening, Welcome to British Airways. Your flight number is ba8004. Flight departure time is 16:45"

#This function returns the values in the search result
def printout(search_result):
    if(search_result!=None):
        return search_result.group()
    else:
        return "No Output"

search_result = re.search(r"British Airways",flight_details)    #Find whether the flight service
                                                                #name, British Airways is present in the
                                                                #given string and if so, display it.
print(printout(search_result))

search_result = re.search(r"16:45$", flight_details)            #Find whether the flight service name,
                                                                #British Airways is present in the given string and if so,
                                                                #display it.
print(printout(search_result))

search_result = re.search(r"^Good",flight_details)              #Find whether the flight details starts with "Good" and if so,
                                                                #display it.
print(printout(search_result))

search_result = re.search(r"F\w{5}",flight_details)           #Find a word which starts with 'F' and having 6 characters in it,
                                                                #if so display it.
                                                                
print(printout(search_result))                                  #Search for a word which starts with "ba" followed by exactly 4
                                                                #digits. If found, replace the two alphabets with the corresponding
                                                                #uppercase alphabets.

print(re.sub(r"ba(\d{4})", r"BA\1", flight_details))                                         