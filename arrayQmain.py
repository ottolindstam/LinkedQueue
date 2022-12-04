from arrayQFile import ArrayQ

# q = ArrayQ()
# q.enqueue(1)
# q.enqueue(2)
# x = q.dequeue()
# y = q.dequeue()
# if (x == 1 and y == 2):
#     print("OK")
# else:
#     print("FAILED")

while True:

    #Create array based queue object
    q = ArrayQ()

    #Create list for printing
    cardsOut=[]

    #Retrieve deck of cards from user, separated by ' '
    cards=input("Enter space separated sequence of numbers for the magic trick: ")
    cards=cards.split(' ')

    #Enqueue cards to linked queue
    for ele in cards:
        q.enqueue(ele)

    #Perform magic trick resulting in reshuffeled cards in list for print
    while q.size()>0:
        q.enqueue(q.dequeue())
        cardsOut.append(q.dequeue())

    #Print output list on singel row with ' 'separator
    print(*cardsOut, sep=' ')
