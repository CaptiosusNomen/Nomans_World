#Nomans' World

Hello and welcome to my attempt at making an RPG game engine on Discord using Discord.py

The idea so far is to create a map layout for a location in one JSON file then have it populated by "NPCs" that will
then have a dialogue tree for players to go though from another JSON file. 

For example:
```json
{"TestTown":{
  "town_center": {
    "Description":"The Center of town",
    "Topic": "",
    "Image":"TownCenter",
    "NPC":[
      "Wizard"
    ]}}}
```
and 
```json
{"Wizard":{
  "Info":{
    "Name": "TestLich",
    "Description": "A little Description box to help keep track of things"},
  "Start": {
    "Template": "800x600FT",
    "BackGround": "",
    "Face": "",
    "Text": "You see living bones wrapped in glorious cloth and jewels. Getting closer you know there is power coming off of this thing as you feel all the hair on your body being tugged in whatever way the energy is flowing.",
    "Border": "",
    "TextBorder": "",
    "FaceBorder": "",
    "Choices": {
      "Next": {
        "Reward": "",
        "Requirement": "",
        "Price": "",
        "Destination": "next",
        "Color": "green"}}},
  "next": {
    "Template": "800x200R",
    "BackGround": "",
    "Face": "Badguy",
    "Text": "Hey there buddy!",
    "Border": "",
    "TextBorder": "GreyTextBackground600X200",
    "FaceBorder": "",
    "Choices":{
      "End Conversation": {
      "Reward": "",
        "Requirement": "",
        "Price": "",
        "Destination": "",
        "Color": "green"}}}}}
```
Combine to create~

![](https://github.com/CaptiosusNomen/Nomans_World/blob/master/Cogs/Files/Images/ForShow/Channels.png?raw=true)
![](https://github.com/CaptiosusNomen/Nomans_World/blob/master/Cogs/Files/Images/ForShow/TownCenterPost.png?raw=true)

Clicking on the button leads to

![](https://github.com/CaptiosusNomen/Nomans_World/blob/master/Cogs/Files/Images/ForShow/Talk1.png?raw=true)
![](https://github.com/CaptiosusNomen/Nomans_World/blob/master/Cogs/Files/Images/ForShow/Talk2.png?raw=true)
