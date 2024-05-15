#Dictionary for store contact
contacts={}

# for add contact in contact dictionary
def add_contact():
    name = input('\nName: ')
    if name in contacts:
        print('\nThis contact is already exist.')
    else:
        phonenumber = input('Phone Number: ')
        email = input('E-mail: ')
        address = input('Address: ')
        contacts[name] = phonenumber, email, address
    
# for change the mobilenumber 
def update_contact():
    name = input('\nName: ')
    if name in contacts:
        phonenumber=input('New Phone Number: ')
        contacts[name]=phonenumber,*contacts[name][1:]
        print('\nPhone Number Successfully Updated.')
    else:
        print('\nThis Contact is not Exist.')
        
#for delet the contact        
def delete_contact():
    name = input('\nName: ')
    if name in contacts:
        del contacts[name]
        print('\nContact Deleted Successfully.')
    else:
      print('\nContact does not exist.')
      
# for search the contact
def search_contact():
    name = input('\nName: ')
    if name in contacts:
        print(contacts[name])
    else:
        print('\nContact does not exist.')

# fkr display the contact list
def display_contact():
    if contacts == {}:
        print('\nThere is no Contact in List.')
    else:
        print('\nContact List:\n')
        for key, value in contacts.items():
            print(key, value)
 
# making loop for ask continuosily                  
while True:
    
    # to tell about the choices and ask from the user
    print('\nContact Book Menu:')
    print('1. Add Contact')
    print('2. Update Contact')
    print('3. Delete Contact')
    print('4. Search Contact')
    print('5. Display Contacts')
    print('6. Exit')
    
    choice=input('\nWrite your choice (1-6): ')
    
# statemnets for do work according to user
    
    if choice =='1':
        add_contact()
        
    elif choice == '2':
         update_contact()
    
    elif choice == '3':
       delete_contact()
      
    elif choice == '4':
       search_contact()
      
    elif choice == '5':
       display_contact()
      
    elif choice == '6':
      print(('Thanks, Exiting...'))
      break
    
    else:
          print('\nInvalid Choice, Please Try Again.')