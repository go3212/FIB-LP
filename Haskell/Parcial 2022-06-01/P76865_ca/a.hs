data Tree a = Empty | Node a (Tree a) (Tree a)
    deriving (Show)

instance Foldable Tree where
    foldr f acc (Empty) = acc
    foldr f acc (Node v left right) = rightAcc
        where 
            newAcc = f v acc
            leftAcc = foldr f newAcc left
            rightAcc = foldr f leftAcc right

avg :: Tree Int -> Double
avg tree = tSum / tCount
    where
        tSum = fromIntegral $ sum tree
        tCount = fromIntegral $ length tree

cat :: Tree String -> String
cat Empty = ""
cat tree = init $ foldl (\acc v -> v ++ " " ++ acc) "" tree
