# maidata 左右反

sql_list = []
new_sql_list = []

with open("input.txt","r",encoding="utf-8") as infile :

    for line in infile :

        sql_list += [line.rstrip("\n")]
    
    for x in range( len(sql_list) ) :

        new_element = ""

        for y in range( len(sql_list[x]) ) :

            if sql_list[x][y].isdigit() :    

                if sql_list[x][y-1] != "[" and sql_list[x][y+1] != "]" and sql_list[x][y+1] != ":" and sql_list[x][y-1] != ":" and sql_list[x][y-1] != "{" and sql_list[x][y+1] != "}" :

                    if sql_list[x][y] == "1" : new_element += "8"
                    elif sql_list[x][y] == "2" : new_element += "7"
                    elif sql_list[x][y] == "3" : new_element += "6"
                    elif sql_list[x][y] == "4" : new_element += "5"
                    elif sql_list[x][y] == "5" : new_element += "4"
                    elif sql_list[x][y] == "6" : new_element += "3"
                    elif sql_list[x][y] == "7" : new_element += "2"
                    elif sql_list[x][y] == "8" : new_element += "1"
                    
                else :

                    new_element += sql_list[x][y]

            else :

                if sql_list[x][y] == "<" : new_element += ">"
                elif sql_list[x][y] == ">" : new_element += "<"
                elif sql_list[x][y] == "q" : new_element += "p"
                elif sql_list[x][y] == "p" : new_element += "q"
                elif sql_list[x][y] == "pp" : new_element += "qq"
                elif sql_list[x][y] == "s" : new_element += "z"
                elif sql_list[x][y] == "z" : new_element += "s"
                else : new_element += sql_list[x][y]
            
        new_sql_list += [new_element]
                
                
    
    for x in range( len(new_sql_list) ) :

        print( new_sql_list[x] )
    
with open("output.txt","w",encoding="utf-8") as outfile :

    for line in range(len(new_sql_list)) :

        outfile.write(new_sql_list[line].rstrip()+"\n")
