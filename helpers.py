def numberToWords(num):
    # Lists containing the words for the numbers
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    thousands = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion", "Sextillion", "Septillion", "Octillion", "Nonillion"]
    
    # Split the number into whole number and decimal parts
    numToStr = str(num)
    wholeNumber = numToStr.split(".")[0]
    decimalParts = numToStr.split(".")[1]
    print(decimalParts)

    # Empty strings to store the words
    decimalPartsToWords = ""
    wholeNumberToWords = ""

    # Convert decimal parts to words
    if int(decimalParts) == 0:
        decimalPartsToWords = "Zero Cents"

    elif len(decimalParts) == 1:
        decimalPartsToWords = tens[int(decimalParts)] + " Cents"

    elif int(decimalParts) // 10 == 0:
        decimalPartsToWords = ones[int(decimalParts)] + " Cents"

    elif int(decimalParts) // 10 == 1:
        decimalPartsToWords = teens[int(decimalParts) % 10] + " Cents"

    else:
        decimalPartsToWords = tens[int(decimalParts) // 10] + " " + ones[int(decimalParts) % 10] + " Cents"

    if int(wholeNumber) == 0:
        return "Zero Dollars and " + decimalPartsToWords

    partOfWholeNumber = ""

    # I've reversed the whole number and then I use // to find the word for the every thousand and % to find the words for the 3 numbers inside the thousand
    for i, n in enumerate(wholeNumber[::-1]):
        if i % 3 == 0:
            if i // 3 == 0:
                partOfWholeNumber = ones[int(n)] + " "
                continue
            partOfWholeNumber = ones[int(n)] + " " + thousands[i // 3] + " " + partOfWholeNumber
        if i % 3 == 1:
            if n == "0":
                continue
            if n == "1":
                partOfWholeNumber = teens[int(wholeNumber[::-1][i-1])] + " " + thousands[i // 3] + " "
            else:
                partOfWholeNumber = tens[int(n)] + " " + partOfWholeNumber
        if i % 3 == 2:
            if n == "0":
                wholeNumberToWords = partOfWholeNumber + wholeNumberToWords
                partOfWholeNumber = ""

                continue
            
            wholeNumberToWords = ones[int(n)] + " Hundred and " + partOfWholeNumber + wholeNumberToWords
            partOfWholeNumber = ""

        # print("Part of whole number: ", partOfWholeNumber)
        # print("Whole Number: ", wholeNumberToWords)

    if i % 3 < 2:
        # print("Inside")
        wholeNumberToWords = partOfWholeNumber + wholeNumberToWords

    # Add the decimal part and return the result
    return wholeNumberToWords + "Dollars and " + decimalPartsToWords