flatten :: [[Int]] -> [Int]
flatten x = foldr (\x y -> x ++ y) [] x

myLength :: String -> Int
myLength x = foldr (+) 0 $ map (\k -> 1) x

myReverse :: [Int] -> [Int]
myReverse (x) = reverse x

countIn :: [[Int]] -> Int -> [Int]
countIn l x = map (count x) l
  where
    count :: Int -> [Int] -> Int
    count x xs = length (filter (\y -> y==x) xs)

firstWord :: String -> String
firstWord str = takeWhile (/= ' ') $ (dropWhile (== ' ') str)