# Semester Project
Quick Intro
Welcome to the semester project for Econ 8320 - Tools for Data Analysis! This project is designed to give you a chance to combine all of the material that we cover during the term, and to show that you can use these tools to collect and clean data, as well as to conduct some rudimentary analysis (other courses will focus much more on the analysis part).

You will create a StreamlitLinks to an external site. dashboard that is updated each time new labor statisticsLinks to an external site. are released by the US Bureau of Labor Statistics (BLS). Here is a link to the  In this project, you will

Create a GitHub repository to contain your code and data
Collect data with the BLS Public API (https://www.bls.gov/developers/home.htmLinks to an external site.). You can find various series on this pageLinks to an external site.. Your dashboard should include at least the total number of non-farm workers, as well as unemployment rates. Full credit will require you to select several other series of your choosing to include.
Your code should collect information EACH TIME THAT DATA IS RELEASED, so that you can add each new month of data to your dashboard as it becomes available
Your final data should contain at least one year of previous data, as well as code to collect new data, process all incoming data, and create a data dashboard.
Once you have processed the data, you will build an interactive dashboard using Streamlit, and launch a website from your GitHub using the free deployment process described on the Streamlit website (with the Community Cloud tool). Details can be found hereLinks to an external site..
Your tool should NOT re-collect the data each time it is loaded, but should instead run a collection script once per month when new data is released through GitHub ActionsLinks to an external site. that will collect and append the most recent month to your dataset, which will be hosted in your repository.
NOTE: You are expected to learn several new skills during this project (how to create a github action, how to use the BLS API, and how to create a Streamlit dashboard). As a data scientist, you will frequently be expected to use new tools to solve new problems. Leverage what you know from class, and create a real product that you can showcase on your website and during interviews!

Steps to Completion
Write a script to collect the data.
Clean and prepare the data for the dashboard.
Create a GitHub Action trigger to process new data each month as it is reported
This should update your data AND your dashboard as it completes!
Submit the following for your completed project:
A link to your GitHub repository
A link to your working dashboard
A link to your YouTube presentation (can be unlisted if you don't want the world to see, but you need to upload it and share the link with me)
Any presentation materials that you use
A 2-5 page writeup (single spaced) describing what you learned in the project, and what you would do differently if you did a similar project in the future. (Page limit not including tables or figures)
NOTE: You do NOT need to submit the complete original data sets, since I already have access to them in your GitHub repository

Presentation
We will present our work to each other. You should prepare a five minute presentation of your working dashboard, and upload that presentation to YouTube. It is okay to either make the video public, or to mark it unlisted (only people with the link can see unlisted videos). Don't make the video private or I won''t be able to see it even if you share a link. After showing your final product, focus on briefly describing what you learned, what you struggled with, and what you would do differently in the future based on your experience with the project. I will share the video and dashboard links with your classmates so that we can learn from one another.

Rubric
Category					Total Points
Code Submission	50 pts
Code is clear, organized, and well-commented	35 pts
Code is clear for the most part, but lacks organization or quality comments	20 pts
Code lacks organization and comments	0 pts
Code not submitted	50 pts
Replicability	25 pts
Code can be executed without modification on a different computer.	15 pts
Code can be executed with minor modifications on another computer	5 pts
Significant work required to run code on a different computer	0 pts
Excessive effort required to execute code on a different machine	25 pts
Project Write-up	75 pts
Project thoughtfully presented, with discussions of results, methods, and difficulties of the process	50 pts
Satisfactory discussion, with room for improvement	25 pts
Some discussion, but lacks detail	0 pts
Discussion not submitted	75 pts
Presentation	50 pts
Clear presentation of project and methods to solve problem	35 pts
Adequate presentation of project and methods	15 pts
Presentation is unclear or leaves major questions about solution	0 pts
No Marks	50 pts
Reported Series	50 pts
Full Marks
The finished product contains both the required series and two or more other series from the jobs report	25 pts
Half-credit
The finished product contains the required series.	
0 pts
No Marks

The finished product does not contain the required series.

50 pts
Total Points: 250
 
