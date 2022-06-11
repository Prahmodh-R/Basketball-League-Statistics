import matplotlib.pyplot as pl
import mysql.connector as sb
con=sb.connect (host='localhost' ,user='root', passwd='aproj70',database='sun')
cur=con.cursor()
def linech():
 cur.execute('select team,sum(tot_points),sum(assists) from players group by team')
 s=cur.fetchall()
 t=[]
 pts=[]
 ast=[]
 for i in s:
    t.append(i[0][:3])
    pts.append(i[1])
    ast.append(i[2])
 pl.xlabel('TEAMS')
 pl.ylabel('POINTS/ASSISTS')
 pl.plot(t,pts,color='r',label='points',marker='x')
 pl.plot(t,ast,color='c',label='assists',marker='x')
 pl.legend(loc='upper right')
 pl.title('Total points/ Total assists of Teams')
 pl.show()
 print()  
def barch():
       te=[]
       pts=[]
       cur.execute('select team_name,points from standings')
       s=cur.fetchall()
       for i in s:
           te.append(i[0][:3])
           pts.append(i[1])
       pl.bar(te,pts,color='b')
       pl.xlabel('TEAMS')
       pl.ylabel('POINTS')
       pl.title('POINTS TABLE')
       pl.show()
       print()              
#give shortcut names to teams to accomadate field names in the graph(along x_axis) 
