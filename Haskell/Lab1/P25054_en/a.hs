myLength :: [Int] -> Int
myLength [] = 0
myLength (x:xs) = 1 + myLength xs

myMaximum :: [Int] -> Int
myMaximum (x:xs) 
    | myLength xs == 0 = x
    | x > max = x
    | x < max = max
    | otherwise = x
    where max = myMaximum xs

averageRec :: [Float] -> Float -> Float
averageRec [] sz = 0.0
averageRec (x:xs) sz = x/sz + averageRec xs sz
    
average :: [Int] -> Float
average x = (averageRec xFloated (fromIntegral (myLength x)))
    where xFloated = map fromIntegral x

buildPalindrome :: [Int] -> [Int]
buildPalindrome x = reverse x ++ x

remove :: [Int] -> [Int] -> [Int]
remove [] nums = []
remove (x:xs) nums
    | elem x nums = restOfList
    | otherwise = x : restOfList
    where restOfList = remove xs nums

flatten :: [[Int]] -> [Int]
flatten [] = []
flatten (x:xs) = x ++ flatten xs

oddsNevens :: [Int] -> ([Int], [Int])
oddsNevens [] = ([], [])
oddsNevens (x:xs) 
    | x `mod` 2 == 0 = case (([], [x]), oddsNevens xs) of ((a, b), (a_, b_)) -> (a ++ a_, b ++ b_)
    | otherwise = case (([x], []), oddsNevens xs) of ((a, b), (a_, b_)) -> (a ++ a_, b ++ b_)

primeDivisors :: Int -> [Int]
primeDivisors n 
    | n <= 1 = []
    | otherwise = [d | d <- [2..n], isPrime d, n `mod` d == 0]
    where
        isPrime :: Int -> Bool
        isPrime x = all (\d -> x `mod` d /= 0) [2..(floor $ sqrt $ fromIntegral x)]
