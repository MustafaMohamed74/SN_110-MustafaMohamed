from abc import ABC , abstractmethod
import math
class Polygon:    #Parent Class Polygon
    @abstractmethod
    def area(self):
     pass
    @abstractmethod
    def perimeter(self):
     pass
    @abstractmethod
    def Draw(self):
     pass
 
 
class Triangle(Polygon):
     no_of_triangles=0
     no_sides=3
     def __init__(self,s1,s2,s3):
       super().__init__()
       self.__s1 = s1
       self.__s2 = s2
       self.__s3 = s3
       self.no_of_triangles += 1
     def setSidesLength(self,newS1,newS2,newS3):
       self.__s1 = newS1
       self.__s2 = newS2
       self.__s3 = newS3
     def area(self):
         S=(self.perimeter())/2
         return math.sqrt(S*(S-self.__s1)*(S-self.__s2)*(S-self.__s3))
     def perimeter(self):
        return self.__s1 + self.__s2 + self.__s3
     def Draw(self):
        print("*   ")
        print("***  ")
        print("***** ")
        print("*******")
        
        
class Quadrilateral(Polygon):
    no_sides=4
    no_Quadrilateral=0
    def __init__(self,s1,s2,s3,s4,theta1,theta2):
      super().__init__()
      self.__s1 = s1
      self.__s2 = s2
      self.__s3 = s3
      self.__s4 = s4
      self.__theta1= theta1
      self.__theta2= theta2
      self.no_Quadrilateral += 1
      
    def setSidesLength(self,newS1,newS2,newS3,newS4):
        self.__s1 = newS1
        self.__s2 = newS2
        self.__s3 = newS3
        self.__s4 = newS4
    def setAngles(self,newTheta1,newTheta2):
        self.__theta1 = newTheta1
        self.__theta2 = newTheta2
        
    def area(self):
        S=(self.perimeter()) /2
        theta=math.radians(self.__theta1 + self.__theta2)
        return math.sqrt(((S-self.__s1)*(S-self.__s2)*(S-self.__s3)*(S-self.__s4))-(self.__s1)*(self.__s2)*(self.__s3)*(self.__s4)*(math.pow(math.cos(theta/2),2)))
    
    def perimeter(self):
        return self.__s1 + self.__s2 + self.__s3 + self.__s4
    def Draw(self):
        pass
class Pentagon(Polygon):   #Child Class From Parent Polygon 
    no_sides=5
    no_pentagons=0
    def __init__(self,length):
      super().__init__()
      self.__length = length
      self.no_pentagons += 1
      
    def setLength(self,newLength):
        self.__length=newLength
    
    def area(self):
        return (0.25)*math.sqrt(5*(5+2*math.sqrt(5)))*((self.__length)**2)
        
    def perimeter(self):
        return self.__length*5
    def Draw(self):
     for size in str(self.__length):
        size=int(size)
        if size < 0:
            continue

        print("\nSide:", size, "\n")
        j = 2
        i = 0
        while i <= (size - 1) * 2:
            if i < size:
                # Print top half layers
                counter = 0
                while counter < size * 2 - (i * 2):
                    print(" ", end="")
                    counter += 1
                print("*", end="")

                counter = 0
                while counter < (i * 2) * 2 - 1:
                    print(" ", end="")
                    counter += 1

                if i > 0:
                    print("*", end="")

            else:
                # Print bottom half layers
                counter = 0
                while counter < j + 1:
                    print(" ", end="")
                    counter += 1

                if i == (size - 1) * 2:
                    counter = 0
                    while counter < (size - 1) * 2 - (i - size):
                        print("* ", end="")
                        counter += 1
                else:
                    print("* ", end="")

                    counter = 0
                    while counter < (size - 1) * 4 - j * 2:
                        print(" ", end="")
                        counter += 1

                    print("*", end="")

                j += 1

            print()
            i += 1

        
class Hexagon(Polygon):   #Child Class From Parent Polygon 
    no_sides=6
    no_Hexagon=0
    def __init__(self,length):
      super().__init__()
      self.__length = length
      self.no_Hexagon += 1
      
    def setLength(self,newLength):
        self.__length=newLength
    
    def area(self):
        return (0.5)*3*math.sqrt(3)*((self.__length)**2)
    def perimeter(self):
        return 6*self.__length
    def Draw(self):
        print(f"    Side Length ={self.__length}")
        sideLength = self.__length
        totalLength = (sideLength)*2 + (sideLength-2)
        loop =1
        while loop<=totalLength :
           if loop==1 or loop==totalLength:
              print (" "*(sideLength-1) + "*"* sideLength + " "*(sideLength-1))

           if loop>=1 and loop<sideLength-1:
              print (" "*(sideLength- 1- loop) + "*" +  " " * ((sideLength-2) + 2*(loop)) + "*" + " "*(sideLength- 1- loop))

           if loop>=2*sideLength-1 and loop<totalLength-1:
               print (" "*(loop-totalLength+sideLength) + "*"+  " " *(totalLength-2*(loop-totalLength+sideLength+1)) + "*" + " "*(sideLength- 1- loop))

           loop+=1
        
        
class Octagon(Polygon):   #Child Class From Parent Polygon 
    no_sides=8
    no_Octagon=0
    def __init__(self,length):
      super().__init__()
      self.__length = length
      self.no_Octagon += 1
      
    def setLength(self,newLength):
        self.__length=newLength

    def area(self):
        return 2*(self.__length**2)*(1+math.sqrt(2))
    def perimeter(self):
        return 8*self.__length
    def Draw(self):
      sideLength = self.__length
      totalLength = (sideLength) + 2*(sideLength-1)
 
      loop = 1

      while loop<=totalLength :
       if loop==1 or loop==totalLength:
        print (" "*(sideLength-1) + "*"* sideLength + " "*(sideLength-1))

       if loop>sideLength-1 and loop<= 2*sideLength-1:
        print ("*" + " "*(totalLength-2) + "*")

       if loop>=1 and loop<sideLength-1:
        print (" "*(sideLength- 1- loop) + "*" +  " " * ((sideLength-2) + 2*(loop)) + "*" + " "*(sideLength- 1- loop))

       if loop>=2*sideLength-1 and loop<totalLength-1:
        print (" "*(loop-totalLength+sideLength) + "*"+  " " *(totalLength-2*(loop-totalLength+sideLength+1)) + "*" + " "*(sideLength- 1- loop))

       loop+=1                                 
   
class IsoscelesTriangle(Triangle):
    def __init__(self, s1, s2, s3 ):
       super().__init__(s1, s2, s3) 
       self.__s1 = s1
       self.__s2 = s2
       self.__s3 = s3
       
    def setSidesLength(self, newS1, newS2, newS3):
       return super().setSidesLength(newS1, newS2, newS3)
    def area(self):
        if self.__s1==self.__s2:
            self.__a=self.__s2
            self.__b=self.__s3
        elif self.__s2==self.__s3:
           self.__a=self.__s2
           self.__b=self.__s1
        elif self.__s1==self.__s3:
           self.__a=self.__s1
           self.__b=self.__s2
        else :
           print("It's Not Isosceles")
           return 1
        return  (0.5) * self.__b * math.sqrt((math.pow(self.__a, 2)) - (math.pow(self.__b, 2) / 4))
    def perimeter(self):
       return super().perimeter()
    def Draw(self):
        height=int(math.sqrt(self.__s1**2 - (self.__s3/2)**2) )
        for i in range(1, height + 1):
        # Calculate the number of spaces and asterisks for each row
            num_spaces = height - i
            num_asterisks = 2 * i - 1

            # Print the leading spaces
            print(" " * num_spaces, end="")

            # Print the asterisks
            print("*" * num_asterisks)
   
class  EquilateralTriangle(Triangle):
    def __init__(self, s):
        self.__s =s
       
    def setSidesLength(self, s):
       self.__s=s
    def area(self):
        return (math.sqrt(3)/4)*(self.__s**2)
    def perimeter(self):
       return self.__s*3
    def Draw(self):
         for i in range(self.__s):
            print(' ' * (self.__s - i - 1) + '*' * (2 * i + 1))
   
class Rectangle(Quadrilateral):
    def __init__(self, s1, s2):
       self.__s1 = s1
       self.__s2 = s2
    def setSidesLength(self,newS1,newS2):
        self.__s1 = newS1
        self.__s2 = newS2
    def area(self):
       return self.__s1*self.__s2
    def perimeter(self):
       return 2*(self.__s1+self.__s2)
    def Draw(self):
        for i in range(self.__s2):
         print("* "* self.__s1)
class Square(Quadrilateral):
    def __init__(self, s1):
       self.__s1 = s1
       
    def setSidesLength(self,newS1):
        self.__s1 = newS1
      
    def area(self):
       return self.__s1*self.__s1
    def perimeter(self):
       return 4*(self.__s1)
    def Draw(self):
        for _ in range(self.__s1):
          print('* ' * self.__s1)
        
def menu():
    print("Select which polygon to compute its area or perimeter or to draw it.")
    print("For Triangle press -> 1 ")
    print("For Quadrilateral press -> 2 ")
    print("For Pentagon press -> 3 ")
    print("For Hexagon press -> 4 ")
    print("For Octagon press -> 5 ")
    
def menu2():
    print("Choose What to Calculate ")
    print("1.Area")
    print("2.Perimeter")
    print("3.Draw")
    
def triMenu():
    print("IS it IsoscelesTriangle , EquilateralTriangle , RegularTriangle")
    print("For IsoscelesTriangle press -> 1 ")
    print("For EquilateralTriangle press -> 2 ")
    print("For RegularTriangle press -> 3 ")
    
def quadMenu():
    print("IS it Square , Rectangle , other")
    print("For Square press -> 1 ")
    print("For Rectangle press -> 2 ")
    print("For other press -> 3 ")
    
    
def Triangle_Calculations(Selected , select) :
        if (Selected==1):
            s1=int(input("Put Side Length\n"))
            s2=int(input("Put Base Length\n"))
            tri=IsoscelesTriangle(s1,s1,s2)
            if select==1:
                print(f"Area = {tri.area()}")
            elif select==2:
                 print(f"Perimeter = {tri.perimeter()}")
            elif select==3:
                tri.Draw()
            else :
                print("Error : Not a valid method")
                
        elif (Selected==2):
             s=int(input("Put Side Length\n"))
             tri=EquilateralTriangle(s)
             if select==1:
                print(f"Area = {tri.area()}")
             elif select==2:
                 print(f"Perimeter = {tri.perimeter()}")
             elif select==3:
                tri.Draw()
             else :
                print("Error : Not a valid method")
        elif (Selected==3):
            s1=int(input("Put Side1 Length\n"))
            s2=int(input("Put Side2 Length\n"))
            s3=int(input("Put Side3 Length\n"))
            tri=Triangle(s1,s2,s3)
            if select==1:
                print(f"Area = {tri.area()}")
            elif select==2:
                 print(f"Perimeter = {tri.perimeter()}")
            elif select==3:
                tri.Draw()
            else :
                print("Error : Not a valid method")
        else :
            print("Error : Wrong Input")
            
def Quadriletral_Calculations(Selected , select):
        if (Selected==1):
            s=int(input("Put Side Length\n"))
            square=Square(s)
            if select==1:
                print(f"Area = {square.area()}")
            elif select==2:
                 print(f"Perimeter = {square.perimeter()}")
            elif select==3:
                square.Draw()
            else :
                print("Error : Not a valid method")
        elif (Selected==2):
             s1=int(input("Put Length\n"))
             s2=int(input("Put Width\n"))
             Rect=Rectangle(s1,s2)
             if select==1:
                print(f"Area = {Rect.area()}")
             elif select==2:
                 print(f"Perimeter = {Rect.perimeter()}")
             elif select==3:
                Rect.Draw()
             else :
                print("Error : Not a valid method")
        elif (Selected==3):
            s1=int(input("Put Side1 Length\n"))
            s2=int(input("Put Side2 Length\n"))
            s3=int(input("Put Side3 Length\n"))
            s4=int(input("Put Side4 Length\n"))
            theta1=int(input("Put theta1\n"))
            theta2=int(input("Put theta2\n"))
            Quad=Quadrilateral(s1,s2,s3,s4,theta1,theta2)
            if select==1:
                print(f"Area = {Quad.area()}")
            elif select==2:
                 print(f"Perimeter = {Quad.perimeter()}")
            elif select==3:
                Quad.Draw()
            else :
                print("Error : Not a valid method")
        else :
            print("Error : Wrong Input")
            
def Pentagon_Calculations(select):
    s=int(input("Put Side Length\n"))
    pent=Pentagon(s)
    if select==1:
        print(f"Area = {pent.area()}")
    elif select==2:
        print(f"Perimeter = {pent.perimeter()}")
    elif select==3:
        pent.Draw()
    else :
        print("Error : Not a valid method")
def Hexagon_Calculations(select):
    s=int(input("Put Side Length\n"))
    hex=Hexagon(s)
    if select==1:
        print(f"Area = {hex.area()}")
    elif select==2:
        print(f"Perimeter = {hex.perimeter()}")
    elif select==3:
        hex.Draw()
    else :
        print("Error : Not a valid method")

def Octagon_Calculations(select):
    s=int(input("Put Side Length\n"))
    oct=Octagon(s)
    if select==1:
        print(f"Area = {oct.area()}")
    elif select==2:
        print(f"Perimeter = {oct.perimeter()}")
    elif select==3:
        oct.Draw()
    else :
        print("Error : Not a valid method")
        
def main(): 
   flag = True
   while flag:
    menu()
    Selected = int(input())
    if (Selected == 1) :
        triMenu()
        Selected2= int(input())
        menu2()
        select= int(input())
        Triangle_Calculations(Selected2,select)
            
    elif  (Selected == 2):
        quadMenu()
        Selected2= int(input())
        menu2()
        select= int(input())
        Quadriletral_Calculations(Selected2 , select)
        
    elif  (Selected == 3):
        menu2()
        select= int(input())
        Pentagon_Calculations(select)
        
    elif  (Selected == 4):
        menu2()
        select= int(input())
        Hexagon_Calculations(select)
        
    elif  (Selected == 5):
        menu2()
        select= int(input())
        Octagon_Calculations(select)
    else: 
        print("Error : Wrong input ")
    
    print("Do you wants to quit the program or continue")
    print("Press 0 to quit or any other Number button to continue")
    Choice=int(input())
    if Choice==0:
        flag=False
    else:
        pass
         


if __name__ == "__main__":
    main()