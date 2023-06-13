# restaurant-finder
I've created a restaurant finder using the Google Places API and Rasa 

## Adding in the API Key 
You'll have to add in your own API Key for Google Places to make this work. You can use any other API as well, but then you'll have to change the URL accordingly as well

You can create your own API Key by heading over to the Google Places API site directly

## Using the restaurant finder
I've tested the API in Postman. Here's what I did:

1) Enter the greeting and say Hi or any other greeting for it to greet back
![image](https://github.com/AzureSky007/restaurant-finder/assets/112969052/fb3683c6-710e-47ba-a152-0ea632166be6)

2) Enter your favorite cuisine type inside the message next
![image](https://github.com/AzureSky007/restaurant-finder/assets/112969052/3da3ad42-04de-4006-9750-a575ce148d3d)

3) Next enter the amount of people who will be there
(I've not really used this in the API finding, so it won't matter much what number you put in)
(Also, it would be better if you put in numbers instead of text, model would have to be highly trained for text to be detected perfectly)
![image](https://github.com/AzureSky007/restaurant-finder/assets/112969052/037ea20b-4b5c-47a5-8298-a6eeb6f7894e)

4) Finally, enter the location you want. In a few minutes, you should have the list displayed in front of you 
![image](https://github.com/AzureSky007/restaurant-finder/assets/112969052/1534d67b-be04-4fe9-8d93-18bac95e8c7a)

I've tried to fit in the whole output above, but it does seem messy. Postman does not consider the "\n" as a new line, or it would've been more clear





