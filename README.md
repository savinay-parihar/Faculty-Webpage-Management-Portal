
**Topic : Intelligent Web Development**<br>
Specification:<br>
1. Framework : Django framework<br>
2. It is an website model for college faculty.<br>
3. They register themselves first. After that they can fill theirs<br>
information after filling the information their own page will be rady.<br>
4. They can fill about themselves, teaching/courses, Publications, Work<br>
and experince, Conatcts, Reseach areas ,etc.<br>
5. They can also update their informations.<br>
6. Some urls by entering those urls you can see demo<br>

**Note** :- this project is for django version less than 2;<br>
if you are usinh django version greater than 2 then replace
this line <br>
 user = models.ForeignKey(User)<br>
 by below line in each models<br>
 user = models.ForeignKey(User,on_delete=models.CASCADE)<br><br>
 
 
7. Go to dirctory IWDproject.<br>
the run the server by typig the command in terminal<br><br>



python manage.py runserver<br><br>

8. After running server just click below link one by one<br>
you and fill the informations and see the demo<br><br>

**● http://127.0.0.1:8000/home/register/**<br>

**9**above link redirect you to profile page then to<br> 
fill the information about you and your research projects,qualifications<br>
teaching courses ,your works etc using the appropriate below links<br><br>

**10**fill your information about you using the below url after getting logged in<br>
**http://127.0.0.1:8000/home/portal/home/**<br>

**11**its will redirect you to profile page where you <br>
will get your own input information with beautifull layout.<br>

**12**fill the teaching details in teaching form by using below link<br> 
**http://127.0.0.1:8000/home/portal/teaching/**<br>
it will redirect you to profile page then click on
teaching button then yu will get your teaching page with input information 


**13**fill informatin of your research projects and other details related to it using below link<br>
**http://127.0.0.1:8000/home/portal/project/**<br>
it will redirect you to profile page then click on the button named "Research"
you will get your research project page with project information


**14**similarly you can put your publication information using the below link<br>
**http://127.0.0.1:8000/home/portal/publication/**<br>

it will redirect you to profile page then click on publications you will get publication page<br>

**15**other similar urls<br>
**http://127.0.0.1:8000/home/portal/experience/**<br>
**http://127.0.0.1:8000/home/portal/qualification/**<br>


**● http://127.0.0.1:8000/home/login/<br>
● http://127.0.0.1:8000/home/profile/<br>
● http://127.0.0.1:8000/home/portal/home/<br>**
9. As you login it direct you those pages where you can fill your<br>
information. As press submit button you will get your ownpage.<br>
Mentor: Dr Santosh Vishwas (indian institute of technology CSE dept)<br>


  
