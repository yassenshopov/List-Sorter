def list_function():
    print('\n#########################################################################')
    print('This function will request integers/floats as input, one at a time.\n')
    print('After you have entered all your inputs, this function will sort the list \nand present the average, median, and mean values.\n')
    print('Once you have entered all your inputs, simple press ENTER to get the result.')
    print('#########################################################################\n')

    ul = []

    while True:

        input_var = input('Enter a numerical value: ')

        if len(ul) != 0:
            if input_var == "":
                break
        else:
            if input_var == "":
                print('List cannot have 0 entries.')
                continue
        try:
             input_var = int(input_var)
        except:
            try:
                input_var = float(input_var)
            except:
                if ',' in input_var:
                    input_var = input_var.replace(',','.')
                    try:
                        input_var = float(input_var)

                    except:
                        print('The data you entered is not numerical. Try again.')
                        continue
                else:
                    print('The data you entered is not numerical. Try again.')
                    continue

        ul.append(input_var)
        print(ul)
        print()

    print('Your final list looks like this, unordered:\n',ul,sep="")
    print()

    ol = []

    while len(ul) != 0:
            temp = ul[0]
            for list_item in ul:
                if list_item < temp:
                    temp = list_item
            ol.append(temp)
            ul.remove(temp)
    
    print()
    print('Your ordered list is:\n',ol,sep='')
    del ul

    average = 0
    length = 0
    for item in ol:
        average += item
        length += 1
    average = average/length
    print('Average:',round(average*1000)/1000)

    if (length%2) == 0:
        index1 = int((length/2) - 1)
        index2 = int((length/2))
        median = (ol[index1] + ol[index2])/2
    else:
        median = ol[int((length/2) - 0.5)]
    print('Median:', median)

    ol_dict = {}
    for item in ol:
        ol_dict[item] = 0
    for item in ol:
        ol_dict[item] += 1
    entry_list = []
    for entry in ol_dict:
        entry_list.append(ol_dict[entry])
    temp = 0
    for entry in entry_list:
        if entry > temp:
            temp = entry
    entry_list = []
    for key, value in ol_dict.items():
        if value == temp:
            entry_list.append(key)
    if len(entry_list) == 1:
        print('Mode:',entry_list[0])
    else:
        string = ', '.join([str(entry) for entry in entry_list])
        print('Modes:', string)



if __name__ == "__main__":
    list_function()