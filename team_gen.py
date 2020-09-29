import random
import sys

def scanfint(string,scope=None):
    while True:
        try:
            inp=int(input(string))
            if scope==None:
                break
            else:
                if inp in scope:
                    break
                else:
                    print("Entered number is out of scope")
        except ValueError:
            print("Invalid Input")
    return(inp)

def factorize(no_of_members):
    factors=[]
    for i in range(2,no_of_members):
        if no_of_members%i==0:
            factors.append(i)
    return(factors)

def random_array_generator(first_member,last_member,no_of_members,exceptions,random_array):
    while len(random_array)<no_of_members:
        randnbr=random.randint(first_member,last_member)
        if randnbr not in random_array and randnbr not in exceptions:
            random_array.append(randnbr)
    return(random_array)

def group(array_linear,no_of_members,no_of_group_members):
    array_grouped=[]
    for i in range(0,no_of_members,no_of_group_members):
        j=i
        temp=[]
        while j<i+no_of_group_members and j<no_of_members:
            temp.append(array_linear[j])
            j+=1;
        array_grouped.append(temp)
    return(array_grouped)

def print_group(array_grouped,no_of_groups):
    for i in range(no_of_groups):
        print("Group "+str(i+1)+" "+str(array_grouped[i]))
    if no_of_groups!=len(array_grouped):
        print("Left Out "+str(array_grouped[no_of_groups]))

print('CC-POCKETAPE.COM')
first_member=scanfint("Enter first member in the range: ")
last_member=scanfint("Enter last member in the range: ")
while True:
    no_of_exceptions=scanfint("Enter number of exceptions in the range: ",range(last_member-first_member+1+1))
    exceptions=[]
    for i in range(no_of_exceptions):
        exception=scanfint("Enter exceptions in the range one by one: ",[k for k in range(first_member,last_member+1) if k not in exceptions])
        exceptions.append(exception)

    no_of_members=last_member-first_member+1-no_of_exceptions

    if exceptions==0:
        print("No Exceptions")
    else:
        print("Exceptions: "+str(exceptions))
    choice=scanfint("Are the exceptions entered correctly?\n1.Yes\n2.No\n:")
    if choice==1:
        break
    
print("Total number of members: "+str(no_of_members))

factors=factorize(no_of_members)
if len(factors)==0:
    print("Number cannot be factorized\nLeaving 1 member out")
    factors=factorize(no_of_members-1)
if len(factors)==1:
    no_of_group_members=factors[0]
else:
    print("Number of possible members in each group is: " + str(factors))
    no_of_group_members=scanfint("Choose the number of members in a group from the possible list: ", factors)
no_of_groups=no_of_members//no_of_group_members


print("Number of members in each group: "+str(no_of_group_members))
print("Number of groups: "+str(no_of_groups))
random_array=[]
choice=scanfint("Choose:\n1. Full Randomization\n2. Some members are already allocated to some groups\n: ",[1,2])
if choice==2:
    while True:
        no_of_groups_beforehand=scanfint("Enter number of Group(s) already allocated: ", range(1,no_of_groups+1))
        for i in range(no_of_groups_beforehand):
            print("Enter members for Group "+str(i+1))
            for j in range(i*no_of_group_members,(i+1)*no_of_group_members):
                member=scanfint("Enter members one by one: ", [k for k in range(first_member, last_member+1) if k not in exceptions and k not in random_array])
                random_array.append(member)
        print("Entered Group(s):")     
        print_group(group(random_array,no_of_groups_beforehand*no_of_group_members,no_of_group_members),no_of_groups_beforehand)
        choice2=scanfint("1.Yes\n2.No. Re-enter members\n: ",[1,2])
        if choice2==1:
            break

 
sys.stdout = open("test.txt", "w")
print("LIST GENERATED SUCCESSFULLY ")
print("do visit https://pocketape.com/ ")
members_in_random_array=random_array_generator(first_member,last_member,no_of_members,exceptions,random_array)
members_in_random_matrix=group(members_in_random_array,no_of_members,no_of_group_members)
print_group(members_in_random_matrix,no_of_groups)
sys.stdout.close()