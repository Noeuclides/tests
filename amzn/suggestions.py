def threeKeywordSuggestions(numreviews, repository, customerQuery):
    #empty list to return the matching patterns
    suggestions = []
    #inner lists:
    inner = []

    count = 1

    #sorting repository array
    repository.sort()

    #outer loop to iterate string from 2 letters to the end of it
    for part in range(2, len(customerQuery) + 1):
        print(customerQuery[:part])
        #inner loop to fill the suggestion arrray with the matching strings
        for index in range(len(repository)):
            customCase = customerQuery[:part].casefold()
            repoCase = repository[index][:part].casefold()
            #conditional to verify if there is a match
            print(customCase, repoCase)
            if customCase == repoCase and count <= 3:
                #fill the array if it match
                inner.append(repository[index])
                count = count + 1
        print("INNER LIST", inner)
        suggestions.append(inner)
        inner = []
        count = 1
    print("SUGGESTIONS", suggestions)
            
