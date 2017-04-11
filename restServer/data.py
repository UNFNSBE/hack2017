from pytrends.request import TrendReq
import time

#Google info
class DataGrabber:
    @classmethod
    def getState(self, state,topic,timeSpan):
        google_username = "unfospreysnsbe@gmail.com"
        google_password = "osprey123"
        print state
        pytrend = TrendReq(google_username, google_password, custom_useragent='My Pytrends Script')
        pytrend.build_payload(kw_list=[topic],geo=state,timeframe=timeSpan)
        return pytrend.interest_over_time()
    
    @classmethod
    def getByDate(self,topic, dateVal):
        google_username = "unfospreysnsbe@gmail.com"
        google_password = "osprey123"
	pytrend = TrendReq(google_username, google_password, custom_useragent='My Pytrends Script')
        pytrend.build_payload(kw_list=[topic],geo='US',timeframe=dateVal)
        dat = pytrend.interest_by_region(resolution='CITY')
        dat = dat.drop(['District of Columbia'])
        return dat
      
