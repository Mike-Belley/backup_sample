import shutil, os
import datetime
print "starting"
os.chdir('C:\\')
now = datetime.datetime.now()

#puts date into variables
day = now.day
month = now.month
year = now.year

#puts date into a single string
All= str(day)+'_'+str(month)+'_'+str(year)
print All

#Original and destination paths
orig = 'C:\Users\Mike Belley\Desktop\spam.txt'
dest = 'C:\Users\Mike Belley\Desktop\delicious\spam.txt'

#path with date in it
rename = 'C:\\Users\\Mike Belley\\Desktop\\delicious\\spam ' + All + '.txt'
print rename

#copies file to destination
shutil.copy(orig, dest)

#renames file
os.rename(dest,rename)
print "ending"
