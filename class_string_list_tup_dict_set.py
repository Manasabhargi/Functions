import logging
logging.basicConfig(filename="test.log", level=logging.DEBUG ,format='%(levelname)s %(asctime)s %(name)s  %(message)s' )

class string :

    def index(self,m):
        logging.info("the string entered by user is %s",m)
        try:
            logging.info("INDEX HAS BEEN JUMPED TO 3 %s",m[1:300:3])
            return m
        except Exception as e:
            logging.exception(e)
            print(e)

    def reverse(self,s):
        logging.info("the string entered by user is %s",s)
        try:
            logging.info("the reveresed string is %s",s[::-1])
            return s
        except Exception as e:
            logging.info(e)

    def split(self,n):
        logging.info("The string is %s",n)
        try:
            m = n.upper()
            b = m.split()
            logging.info("The string after split operation is %s",b)
            return b
        except Exception as e:
            logging.info(e)

    def lower(self,l):
        logging.info("The string entered by user is %s",l)
        try:
            logging.info("After converting the string into lowercase is %s",l.lower())
            return l
        except Exception as e:
            logging.info(e)

    def capitalize(self,k):
        logging.info("The string which needs to be capitalized is %s",k)
        try:
            logging.info("After capitalizing %s",k.capitalize())
            return k
        except Exception as e:
            logging.info(e)

    def replace(self,a,b):
        m = "Hi the string and its replaced string"
        try:
            logging.info("Before replacement %s",m)
            n = m.replace(a, b)
            logging.info("After replacement %s", n)
            return n
        except Exception as e:
            logging.info(e)

    def centre(self,j):
        logging.info("The string entered by user is %s",j)
        try:
            d = j.center(50,'$')
            logging.info("After %s",d)
            return d
        except Exception as e:
            logging.info(e)


sudh = string()

sudh.index("The first python program")

sudh.reverse("Manasa")

sudh.split("This is my first python project")

sudh.lower("Checking FOR ALL LOWERCASE")

sudh.capitalize("all are in small case")

sudh.replace("Hi","Me")

sudh.centre("Hi Sudhanshu sir")

l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]

l2  = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

class list :
    for i in l2:
        if type(i) == list:
            logging.info("list entities are %s", i)
            #print(i)

    def list(self,l):
        logging.info("The original string is %s", l)
        try:

            logging.info("The reversed string is %s", l[::-1])
            logging.info("Only the list collection in l is %s", l[5:7])
            return l

        except Exception as e:
            logging.info(e)
        finally:
            logging.info("The required string is %s", l[5][1])
            return l

sudh1 = list()

sudh1.list(l)

class tuple :
    for i in l:
        if type(i) == tuple:
            logging.info("The tuple present in list l2 is %s",i)
            #print(i)
    def tup(self,l):
        try:
            logging.info("The required element from the tuple is %s", l[7][0])
            return l
        except Exception as e:
            logging.info(e)

sudh2 = tuple()

sudh2.tup(l)

class dictionary :
    for i in l:
        if type(i) == dict:
            #print(i)
            logging.info("The dict set is %s",i)
    def dict(self,l):
        try:
            logging.info("Extracted string from the dict of the original list l is '%s'",l[8]['key1'])
            logging.info("Listing all the keys in dict element available in the list l is [%s]",l[8].keys())
            logging.info("Listing all the keys in dict element available in the list l is [%s]", l[8].values())
            return l
        except Exception as e:
            logging.info(e)

sudh3 = dictionary()

sudh3.dict(l)



