import requests
from bs4 import BeautifulSoup
from io import StringIO
import xlwt as ExcelWrite


page = 1
dict1 = {}

max_page_number = 2
#根据steam网页的命名规则进入热销商店page
while page<max_page_number:
	url = "https://store.steampowered.com/search/?filter=globaltopsellers&page=" + str(page) + "&os=win"
	s = requests.session()
	res = s.get(url).text
	soup = BeautifulSoup(res, "html.parser")
	contents = soup.find(id="search_result_container").find_all('a')
	for content in contents:

		try:
			href2=content.get("href")
			#print(name,href,date,price,img_src)
			s2 = requests.session()
			res2 = s2.get(href2).text
			soup2 = BeautifulSoup(res2, "html.parser")

			developers = soup2.find("div",id = "developers_list").find("a").string.strip()
			developer_net = soup2.find("div",id = "developers_list").find("a").get('href')

			k = soup2.find_all("div",class_="dev_row")
			publisher_net = k[1].find("a").get('href')
			publisher = k[1].find("a").string.strip()

			try:
				if developers not in dict1:
					s3 = requests.session()
					res3 = s3.get(developer_net).text
					soup3 = BeautifulSoup(res3, "html.parser")
					Attention1 = soup3.find("div",class_="num_followers").string.strip()
					dict1[developers]=Attention1


			except:
				Attention1 = '0'
				if developers in dict1:
					fff=0
				else:
					dict1[developers]=Attention1

			try:
				if publisher not in dict1:
					s4 = requests.session()
					res4 = s4.get(publisher_net).text
					soup4 = BeautifulSoup(res4, "html.parser")
					Attention2 = soup4.find("div",class_="num_followers").string.strip()
					dict1[publisher] = Attention2

			except:
				Attention2 = '0'
				if publisher in dict1:
					pass
				else:
					dict1[publisher] = Attention2

		except Exception as e:
			pass

	page = page + 1
	print(page)


def make_excel(dict_data):

	header = [u'Name',u'Viewers']
	xls = ExcelWrite.Workbook(style_compression=2)
	sheet = xls.add_sheet('Sheet1')

	f = 0

	for each_header in header:
		sheet.write(0,f,each_header)
		f+=1

	a = list(dict_data.values())
	for i in range(len(a)):
		sheet.write(i+1,1,a[i])

	b = list(dict_data.keys())
	for n in range(len(b)):
		sheet.write(n+1,0,b[n])

	xls.save('company_form.xls')


make_excel(dict1)









