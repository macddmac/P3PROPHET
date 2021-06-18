# P3 PROPHETS
# ![banner](https://user-images.githubusercontent.com/72889343/112936650-0e794c00-90db-11eb-8ca9-f9dc3afd2ebf.JPG)
This is the repository for team "PROPHETS" in Mr. Mortensens Period 3 Data Structures class.

# How It's Made
## Theme Section (5pt)
- Our theme is about Animals! Explore our website and you will find countless ways to learn and have fun with animals :D
![image](https://user-images.githubusercontent.com/72889343/122511985-04216c80-cfbd-11eb-896e-85a28121c202.png)
![image](https://user-images.githubusercontent.com/72889343/122512135-43e85400-cfbd-11eb-92cd-a65513b41354.png)
![image](https://user-images.githubusercontent.com/72889343/122512382-9de91980-cfbd-11eb-92a4-f5ce82b380e6.png)

## Individual Section (3pt)
- As for our individual work, we have a section in the navbar called 'Minilabs' that you can click to locate each contributor's work from the trimester!
![image](https://user-images.githubusercontent.com/72889343/122512542-da1c7a00-cfbd-11eb-90a6-92df6e69203e.png)
![image](https://user-images.githubusercontent.com/72889343/122512578-e9032c80-cfbd-11eb-8970-affd33e4db53.png)
```html
{% extends "base.html" %}
<html lang="en">
{% block content %}
<!--<script>
    function success() {
        if(document.getElementById("textsend").value==="") {
            document.getElementById('button').disabled = true;
        } else {
            document.getElementById('button').disabled = false;
        }
    }
</script>
-->
<div style="white">
<div class="container">

    <div class="center-block">
        <h1 class="col-12" style="text-align:center; color:lightgray;"><strong>BubbleSort</strong></h1>

        <div class="jumbotron text-center row" style="background-color:slateblue;">
            <div>
                <h3>Input</h3>
                <form id="stringForm" action="/sambubblesort" method="post" style="width:500px">
                    <textarea name="string" class="input" id="string" type="integer" style="height:71px; overflow:hidden; resize:none" onkeyup="success()" placeholder="Enter as many numbers as you want"></textarea>

                    <button type="submit" id="button" style="background-color:peachpuff;">Submit</button>
                </form>
            </div>
            <div class="col-md-6">
                <table class="mx-auto">
                    <tr>

                    </tr>
                    <tr>

                    </tr>
                    <tr>
                        <th class="row" style="color:tomato">Sorted List:</th>
                    </tr>
                    <tr>
                        <td>{{sorted_list}}</td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
</div>
</div>
<script>
  var submitButton = document.getElementById("button");

  submitButton.addEventListener("click", function(){
    console.log('clicked')
  }, false);
</script>
{% endblock %}
</html>
```

## API Section (3pt)
- This is our Cat API! It is a fun way to learn more about facts, just click on the button and a random fact about cats will pop up to sate your cat curiosities :)
![image](https://user-images.githubusercontent.com/72889343/122512725-2667ba00-cfbe-11eb-93bc-64429cdb8713.png)
```python
from flask import Flask, redirect, url_for, render_template, request, session
import requests as r
app = Flask(__name__)

@app.route("/random_cat_fact", methods=["GET"])
def random_cat_fact():
    x = r.get("https://catfact.ninja/fact?max_length=140")
    data = x.json()
    fact = data.get("fact")

    return fact

if __name__ == "__main__":
    app.run(debug=True, port=3000)
```

## Deployment Section (3pt)
- How It's Made section (+2pt How Its Made, +1pt Visuals)
    - This is our 'How it's Made'
- Commercial (+2pt)
    - [LINK TO VIDEO]()
- Failed to Deploy on Mr. M's Machine(-1pt)

# Links
Project Plan: https://docs.google.com/document/d/1KWPlPDd_6blTJ15MXSY9-g9YZ7K22wgo52YYNsyNvW8/edit

Project Board: https://github.com/macddmac/P3PROPHET/projects/1

Runtime Link: http://animalsoftheworld.cf/

# Umbrella Ticket with Individual Tasks for EOY
- [Umbrella Ticket](https://github.com/macddmac/P3PROPHET/issues/17)
- In this Umbrella Ticket you will find each of the contributors' goals for the final project 
- Currently we have our checkpoints for 6/1 completed and linked as well as our general plans for the next week

# Contributors(+ individual ideas)
- Rohan - Look to set up graphing system to track trends and represent data
- Sam - RPI owner and works with the back end of the code to create routes 
- Shekar - Works with the front end to make the site more aesthetically pleasing with images and such
- Jason - Our other back end coder who created the blueprint and helps make our website more efficient 
- Rivan - Our alternate front end coder who is focusing on analyzing data for endangered species 

# What is our project?
Our project focues on endagered animal species and shows trends in the statistics related to them! We also give information through fun activities for kids and adults. People of all ages can navigate and learn about all kinds of animals and hopefully gain insight into how precious they are to our world. 

# What will the website feature?
- Home page with navigation options to our key wesbite highlights
- Cat API that gives random facts about cats
- Login system used for new/old users to log in and access our page
- Cool looking tiger animations
- About us page that gives credit to everyone that helped build the page
- Data storage page that gives information about animals not specially featured
- Minilabs where collaborators can show cool codes that have built
---------------------------
