# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
def arithmetic_arranger(problems, solve = False):
    if len(problems) > 5: return 'Error: Too many problems.'
    problemsArr = []

    for problem in problems:
      problemsArr.append(problem.split())

    # problem[0] = primer número
    # problem[1] = operador
    # problem[2] = segundo número

    firstRow = '' # primera fila
    secondRow = '' # segunda fila
    linesRow = '' # fila lineas
    resultsRow = '' # fila resultados

    for problem in problemsArr:
      firstNum = problem[0]
      secondNum = problem[2]
      operator = problem[1]
      diff = 0 # los espacios de más que hay que dejar para alinear ambos números
      firstLength = len(firstNum)
      secondLength = len(secondNum)
      linesLength = firstLength + 2

      if not firstNum.isnumeric() or not secondNum.isnumeric(): 
        return 'Error: Numbers must only contain digits.'
      if operator != '+' and operator != '-':
        return 'Error: Operator must be \'+\' or \'-\'.'
      if firstLength > 4 or secondLength > 4:
        return 'Error: Numbers cannot be more than four digits.'

      secondRow += operator + ' '

      if secondLength > firstLength:
        diff = secondLength - firstLength
        linesLength += diff
        for x in range(diff):
          firstRow += ' '
      elif firstLength > secondLength:
        diff = firstLength - secondLength
        for x in range(diff):
          secondRow += ' '

      for x in range(linesLength):
        linesRow += '-'

      if solve:
        if operator == '+':
          result = int(firstNum) + int(secondNum)
        elif operator == '-':
          result = int(firstNum) - int(secondNum) 

        resultLength = len(str(result))

        diff = linesLength - resultLength

        for x in range(diff):
          resultsRow += ' '
        
        resultsRow += str(result)
      
      firstRow += '  ' + firstNum
      secondRow += secondNum

      if problem != problemsArr[len(problemsArr) - 1]:
        firstRow += '    '
        secondRow += '    '
        linesRow += '    '
        resultsRow += '    '

      arranged_problems = firstRow + '\n' + secondRow + '\n' + linesRow

      if solve: 
        arranged_problems += '\n' + resultsRow



    return arranged_problems