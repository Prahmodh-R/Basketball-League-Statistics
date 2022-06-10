import matplotlib.pyplot as pl
#import chart
import random
import mysql.connector as sb
con=sb.connect (host='localhost' ,user='root', passwd='Assami1',database='sun')
cur=con.cursor()
def add():
    c=input("Enter the  Team to which you want to add players: ")
    ch='y'
    while ch=='y':
        jer_no=int(input("Enter the jersey number : "))
        nm=input("Enter player name : ")
        matches=int(input("Enter the no. of matches : "))
        points=int(input("Enter the total no. of points scored by your player : "))
        assists=int(input("Enter the no. of assists : "))
        fouls=int(input("Enter the no. of fouls committed : "))
        cur.execute('insert into {0} values({1},"{2}",{3},{4},{5},{6})'.format(c,jer_no,nm,matches,points,assists,fouls))
        cur.execute('Insert into players values({0},"{1}","{2}",{3},{4},{5},{6})'.format(jer_no,c,nm,matches,points,assists,fouls))
        print()
        print('Player added successfully')
        print()
        ch=input("Do you want to add more records ?")
        con.commit()     
    print()        
def updating():
    c=input("Enter the  Team whose records you want to update : ")
    jer_no=int(input("Enter the jersey number of the player : "))
    cur.execute('select * from {} where jersey_no={}'.format(c,jer_no))
    sr=cur.fetchone()
    if sr!=None:
         print('The Player is ',sr[1])
         us=input("Do u want to change player's records? ")
         print()
         if us=='y':
               matches=int(input("Enter the no. of matches : "))
               points=int(input("Enter the total no. of points scored by your player : "))
               assists=int(input("Enter the no. of assists : "))
               fouls=int(input("Enter the no. of fouls committed : "))
               cur.execute('update {} set matches={},tot_points={},assists={},fouls={} where jersey_no={}'.format(c,matches,points,assists,fouls,jer_no))
               cur.execute('Update players set matches={},tot_points={},assists={},fouls={} where jersey_no={}'.format(matches,points,assists,fouls,jer_no)) 
               con.commit()
               print("Player details updated successfully !!!")
    else:
        print("ERROR ! No such player exists")
    print()
#updating()
def deletion():
    c=input("Enter the  Team from which you want to remove a player : ")
    jer_no=int(input("Enter the jersey number of the player : "))
    cur.execute('select * from {} where jersey_no={}'.format(c,jer_no))
    er=cur.fetchone()
    if er!=None:
        eu=input("Do u want to remove the player ? ")
        if eu=='y':
              cur.execute('delete from {} where jersey_no={}'.format(c,jer_no))
              cur.execute('delete from players where jersey_no={}'.format(jer_no))
              con.commit()
              print("Player has been removed successfully from ",c)
    else:
            print("ERROR !!! No such player exists.")
    print()
def display():
    c=input("Enter the  Team : ")
    print()
    cur.execute('select * from {}'.format(c))
    my=cur.fetchall()
    print('%10s'%'---------','%10s'%'----','%10s'%'-------','%10s'%'------------','%10s'%'-------','%10s'%'-----')
    print('%10s'%'Jersey-no','%10s'%'Name','%10s'%'Matches','%10s'%'Total points','%10s'%'Assists','%10s'%'Fouls')
    print('%10s'%'---------','%10s'%'----','%10s'%'-------','%10s'%'------------','%10s'%'-------','%10s'%'-----')
    print()
    for row in my:
          print('%10s'%row[0],'%10s'%row[1],'%10s'%row[2],'%10s'%row[3],'%10s'%row[4],'%10s'%row[5]) 
    print()
def topsc():
    c=input("Enter the  Team to display the topscorer : ")
    cur.execute('select name,tot_points from {} order by tot_points desc,assists desc'.format(c))
    s=cur.fetchone()
    print()
    print('Name : ',s[0],'Total points : ',s[1])
    print()
def pttable():
       cur.execute('select players.team,standings.matches,points,won,lost,per,recentform,sum(tot_points) from standings,players where team_name=players.team group by players.team order by standings.points desc,sum(tot_points) desc')
       s=cur.fetchall()
       print()
       print('%13s'%'----','%13s'%'-------','%13s'%'------','%13s'%'----','%13s'%'---','%13s'%'-----------','%13s'%'-----------')
       print('%13s'%'Team','%13s'%'Matches','%13s'%'Points','%13s'%'Lost','%13s'%'Won','%13s'%'Win Percent','%13s'%'Recent Form')
       print('%13s'%'----','%13s'%'-------','%13s'%'------','%13s'%'----','%13s'%'---','%13s'%'-----------','%13s'%'-----------')
       for i in s:
        print('%13s'%i[0],'%13s'%i[1],'%13s'%i[2],'%13s'%i[4],'%13s'%i[3],'%13s'%i[5],'%13s'%i[6]) 
       print()
       chart.barch()     
def indaccess(nm):
    cur.execute('select * from players where name="{}"'.format(nm))
    s=cur.fetchone()
    print()
    print('Jersey no : ',s[0])
    print('Team Name : ',s[1])
    print('Player Name: ',s[2])
    print('Matches Played:',s[3])
    print('Total points:',s[4])
    print('Assists: ',s[5])
    print('Fouls : ',s[6]) 
    print()     
def ptanalysis():
    ch=input("Enter the team : ")
    print()
    nm=input("Enter the name : ")
    cur.execute("select name,tot_points from {} where name='{}'".format(ch,nm))
    sc=cur.fetchone()
    s=sc[1]
    print('The Total points scored by ',sc[0],' this season is ',s)
    print()
    thrp=int(input("Enter the number of three pointers : "))
    twop=int(input("Enter the number of two pointers : "))
    sc3=thrp*3
    sc2=twop*2
    if sc3+sc2==s:
        pt3=round((sc3/s)*100,2)
        pt2=round((sc2/s)*100,2)
        print("The percentage of points scored by three pointers is : ",pt3,"%")
        print("The percentage of points scored by two pointers is : ",pt2,"%")
        if sc3>sc2:
           print(sc[0]," is a better long range shooter")
        else:
           print("We would prefer you to have",sc[0],"closer to the targets.")
           print()
    else:
        print('Entered data is incorrect, Please try again')
        print()
    print('Free throw percentage : ')
    print()        
    suc=int(input("Enter the no. of successful free throws : "))
    attempts=int(input("Enter the total no. of free throw attempts : "))
    free_per=round((suc/attempts)*100,2)
    print("The free point percentage of your player is: ",free_per,"%") 
    print()
def avergpl(na):
    ch=input('Average points (pts) or Average assists(ast)? ')
    print()
    if ch=='ast':
        cur.execute('select name,team,assists/matches as avg_assists from players where name="{}"'.format(na))
        s=cur.fetchone()
        print('Player ',s[0],'of ',s[1],' has an average of ',round(s[2],2),' assists per match')
    elif ch=='pts':    
        cur.execute('select name,team,tot_points/matches as average from players where name="{}"'.format(na))
        s=cur.fetchone()
        print('Player ',s[0],' of',s[1],' has an average of ',round(s[2],2),' points per match')
    print()
def avergtm(nm):
    ch=input('Average points (pts) or Average assists(ast)? ')
    print()
    if ch=='ast':
        cur.execute('select team,sum(assists)/standings.matches from players,standings where team="{}"'.format(nm))
        s=cur.fetchone()
        print('Team :',nm)
        print('Average Assists: ',s[1])
    elif ch=='pts':
        cur.execute('select team,sum(tot_points)/standings.matches from players,standings where team="{}"'.format(nm)) 
        s=cur.fetchone()
        print('Team :',nm)
        print('Average Points: ',s[1])
    print()
def viewcoaches():
    tn=input("Enter the team : ")
    print()
    a='coaches_'+tn
    cur.execute('select * from {}'.format(a))
    s=cur.fetchall()
    print('%15s'%'---------','%15s'%'--------','%15s'%'----------------','%15s'%'-------','%15s'%'-----------')
    print('%15s'%'Coachname','%15s'%'Position','%15s'%'Years of service','%15s'%'Matches','%15s'%'Matches Won')
    print('%15s'%'---------','%15s'%'--------','%15s'%'----------------','%15s'%'-------','%15s'%'-----------')
    for i in s:
        print('%15s'%i[0],'%15s'%i[1],'%15s'%i[2],'%15s'%i[3],'%15s'%i[4])
    print()
def tptass():
    cur.execute('select team,sum(tot_points) from players group by team order by sum(tot_points) desc,sum(assists) desc') 
    s=cur.fetchall()
    print('Max Points')
    print(s[0][0],'with ',s[0][1],' points')
    print()
    cur.execute('select team,sum(assists) from players group by team order by sum(assists) desc,sum(tot_points) desc')
    s1=cur.fetchall()
    print('Max assists')
    print(s1[0][0],'with ',s1[0][1],' assists') 
    print()
def cperform():
    t=input('Enter the team: ')
    a='coaches_'+t
    cur.execute('select * from {} where position="Head coach"'.format(a))
    s=cur.fetchone()
    print('The name of the coach is : ',s[0])
    d=round((s[4]/s[3])*100,2)
    print()
    print("Winning Percentage: ",d,'%')
    if d<80:
        print("Your coach's performance is critical")
        print('Please choose one of the options given below')
        ch=int(input('1. Replace my coach,   2. Continue with the same coach '))
        if ch==1:
           cur.execute('delete from {} where position="head coach"'.format(a))
           con.commit()
           print('Coach has been removed')
           print()
           nm=input('Enter the name of the new coach - ')
           cur.execute('insert into {} values("{}","Head coach","2020-",0,0)'.format(a,nm))
           con.commit()
           print('Coach- ',nm,' has been appointed as your new coach')
        else:
           print('You can continue with your same coach')  
    print()   
def upptable():
    t1=input("Enter the winning team: ")
    print()
    t2=input("Enter the losing team: ")
    cur.execute('update standings set points=points+2,matches=matches+1,won=won+1 where Team_name="{}"'.format(t1))
    cur.execute('update standings set matches=matches+1,lost=lost+1 where Team_name="{}"'.format(t2))
    con.commit()    
    a='fixtures_'+t1
    b='fixtures_'+t2
    cur.execute('delete from {} where opposition="{}"'.format(a,t2))
    cur.execute('delete from {} where opposition="{}"'.format(b,t1))
    con.commit()
    cur.execute('select recentform from standings where Team_name="{}"'.format(t1))
    m=cur.fetchone() 
    s='W'+m[0] 
    if len(s)>=6: 
      k=s[:5] 
      cur.execute('update standings set recentform="{}" where Team_name="{}"'.format(k,t1))
      con.commit() 
    else: 
      cur.execute('update standings set recentform="{}" where Team_name="{}"'.format(s,t1)) 
      con.commit() 
    cur.execute('select recentform from standings where Team_name="{}"'.format(t2)) 
    t=cur.fetchone() 
    u='L'+t[0] 
    if len(u)>=6: 
      p=u[ :5] 
      cur.execute('update standings set recentform="{}" where Team_name="{}"'.format(p,t2))
      con.commit() 
    else: 
      cur.execute('update standings set recentform="{}" where Team_name="{}"'.format(u,t2)) 
      con.commit()
    print("Standings has been updated successfully!!!") 
    print()
def rec(a):
    cur.execute('Select Team_name,recentform from standings where team_name="{}"'.format(a))
    print()
    s=cur.fetchone()
    print('Team :',s[0],'with recent form',s[1])   
    print()        
def fixtures():
     tn=input("Enter the team you want to see : ")
     tno=input("Enter the opponent team  : ") 
     print()
     a='fixtures_'+tn
     b=tn+' vs '+tno
     cur.execute("select matchdate,time from {} where teams='{}' ".format(a,b)) 
     m=cur.fetchall()
     print('Match between ',tn,' and ',tno)
     print("Date: ",m[0][0]) 
     print("Time: ",m[0][1])
     print()
def squad():
    t1=input("Enter team1: ")
    print()
    t2=input("Enter team2: ")
    l1=[]
    l2=[]
    cur.execute('select name,tot_points from {} order by tot_points desc,assists desc'.format(t1))
    s1=cur.fetchall()
    cur.execute('select name,tot_points from {} order by tot_points desc,assists desc'.format(t2))
    s2=cur.fetchall()
    c1=0
    for i in s1:
        if c1<=6:
           l1.append(i)
        c1+=1
    c2=0    
    for i in s2:
        if c2<=6:
            l2.append(i)
        c2+=1    
    print('%10s'%'Team : ',t1)
    print()
    print('%10s'%'-------','%16s'%'------') 
    print('%10s'%'PLAYERS','%16s'%'POINTS')
    print('%10s'%'-------','%16s'%'------')        
    for i in l1:
         print('%10s'%i[0],'%16s'%i[1])
    print()     
    print('%10s'%'Team : ',t2)
    print()
    print('%10s'%'-------','%16s'%'------')
    print('%10s'%'PLAYERS','%16s'%'POINTS')
    print('%10s'%'-------','%16s'%'------')     
    for i in l2:
         print('%10s'%i[0],'%16s'%i[1])
    print()     
def maxscrass():
    ch=int(input('Make your choice : 1.Top assists  2. Top scorer '))
    print()
    if ch==1:
        l=[]
        cur.execute('select jersey_no,name,team,assists from players order by assists desc,tot_points desc')
        s=cur.fetchall()
        for i in s:
           l.append(i[3])
        a=max(l)
        print('The Player with leading assists of PREMIER BASKETBALL LEAGUE')
        for j in s:
          if j[3]==a:
            print('Jersey no: ',j[0])
            print('Name :  ',j[1])
            print('Team : ',j[2])
            print('Assists : ',j[3])    
    elif ch==2:
        l=[]
        cur.execute('select jersey_no,name,team,tot_points from players order by tot_points desc,assists desc')
        s=cur.fetchall()
        for i in s:
          l.append(i[3])
        a=max(l)
        print('The leading scorer of PREMIER BASKETBALL LEAGUE')
        for j in s:
           if j[3]==a:
              print('Jersey no: ',j[0])
              print('Name : ',j[1])
              print('Team : ',j[2])
              print('Points : ',j[3])
    print()
def awards():
    cur.execute('select team,sum(fouls) from players group by team order by sum(fouls) asc,sum(tot_points) desc')
    s=cur.fetchall()
    a=s[0][1]
    st=s[0][0]
    for i in s:
        if i[1]<a:
            a=i[1]
            st=i[0]         
    print('THE FAIR PLAY AWARD FOR THE SEASON 2020-2021 GOES TO:')        
    print('TEAM ',st,' with minimum fouls of ',a)
    cur.execute('select name,team,matches,won from hcoach order by won desc,adaptability desc')
    s=cur.fetchall()
    l=[]
    print('AND')
    print('THE BEST COACH FOR THE SEASON 2020-2021 GOES TO')
    for i in s:
        l.append(round((i[3]/i[2])*100,2))
    a=max(l)
    for j in s:
        if round((j[3]/j[2])*100,2)==a:
            print('Coach ',j[0],'of ',j[1],' with an excellent win percentage of : ',a,'%')
    print() 
#awards()       
def matchtickets():
  print(" Cost per ticket ---> ₹ 500 ")
  print()
  m=input(" Enter the match whose tickets you want to buy : ")
  cur.execute('select tickets from tickets8 where matchname="{}"'.format(m))
  k=cur.fetchone()
  p=k[0]
  print()
  print("Number of available tickets: ",p)
  print()
  if k[0]==0:
     print(" Sorry !! We do not have any tickets available for the match "+m)
  else:
    n=int(input("Enter the number of tickets you want to buy : "))
    print()
    if n>k[0]:
        print("Sorry !! We have only ",k[0]," tickets available for the game")
    else:
     print(" Your cost is ₹",n*500,"/- only")
     print("Transaction successful !! ")
     print("You have successfully purchased ",n," tickets")
     s=k[0]-n
     cur.execute('update tickets8 set tickets={} where matchname="{}"'.format(s,m))
     con.commit()
  print()            
def title():
    ch=input('Has the season ended? ')
    if ch.lower()=='yes':
        cur.execute('select players.team,standings.matches,points,won,per,sum(tot_points) from standings,players where team_name=players.team group by players.team order by standings.points desc,sum(tot_points) desc')
        s=cur.fetchall()
        print()
        print('THE WINNER OF PREMIER BASKETBALL LEAGUE 2020-2021 IS - ',s[0][0],' with ',s[0][2],' points')
        print()
        print('THE RUNNER UPS OF PREMIER BASKETBALL LEAGUE 2020-2021 IS- ',s[1][0],' with ',s[1][2],' points')
        print()
        print(s[7][0],' HAS BEEN RELEGATED')
        cur.execute('delete from players where team="{}"'.format(s[7][0]))
        con.commit()
        print()
def predict():
    t1=input('Enter team 1 : ')
    print()
    t2=input('Enter team 2 : ')
    cur.execute('select Team,per,points,sum(tot_points) from standings,players where players.team=standings.Team_name and team in("{}","{}") group by team'.format(t1,t2))
    s=cur.fetchall()
    print()
    if s[0][2]>s[1][2]:
         print('Team ',t1,' has greater chances of winning')
    if s[0][2]==s[1][2]:
        if s[0][3]>s[1][3]:
            print('Team ',t1,' has greater chances of winning')
        elif s[1][3]>s[0][3]:
            print('Team ',t2,' has greater chances of winning')
    elif s[0][2]<s[1][2]:
        print('Team ',t2,' has greater chances of winning') 
    print()

    
   
print()
print('\t----------------------------------------------')
print('\t    WELCOME TO PREMIER BASKETBALL LEAGUE !')
print('\t----------------------------------------------')
print()    
print("\t--- Teams with their Respective codes---\t" )
print()
print("\t---Mavericks:   Mav---")
print("\t---Rockets:     Roc---")
print("\t---Hornets:     Hor---")
print('\t---Pelicans:    Pel---')
print('\t---Patriots:    Pat---')
print('\t---Aviators:    Avi---')
print('\t---Titans:      Tit---')
print('\t---Challengers: Cha---')
print()
f=open('D:\\ids.txt','r')
fd=open('D:\\users.txt','a')
us='work'
while us:
   us=input('ARE YOU A USER OR SUPPORT STAFF - ')
   print()
   if us.lower()=='support staff': 
    print("\t SIGN-IN TO ENTER...")
    num=input("Enter your id number: "+'\n')
    l=[]
    s=f.readlines()
    for j in s:
        l.append(j)    
    if str(num)+'\n' in l:   
        name=input("Enter your name : "+'\n')
        cur.execute('select sysdate()')
        s=cur.fetchone()
        for i in s:
           a=str(i)
           fd.write(name+'--'+a+'\n') 
        otp=random.randint(100,999)
        print("YOUR OTP IS : ",otp)
        n=int(input("Enter your OTP : "))
        if n==otp:
         print("\t----")
         print("\tMENU")
         print("\t----")
         print("1.  Add a new Player to your squad")
         print("2.  Display your list of players")
         print("3.  Update your player's stats")         
         print("4.  Analyse your player's overall performance-3pts and 2pts")
         print("5.  Remove a player from your squad")
         print("6.  Display the points table")
         print('7.  Get a suggested squad for your game')
         print('8.  Update points table')
         print('9.  Analyze your coach"s performance')
         print('10. View coaches')
         print('11. Sign out')
         choice=1
         while choice!=11:
             choice=int(input("Enter your choice please : "))
             if choice==1:
               add()    
             elif choice==2:
                 display()    
             elif choice==3:
                updating()    
             elif choice==4:
                ptanalysis()    
             elif choice==5:
                deletion()
             elif choice==6:
                 pttable()
             elif choice==7:
                  squad()
             elif choice==8:
                upptable()    
             elif choice==9:
                  cperform()    
             elif choice==10:
                  viewcoaches()
             else:
                print('You have successfully signed out!')
                print('Thanks for visiting Premier Basketball league!')
                break
        else:
                print("Incorrect OTP") 
                break
    else:
               print('Invalid id! Access denied')
               break            
   elif us.lower()=='user':
    print('\t ---------')
    print("\t USER MENU")
    print("\t ---------")
    print("1.  Display the coaches")
    print("2.  Analyse the player's overall performance-3pts and 2pts")
    print("3.  Upcoming matches and their dates")
    print("4.  Points table")
    print('5.  Display the title winner')
    print('6.  Display the top scorer or top assists')
    print('7.  Display the team with most points and most assists')
    print('8.  Prebook tickets for a match')
    print('9.  Average points scored per match by your player')
    print('10. Access a players record individually')
    print('11. Top scorer for each team')
    print('12. Awards ceremony')
    print('13. Predict the winner of the match based on standings')
    print('14. The recent form of teams')
    print('15. Chart for displaying total points and assists of teams')
    print('16. Exit')
    print()
    choiceu=1
    while choiceu!=16:
      choiceu=int(input('Enter your choice : '))
      if choiceu==1:
       viewcoaches() 
      elif choiceu==2:
        ptanalysis()     
      elif choiceu==3:
        fixtures()
      elif choiceu==4:
        pttable()
      elif choiceu==5:
        title()
      elif choiceu==6:
        maxscrass()
      elif choiceu==7:
        tptass()
      elif choiceu==8:
        matchtickets()
      elif choiceu==9:
        na=input('Enter the name of your player : ')
        avergpl(na)  
      elif choiceu==10:
        nm=input('Enter the name : ')
        indaccess(nm)
      elif choiceu==11:
        topsc()
      elif choiceu==12:
        awards() 
      elif choiceu==13:
        predict()
      elif choiceu==14:
        a=input('Enter the team : ')
        rec(a)
      elif choiceu==15:
        chart.linech()
      else:
        print('------')
        print("Thanks for visiting premier basketball League") 
        print("------")
        break
   else:
       print('Invalid input')
       break
f.close()
fd.close()    
con.close()
