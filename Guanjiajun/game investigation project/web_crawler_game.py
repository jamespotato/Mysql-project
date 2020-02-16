import requests
from bs4 import BeautifulSoup
from io import StringIO
import xlwt as ExcelWrite
#根据steam网页的命名规则
page = 1
data_list = []
dict1 = {}
max_page_number = 1



def make_excel(data):

    header = [u'Name',u'Price',u'Date',u'Image_Source',u'Developers',u'Publisher',u'comment',u'comment_data',u'Tag',u'Window',u'Apple',u'Limitation']
    xls = ExcelWrite.Workbook(style_compression=2)
    sheet = xls.add_sheet('Sheet1')

    i = 0

    for each_header in header:
        sheet.write(0,i,each_header)
        i += 1

    row = 1
    for dicts in data:

        a = list(dicts.values())
        for i in range(len(a)):
            sheet.write(row,i,a[i])

        row += 1

    xls.save('game_form.xls')




while page <= max_page_number:
    print(page)
    url = "https://store.steampowered.com/search/?filter=globaltopsellers&page=" + str(page) + "&os=win"
    s = requests.session()
    res = s.get(url).text
    soup = BeautifulSoup(res, "html.parser")
    contents = soup.find(id="search_result_container").find_all('a')

    for content in contents:
        try:    #Get the games' names, price and publishing date
            name = content.find(class_="title").string.strip()
            date = content.find("div",class_="col search_released responsive_secondrow").string.strip()
            try:
                price = content.find("div",class_="col search_price responsive_secondrow").string.strip()
            except:
                price = content.find("strike").string.strip()

            # The icon image of the game
            img_src = content.find("div",class_="col search_capsule").find('img').get("src")

            href = content.get("href")
            s2 = requests.session()
            #  *******Enter each game by reaching its href
            res2 = s2.get(href).text
            soup2 = BeautifulSoup(res2, "html.parser")


            try:       #Getting the comment of each game
                comment = soup2.find("span",class_="game_review_summary positive").string.strip()
                comment_data = soup2.find("span",class_="nonresponsive_hidden responsive_reviewdesc").string.strip()
            except:
                comment = "No comments yet"
                comment_data = "No comments_data yet"


            # Getting the developer and publisher information
            developers = soup2.find("div",id = "developers_list").find("a").string.strip()

            k = soup2.find_all("div",class_="dev_row")
            publisher = k[1].find("a").string.strip()

            # Tag contets
            tag_contents = soup2.find("div",class_="glance_tags popular_tags").find_all('a')
            tags = ''
            for ta in tag_contents:
                tags += ta.string.strip()
                tags += "\t"

            # Adult Limitation
            try:
                Limitation = soup2.find(id="game_area_content_descriptors").find("i").string.strip()
            except:
                Limitation = 'None'

            Win_req = ''
            apple_req = ''

            count = 1

            a = soup2.find_all("div",class_="game_area_sys_req_leftCol")

            #Computer requirement
            for requirement_sum in a:
                requirement_each = requirement_sum.find_all("li")
                if count == 1:
                    for specific_requirement in requirement_each:
                        Win_req = (Win_req + specific_requirement.get_text() + ' ')

                if count == 2:
                    for specific_requirement in requirement_each:
                        apple_req = (apple_req + specific_requirement.get_text() + ' ')

                count += 1


            dict1 = {'Name':name,'Price':price,'Date':date,'Image_Source':img_src,'Developers':developers,'Publisher':publisher,'comment':comment,'comment_data':comment_data,'Tag':tags,'Window':Win_req,"Apple":apple_req,'Limitation':Limitation}

            data_list.append(dict1)

        except Exception as e:
            print(e)

    page = page + 1


make_excel(data_list)













