#Clarifaing Gender Roles

###The Idea
I wanted to play around with the Clarifai API, but had no long-term project in mind. As an advocate for women in tech, I wanted to see if the gender disparity in STEM fields could be quantified from Bing, [the image search engine used by one in five people](http://money.cnn.com/2015/04/16/technology/bing-usage/).

###The Implementation
I coded a Python script that uses the Bing Cognitive Search API to find the first 150 hits from a given search term, and then save the content URL for each hit in a text file. I created another Python script that tags every uncorrupted image using the Clarifai Python API, and builds a dictionary of tags and frequencies. I use d3.js to [visualize the results as bubbles](http://bl.ocks.org/mbostock/4063269) such that tag frequency is equated to bubble area.

This code has been abstracted for use with any search term, so feel free to clone/star this repository to try it out!

###Quick Caveat
Machine learning and artificial intelligence technologies *cannot* define someone's gender identity. The results that follow give the Clarifai API's best guesses of who is seen each image, which is inherently biased by training data. For more on AI bias, check out [this article from "Model View Culture"](https://modelviewculture.com/pieces/the-hidden-dangers-of-ai-for-queer-and-trans-people).

###First Results: "Engineer"
In the first 150 Bing Image Search results for the term "engineer," the Clarifai API counts 116 images tagged with "man" versus 33 tagged with "woman." "Man" was also the most frequent tag. Yikes. 

![Who is an engineer?](https://raw.githubusercontent.com/alainakafkes/clarifaing-gender-roles/master/engineer/engineerviz.png)

Keep in mind that this is what any Internet user sees when they search Bing for "engineer" -- mostly men. There is an evident lack of diversity in many engineering fields, so I believe that search results should strive to be gender-balanced to show girls & young women that they can and should exist in these spaces.

###"Doctor"
"Man" (114 tags) still outnumber "woman" (73 tags), but to a much lesser extent. Unfortunately, even the tag "stethoscope" appears more than "woman." Other notable, frequent Clarifai tags include "isolated" and "fine-looking." 😉

![Who is a doctor?](https://raw.githubusercontent.com/alainakafkes/clarifaing-gender-roles/master/doctor/doctorviz.png)

###How To Contribute
Create a pull request! ```bingscraper.py``` can be run in any Python 2 interpreter, whereas ```accumulator.py``` needs to be run in a Python 3 interpreter after [creating your first Clarifai app](https://developer.clarifai.com/) and by following the guidelines found [here](https://github.com/Clarifai/clarifai-python).

**Comments? Questions? Suggestions for terms to explore? Feel free to share them with me.**
