data Tree a = Empty | Node a (Tree a) (Tree a)

instance Show a => Show (Tree a) where
    show Empty = "()"
    show (Node n left right) = "(" ++ show left ++ "," ++ show n ++ "," ++ show right ++ ")"


instance Functor Tree where
    fmap _ Empty = Empty
    fmap f (Node n left right) = Node (f n) (fmap f left) (fmap f right) 

doubleT :: Num a => Tree a -> Tree a
doubleT = fmap (*2)

data Forest a = Forest [Tree a] deriving (Show)

instance Functor Forest where
    fmap _ (Forest []) = Forest []
    fmap f (Forest trees) =  Forest (fTrees f trees)
        where 
            fTrees :: (a -> b) -> [Tree a] -> [Tree b]
            fTrees _ [] = []
            fTrees f (t:ts) = fmap f t : fTrees f ts 

doubleF :: Num a => Forest a -> Forest a
doubleF = fmap (*2)

