# -*- coding: utf-8 -*-
import re
#Script for Union files with goods which has rests.


#list_for_set - list for goods codes
#list_for_group - list for name groups
#??
list_for_set=[]
list_for_group=[]


def check_rests(list2, y):
    global banned_list
    global i
    for x2 in list2:
        y2=x2.split(';')
        if y[0]==y2[0] and y[1] != '' and x!=x2 and y[0] not in banned_list:
            banned_list.append(y[0])

            #print y[2] + ' ' + y2[2]+ ' ' +y[3] + ' ' + y2[3]
            if y[2] !='':
                vary2=float(re.sub('\,','.',y[2]))
            else:
               vary2=0 
            if y2[2] !='':  
                vary3=float(re.sub('\,','.',y2[2]))
            else:
                vary3=0
            vary2_y2=vary2+vary3

            if y[3] !='':
                vary4=float(re.sub('\,','.',y[3]))
            else:
                vary4=0
            if y2[3] !='':   
                vary5=float(re.sub('\,','.',y2[3]))
            else:
                vary5=0
            vary3_y3=vary4+vary5

            
            vary4_y4=vary2_y2-vary3_y3
            vary5_y5=vary3_y3-vary2_y2

            vary2_y2=re.sub('\.',',',str(vary2_y2))
            vary3_y3=re.sub('\.',',',str(vary3_y3))
            vary4_y4=re.sub('\.',',',str(vary4_y4))
            vary5_y5=re.sub('\.',',',str(vary5_y5))
            
            
            var_for_add=y[0]+';'+y[1]+';'+vary2_y2+';'+vary3_y3+';'+vary4_y4+';'+vary5_y5
            lines1.remove(x)
            lines1.insert(i,var_for_add)
            #print str(i)+'  '+var_for_add
            i=i+1            
    i=i+1
    
    


def add_groups_and_codes_to_first_file(lines2):

    global lines1
    global list_for_set
    global list_for_group

    ot=0
    var_for_second_list=''
    for x2 in lines2:
        y2=x2.split(';')
        if var_for_second_list!='': 
              if y2[0] not in list_for_set:
                  if re.search('^\d[\d\-]+',y2[0]) and y2[1] != '': 
                      #print var_for_second_list
                      ##Check for same group, new goods code
                      if var_for_first_list==var_for_second_list:
                          ##Add code to goods code list
                          list_for_set.append(y2[0])
                          ##Add string to list of first file
                          lines1.insert(i, x2)
        ##if this is new group    
        elif y2[1] == '' and y2[2] == '':
            if y2[0] not in list_for_group:
                 ##Add group to group list
                 #print y2[0]
                 list_for_group.append(y2[0])
                 ##Add new group at the end of file
                 lines1.append(x2)
                 ok=1
                 while lines2[ot+ok] not in lines1 and re.search('^\d[\d\-]',lines2[ot+ok]):
                      ##Add goods code of new group at the end of file  
                      lines1.append(lines2[ot+ok])
                      ##Add goods code to the list of goods code first file
                      var_for_add_to_list=lines2[ot+ok].split(';')
                      list_for_set.append(var_for_add_to_list[0])
                      ok=ok+1
                      #print var_for_add_to_list[0]+var_for_add_to_list[1]
        ##Find group
        elif y2[1] == '':
             if y2[2] == '':
                 if y2[0] in list_for_group:
                      var_for_second_list=y2[0]
            
        ot=ot+1


#Open first file
f1 = open(r'C:\\27410.csv')
lines1 = f1.readlines()
f1.close()

#Open second file
f2 = open(r'C:\\27026.csv')
lines2 = f2.readlines()
f2.close()

#Open third file
f3 = open(r'C:\\27377.csv')
lines3 = f3.readlines()
f3.close()


var_for_first_list=1
var_for_second_list=2


#Create list of groups and goods codes
for x in lines1:
    y=x.split(';')
    if re.search('^\d',y[0]):
        list_for_set.append(y[0])
    else:
        list_for_group.append(y[0])


#Iterator
i=0

##Adding 
for x in lines1:
        sec=0
        i=+1
        y=x.split(';')
        if re.search('[^\d\-]',y[0]):
                var_for_first_list=y[0]
                print y[0]

        add_groups_and_codes_to_first_file(lines2)
        add_groups_and_codes_to_first_file(lines3)




i=0
banned_list=[]
for x in lines1:
    y=x.split(';')
    check_rests(lines2, y)
i=0
for x in lines1:
    y=x.split(';')    
    check_rests(lines3, y)


    

f = open(r'C:\export.csv','w')
f.writelines(lines1)
f.close()

