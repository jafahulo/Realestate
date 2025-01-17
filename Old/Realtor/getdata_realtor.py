# set up working directory
import  os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
#os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import zipcodes
from csvreader import csvread
filename = 'zipcodes.csv'
zipcodes_all = csvread(filename)

# select subset of zip codes
zipcodes = ['94025', '94026', '94027', '94028']
#zipcode = zipcodes[0]

# scrape MLS listings
from scrapeweb_realtor import webscrape
data_raw = webscrape(zipcodes)

# write .csv file with data
data_raw.to_csv('./data/data_menlo.csv')
