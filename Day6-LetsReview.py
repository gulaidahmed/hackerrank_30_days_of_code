number_test_cases = int(input())

for i in range(0, number_test_cases):
    
    string_input = input()

    for j in range(0, len(string_input)):
        if j % 2 == 0:
            print(string_input[j], end='')
        
    print(" ", end='')
        
    for j in range(0, len(string_input)):
        if j % 2 !=0:
            print(string_input[j], end='')
    
    print("")
