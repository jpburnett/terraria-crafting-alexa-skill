[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://raw.githubusercontent.com/jpburnett/byu-facts-alexa-skill/master/LICENSE)
[![Python 3.8.5](https://img.shields.io/badge/python-3.8.5-blue.svg)](https://www.python.org/downloads/release/python-382/)

# terraria-tool-alexa-skill
The Terraria tool Alexa skill is aimed to help find recipes for crafting things easier when playing terraria. There are a variety of different item combinations used to make cooler items. 


# What does it do?
Alexa skill that gives instructions on how to craft items in the video game terraria.
The list of items is quite extensive, eventually I'll try to include them all...maybe...

## Intents
 
### Main Intent 
Get the recipe for the item that a user requested
- To use Say, "Alexa, open Terraria Tool" or
- "Alexa ask Terraria tool how to craft <Item Name Here>" 

### Random Item Intent
Gets a random recipe from the dictionary of items
- To use Say, "Alexa, open Terraria Tool" or
- "Alexa ask Terraria tool for a random item"

### [Link to the Skill on Amazon](https://www.amazon.com/Parker-Burnett-Terraria-Tool/dp/B075831DPC/ref=sr_1_1?dchild=1&keywords=Terraria+tool&qid=1590714662&s=digital-skills&sr=1-1)



# Deploying Code to AWS 

When deploying code for the Alexa Skill, make sure to do the following 4 steps:

1. ```pip install -r py/requirements.txt -t skill_env```

2. ```cp -r py/* skill_env/```

3. Zip the contents of the skill_env folder. Zip the contents of the folder and NOT the folder itself. If you zip the folder it will not work

4. Upload the .ZIP file to the AWS Lambda console
