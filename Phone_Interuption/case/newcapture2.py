import cv2
from PIL import Image


class PicVerify(object):
	
	'''
	拍照和默认图片是否一致；
	参数pic：默认图片的路径；
	'''
	def __init__(self,pic):

		#获取传入图片的名称
		s = pic.split('\\')
		for i in s:
			if '.jpg' in i:
				newname = i
				#print(i)
			
		#原图路径
		self.inipath1 = '..\\Picture\\PicTemp\\'
		self.inipath = self.inipath1 + pic

		#self.image1 = Image.open(self.inipath)

		#截图路径
		self.path = '..\\Picture\\ScreenShot\\'

		self.picpath = self.path + 'verify_'+newname

		# self,image1
		# self.image2

		self.Psize = (256,256)
		self.Ppart_size=(64,64)



	def capture(self):
		'''
		获取截图
		'''
		cap = cv2.VideoCapture(0)
		ret, frame = cap.read()
		#path = os.getcwd()
		#newpath = '..\\Picture\\Screenshot\\'
		#picpath = self.path + '14.jpg'

		#cv2.imwrite(r'C:\Users\ZhangJiankai\Desktop\14.jpg', frame)
		cv2.imwrite(self.picpath, frame)
		#print ("sys.argv[0]=%s" % sys.argv[0])h #获取当前py的路径
		cap.release()



	def calculate(self,image1,image2):
		g = image1.histogram()
		s = image2.histogram()
		assert len(g) == len(s),"error"


		data = []

		for index in range(0,len(g)):
			if g[index] != s[index]:
				data.append(1 - float(abs(g[index] - s[index]))/max(g[index],s[index]) )
			else:
				data.append(1)

		return sum(data)/len(g)

		#for i,r in zip(g,s):
			
		# cal = sum(1 -(0 if i == r else float(abs(i - r))/max(i,r) ) for i,r in zip(g,s) )/len(g)
		
		# return cal

	def split_imgae(self,image,part_size):
		pw,ph = part_size
		w,h = image.size

		sub_image_list = []

		#assert w % pw == h % ph == 0,"error"

		for i in range(0,w,pw):
			for j in range(0,h,ph):
				sub_image = image.crop((i,j,i+pw,j+ph)).copy()
				sub_image_list.append(sub_image)

		return sub_image_list

	def classfiy_histogram_with_split(self):
		''' 'image1' and 'image2' is a Image Object.
		You can build it by 'Image.open(path)'.
		'Size' is parameter what the image will resize to it.It's 256 * 256 when it default.  
		'part_size' is size of piece what the image will be divided.It's 64*64 when it default.
		This function return the similarity rate betweene 'image1' and 'image2'
		'''

		size = self.Psize
		part_size=self.Ppart_size

		self.capture()

		self.image1 = Image.open(self.inipath)
		self.image2 = Image.open(self.picpath)
		#self.image2 = Image.open(r'D:\Code\Python\Phone_Interuption\Picture\Screenshot\12.jpg')


		newimage1 = self.image1.resize(size).convert("RGB")
		sub_image1 = self.split_imgae(self.image1,part_size)

		newimage2 = self.image2.resize(size).convert("RGB")
		sub_image2 = self.split_imgae(self.image2,part_size)

		sub_data = 0;
		for im1,im2 in zip(sub_image1,sub_image2):
			sub_data += self.calculate(im1, im2)

		x = size[0]/part_size[0]
		y = size[1]/part_size[1]

		pre = round((sub_data/(x*y) ),3 )
		print(pre)	
		

if __name__ == '__main__':

	p1 = PicVerify('11.jpg')
	p1.classfiy_histogram_with_split()



	



