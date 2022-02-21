class ToSell:
	__slots__ = ['title', 'category', 'price', 'negotiable', 'publishing_date', 'desc', 'photos', 'size']

	def __init__(self, title, price, category='Literatura', negotiable='', publishing_date='', desc='', photos='', size='A'):
		self.title = title
		self.price = price
		self.category = category
		self.negotiable = negotiable
		self.publishing_date = publishing_date
		self.desc = desc
		self.photos = photos
		self.size = size

	def __repr__(self):
		result = f"\n\nTitle - {self.title} \nPrice - {self.price} \nCategory - {self.category} \nPublishing date - {self.publishing_date} \nDesc - {self.desc} \nSize - {self.size} \nNegotiable - {self.negotiable}"
		return result
