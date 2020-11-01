# TLInternshipExercise

First approach:<br/>
 -I used the warcio archive iterator<br/>
 -Attempted to write a query to look at 2020 archives<br/>
    -selecting from 2020 indecies and using SQLite to include parameters about coronavirus and economics<br/>
 -Couldn't properly access 2020 archives (Warc, WAT, and WET) so moved on to next approach<br/>
 
 Second Approach:<br/>
 -Researched Common Crawl packages<br/>
    -Found https://github.com/michaelharms/comcrawl (comcrawl package)<br/>
 -Used IndexClient to go through 2020 archives<br/>
 -Used a list comprehension with conditions to filter URLS that included "covid" and another economics-related keyword<br/>
 -Used Pandas to put results in a CSV<br/>
 
 Complications and What I Woudld've Improved with More Time:<br/>
 -Couldn't get client.search() to work with searching multiple websites<br/>
    -Given more time I would've figured out a regex pattern to search over all website in the 2020 archives<br/>
 -Tried to use a for loop to search multiple websites<br/>
    -search wasn't cumulative<br/>
    -attempted to fix this by concatenating dataframes after each search, but ran into data type issues<br/>
 -If I had more time I'd also make the table columns cleaner<br/>
    
 End Result:<br/>
 -The CSV contains URLs with the proper criteria but doesn't have the results of all webpage searches<br/>
 -Looking back I would've stuck with the original script given by https://github.com/code402/warc-benchmark/blob/master/python/go.py<br/>
 -The package I ended up using gave me more complications<br/>
 
 Thank you for the opportunity to try this coding exercise. I learned a lot from this experience.<br/>
