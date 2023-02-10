
class Node:
    def __init__(self,v=None,l=None,r=None):
        
        self._v = v
        self._l = l
        self._r = r

    def getl(self):
        return self._l

    def getr(self):
        return self._r
    
    def getv(self):
        return self._v

    def setl(self,l):
        self._l = l

    def setr(self,r):
        self._r = r

    def setv(self,v):
        self._v = v

class TNode(Node):
    def __init__(self,v=None, l =None, r = None, p = None):
        super().__init__(v,l,r)
        self._p = p

        if self.getl() == None:
            self.lh = 0
        elif self.getl() != None:
            self.lh = max(self._l.lh,self._l.rh)+1

        if self.getr() == None:
            self.rh = 0
        elif self._r.getr() != None:
            self.rh = max(self._r.lh,self._r.rh)+1

    def setl(self, v):
        super().setl(v)
        if v != None:
            v._p = self

    def setr(self,v):
        super().setr(v)
        if v != None:
            v._p = self
            

    def getp(self):
        return self._p 

    def getside(self):
        if self._p == None:
            return None
        if self._p.getl() == self:
            return super().getl
        else:
            return super().getr


class AVL:
    def __init__(self,root:TNode =None ):
        self.r = root
        self._h = 0
               

    def add(self, v : TNode):
        target : TNode= self.r
        v0 = v.getv()

        while(target != None):
            v1 = target.getv()
            tl = target.getl()
            tr = target.getr()
            

            if v1>= v0 and tl != None:
                target = tl

            elif v1 <v0 and tr != None:
                target = tr
            elif v1 >= v0 and tl == None:
                target.setl(v)
                # target = None
                break
            elif v1 < v0 and tr == None:
                target.setr(v)
                # target = None
                break
        
        self.height(self.r)
        self.rot(self.r)

    
    def height(self,v: TNode):
        tl = v.getl()
        tr = v.getr()

        if v == self.r:
            self._h  =0


        if tl != None and tr != None:
            v.lh = self.height(tl)+1
            v.rh = self.height(tr)+1
            self._h = max(self._h,v.lh,v.rh)
            return max(v.lh,v.rh)
            
        elif tl != None and tr == None:
            v.lh = self.height(tl)+1       
            self._h = max(self._h,v.lh)

            return v.lh
        elif tl == None and tr != None:
            v.rh = self.height(tr)+1
            self._h = max(self._h,v.rh)

            return v.rh
        else:
            return 0

    
    def rot(self,v:TNode):

        l = v.getl()
        r = v.getr()

        if l != None and r != None:
            self.rot(l)
            self.rot(r)

        elif l != None and r == None:
            self.rot(l)
        elif l == None and r != None:
            self.rot(r)
        else :
            return None


        bal = v.lh -v.rh

        if bal > 1:

            lt = v.getl()
            bal2 = lt.lh -lt.rh
            if bal2 > 0:
                rb = lt.getr()
                p = v.getp()

                lt.setr(v)

                if p != None:
                    if p.getside() == TNode.getl:
                        p.setl(lt)
                    else:
                        p.setr(lt)
                else:
                    self.r = lt
                v.setl(rb)

            elif bal2 < 0:
                p = v.getp()
                P = lt.getr()

                if P != None: 
                    Lp= P.getl()
                else:
                    LP = None
                if P!= None:
                    Rp = P.getr()
                else:
                    Rp = None
                
                P.setl(lt)
                P.setr(v)
                lt.setr(Lp)
                v.setl(Rp)

                if p != None:
                    if P.getside()==TNode.getl:
                        p.setl(P)
                    else:
                        p.setr(P)
                else:
                    self.r = P

        if bal < -1:

            rt = v.getr()
            bal2 = rt.lh -rt.rh
            if bal2 < 0:
                lb = rt.getl()
                p = v.getp()

                rt.setl(v)

                if p != None:
                    if p.getside() == TNode.getl:
                        p.setl(rt)
                    else:
                        p.setr(rt)
                else:
                    self.r = rt
                v.setr(lb)

            elif bal2 > 0:
                p = v.getp()
                P = rt.getl()
                Rp= P.getr()
                Lp = P.getl()
                P.setr(rt)
                P.setl(v)
                rt.setl(Rp)
                v.setr(Lp)

                if p != None:
                    if P.getside()==TNode.getl:
                        p.setl(P)
                    else:
                        p.setr(P)
                else:
                    self.r = P
    # searches wit ha key and returns the first node with that key
    def search(self, key, n:TNode=None, c=None):
        if n == None:
            n = self.r
        
        l = n.getl()
        r = n.getr()
        v = n.getv()

        if v == key:
            return n
        
        if v > key and l != None:
            return self.search(key,l,c)
        
        if v > key and l== None:
            if c != None:
                return n
            return None
        
        if v < key and r != None:
            return self.search(key,r,c)
        
        if v < key and r == None:
            if c != None:
                return n     
            return None
    @staticmethod
    def _swap(v:TNode, w:TNode):
        if v != None != w:
            val = v.getv()
            v.setv(w.getv())
            w.setv(val)
        

    def __list__(self,n=None,k = 0):
        self.height(self.r)
        if n == None:
            n = self.r
            self.arr = [ None for i in range(0,2**(self._h+1))]
        
        l = n.getl()
        r = n.getr()
        if l != None != r:
            self.arr[k]= n
            self.arr[2*k+1]=self.__list__(l,2*k+1)
            self.arr[2*(k+1)]=self.__list__(r,2*(k+1))
            return n


        if l!= None :
            self.arr[k]= n 
            self.arr[2*k+1]=self.__list__(l,2*k+1)
            return n
        if r!= None:
            self.arr[k]=n
            self.arr[2*(k+1)]=self.__list__(r,2*(k+1))
            return n

        else:
            return n

    def __str__(self):
        self.__list__()
        arr = self.arr
        l = len(self.arr)
        s = []
        for i in range(0,l):
            if arr[i] != None:
                s.append(str(arr[i].getv()))
            else:
                s.append("None")
        
        return ", ".join(s)


    def __repr__(self):
        return str(self.__list__())



    def dele(self,key,n=None,c=None):
        v = self.search(key,n,c)
        sn = None
        sv = None

        if v.getr()!= None:
            sn = self.search(v.getv(),v.getr())
            if sn != None:
                AVL._swap(v, sn)
                self.dele(sn.getv(),sn)
                return None
            else:
                r = v.getr()
                AVL._swap(v, r)
                v.setr(None)
                del r
                self.height(self.r)
                self.rot(self.r)
                return None

        if v.getl() !=None:
            sv = self.search(v.getv(),v.getl())
            if sv != None:
                AVL._swap(v, sv)
                self.dele(sv.getv(),sv)
                return None
            else:
                l = v.getl()
                AVL._swap(v, l)
                v.setl(None)
                del l
                self.height(self.r)
                self.rot(self.r)
                return None

        if v.getl() == v.getr()==None:
            p = v.getp()
            if v.getside() == TNode.getl:
                p.setl(None)
            elif v.getside() == TNode.getr:
                p.setr(None)
            del v

        


        return None


class Queue:
    def __init__(self,Left, Right):
        self.__Left = Left
        self.__Right = Right
        self.__Left.setr(self.__Right)
        self.__Right.setl(self.__Left)
        self.__Mid = Left


    def search(self, key):
        v = self.__Mid.getv()

        while v != None:
            if v == key:
                return v
            
            elif v < key :
                v = v.getr()
            elif v > key:
                v = v.getl()

    def enq(self,v :Node):
        oleft = self.__Left
        self.__Left = v
        self.__Left.setr(oleft)

        
        self.__Mid = self.__Mid.getl()

    def deq(self,v:Node):
        oright = self.__Right
        self.__Right = self.__Right.getl()
        oright.setl(None)
        self.__Right.setr(None)
        del oright

        self.__Mid = self.__Mid.getl()


                






    def add(self,v : Node):
        pass

class Heap:
    pass

class Graph:
    pass
                

if __name__ == "__main__":
    t = AVL(TNode(15))
    t.add(TNode(12))
    t.add(TNode(16))
    t.add(TNode(11))
    t.add(TNode(14))
    t.add(TNode(20))
    # arr = t.__list__()
    print(t)
    t.dele(12)
    print(t)
