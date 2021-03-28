class DoubleLinkedNode:
	def __init__(self, value: int=0):
		self.value, self.left, self.right = value, None, None

class Stack:
	def __init__(self):
		self.head = None
		self.middle = None
		self.size = 0

	def deleteMiddle(self) -> int:
		if self.size == 0:
			return None

		elif self.size == 1:
			outputValue = self.middle
			self.head, self.middle = None, None
			self.size -= 1
			return outputValue

		else:
			# Any size >= 2
			outputValue = self.middle.value
			
			middleLeft = self.middle.left
			middleRight = self.middle.right
			
			# Removing our middle's references
			self.middle.left = None
			self.middle.right = None

			# Connecting the two nodes to the left/right of our middle together
			if middleLeft:
				middleLeft.right = middleRight

			if middleRight:
				middleRight.left = middleLeft

			if self.size % 2 == 0:
				self.middle = middleLeft

			elif self.size % 2 == 1:
				self.middle = middleRight
		
			self.size -= 1
			return outputValue

	def __moveMiddle__(self, newSize) -> None:
		if self.size == 0 and newSize == 1:
			# Going from None middle to initializing it as the head
			self.middle = self.head
		elif self.size == 1 and newSize == 0:
			# Removing our head
			self.middle = None

		else:
			# Handling overall deltas
			sizeMod = newSize % 2
			if self.size > newSize:
				# Decreaing our total size, moving our middle to the right if applicable
				if sizeMod == 0:
					self.middle = self.middle.right
			else:
				# Increaing our total size, moving our middle to the left if applicable
				if sizeMod == 1:
					self.middle = self.middle.left

	def pop(self) -> int:
		# TODO: Come back and ensure that our 'middle' value gets modified appropriately
		if not self.head:
			return None
		elif self.size == 1:
			outputValue = self.head.value
			self.head, self.middle = None, None
			return outputValue
		else:
			outputValue = self.head.value
			self.head = self.head.right
			self.head.left = None
			self.__moveMiddle__(self.size - 1)
			self.size -= 1
			return outputValue

	def push(self, value: int) -> None:
		# TODO: Come back and ensure that our 'middle' value gets modified appropriately
		if not self.head:
			self.head = DoubleLinkedNode(value)
		else:
			newHead = DoubleLinkedNode(value)
			self.head.left = newHead
			newHead.right = self.head
			self.head = newHead
		self.__moveMiddle__(self.size + 1)
		self.size += 1

	def __repr__(self) -> str:
		o = list()
		n = self.head
		while n:
			o.append(str(n.value))
			n = n.right
		return ' '.join(o)

s = Stack()
for i in range(10):
    s.push(i)
    #print(s)

for j in range(5):
    print(s)
    v = s.deleteMiddle()
    print(v,",",s)