roman2int :: String -> Int
roman2int [] = 0
roman2int (x:xs)
    | currentValue < nextValue = (-currentValue) + roman2int xs
    | otherwise = currentValue + roman2int xs
    where
        getValue :: Char -> Int
        getValue x
            | x == 'I' = 1
            | x == 'V' = 5
            | x == 'X' = 10
            | x == 'L' = 50
            | x == 'C' = 100
            | x == 'D' = 500
            | x == 'M' = 1000
        getNextValue :: String -> Int
        getNextValue [] = 0
        getNextValue (x:xs) = getValue x
        currentValue = getValue x
        nextValue = getNextValue xs

roman2int' :: String -> Int
roman2int' = snd . foldr (sumRoman . getValue) (Nothing, 0)
  where
    getValue :: Char -> Int
    getValue x
      | x == 'I' = 1
      | x == 'V' = 5
      | x == 'X' = 10
      | x == 'L' = 50
      | x == 'C' = 100
      | x == 'D' = 500
      | x == 'M' = 1000
    sumRoman :: Int -> (Maybe Int, Int) -> (Maybe Int, Int)
    sumRoman c (Nothing, acc) = (Just c, acc + c)
    sumRoman c (Just prev, acc)
      | prev > c = (Just c,  (-c) + acc)
      | otherwise    = (Just c, acc + c)

arrels :: Float -> [Float]
arrels = arrelsRec 1

arrelsRec :: Float -> Float -> [Float]
arrelsRec 1 n = n : arrelsRec n n
arrelsRec p x = act : arrelsRec act x
    where
        act = 0.5*(p + x/p)

arrel :: Float -> Float -> Float
arrel x e = arrelRec (drop 1 $ arrels x) x e

arrelRec ::  [Float] -> Float -> Float -> Float
arrelRec (r:rs) p e
    | currentError <= e = r
    | otherwise = arrelRec rs r e
    where
        currentError = abs (r + (-p))

data LTree a = Leaf a | Node (LTree a) (LTree a)

instance Show a => Show (LTree a) where
    show (Leaf k) = "{" ++ (show k) ++ "}"
    show (Node left right) = "<" ++ (show left) ++ "," ++ (show right) ++ ">"

build :: [a] -> LTree a
build [x] = Leaf x
build xs = Node (build firstHalf) (build secondHalf)
    where
        len = length xs
        mid =  if even len then len `div` 2 else (len + 1) `div` 2
        (firstHalf, secondHalf) = splitAt mid xs

zipLTrees :: LTree a -> LTree b -> Maybe (LTree (a, b))
zipLTrees (Leaf a) (Leaf b) = Just (Leaf (a, b))
zipLTrees (Node leftA rightA) (Node leftB rightB) = do
    zippedLeft <- zipLTrees leftA leftB
    zippedRight <- zipLTrees rightA rightB
    return (Node zippedLeft zippedRight)
zipLTrees _ _ = Nothing

