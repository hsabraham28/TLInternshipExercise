# TLInternshipExercise

First approach:
 -I used the warcio archive iterator
 -Attempted to write a query to look at 2020 archives
    -selecting from 2020 indecies and using SQLite to include parameters about coronavirus and economics
 -Couldn't properly access 2020 archives (Warc, WAT, and WET) so moved on to next approach
 
 Second Approach:
 -Researched Common Crawl packages
    -Found https://github.com/michaelharms/comcrawl (comcrawl package)
 -Used IndexClient to go through 2020 archives
 -Used a list comprehension with conditions to filter URLS that included "covid" and another economics-related keyword
 -Used Pandas to put results in a CSV
 
 Complications and What I Woudld've Improved with More Time:
 -Couldn't get client.search() to work with searching multiple websites
    -Given more time I would've figured out a regex pattern to search over all website in the 2020 archives
 -Tried to use a for loop to search multiple websites
    -search wasn't cumulative
    -attempted to fix this by concatenating dataframes after each search, but ran into data type issues
 -If I had more time I'd also make the table columns cleaner
    
 End Result:
 -The CSV contains URLs with the proper criteria but doesn't have the results of all webpage searches
 -Looking back I would've stuck with the original script given by https://github.com/code402/warc-benchmark/blob/master/python/go.py
 -The package I ended up using gave me more complications
 
 Thank you for the opportunity to try this coding exercise. I learned a lot from this experience.
