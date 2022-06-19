# Therapy and You

For you and us

## 💡 Inspiration

According to WHO, depression is a common illness worldwide, with an estimated 3.8% of the population affected, including 5.0% among adults and 5.7% among adults older than 60 years. Approximately 280 million people in the world have depression. Depression is different from usual mood fluctuations and short-lived emotional responses to challenges in everyday life. Especially when recurrent and with moderate or severe intensity, depression may become a serious health condition. We focused on developing a feasible solution **Therapy and You** to tackle the Mental health crisis on our scale throughout the brainstorming process. On our website you can check your sentiment using NLP and get suggestive exercise and music . we will also provide you with mental health score with a graphical representation.

## 💻 What it does

- User can write a daily journal
- Using NLP to check the sentiment
- Suggestions of exercise and music according to users' sentiments (Happy, sad, depressed)
- If a user is happy for continuous 30 days, they will get rewarded
- A mental health score to check your health
- A graphical representation of your mood(Happy, Sad, Depressed)

## ⚙️How we built it

- ML: Python, MATLAB
- Frontend: HTML, CSS, JS
- Backend: Django
- Authentication: Auth0

## 🤖 Best Use of MATLAB

We used MATLAB to build the sentiment analysis model. The model was trained on a dataset of emotions and their corresponding sentiment. The model was then used to predict the sentiment of a given sentence user input for the diary. MATLAB helped us in the following ways:

- We used the MATLAB function `textscan` to parse the user input into a matrix.
- We used the MATLAB function `strsplit` to split the user input into individual words.
- We used the MATLAB function `strcat` to concatenate the words into a single string.

## 🔑 Best Use of Auth0

We used Auth0 authentication system for LogIn of users because we wanted to make an application very very secure. Auth0 provides the most extensive functionality to ensure the user authentication and authorization, with detailed analytics, a variety of available providers, and a diverse set of user-friendly tools the developer will really like. During the app development, we used social services to log-in like using Google which supported by Auth0.

## 🧠 Challenges we ran into

- Using MATLAB to build the model was a challenge.
- Completing the project under given time frame.

## 🏅 Accomplishments that we're proud of

- We built the sentiment analysis model using MATLAB.
- Implementing the sentiment analysis model to the frontend.

## 📖 What we learned

- Using MATLAB to build the model.
- Implementation of Auyth0 and MATLAB.
- Collaboration with other developers.

## 🚀 What's next for Therapy and You
- We aim to develop this platform and collaborate with doctors and hospitals to make it a genuine free product that benefits everyone and introduces new features and other enhancements.

- Improving the sentiment analysis model.
- Deploying the web app.
- Building a mobile app
