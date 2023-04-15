data Tree a = Node a (Tree a) (Tree a) | Empty deriving (Show)

size :: Tree a -> Int
size Empty = 0
size (Node a izq der) = 1 + size izq + size der

height :: Tree a -> Int
height Empty = 0
height (Node a izq der) = 1 + max (height izq) (height der)

equal :: Eq a => Tree a -> Tree a -> Bool
equal (Node i iIzq iDer) Empty = False
equal Empty (Node j jIzq jDer) = False
equal Empty Empty = True
equal (Node i iIzq iDer) (Node j jIzq jDer) = 
    i == j && equal iIzq iDer && equal iDer jDer

isomorphic :: Eq a => Tree a -> Tree a -> Bool
isomorphic Empty Empty = True
isomorphic (Node i iIzq iDer) Empty = False
isomorphic Empty (Node j jIzq jDer) = False
isomorphic (Node i iIzq iDer) (Node j jIzq jDer) = 
    (i == j) && 
    ((isomorphic iIzq jIzq && isomorphic iDer jDer) || 
     (isomorphic iIzq jDer && isomorphic jIzq iDer))

preOrder :: Tree a -> [a]
preOrder Empty = []
preOrder (Node n l r) = n : preOrder l ++ preOrder r

postOrder :: Tree a -> [a]
postOrder Empty = []
postOrder (Node n l r) =  postOrder l ++ postOrder r ++ [n]

inOrder :: Tree a -> [a]
inOrder Empty = []
inOrder (Node n l r) =  inOrder l ++ [n] ++ inOrder r


breadthFirst :: Tree a -> [a]
breadthFirst tree = bfs [tree]
  where
    bfs [] = []
    bfs ts = [x | Node x _ _ <- ts] ++ bfs (concatMap children ts)

    children Empty = []
    children (Node _ left right) = [left, right]
    
build :: Eq a => [a] -> [a] -> Tree a
build [] [] = Empty
build (preRoot:preRest) inOrder = Node preRoot leftTree rightTree
  where
    (leftInOrder, _:rightInOrder) = break (== preRoot) inOrder
    (leftPreOrder, rightPreOrder) = splitAt (length leftInOrder) preRest
    leftTree = build leftPreOrder leftInOrder
    rightTree = build rightPreOrder rightInOrder

overlap :: (a -> a -> a) -> Tree a -> Tree a -> Tree a
overlap _ Empty t2 = t2
overlap _ t1 Empty = t1
overlap f (Node v1 l1 r1) (Node v2 l2 r2) = Node combinedValue combinedLeft combinedRight
  where
    combinedValue = f v1 v2
    combinedLeft = overlap f l1 l2
    combinedRight = overlap f r1 r2




