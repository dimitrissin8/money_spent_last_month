#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Written by Dimitris Sinanis on 20/04/2018.
#This program makes a monthly graph. You can see how much money you spent each month.
#Python version: 3.6.4
#Specifications: The .txt folder must have 31 lines only. Neither more nor less! Each line must have an integer number.For example, if this month has 28 days fill in with zeros the other days in .txt folder.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#"=================================The_code_begins_here================================="
def log_in():
    vote_for_graph=input("Would you like to see the graph (yes or no) :")
    if vote_for_graph=="yes":
        make_graph()
        print("\nMore informations:\n\nThe total amount you spent the last month is {}.\nThe {}'st day you spent the smallest amount ==> {}.\nThe {}'st day you spent the biggest amount ==> {}.\nThe average amount you spent the last month is {}. ".format(sum(read_from_txt("money_spent.txt")),read_from_txt("money_spent.txt").index(min(read_from_txt("money_spent.txt")))+1,min(read_from_txt("money_spent.txt")),read_from_txt("money_spent.txt").index(max(read_from_txt("money_spent.txt")))+1,max(read_from_txt("money_spent.txt")),float((sum(read_from_txt("money_spent.txt")))/31)))
        print("\n===========================")
        print("Written by Dimitris Sinanis.")
        print("============================")
        input("")
    else:
        import datetime
        x=input("Tell us, have you fill in how much money you spent today {} ? (yes or no) ".format(datetime.datetime.now().strftime('%d/%m/%Y')))
        if x=="yes":
            return False
        else:
            return True

def read_from_txt(x):
    #SOS_SOS_SOS : the txt folder must you 31 lines only. Neither more nor less! Each line must have an integer number.
    F=open(x,"r")
    list1=F.readlines()
    F.close()
    list2=[]
    list3=[]
    for i in list1:
        list2.extend(i.split())
    for i in list2:
        list3.append(float(i))
    return list3

def write_to_txt(y):
        F=open(y,"a")
        logariasmos=(input("Fill in, how much money you spent (Today)  :"))
        F.write("\n{}".format(logariasmos))
        F.close()

def make_graph():
    try:
        import matplotlib.pyplot as plt
        days=[x for x in range(1,31+1)]
        money_spent=read_from_txt("money_spent.txt")
        plt.plot(days,money_spent,color = "#82edc9",linestyle=":",marker = "*")
        plt.ylabel("Money Spent")
        plt.xlabel("Days")
        plt.title("Statistics (Money spent last month)")
        plt.show()
    except ValueError:
        print("The .txt folder must have 31 lines only. Neither more nor less! Each line must have an integer number.")
        input("")
        quit()
  
def main():
    print("-------------------------------------------------------------")
    if log_in()!=True:
        quit()
    else:
        write_to_txt("money_spent.txt")
        input("Information saved successfully !")
        
main()    
#"==========================================The_end=========================================="
    
