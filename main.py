from linkedQFile import LinkedQ

#Create linked queue object
q = LinkedQ()

#Create list for printing
cardsOut=[]

#Retrieve deck of cards from user, separated by ' '
cards=input()
cards=cards.split(' ')

#Enqueue cards to linked queue
for ele in cards:
    q.enqueue(ele)

#Perform magic trick resulting in reshuffeled cards in list for print
while q.isEmpty()==False:
    q.enqueue(q.dequeue())
    cardsOut.append(q.dequeue())

#Print output list
print(*cardsOut, sep=' ')
