import pickle,ztudent

f=open('student.dat','wb')
s=ztudent.student(123,'john',90)
pickle.dump(s,f)
f.close()