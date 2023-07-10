# Day 42
# The HTML Boilerplate 

# Nesting in an HTML Document 
# Make sure you put proper indentation
<!DOCTYPE html>
<html lang="en"> #language of the text content 
  <head>
     #important information about the website is placed. Not displayed for the user.
    <meta charset="UTF-8"> # ensures that characters are displayed correctly
    <title> This is the title of website </title>
  </head>

  <body>
     <h1>Hello World </h1>
  </body>
</html>


# ------------------ Build your own burger -------------------#
<!DOCTYPE html>
<bun topping="sesame">
  <tomato>
    <cheese></cheese>
  </tomato>
            
  <lettuce>
    <sauce>
      <meat></meat>
    </sauce>
  </lettuce>
</bun>

# ------------------------ How to create lists -------------------#
# Unordered list 
<ul>
     <li>Milk</li>
     <li>Eggs</li>
     <li>Flour</li>    
</ul>

# Ordered list
<ol>
     <li>Milk</li>
     <li>Eggs</li>
     <li>Flour</li>    
</ol>
            
#------------------------ Short Exercise -------------------------#
<h1>Angela's Cinnamon Roll Recipe</h1>

<h2>Ingredients</h2>

<h3>For the dough:</h3>
<ul>
    <li>¾ cup warm milk</li>
    <li>2 ¼ teaspoons yeast </li>
    <li>¼ cup granulated sugar</li>
    <li>1 egg plus 1 egg yolk</li>
    <li>¼ cup butter</li>
    <li>3 cups bread flour</li>
    
</ul>

<h3>For the filling:</h3>
<ul>
    <li>2/3 cup dark brown sugar </li>
    <li>1 ½ tablespoons ground cinnamon</li>
    <li>¼ cup butter</li>
</ul>

<h2>Instructions</h2>

<ol>
    <li>Mix the milk with the yeast, sugar, eggs.</li>
    <li>Melt the butter and add to the mixture.</li>
    <li>Add in the flour and mix until combined into a dough.</li>
    <li>Knead the dough for 10 minuites. </li>
    <li>Transfer the dough into a large bowl and cover with plastic wrap. Leave it somewhere to rise for 2 hours.</li>
    <li>After the dough has doubled in size, roll it out into a large rectangle. </li>
    <li>Melt the butter for the filling and mix in the sugar and cinnamon.</li>
    <li>Spread the filling onto the dough then roll the dough into a swiss roll. </li>
    <li>Cut the roll into 3cm sections and place flat into a baking tray.</li>
    <li>Pre-heat the oven to 350F or 180C, then bake the rolls for 20-25min until lightly brown.</li>     

</ol>

#-------------------- Anchor Elements -----------------------------------#
<a href ="http://www.google.com"> Content </a>
<tag attribute=value> Content </tag>
'''
All attributes go with the opening tag
There are some global attributes that can be applied to any tag.
'''
<h1>My top 5 Favourite Websites</h1>
<ol>
    <li><a href="https://www.producthunt.com/">Product Hunt</a></li>
    <li><a href="https://smashthewalls.com/">Smash the Walls</a></li>
    <li><a href="https://www.nytimes.com/games/wordle">Wordle</a></li>
    <li><a href="https://hackertyper.com/">Hacker typer</a></li>
    <li><a href="https://stellarium-web.org/">Stellarium</a></li>
</ol>

#-------------------- Image Elements -----------------------------------#
<img src="url"/>
# Does not have a closing tag
# Source of the image and location of the image 
'''
Attributes
alt (alternative text description
'''
<h1>I am a dog person </h1>
<img src="https://raw.githubusercontent.com/appbrewery/webdev/main/puppy.gif" alt="Dog digging through the sand"/>

#------------ Birthday Invite Project ------------------# 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>It's My Birthday!</title>
</head>
<body>
    <h1>It's My Birthday!</h1>
    <h2>On the 12th May</h2>
    <img src="https://raw.githubusercontent.com/appbrewery/webdev/main/birthday-cake3.4.jpeg
    "/>
    <h3>What to bring:</h3>

    <ul>
        <li>Baloons (I love balloons)</li>
        <li>Cake (I'm really good at eating)</li>
        <li>An appetite (There will be lots of food)</li>
    </ul>
    <h3> This is where you need to go:</h3>
    <a href="https://www.google.com/maps/@35.7040744,139.5577317,3a,75y,289.6h,87.01t,0.72r/data=!3m6!1e1!3m4!1sgT28ssf0BB2LxZ63JNcL1w!2e0!7i13312!8i6656">Google map link</a>

</body>
</html>














            
