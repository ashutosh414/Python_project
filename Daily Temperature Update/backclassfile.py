from requests_html import HTMLSession
class TemperatureByLocation:
    def __init__(self,location):
        self.location=location
        self.detail=''
        self.temperature=0
        self.degree=''
        self.h1=''
        self.h1_data=0
        self.time1=''
    def __str__(self):
        return f'The {self.detail} Temperature is {self.temperature} {self.degree}'
    def TemperatureByLocation_fun(self):
        # self.__init__(location)
        s=HTMLSession()
        url=f"https://www.google.com/search?q=weather+{self.location}"
        r=s.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'})
        detail=r.html.find('div.s6JM6d span.BBwThe',first=True).text
        temperature=r.html.find('span#wob_tm',first=True).text
        degree=r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text
        time1=r.html.find('div#wob_dts',first=True).text
        self.detail=detail.split()[0].title()
        self.temperature=temperature
        self.degree=degree
        self.time1=time1
        return f'The {self.detail} Temperature is {self.temperature} {self.degree} at {self.time1}'
        # self.h1=detail=r.html.find('div.s6JM6d span.BBwThe',first=True).text
        # self.h1_data=

if __name__=='__main__':
    print('done')