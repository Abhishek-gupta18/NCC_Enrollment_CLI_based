import csv

fn = open('enrollment 2023-24.csv', 'a')  # Open the file in append mode to keep previous data
stuwriter1 = csv.writer(fn)
stuwriter1.writerow(['Group name', 'battalion name', 'regimental no.', 'Cadet firsrt name', 'Cadets middle name', 'Cadets last name','fathers firsst name','father middle name','father last name', 'mother first nme',' mother middle name', 'mother last name', 'gross oncome', 'instituion name',' gender', 'date of birth', 'adhaar no.',' blood group', 'e-mail',' parents mobile number', 'cadets moile no.', 'regimental no.', 'namo app','date of joining', 'height', 'stream', 'marks', 'bank name', 'ifsc code',' Bank address', 'account no.', 'institute'  ])



print('Enter some details below:')

while True:
  
    group = input('Enter group headquarters: ')
    bn = input('Enter battalion: ')
    regimental = input('Enter regimental number: ')
    CFname = input('Enter First Name According to class 10 marksheet: ')
    CMname = input('Enter Middle name according to class 10 marksheet: ')
    CLname = input('Enter last name According to 10th marksheet: ')
    FFname = input('Enter father first name: ')
    FMname = input('Enter father middle name: ')
    FLname = input('Enter father last name: ')
    MFname = input('Enter mother first name: ')
    MMname = input('Enter mother middle name: ')
    MLname = input('Enter mother last name: ')
    GIncome = eval(input('Enter the gross yearly income of parents in Rupees: '))
    Insti = input('Enter name of Institution: ')
    Gender = input('Enter cadet gender: ')
    DOB = input('Enter Date of Birth in dd/mm/yyyy format: ')
    A_C_No = int(input('Enter Adhar no.: '))
    B_Group = input('Enter Blood group of the Cadet: ')
    E_mail = input('Enter E-mail address: ')
    Mob1 = int(input('Enter parents Mobile No.: '))
    Mob2 = int(input('Enter cadet Mobile No.: '))
    address = input("Enter address in format of 'S/O or D/O: Address': ")
    namo = input('Enter yes or no for Namo app: ')
    DOJ = input('Enter Date of joining in the format of dd/mm/yyyy: ')
    height = eval(input('Enter height of cadet in cm: '))
    stream = input('Enter stream (science, commerce, humanities): ')
    Marks = eval(input('Enter marks obtained in previous class: '))
    NBank = input('Enter bank name: ')
    IFSC = input('Enter IFSC code of the bank: ')
    ABank = input('Enter Bank Address: ')
    Account = eval(input('Enter account No.: '))

    print('''1 = rural area
2 = Urban Area''')
    institute = int(input('Enter area according to the above data (only number): '))
    if institute == 1:
        print('Rural area')
    elif institute == 2:
        print('Urban area')
    else:
        print('Wrong input')

    sturec1 = [group, bn, regimental, CFname, CMname, CLname, FFname, FMname, FLname, MFname, MMname, MLname, GIncome,
Insti, Gender, DOB, A_C_No, B_Group, E_mail, Mob1, Mob2, address, namo, DOJ, height, stream, Marks,
NBank, IFSC, ABank, Account, institute]
    stuwriter1.writerow(sturec1)

    choice = input('Do you want to add another record? (yes/no): ')
    if choice.lower() != 'yes':
        break

fn.close()
