from unittest import TestCase
from Ds import Node,AVL,TNode,Graph,Heap,Queue
from random import sample

class AVL_Test(TestCase):

    def test1(self):
        root = TNode(8)
        tree = AVL(root)
        
        res = tree.r.getv()
        exp = root.getv()
        self.assertEqual(res, exp)

    def test2(self):
        root = TNode(8)
        tree = AVL(root)
        root2 = TNode(12,root)
        tree.r = root2
        res = tree.r.getv()
        exp = root2.getv()
        self.assertEqual(res, exp)

    def test2_1(self):
        n = TNode(3)
        n2 = TNode(1)
        n.setl(n2)

        self.assertTrue(n.getl() is n2)

    def test2_2(self):
        n = TNode(3)
        n2 = TNode(1)
        var = n
        var2 = var
        var2.setl(n2)

        self.assertTrue(n.getl() is n2)


    def test3(self):
        root = TNode(8)
        tree = AVL(root)
        tree.add(TNode(2))        
        tree.add(TNode(9))

        res = (tree.r.getl().getv(),tree.r.getr().getv())
        exp = (2,9)
        self.assertEqual(res, exp)

    def test4(self):
        root = TNode(8)
        tree = AVL(root)
        tree.add(TNode(2))        
        tree.add(TNode(9))

        res = root.lh
        exp = 1
        self.assertEqual(res, exp, root.rh)

    def test5(self):
        root = TNode(8)
        tree = AVL(root)
        tree.add(TNode(2))        
        tree.add(TNode(9))
        tree.add(TNode(13))


        res = root.rh
        exp = 2
        self.assertEqual(res, exp)


    def test6(self):
        root = TNode(8)
        tree = AVL(root)
        n1 = TNode(2)
        tree.add(n1)        
        tree.add(TNode(9))
        tree.add(TNode(13))

        exp = root
        res = n1.getp()
        self.assertEqual(exp , res)

    def test7(self):
        root = TNode(8)
        tree = AVL(root)
        tree.add(TNode(6))        
        tree.add(TNode(9))
        tree.add(TNode(7))
        tree.add(TNode(5))
        tree.add(TNode(4))


        root = tree.r
        rlt = root.getl()
        rrt = root.getr()
        rrtrt = rrt.getr()
        rrtlt = rrt.getl()
        rltlt = rlt.getl()
        self.assertTrue(root.getv() == 6 and rlt.getv() == 5 and rrt.getv() == 8 and rrtrt.getv()==9 and rrtlt.getv()==7 and rltlt.getv()== 4)

    def test8(self):
        A = TNode(9) 
        B = TNode(5)
        P = TNode(7)
        LB = TNode(4)
        LP = TNode(6)
        RP = TNode(8)
        RA = TNode(10)
        tree = AVL(A)
        tree.add(RA)
        tree.add(B)
        tree.add(LB)
        tree.add(P)
        tree.add(LP)
        tree.add(RP)
        self.assertTrue(tree.r is P and tree.r.getl() is B and tree.r.getr() is A and tree.r.getl().getl() is LB and tree.r.getr().getr() is RA and tree.r.getl().getr() is LP and tree.r.getr().getl() is RP)

    def test9(self):
            
        t = AVL(TNode(15))
        t.add(TNode(12))
        t.add(TNode(16))
        t.add(TNode(11))
        t.add(TNode(14))
        t.add(TNode(20))
        print(t)
        t.dele(12)
        print(t)
        self.assertTrue(t.r.getv()==15 and t.r.getl().getv()==14 and t.r.getr().getv()==16 and
        t.r.getr().getr().getv()==20)

    def test10(self):
        nodes = [TNode(i) for i in sample(list(range(0,10)),6)]
        t = AVL(TNode(sample(list(range(0,10)),1)[0]))

        for n in nodes:
            t.add(n)
        
