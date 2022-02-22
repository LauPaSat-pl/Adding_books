class ToSell:
	__slots__ = ['title', 'category', 'price', 'negotiable', 'publishing_date', 'desc', 'photos', 'size']

	def __init__(self, title, price, category, negotiable, publishing_date='', desc='', photos='', size=''):
		self.title = title
		self.price = price
		if category == '':
			category = "Literatura"
		self.category = category
		if negotiable == '':
			negotiable = True
		self.negotiable = negotiable
		self.publishing_date = publishing_date
		self.desc = desc
		self.photos = photos
		if size == '':
			size='A'
		self.size = size

	def __repr__(self):
		result = f"\n\nTitle - {self.title} \nPrice - {self.price} \nCategory - {self.category} \nPublishing date - {self.publishing_date} \nDesc - {self.desc} \nSize - {self.size} \nNegotiable - {self.negotiable}"
		return result
